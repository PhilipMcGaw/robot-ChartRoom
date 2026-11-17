"""Install dependencies and copy Adeept Robot HAT V3 examples to a Pi."""

from pathlib import Path

from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.operations import apt, files, pip, systemd


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

apt.packages(
    name="Install host packages for the Adeept examples",
    packages=[
        "i2c-tools",
        "libgpiod-dev",
        "openssh-server",
        "python3-gpiozero",
        "python3-lgpio",
        "python3-libgpiod",
        "python3-numpy",
        "python3-pil",
        "python3-smbus",
        "python3-spidev",
        "python3-venv",
    ],
    update=True,
    sudo=True,
)

systemd.service(
    name="Enable and start the OpenSSH server",
    service="ssh.service",
    running=True,
    enabled=True,
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
