# Adeept Robot HAT V3 example code

This folder contains unmodified copies of Adeept examples `02`–`13` from the user-supplied files in `inbox/Adeept_Robot_HAT-V3/`. The source headers identify Adeept as author and give the date as 2025-04-02. The user reports that Adeept authorised redistribution of these examples in Chartroom on 2026-11-17. The upstream source repository is [Adeept_Robot_HAT-V3](https://github.com/adeept/Adeept_Robot_HAT-V3).

`01_Servo.py` is indexed below but is not copied here; the user's [Adeept HAT blog post](https://philipmcgaw.com/adeept-robot-hat-for-raspberry-pi/) describes running that example on channel 0. The supplied `setup.py` is also not copied: it runs package-manager commands with `sudo`, installs packages globally, and uses `--break-system-packages` on newer Debian releases. It has not been run.

These examples have not been tested in this repository. They target Raspberry Pi GPIO and the Adeept HAT interfaces. Confirm the fitted HAT revision, wiring, enabled interfaces, and dependencies before use. The source's pin assignments and assumptions have not been checked against the user's physical board.

## Example index

| File | Function | Initial test consideration |
| --- | --- | --- |
| `01_Servo.py` (not copied) | PCA9685 servo sweep on channel 0, I²C address `0x5f`. | Previously used according to the blog post. The script repeatedly moves the servo; start with one unloaded servo. |
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
- `spidev` and `numpy`: `04_WS2812.py`.
- Adafruit CircuitPython PCA9685 and motor libraries, plus `board` and `busio` support: `05_Motor.py`.
- Adafruit CircuitPython SSD1306, Pillow, and `board`/`busio` support: `07_OLED.py`.
- `mpu6050-raspberrypi`: `08_Mpu6050.py`.
- Adafruit CircuitPython bus-device and `board`/`busio` support: `12_Battrey_Level.py`.
- Adafruit CircuitPython ADS7830 and `board` support: `13_LightTracking.py`.

Package versions and compatibility with the current Raspberry Pi OS have not been verified. Enable the required I²C or SPI interface only for the matching test. Do not run a system-wide installer as a substitute for checking each dependency.
## Suggested bench sequence

1. **Check D1 and the power path first.** The examples do not test D1. Disconnect power and peripherals before checking the SS34 with a multimeter in diode mode. An in-circuit reading can be affected by other components; confirm the D1 orientation and circuit against the supplied schematic and fitted board revision. Do not power the HAT or run demos until the fault and power path are understood.
2. After the power path is confirmed, start with read-only sensor examples whose required modules are connected: `02_Ultra.py`, `03_LineTracking.py`, `08_Mpu6050.py`, `10_IR_Receiver.py`, `12_Battrey_Level.py`, and `13_LightTracking.py`.
3. Test the individual indicator outputs (`04_WS2812.py`, `06_LED.py`, `07_OLED.py`, `09_Buzzer.py`, and `11_RGB.py`) one at a time.
4. Test moving outputs last. Use one unloaded servo for `01_Servo.py`. For `05_Motor.py`, secure the robot with wheels clear and be ready to stop the program. Do not run multiple examples at once.

A successful software example does not establish that D1 is healthy. Record the actual board revision, supply, connected loads, and observed readings separately from this source index.