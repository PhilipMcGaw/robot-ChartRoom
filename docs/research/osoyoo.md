# OSOYOO robotics research notes

OSOYOO is a useful reference for **educational, low-cost robotics and staged learning** rather than as a source of architecture to copy. Its current catalogue spans Arduino, ESP32, Raspberry Pi, Raspberry Pi Pico, Micro:bit, sensors, motor-driver boards, robot-car platforms, mecanum vehicles, tank vehicles, displays, and IoT learning kits. citeturn0search0

This is comparative research and design inspiration, not a specification or project dependency.

## Educational progression

OSOYOO's material explicitly distinguishes between simple microcontroller projects and more complex Raspberry Pi robotics. Its Raspberry Pi robot-car documentation explains that Arduino is well suited to simple sensor/actuator logic, while a Raspberry Pi adds Linux, substantially more processing capability, web applications, databases, computer vision, AI/ML, and broader programming-language support. citeturn0search12turn0search13

This is relevant to the **Test in a Box** and **SwarmBot** educational direction because it suggests a useful progression rather than forcing one computing platform on every learner:

- simple MCU exercises;
- sensor and actuator programming;
- motor control and feedback;
- networked robot control;
- Linux/SBC robotics;
- web-based operator interfaces; and
- computer vision/autonomy.

The exact OSOYOO curriculum should not be treated as the intended ChartRoom curriculum, but the progression is worth studying.

## Robot platforms

The current OSOYOO catalogue contains a broad range of robot-car architectures, including differential-drive cars, servo-steering cars, mecanum platforms, tank-style vehicles, Raspberry Pi robots, ESP32 robots, and compact platforms. citeturn0search0turn0search1

Useful comparisons include:

- **differential drive** as a simple starting point for SwarmBot;
- **mecanum drive** as an optional experiment in holonomic motion;
- **servo steering** as a comparison with conventional Ackermann-like vehicle control;
- **tank tracks** as a comparison for MarsBot terrain experiments; and
- **Raspberry Pi robot platforms** as simple test vehicles for Cockpit and networked control.

The important lesson is not that every drive type should be supported. It is that Cockpit and the underlying control interfaces should describe vehicle capabilities rather than assuming one particular mechanical arrangement.

## Raspberry Pi and web control

OSOYOO's Raspberry Pi robot material uses the Pi as a Linux computer and teaches users to control the robot from a web browser, including camera-based operation. The documentation provides step-by-step Linux, Python, GPIO, web-control, and camera examples. citeturn0search13

This is directly relevant to **Cockpit** as an educational reference. It demonstrates a progression from physical robot hardware to a browser-accessible operator interface without requiring a specialist ground-station computer.

Compare this with the project's intended architecture:

**Browser → Cockpit → NATS → Control → hardware**

rather than coupling the browser directly to GPIO or motor-driver implementation.

## Hardware abstraction and modularity

OSOYOO sells and documents discrete motor-driver boards, I/O breakout boards, sensor modules, displays, and single-board-computer accessories alongside complete robots. citeturn0search0

This is useful as a reference for **SwarmBot educational hardware modules**. Students can learn one subsystem at a time before assembling a complete robot.

Potential ChartRoom design principle:

> A learning platform should expose useful subsystems independently before requiring the learner to understand the entire vehicle.

This aligns with the existing interest in replaceable SwarmBot payloads, optional displays, and a constrained Test in a Box programming interface.

## MarsBot relevance

OSOYOO is less relevant to MarsBot's eventual mechanical architecture than JPL Open Source Rover or Sawppy, but its range of inexpensive drive platforms is useful for **early mobility experiments**.

Potential uses include:

- differential-drive control experiments;
- encoder and motor-control experiments;
- obstacle sensing;
- camera integration;
- simple autonomous navigation;
- alternative drive-geometry experiments; and
- rapid prototyping before committing to a larger rover chassis.

The OSOYOO Mars Explorer and mecanum platforms are particularly worth keeping as comparative references, but they should not drive the MarsBot mechanical design. citeturn0search1

## Engineering and documentation lessons

OSOYOO's strongest value may be the sheer quantity of build and tutorial material. The Raspberry Pi robot documentation includes hardware lists, wiring information, installation instructions, example software, and staged lessons. citeturn0search13

This is worth comparing with the project's own documentation goals:

- complete bill of materials;
- explicit wiring and interface information;
- staged bring-up;
- known-good example programs;
- troubleshooting guidance;
- progression from basic to advanced exercises; and
- clear separation between educational examples and production architecture.

The documentation is aimed at learning rather than engineering assurance, so it should not be treated as a substitute for formal electrical, software, or safety specifications.

## Design cautions

OSOYOO's catalogue spans many generations of products and tutorials. Hardware and software combinations therefore need to be evaluated individually rather than assuming that a current product, old tutorial, and different controller revision are interchangeable. The site currently lists both long-established Arduino/Raspberry Pi products and newer ESP32-based platforms. citeturn0search0

For ChartRoom, use OSOYOO primarily for:

- educational progression;
- low-cost robot platform comparisons;
- subsystem teaching;
- browser-based control examples; and
- documentation/bring-up inspiration.

Do not adopt OSOYOO's hardware, software, Blynk/MQTT examples, or specific robot-control architecture as project dependencies. In particular, this does not change the existing **NATS** decision for the Robots ecosystem.

## Sources

- [OSOYOO](https://osoyoo.com/)
- [OSOYOO Raspberry Pi Robot Car documentation](https://osoyoo.com/manual/2020005500.pdf)
- [OSOYOO Raspberry Pi Robot Car introduction](https://www.osoyoo.com/picture/RPi_Robot_Car/Rpi_car_manual.pdf)

**Status:** Research / educational robotics reference. No OSOYOO hardware or software dependency is planned.

**Read later:** Review the current ESP32, Raspberry Pi, differential-drive, mecanum, and Mars Explorer platforms, concentrating on their curriculum structure, interfaces, and documentation rather than product selection.
