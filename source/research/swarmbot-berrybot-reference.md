---
title: "BerryBot reference for SwarmBot education"
description: "Reference notes on BerryBot as an educational hardware and programming comparison for SwarmBot."
date: 2026-09-22
tags:
  - research
  - educational-robotics
  - rp2040
  - micropython
  - arduino
  - robotics
status: reference
authority: Chartroom
---

# BerryBot reference for SwarmBot education

## Scope

This page records reference information from the supplied BerryBot booklet. BerryBot is an educational mobile robot kit intended to teach assembly, programming, sensing, and basic autonomous behaviours. It is particularly relevant to the planned SwarmBot and Test in a Box educational direction. The material is useful as a teaching and interface reference; it is not a Chartroom implementation, project requirement, or validation of the Robots project's control architecture.

## Hardware overview

The booklet describes a robot built from a wooden and plexiglass chassis with two DC motors, wheels, a small support wheel, an HC-SR04 ultrasonic distance sensor, a line-tracker sensor, two light sensors, an infrared receiver, a buzzer, six RGB LEDs, a 5 × 5 LED matrix, a button, a servo connector, an I²C connector, an ADC connector, and a Bluetooth module.

The main board is based on an RP2040 microcontroller. It includes USB-C, BOOTSEL and reset controls, a battery holder, motor connections, and labelled expansion or sensor interfaces. The booklet presents the board as a combined teaching platform rather than as a general-purpose robot-computer architecture.

## Programming environments

The documented programming routes are:

- PicoBricks IDE for block-based programming;
- PicoBricks IDE's text-based PicoPy/MicroPython environment;
- Thonny IDE for MicroPython;
- Arduino IDE for C/C++; and
- PicoBricks Go! for Bluetooth control and pre-made modes.

The Thonny workflow requires the BerryBot firmware and `berrybot.py` library to be loaded onto the board. The booklet points to the BerryBot GitHub repository for the firmware and to a short link for the library. These external links should be checked before being treated as current installation instructions.

The sample activities include blinking or changing RGB LEDs, driving the buzzer from a button, and using the mobile application to control the matrix, RGB LEDs, and robot movement.

## Behaviour examples

The booklet documents four pre-made behaviours:

- obstacle avoidance using the front ultrasonic sensor;
- line following using the underside line-tracker sensor;
- sumo behaviour using the line sensor and front distance sensor; and
- light following using left and right light sensors.

It also describes infrared remote control using the direction buttons on the supplied remote. These examples are useful for teaching event loops, sensor thresholds, motor commands, and simple state logic. They should not be interpreted as autonomous-navigation capability or as evidence for the project's Testbot, Nav2, NATS, or safety systems.

## Pinout reference

The final booklet page provides a BerryBot pinout for the RP2040 board. The labelled assignments include:

- Motor A: GPIO22–GPIO25;
- Motor B: GPIO10–GPIO13;
- ultrasonic trigger and echo: GP8 and GP9;
- line tracker: GP26 and GP27;
- left and right light sensors: GP29 and GP28;
- infrared receiver: GP20;
- buzzer: GP14;
- I²C: GPIO6 and GPIO7;
- UART: GP10 and GP11 as shown in the diagram;
- RGB LED and matrix-related connections across the GPIO assignments; and
- RP2040 power, reset, oscillator, ADC, and ground pins.

The diagram should be treated as board-revision-specific. The extracted text representation cannot preserve the diagram's physical layout, and the booklet should be consulted before wiring or assigning a pin. Any project firmware should verify the actual board revision and library definitions rather than relying on this summary alone.

## Relevance to SwarmBot and Test in a Box

BerryBot is useful as a compact example of an educational progression:

```text
Assembly
  -> block programming
  -> MicroPython or Arduino
  -> sensor-driven behaviour
  -> repeatable exercises and debugging
```

It may inform beginner tutorials, small-robot sensor exercises, and comparisons of RP2040-based educational platforms. Its staged progression from block programming to MicroPython or Arduino, then to sensor-driven behaviours, is a useful comparison for the planned SwarmBot classroom workflow.

BerryBot should remain a reference platform rather than a hardware dependency. SwarmBot's own robot-control, communications, safety, multi-robot, and physical-test decisions must be defined separately. The BerryBot pinout is not a SwarmBot pinout, and the booklet does not establish compatibility with NATS, ROS 2, HiL/SiL, or the Testbot.

## Provenance

- Source: user-supplied [BerryBot Project booklet](evidence/berrybot-project-booklet.pdf).
- Source title: BerryBot booklet; the PDF filename was supplied as `BERRYBOT+KİTAPÇIK.pdf`.
- Source length: 54 pages.
- Named organisations and products: Robotistan, PicoBricks, PicoBricks IDE, PicoBricks Go!, Thonny, and Arduino IDE.
- Hardware reference reviewed: pages 1–9 and 53–54; programming and behaviour sections reviewed across pages 10–52.
- Status: reference only; source copyright and publication permissions have not been assessed.
