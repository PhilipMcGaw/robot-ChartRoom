"""Install dependencies and copy Adeept Robot HAT V3 examples to a Pi."""

from pathlib import Path

from pyinfra.operations import apt, files, pip


EXAMPLE_DIR = Path(__file__).resolve().parent.parent
INSTALL_DIR = "/opt/adeept-rpi-robot-hat-v3"
VENV_DIR = f"{INSTALL_DIR}/.venv"

apt.packages(
    name="Install host packages for the Adeept examples",
    packages=[
        "i2c-tools",
        "libgpiod-dev",
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
