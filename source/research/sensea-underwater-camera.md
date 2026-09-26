---
title: "Sensea Raspberry Pi underwater camera"
description: "Reference notes on the Sensea low-cost underwater camera and environmental logger."
date: 2026-09-26
type: research
status: reference
authority: Chartroom
tags:
  - research
  - raspberry-pi
  - underwater
  - camera
  - environmental-monitoring
---

# Sensea Raspberry Pi underwater camera

## Scope

This note summarises Raspberry Pi's report on Sensea, a low-cost underwater camera and water-temperature logger built by Unboxed STEM Club. It is a reference for underwater observation and data logging, not a validated enclosure design or a project requirement.

## Reported design

The reported build uses a Raspberry Pi 3 Model B+, Raspberry Pi Camera Module 3, DS18B20 waterproof temperature probe, PCF8523 real-time clock, and microSD storage. A Python logger captures ten-second video clips and writes timestamped temperature readings locally. The camera uses fixed focus because the builders found autofocus unreliable in water with suspended particles.

The electronics sit on a custom 3D-printed base inside a transparent acrylic tube. One end is sealed with a bonded acrylic disc; a cable gland passes the temperature probe cable through the enclosure, and an expanding plumbing test plug closes the other end. A 2 kg dumbbell provides ballast for the reported lake and river deployments. The builders describe a five-minute bucket leak check before deployment.

These details are reported by the article; they do not establish a pressure rating, maximum operating depth, long-term seal life, or suitability of the same ballast and enclosure for another vehicle.

## Relevance to the Robots project

Sensea is a **static, recoverable observation payload**, not an ROV system. It sinks to the bottom, records locally, and is recovered for footage and data. The article does not describe tethered live video, remote piloting, propulsion, or integration with BlueOS or Blue Robotics Cockpit.

The project could use it as inspiration for a staged camera-and-environmental-sensor experiment alongside the planned Raspberry Pi 4B and Adeept HAT work:

- first verify camera capture and temperature logging on the bench;
- then evaluate video handling separately from the Cockpit telemetry and control paths;
- retain local recording as a possible fallback if a live link is unavailable; and
- treat enclosure and ballast design as a separate mechanical and pressure-validation task.

This is a possible adaptation, not an approved design. The Sensea build uses a Raspberry Pi 3B+ and its own enclosure and logging script; the article does not show that its software works on BlueOS.

## I²C address consideration

Sensea reports using a PCF8523 real-time clock. NXP assigns the PCF8523 the I²C address `0x68`. The NautiPi reference for the Adeept ADM133 HAT V3.1 lists the optional MPU6050 module at the same address, `0x68`.

If both devices are fitted to the same I²C bus, this is an address collision risk: standard address scanning cannot distinguish two devices responding at the same address. Confirm the fitted HAT revision and whether its MPU6050 module is installed before connecting an RTC. If both functions are needed, assess a separate bus or an appropriate I²C multiplexer before wiring; do not assume the address can be changed.

This is a compatibility inference from the published device addresses. It has not been checked on the project's physical Pi/HAT assembly.

## Limitations and evidence boundary

- The reported five-minute bucket check is a basic leak check, not a hydrostatic pressure test or a certified depth rating.
- The article gives no controlled comparison of image quality, focus distance, recording duration, or temperature accuracy.
- The 2 kg ballast is specific to the reported enclosure and deployment; it must not be copied without buoyancy and recovery analysis.
- A successful Sensea recording would demonstrate that a camera and logger captured data in that setup. It would not validate ROV camera latency, Cockpit display, BlueOS integration, or the project's pressure housing.

## Provenance

- Raspberry Pi, “Sensea underwater camera — Raspberry Pi Official Magazine #170”, published 2026-09-25: [article](https://www.raspberrypi.com/news/sensea-underwater-camera-raspberry-pi-official-magazine-170/).
- Project instructions linked by the article: [Sensea: DIY Underwater Explorer With Raspberry Pi, Camera & Temperature Sensor](https://www.instructables.com/Sensea-DIY-Underwater-Explorer-With-Raspberry-Pi-C/).
- NXP Semiconductors, *PCF8523 Real-Time Clock (RTC) and calendar*, Rev. 7, 2015-04-28: [datasheet](https://www.nxp.com/docs/en/data-sheet/PCF8523.pdf), I²C address stated as `1101000` (7-bit `0x68`).
- NautiPi, [Adeept ADM133 Robot HAT V3.1 interfaces](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/ROV%20-%20Main%20Body/docs/reference/adeept-robot-hat-adm133-interfaces.md), for the HAT's PCA9685, ADS7830, and optional MPU6050 address mappings.
- Status: reference only; no Sensea-derived hardware has been built or tested in the Robots project.
