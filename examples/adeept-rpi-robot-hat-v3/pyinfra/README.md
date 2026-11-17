# PyInfra setup for Adeept Robot HAT V3 examples

This deployment applies the Linux defaults described in the linked setup posts, installs and enables the OpenSSH server, enables I²C and SPI in the Raspberry Pi boot configuration, and copies example scripts `01`–`13` into `/opt/adeept-rpi-robot-hat-v3/`. It updates and upgrades APT packages, removes unused dependencies, installs `git`, `nano`, `zsh`, and `pipx`, installs Oh My Zsh and Hyfetch for the SSH login user, sets Zsh as that user's login shell, and configures the `clean` theme and Hyfetch at interactive login. It checks `/boot/firmware/config.txt` first and falls back to `/boot/config.txt`; before changing it, PyInfra creates a dated backup. It leaves the archived Adeept `setup.py` on the source computer and does not execute any demo.

PyInfra runs from the computer administering the Pi over SSH. Install PyInfra 3.5.1 on that computer, review a dry run, then apply it:

```sh
uv tool install pyinfra==3.5.1
pyinfra pi-user@raspberrypi.local examples/adeept-rpi-robot-hat-v3/pyinfra/deploy.py --dry
pyinfra pi-user@raspberrypi.local examples/adeept-rpi-robot-hat-v3/pyinfra/deploy.py
```

Replace the sample SSH target with the actual target. The deployment uses `sudo` for APT and writes below `/opt`. It installs APT packages for GPIO, SPI, I²C tools, Pillow, and NumPy; Python packages installed in the virtual environment provide Blinka (`board` and `busio`), the Adafruit device libraries, and `mpu6050-raspberrypi`. The virtual environment can see the APT-installed Python packages to avoid duplicating compiled GPIO, SPI, and image packages through PyPI.

PyInfra connects to the Pi over SSH, so this can ensure the server stays installed, running, and enabled after a connection is available. It cannot bootstrap the first SSH connection to a Pi where SSH is disabled or unreachable. Use Raspberry Pi Imager or local access for that first setup. The shell defaults apply to the SSH login account. The deployment does not enrol an SSH key or change SSH authentication settings or firewall rules. The linked passwordless-sudo post describes an Ubuntu virtual machine; its basic Linux setup post reports that Raspberry Pi OS already gives the Pi user passwordless sudo, so this deployment does not edit sudoers.

Run an example manually after checking its hardware and interface requirements:

```sh
sudo /opt/adeept-rpi-robot-hat-v3/.venv/bin/python /opt/adeept-rpi-robot-hat-v3/01_Servo.py
```

The interface settings take effect after a reboot. The OS upgrade may also require a reboot. The deployment does not reboot the Pi, so reboot it manually after a successful run. It does not change GPIO permissions, check the HAT power path, or validate the packages against a particular Raspberry Pi OS release. This configuration has not been run on a Raspberry Pi. Resolve the D1/power-path concern before powering the board.
