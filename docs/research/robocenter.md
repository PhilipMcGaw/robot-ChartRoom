# RoboCenter ROV research notes

RoboCenter is a useful reference for the ROV project because its surviving documentation covers the complete vehicle stack: mechanical construction, thrusters, payloads, onboard control, operator software, simulation, and practical testing.

This page records ideas worth revisiting. It is **inspiration and comparative research, not a specification**. We should not copy RoboCenter implementations or make its architecture a dependency.

## Mechanical

- **Open thruster design:** study the OpenThruster projects as a reference for inexpensive, inspectable thruster construction and modular propulsion hardware.
- **Thruster guards and meshes:** consider the value of replaceable guards/ducts as both mechanical protection and a configurable part of the vehicle design.
- **Modular vehicle structure:** retain the idea of a simple frame with defined attachment points so propulsion, buoyancy, cameras, lights, and payloads can be changed without redesigning the whole vehicle.
- **Payload modularity:** treat manipulators, cameras, and other payloads as replaceable modules rather than hard-coded vehicle functions.
- **Buoyancy and sealing as first-class design work:** include buoyancy, pressure/sealing, cable routing, and serviceability in the same design loop as the frame and electronics.

## Electrical and embedded systems

- **Distributed propulsion/control:** study the separation between high-level vehicle commands and the low-level actuator/sensor layer. This is compatible with the existing ROV Control boundary, while leaving NATS as the project communications layer.
- **Telemetry at the actuator boundary:** capture useful motor/driver state and expose it through the normal vehicle telemetry model rather than treating propulsion as a black box.
- **Configurable I/O and payload interfaces:** define a clear interface for additional sensors, lights, cameras, manipulators, and future payload electronics.
- **Practical underwater wiring:** study RoboCenter's approach to power distribution, Ethernet/controller links, sealed electronics, and service connections as a comparison against the ROV electrical architecture.
- **Protection and failure behaviour:** use the older thruster specifications and manuals as prompts to document current limiting, loss-of-communications behaviour, actuator faults, and safe-state behaviour explicitly.

## Software architecture

The HighROV documentation provides a useful conceptual decomposition:

1. receive commands from the operator interface;
2. update sensors;
3. update vehicle telemetry;
4. control thrusters from the latest command and vehicle state;
5. publish actuator telemetry;
6. control payloads and publish payload telemetry; and
7. return telemetry to the operator interface.

This is particularly relevant to the existing **Cockpit → Control → Datalogger** separation. The useful lesson is the ownership of responsibilities, not the specific implementation or protocol.

- **Payload abstraction:** investigate the `PayloadTool` idea (`init`, `update`, `commit`) as a possible conceptual model for Cockpit/Control payload plugins.
- **Vehicle profiles:** consider configuration describing available thrusters, payloads, sensors, limits, and controls rather than embedding every vehicle-specific assumption in Cockpit.
- **Common simulator/programming environment:** study MUR IDE and the competition simulator as examples of keeping vehicle software, telemetry, control, camera viewing, and simulation accessible from one development workflow.

## Cockpit / operator UI

The HighROV UI is particularly relevant to the current Cockpit work. Its central camera view is surrounded by dedicated operator functions rather than trying to put everything into one instrument.

Useful ideas to evaluate:

- central live video with supporting telemetry;
- dedicated telemetry and diagnostic/message areas;
- configurable thrust limiting;
- explicit controller/regulator controls;
- integrated logging;
- configurable gamepad control;
- clear separation between normal operation and engineering/debug information; and
- a UI that can be used as a starting point for a custom vehicle rather than being tied to one fixed hardware build.

These ideas fit the current goal of making Cockpit a generic robotics operator interface. They should be compared with Blue Robotics Cockpit and other ROV interfaces before implementation decisions are made.

## HiL / SiL and testing

RoboCenter's simulator and MUR IDE suggest several useful test directions:

- run control software against a simulated vehicle before connecting hardware;
- exercise repeatable missions and operator workflows in simulation;
- test telemetry and UI behaviour without a pool test;
- keep air/debug tests separate from wet/pool tests;
- use the same conceptual vehicle model for simulation and hardware where practical; and
- record enough state to reproduce a failure after a test.

This supports the existing **ROV - HiL-and-SiL** direction and the aim of making simulation a normal engineering tool rather than a separate demonstration system.

## Sources

### Primary RoboCenter material

- [RoboCenter materials index](https://robocenter.net/materials/) — surviving project and software material.
- [OpenThruster 150](https://robocenter.net/projects/openthruster-150/) — open thruster project.
- [OpenGrabber](https://robocenter.net/projects/opengrabber/) — modular manipulator/grabber reference.
- [Thruster meshes and guards](https://robocenter.net/projects/mesh/) — propulsion protection and mechanical reference.
- [HighROV Manual](https://robocenter.net/media/documents/HighROV_Manual_RUS.pdf) — vehicle software, telemetry, payload, and control workflow.
- [HighROV 2022 Manual](https://robocenter.net/media/documents/%D0%A0%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE_HighROV_2022.pdf) — operator UI, control computer/network, telemetry, logging, and custom-UI reference.
- [HighROV 2019 Manual](https://robocenter.net/media/documents/HighROV_Manual_RUS_04.07.2019_v.8_qvzHO4f.pdf) — payload abstraction and earlier software architecture.
- [MUR Thruster 200 specification](https://robocenter.net/documents/77/%D0%A1%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F_MUR_Thruster_200.pdf) — propulsion electrical/mechanical specification.
- [MUR simulator](https://simulator.robocenter.org/) — simulation and competition environment.
- [MUR firmware](https://github.com/murproject/rov_firmware) — implementation reference for the vehicle-control concepts described in the manuals.
- [RovUI](https://github.com/murproject/RovUI) — operator-interface implementation reference.

### Related educational material

- [Marine school material](https://marine.robocenter.org/news/425) — underwater robotics electronics, communications, CAD, sealed devices, programming, and testing.
- [2021 marine robotics school](https://marine.robocenter.org/news/300) — OpenThruster construction, frame design, buoyancy, payloads, controller/electronics design, and air/pool debugging.

## Questions to answer later

- Which parts of RoboCenter's payload abstraction would improve our existing Control/Cockpit boundary without adding unnecessary complexity?
- Should ROV vehicle profiles describe payloads and actuator limits in configuration, and if so, where should that configuration live?
- Which UI functions belong in Cockpit core versus vehicle-specific plugins/modules?
- Can the existing ROV HiL/SiL environment reproduce the useful MUR simulator workflow while retaining our NATS architecture?
- Which propulsion telemetry is worth standardising before adding more actuator hardware?
