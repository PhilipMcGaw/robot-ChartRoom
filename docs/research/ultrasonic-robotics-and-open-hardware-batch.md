# Ultrasonic robotics, open hardware, and educational references

**Status:** Research / read later  
**Added:** 2026-09-09

## Sources

- [SonicDisc: A 360° Ultrasonic Scanner](https://www.hackster.io/platisd/sonicdisc-a-360-ultrasonic-scanner-211e6a)
- [MicBooster ultrasonic microphone board](https://micbooster.com/product/ultrasonic-mic-board/)
- [OZ Robotics robotic kits](https://ozrobotics.com/product-category/robotics/robotic-kits/)
- [WiFi penetration testing with an ESP32](https://hackaday.com/2021/05/27/wifi-penetration-testing-with-an-esp32/)
- [OpenROV GitHub organisation](https://github.com/OpenROV/)
- [Obsidian ESP32](https://www.crowdsupply.com/thomas-mckahan/obsidian-esp32)
- [Arduino Drawing Robot / Engineering Kit material](https://www.instructables.com/Using-an-Arduino-Drawing-Robot-with-Hour-of-Code-T/)

## SonicDisc — inexpensive 360° ranging

SonicDisc is an open-source, Apache-2.0 project using eight HC-SR04 ultrasonic sensors around an ATmega328P to create a circular proximity view. It demonstrates obstacle following and autonomous parking using the same sensing platform. The project is especially interesting because the sensing hardware is deliberately cheap, distributed, and application-agnostic.

### Relevance

- Potential low-cost proximity ring for SwarmBot or other small terrestrial robots.
- Useful reference for sensor abstraction: expose distance plus bearing rather than tying the application directly to individual ultrasonic devices.
- Good educational/Test in a Box example because the same sensor interface can support obstacle detection, following, parking, and validation exercises.
- Worth comparing with 2D LiDAR on Maker's Pet: ultrasonic gives a much cheaper but lower-resolution spatial model.

## Ultrasonic microphone board

MicBooster's ultrasonic microphone board uses a Knowles SPU0410LR5H-QB ultrasonic-capable microphone. This is a useful reminder that ultrasonic sensing need not be limited to reflected-pulse distance measurement: a microphone-based receiver can support acoustic measurement, localisation, or experimentation with active/passive ultrasonic signals.

### Relevance

- Possible experimental acoustic sensing for ROV/subsea work.
- Could support investigations into ultrasonic beacon detection or localisation.
- Potential Smart Buoy environmental/acoustic sensing reference, although suitability, waterproofing, bandwidth, and signal-processing requirements would need engineering validation.

## OZ Robotics

OZ Robotics is useful primarily as a catalogue of robotics-kit approaches rather than as a specific architectural reference. It is worth browsing for mechanical packaging, educational progression, actuator/sensor combinations, and examples of how complex robotics concepts are reduced to accessible kits.

### Relevance

- Inspiration for modular educational robot kits.
- Useful when considering how SwarmBot or Test in a Box hardware could be packaged for repeatable construction.
- Look for reusable mechanical and electronics modules rather than adopting a particular kit.

## ESP32 wireless security project

The Hackaday ESP32 Wi-Fi penetration-testing project is relevant mainly as an ESP32 capability reference. It demonstrates that an inexpensive ESP32-class controller can combine Wi-Fi functionality with a purpose-built embedded application and user interface.

### Relevance

- Useful reminder that ESP32 hardware can provide substantial networking capability at low power.
- Relevant to Smart Buoy and other remotely deployed embedded nodes.
- Security-testing capabilities should remain isolated from normal vehicle/control firmware; this is not a reason to incorporate penetration-testing functions into Cockpit or vehicle control systems.

## OpenROV

The OpenROV GitHub organisation is an important historical reference for open-source ROV development. It is useful alongside Blue Robotics, ArduSub, and the other ROV projects already tracked in ChartRoom.

### Relevance

- Historical open-source ROV electronics/software architecture.
- Useful for understanding the evolution from DIY ROVs toward integrated vehicle/control ecosystems.
- Potential reference for modular subsea hardware, tethered operation, vehicle control, and operator software.
- Compare its historical approach with the current ROV split of Cockpit, Control, and Datalogger, with NATS as the internal messaging layer.

## Obsidian ESP32 — Raspberry Pi form factor for a microcontroller

Obsidian ESP32 combines an ESP32-WROVER-B with a Raspberry Pi-compatible physical form factor and 40-pin expansion header. It supports the ESP32 Arduino core, MicroPython, and ESP-IDF, with I²C, SPI, UART, I²S, GPIO expansion, and substantial flash/PSRAM. The project was designed in KiCad and released as open hardware under CERN OHL v1.2. citehttps://www.crowdsupply.com/thomas-mckahan/obsidian-esp32

### Relevance

- Strong reference for bridging the physical ecosystem of SBCs with the real-time/low-power characteristics of microcontrollers.
- Useful architectural inspiration for Smart Buoy nodes and small robot peripherals where Linux is unnecessary.
- Particularly relevant to the principle of keeping hardware interfaces portable between an SBC and MCU implementation.
- The Pi-compatible form factor is interesting, but the concept matters more than the historical ESP32-WROVER hardware.

## Arduino Drawing Robot / Engineering Kit

The drawing-robot material demonstrates a complete engineering workflow around a physical robot: connect to the controller, command individual actuators, calibrate and test motion, map motor commands into Cartesian movement, define working limits, process an image, and generate motion commands. The broader Arduino Engineering Kit material also explicitly combines hardware, MATLAB/Simulink, geometry, physics, and image processing.

### Relevance

- Excellent Test in a Box teaching pattern: start with direct actuator control, then calibration, then coordinate transforms, then application-level behaviour.
- Useful model for progressive HiL/SiL exercises where the same control abstraction is tested first in software and then against hardware.
- The separation between low-level motor control and higher-level path generation is directly relevant to the ChartRoom vehicle architecture.
- Could inspire a simple drawing/plotting mechanism as a non-ROV validation platform for kinematics and command interfaces.

## Cross-project lessons

1. **Cheap sensors can be valuable when the interface is general.** SonicDisc is more interesting as a reusable spatial-sensing interface than as an HC-SR04-specific design.
2. **MCU and SBC roles should remain separable.** Obsidian ESP32 is a useful example of a microcontroller taking advantage of an SBC-style hardware ecosystem without requiring Linux.
3. **Educational robots benefit from staged abstraction.** Direct actuator control → calibrated motion → coordinate system → behaviour → autonomy is a useful pattern for Test in a Box and HiL/SiL.
4. **Open-source ROV history matters.** OpenROV should be considered alongside Blue Robotics and ArduPilot/ArduSub when studying ROV architecture and evolution.
5. **Ultrasonic sensing has several distinct use cases.** Time-of-flight ranging, passive acoustic reception, active acoustic localisation, and environmental acoustic sensing should not be conflated; each needs its own transducer, analogue front end, signal processing, and validation strategy.

## Read later

- Compare SonicDisc's multi-sensor ultrasonic ring with the Maker's Pet 2D LiDAR approach.
- Inspect the OpenROV repositories for historical electronics, control, and operator-interface architecture.
- Investigate ultrasonic/acoustic sensing as a possible ROV or Smart Buoy payload.
- Review the Obsidian ESP32 hardware files for MCU/SBC interface ideas, without treating the historical board as a current hardware recommendation.
- Extract a staged Test in a Box exercise from the Drawing Robot progression: actuator → calibration → kinematics → path → validation.
