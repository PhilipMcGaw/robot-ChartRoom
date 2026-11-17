# Adeept Robot HAT V3 example code

This folder contains unmodified Adeept examples `01`–`13` and the supplied `setup.py`, originally provided by Adeept and now archived here. The source headers identify Adeept as author and give the date as 2025-04-02. The user reports that Adeept authorised redistribution of examples 02–13 in Chartroom on 2026-11-17. `01_Servo.py` contains an MIT identifier inside its source docstring. The upstream source repository is [Adeept_Robot_HAT-V3](https://github.com/adeept/Adeept_Robot_HAT-V3).

`01_Servo.py` is included for a complete example set; the user's [Adeept HAT blog post](https://philipmcgaw.com/adeept-robot-hat-for-raspberry-pi/) describes previously running it on channel 0. The supplied `setup.py` is archived as a reference but has not been run. It invokes `sudo apt-get` and global `sudo pip3` installs, including `--break-system-packages` on newer Debian releases. Review it before any use.

These examples have not been tested in this repository. They target Raspberry Pi GPIO and the Adeept HAT interfaces. Confirm the fitted HAT revision, wiring, enabled interfaces, and dependencies before use. The source's pin assignments and assumptions have not been checked against the user's physical board.

## Example index

| File | Function | Initial test consideration |
| --- | --- | --- |
| `01_Servo.py` | PCA9685 servo sweep on channel 0, I²C address `0x5f`. | Previously used according to the blog post. The script repeatedly moves the servo; start with one unloaded servo. |
| `02_Ultra.py` | Ultrasonic distance readout using GPIO 23 (trigger) and GPIO 24 (echo). | Requires the matching ultrasonic module and correct echo-level interface. |
| `03_LineTracking.py` | Reads three line-tracking inputs on GPIO 22, 27, and 17. | Source appears to print the right input under the `left` label; confirm before interpreting readings. |
| `04_WS2812.py` | Drives eight WS2812 pixels over SPI, using bus 0/device 0 by default. | Enables SPI and uses GPIO 10 as MOSI; check for pin conflicts and LED power first. |
| `05_Motor.py` | Drives four motor channels through the PCA9685 at `0x5f`. | **Motion test.** The script runs M1 forward and reverse at 50% for 2 s each, repeated 100 times. Keep the robot secured and wheels clear; do not run until the HAT power path is checked. |
| `06_LED.py` | Cycles three status LEDs on GPIO 9, 25, and 11. | Output test; confirm the board revision's mapping. |
| `07_OLED.py` | Displays date and time on an I²C SSD1306 128 × 64 display. | Requires a compatible OLED connected on the expected I²C bus. |
| `08_Mpu6050.py` | Reads and averages accelerometer values from an MPU-6050 at I²C address `0x68`. | Requires the breakout header to be soldered and its VCC, GND, SCL, SDA pins aligned with HAT J1 pins 1–4. The broad exception handler suppresses errors, so a silent exit is not proof of success. |
| `09_Buzzer.py` | Plays a short tune through a tonal buzzer on GPIO 18. | Audible output test. |
| `10_IR_Receiver.py` | Waits for a receiver input on GPIO 12 and prints when pressed. | The callback does not decode or print a signal value. |
| `11_RGB.py` | Cycles two RGB outputs using GPIO 13, 19, 0, 1, 5, and 6. | GPIO output test; confirm pin mapping and active-low LED wiring. |
| `12_Battrey_Level.py` | Reads ADS7830 channel 0 at `0x48` and estimates battery percentage. | The original filename contains the spelling `Battrey`. The calculation hard-codes an 8.4 V reference, a 6.0 V warning point, and resistor values; verify against the actual battery and divider before trusting the result. |
| `13_LightTracking.py` | Reads ADS7830 channel 1 at `0x48`. | Requires the light sensor on the expected analogue channel. |

## Dependencies and interfaces

The imports in the examples indicate these third-party Python packages:

- `gpiozero`: `02_Ultra.py`, `03_LineTracking.py`, `06_LED.py`, `09_Buzzer.py`, `10_IR_Receiver.py`, and `11_RGB.py`.
- Adafruit Blinka: `board` and `busio` compatibility modules used by examples `01`, `05`, `07`, `12`, and `13`.
- `spidev` and `numpy`: `04_WS2812.py`.
- Adafruit CircuitPython PCA9685 and motor libraries, plus `board` and `busio` support: `01_Servo.py` and `05_Motor.py`.
- Adafruit CircuitPython SSD1306, Pillow, and `board`/`busio` support: `07_OLED.py`.
- `mpu6050-raspberrypi`: `08_Mpu6050.py`.
- Adafruit CircuitPython bus-device and `board`/`busio` support: `12_Battrey_Level.py`.
- Adafruit CircuitPython ADS7830 and `board` support: `13_LightTracking.py`.

Package versions and compatibility with the current Raspberry Pi OS have not been verified. Enable the required I²C or SPI interface only for the matching test. Do not run a system-wide installer as a substitute for checking each dependency.

## Automated setup with PyInfra

The `pyinfra/` directory contains a PyInfra deployment for Raspberry Pi OS. It installs and enables the OpenSSH server; enables I²C and SPI in `config.txt` with a dated backup; installs the host packages used by the examples; creates `/opt/adeept-rpi-robot-hat-v3/.venv` with access to those host packages; installs the Adafruit and MPU-6050 Python libraries in that virtual environment; and copies examples `01`–`13` to `/opt/adeept-rpi-robot-hat-v3/`. The interface settings require a manual reboot to take effect. PyInfra itself requires an existing SSH connection, so it cannot provide the first remote access to a Pi with SSH disabled. The deployment does not change SSH authentication settings or firewall rules, run the examples or Adeept's `setup.py`, or change GPIO permissions. It uses `sudo` for APT, service management, boot configuration, and `/opt` writes.

Install PyInfra on the computer that will control the Pi, then review the proposed changes with a dry run:

```sh
uv tool install pyinfra==3.5.1
pyinfra pi-user@raspberrypi.local examples/adeept-rpi-robot-hat-v3/pyinfra/deploy.py --dry
```

Replace `pi-user@raspberrypi.local` with the SSH user and hostname for the target. If the dry-run output is correct, run the same command without `--dry` to apply it. After deployment, run an example with its specific setup, for example:

```sh
ssh pi-user@raspberrypi.local
cd /opt/adeept-rpi-robot-hat-v3
sudo .venv/bin/python 01_Servo.py
```

Use `sudo` when running examples because the GPIO and bus permissions vary by Raspberry Pi OS configuration. Check the D1/power-path and hardware cautions above before powering the HAT; the deployment does not establish board safety or example compatibility. The Pi OS version and target hardware have not been checked, and this deployment has not yet been run against a Pi.
## Suggested bench sequence

1. **Check D1 and the power path first.** The examples do not test D1. Disconnect power and peripherals before checking the SS34 with a multimeter in diode mode. An in-circuit reading can be affected by other components; confirm the D1 orientation and circuit against the supplied schematic and fitted board revision. Do not power the HAT or run demos until the fault and power path are understood.
2. After the power path is confirmed, start with read-only sensor examples whose required modules are connected: `02_Ultra.py`, `03_LineTracking.py`, `08_Mpu6050.py`, `10_IR_Receiver.py`, `12_Battrey_Level.py`, and `13_LightTracking.py`.
3. Test the individual indicator outputs (`04_WS2812.py`, `06_LED.py`, `07_OLED.py`, `09_Buzzer.py`, and `11_RGB.py`) one at a time.
4. Test moving outputs last. Use one unloaded servo for `01_Servo.py`. For `05_Motor.py`, secure the robot with wheels clear and be ready to stop the program. Do not run multiple examples at once.

A successful software example does not establish that D1 is healthy. Record the actual board revision, supply, connected loads, and observed readings separately from this source index.
