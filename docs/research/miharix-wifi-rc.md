# Miharix WiFi RC

## Source

- [Miharix WiFi RC](https://github.com/miharix/miharix-wifi-rc)

## Summary

Miharix WiFi RC is a deliberately inexpensive WiFi remote-control platform built around an ESP-12E/ESP8266. The project was designed for classroom use: the author wanted a system that could be built by a full class at roughly €15 per student, without requiring a dedicated phone application or Internet connection.

The vehicle/control interface is browser-based and can be operated from a phone, tablet, or PC. The repository includes PCB design material, a simple 3D-printed enclosure, Arduino examples, Python PC-control examples, documentation, and manufacturing files.

The author reports classroom and summer-camp use with around 300 students and a ground-range test of approximately 90 m before loss of signal and vehicle stop.

## Relevance to Cockpit and SwarmBot

This is a useful reference for the idea that **Cockpit can be a browser-accessible robotics interface without requiring a specialised client application**.

It reinforces several existing directions:

- browser-first robot operation;
- no Internet requirement for local robot control;
- low-cost hardware suitable for education;
- a common operator interface across phones, tablets, and computers;
- simple logical control channels rather than exposing hardware-specific details to the operator; and
- a progression from simple RC control towards programmable robotics.

The project is particularly relevant to the planned **SwarmBot classroom mode** and Test in a Box. A classroom should not need to install a different application on every student's device simply to operate a robot.

## Architecture lessons

The WiFi RC module is intentionally much simpler than the current Robots architecture. It is therefore not a direct architectural model for NATS or the Control service. Its value is primarily at the **human-interface boundary**.

A useful distinction is:

- **browser UI:** generic user interaction and command generation;
- **robot control:** bounded interpretation of commands and actuator control;
- **communications:** transport between the operator and vehicle;
- **hardware:** MCU, motor/servo outputs, and sensors.

That maps well onto the desired separation between Cockpit, Control, NATS, and the vehicle hardware.

## Educational lessons

The repository is unusually relevant to the educational side of the project because it includes:

- a low-cost BOM;
- PCB and DIY construction information;
- 3D-printed enclosure material;
- Arduino programming examples;
- Python PC-control examples; and
- practical deployment experience in classrooms.

This is a good reference for making Test in a Box and SwarmBot accessible without making the underlying production architecture unnecessarily simple.

## Design cautions

The project uses direct WiFi RC control and is not a suitable replacement for the NATS-based architecture. Its reported range is also a project-specific ground test, not a general RF-performance specification.

For SwarmBot, WiFi should be treated as a transport option while safety, command bounds, neutral behaviour, timeout handling, and E-stop remain responsibilities of the robot-control layer.

## Status

**Research / educational and operator-interface inspiration.** No dependency on the Miharix hardware or software is planned.
