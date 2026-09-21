---
title: "GY-91 MPU-9250/9255 IMU module assessment"
description: "Assessment of the pictured GY-91 10-DOF sensor module for the Robots project."
date: 2026-09-21
tags:
  - research
  - imu
  - sensors
  - hardware
  - rov
status: assessed
---

# GY-91 MPU-9250/9255 IMU module assessment

## Summary

The pictured module is a GY-91 10-DOF board, normally advertised as containing an MPU-9250 or MPU-9255 motion sensor and a BMP280 barometric pressure sensor.

It is suitable for low-cost bench testing, Raspberry Pi experimentation, and experimental ROS 2 sensor input. It is not recommended as the primary IMU or depth-control sensor for the ROV.

## Assessment

### Motion sensing

The MPU-9250 provides a three-axis accelerometer, three-axis gyroscope, and three-axis magnetometer. The device supports configurable accelerometer ranges of ±2, ±4, ±8, and ±16 g, gyro ranges of ±250, ±500, ±1,000, and ±2,000 degrees per second, and I²C or SPI host interfaces.

This makes the board useful for:

- bench calibration and motion testing;
- experimental Raspberry Pi attitude sensing;
- non-safety-critical sensor acquisition;
- early ROS 2 or simulation-interface experiments.

The board is not a drop-in replacement for the MPU6050 mentioned in earlier Chartroom planning. It requires its own driver and register configuration.

### Magnetometer limitations

The magnetometer should not be treated as a reliable underwater heading source without calibration and testing. ROV motors, current-carrying conductors, steel hardware, nearby electronics, and the vehicle structure can distort the magnetic field.

Heading quality would need to be demonstrated on the assembled vehicle rather than assumed from the component specification.

### Pressure sensor limitations

The BMP280 is an atmospheric barometric pressure sensor with an operating range of approximately 300–1,100 hPa. It is intended for applications such as altitude estimation and environmental sensing.

It is not a submerged water-pressure sensor and must not be used as the ROV depth sensor. Depth measurement requires a suitable pressure transducer, pressure interface, calibration process, and pressure-rated mechanical arrangement.

### Supply and interface

The MPU-9250 silicon requires low-voltage digital operation. GY-91 boards vary, and some include regulators or level shifting while others do not. The exact board should be checked before connecting it to a Raspberry Pi.

Before use:

1. confirm the actual fitted sensor by reading its identity registers;
2. confirm whether the board accepts 5 V power or requires 3.3 V;
3. confirm the logic levels and pull-ups;
4. test I²C and SPI behaviour independently;
5. record the actual chip identity as MPU-9250, MPU-9255, or another device.

GY-91 boards are not necessarily consistent across vendors. A board labelled MPU-9250 may contain an MPU-9255 or a lower-quality substitute.

## Recommendation

Use this module as an inexpensive experimental external IMU only.

Do not use it as:

- the primary ArduSub stabilisation sensor;
- the primary depth-control sensor;
- a safety-critical vehicle-control sensor;
- evidence that the final vehicle sensor architecture has been validated.

For the production control path, prefer a supported autopilot or flight-controller board with a known IMU, validated sensor drivers, calibration support, and defined failure behaviour. Use a dedicated underwater pressure sensor for depth.

## Proposed validation path

If the module is purchased, perform these checks before integrating it into the vehicle:

- identify the fitted motion sensor and pressure sensor;
- verify supply voltage and logic levels;
- collect raw accelerometer, gyro, magnetometer, and temperature data;
- measure gyro bias and noise while stationary;
- calibrate accelerometer and magnetometer offsets and scale;
- test magnetic distortion near the intended motors, wiring, enclosure, and frame;
- compare attitude estimates against a known reference;
- verify sensor timestamps and missing-data handling;
- keep the module outside the safety-critical control loop until the results are documented.

## Sources

- TDK InvenSense, [MPU-9250 Product Specification](https://invensense.tdk.com/wp-content/uploads/2015/02/PS-MPU-9250A-01-v1.1.pdf). The MPU-9250 is now listed as obsolete, with the ICM-20948 given as a recommended alternative; compatibility is not guaranteed.
- Bosch Sensortec, [BMP280 product page](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp280/). The BMP280 is specified as an atmospheric pressure sensor with a 300–1,100 hPa operating range.
- User-supplied product screenshot: Y:/Photos/IMG_7781.PNG, reviewed 2026-09-21. The listing identifies the board as a GY-91 10-DOF module with MPU-9250 and barometric pressure sensing. The listing alone does not verify the fitted silicon or board revision.

## Confidence

- GY-91 board category: Medium.
- MPU-9250/9255 and BMP280 contents on this specific board: Unverified until read from the hardware.
- Suitability for experimental IMU work: Medium to High.
- Suitability for ROV depth measurement: High confidence that the onboard BMP280 is unsuitable.
- Suitability for primary safety-critical vehicle control: Not recommended.
