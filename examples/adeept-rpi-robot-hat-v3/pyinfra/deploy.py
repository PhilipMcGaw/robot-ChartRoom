"""Install dependencies and copy Adeept Robot HAT V3 examples to a Pi."""

from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.facts.server import Home, User
from pyinfra.operations import apt, files, pip, server, systemd


EXAMPLE_DIR = Path(__file__).resolve().parent.parent
INSTALL_DIR = "/opt/adeept-rpi-robot-hat-v3"
VENV_DIR = f"{INSTALL_DIR}/.venv"
BOOT_CONFIG_PATHS = ["/boot/firmware/config.txt", "/boot/config.txt"]

BOOT_CONFIG = next(
    (
        path
        for path in BOOT_CONFIG_PATHS
        if host.get_fact(File, path=path) is not None
    ),
    None,
)

if BOOT_CONFIG is None:
    raise RuntimeError(
        "Could not find Raspberry Pi config.txt at /boot/firmware/config.txt "
        "or /boot/config.txt"
    )

LOGIN_USER = host.get_fact(User)
LOGIN_HOME = host.get_fact(Home, user=LOGIN_USER)

if not LOGIN_USER or not LOGIN_HOME:
    raise RuntimeError("Could not identify the SSH login user's home directory")

ZSH_CONFIG = '''export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="clean"
plugins=(git)
source "$ZSH/oh-my-zsh.sh"'''

ZPROFILE_CONFIG = '''export PATH="$HOME/.local/bin:$PATH"
if [[ -o interactive ]]; then
  clear
  hyfetch
fi'''

apt.update(
    name="Update APT package lists",
    sudo=True,
)

apt.dist_upgrade(
    name="Upgrade the Raspberry Pi OS packages and remove unused dependencies",
    auto_remove=True,
    sudo=True,
)

apt.packages(
    name="Install Linux defaults and host packages for the Adeept examples",
    packages=[
        "git",
        "i2c-tools",
        "libgpiod-dev",
        "nano",
        "openssh-server",
        "pipx",
        "python3-gpiozero",
        "python3-lgpio",
        "python3-libgpiod",
        "python3-numpy",
        "python3-pil",
        "python3-smbus",
        "python3-spidev",
        "python3-venv",
        "zsh",
    ],
    sudo=True,
)

systemd.service(
    name="Enable and start the OpenSSH server",
    service="ssh.service",
    running=True,
    enabled=True,
    sudo=True,
)

server.shell(
    name="Install Oh My Zsh and Hyfetch for the SSH login user",
    commands=[
        'if [ ! -d "$HOME/.oh-my-zsh" ]; then '
        'git clone --depth=1 https://github.com/ohmyzsh/ohmyzsh.git '
        '"$HOME/.oh-my-zsh"; fi',
        'if ! command -v hyfetch >/dev/null 2>&1; then '
        'pipx install hyfetch; fi',
    ],
)

files.block(
    name="Set the clean Oh My Zsh theme for the SSH login user",
    path=f"{LOGIN_HOME}/.zshrc",
    content=ZSH_CONFIG,
    marker="# {mark} ADEEPT ROBOT LINUX DEFAULTS",
    backup=True,
)

files.block(
    name="Show Hyfetch at interactive Zsh login",
    path=f"{LOGIN_HOME}/.zprofile",
    content=ZPROFILE_CONFIG,
    marker="# {mark} ADEEPT ROBOT LINUX DEFAULTS",
    backup=True,
)

server.user(
    name="Set Zsh as the login shell for the SSH login user",
    user=LOGIN_USER,
    shell="/usr/bin/zsh",
    sudo=True,
)

files.block(
    name="Enable I2C and SPI interfaces in Raspberry Pi boot configuration",
    path=BOOT_CONFIG,
    content="[all]\ndtparam=i2c_arm=on\ndtparam=spi=on",
    marker="# {mark} ADEEPT ROBOT HAT V3 INTERFACES",
    backup=True,
    sudo=True,
)

files.directory(
    name="Create the example installation directory",
    path=INSTALL_DIR,
    user="root",
    group="root",
    mode="755",
    sudo=True,
)

pip.virtualenv(
    name="Create a virtual environment with access to Raspberry Pi OS packages",
    path=VENV_DIR,
    python="python3",
    venv=True,
    site_packages=True,
    sudo=True,
)

pip.packages(
    name="Install Python libraries used by the examples",
    packages=[
        "adafruit-blinka",
        "adafruit-circuitpython-ads7830",
        "adafruit-circuitpython-busdevice",
        "adafruit-circuitpython-motor",
        "adafruit-circuitpython-pca9685",
        "adafruit-circuitpython-ssd1306",
        "mpu6050-raspberrypi",
    ],
    virtualenv=VENV_DIR,
    sudo=True,
)

for source in sorted(EXAMPLE_DIR.glob("[0-9][0-9]_*.py")):
    files.put(
        name=f"Copy {source.name}",
        src=str(source),
        dest=f"{INSTALL_DIR}/{source.name}",
        mode="644",
        sudo=True,
    )
