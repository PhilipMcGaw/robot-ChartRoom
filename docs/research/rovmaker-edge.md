# RovMaker Edge research notes

RovMaker Edge is an open-source underwater robot project from ROVMAKER, created as an educational and exploratory ROV and based on ArduSub. It is a useful historical reference for physical ROV architecture, pressure housing, buoyancy, penetrators, propulsion, and integration of Raspberry Pi and Pixhawk-class hardware.

This is comparative research and design inspiration, not a specification or project dependency.

## Mechanical architecture

- six-thruster configuration: two vertical thrusters and four horizontal thrusters;
- approximately 430 × 390 × 220 mm overall frame size;
- 12 mm HDPE frame plates with CNC-machined mounting parts;
- modular mounting slots for the watertight enclosure, lights, and other equipment;
- separate battery and electronics pressure enclosures;
- CNC-machined aluminium pressure tubes/enclosures;
- acrylic end-cap arrangements and O-ring flange sealing; and
- serviceable enclosure mounting using a fixed front position and sliding rear slot.

The separation of battery and electronics pressure volumes is particularly worth comparing with the ROV electrical architecture.

## Buoyancy and trim

RovMaker describes the use of solid marine buoyancy material rated to approximately 6.5 MPa and 300 m, with adjustable lead ballast mounted low on the frame. Ballast quantity and position are adjusted to achieve nearly neutral but slightly positive buoyancy.

The useful lesson is not the particular material or target depth, but the explicit treatment of buoyancy and trim as adjustable system parameters. The frame provides slots so ballast can be moved and adjusted after the physical vehicle is assembled.

## Pressure housings and serviceability

The project gives unusually useful attention to practical pressure-housing details for an open ROV reference:

- cable penetrators are treated as modular interfaces;
- the same penetrator size can accommodate different functions, including a depth sensor or switch;
- vacuum plugs are provided as a means of checking enclosure sealing;
- multiple O-ring and end-cap arrangements are shown; and
- enclosure dimensions and mounting arrangements are documented.

These are useful references for defining a repeatable leak-test and service procedure rather than treating the pressure housing as a one-off mechanical component.

## Propulsion

The project starts its design process with the thruster. The six-thruster vector arrangement is explicitly defined before finalising the frame. The custom thruster uses a protected brushless motor and an integrated 30 A ESC, with the ESC mounted in an aluminium structure and sealed using resin for thermal management.

The published thruster figures include a 350 kV motor, 3S–6S operation, and a stated maximum current of 10 A. These figures should be treated as historical project data rather than requirements for the current ROV.

The project also describes testing the thruster/ESC using an NI PXI-based test platform. This is particularly relevant to the project's preference for characterising propulsion hardware before committing it to vehicle-level control.

## Electrical and control architecture

RovMaker Edge is based on ArduSub and uses a Pixhawk-class controller alongside Raspberry Pi computing. The project also experimented with alternative computing/control platforms including NI myRIO and Intel Edison.

This provides a useful comparison for the current architecture:

- high-level Linux computing;
- dedicated real-time vehicle-control hardware;
- separate power and electronics volumes; and
- defined interfaces between propulsion, sensors, communications, and the tether.

The specific ArduSub/Pixhawk architecture is not a requirement for the project. The useful lesson is the existence of a clear boundary between general-purpose computing and deterministic vehicle control.

## Sensors, connectors, and tether interfaces

The project shows modular subsea connectors, cable penetrators, an MS5837 depth-sensor option, underwater switches, and an interface carrying power and communications through the buoyancy/tether cable.

This is relevant to the project's distributed sensor and RS-485 work. In particular, the idea of standardising mechanical penetrator interfaces while allowing different electrical functions is worth considering for future ROV payload modules.

## Additional open ROV references

Several of the supplied references broaden the historical comparison beyond RovMaker itself:

### OpenROV electronics

The [OpenROV electronics repository](https://github.com/OpenROV/openrov-electronics) is a particularly useful hardware reference. It contains schematics, Gerbers, and data packages for several generations of controller, power, lighting, IMU/depth, topside adapter, and BeagleBone interface boards. The v2.6–v2.8 controller evolved into an all-in-one power/control board around an ATmega2560 with substantial I/O and a BeagleBone interface.

The important lesson is architectural rather than component-specific: an embedded controller can own deterministic I/O, power/control interfaces, and low-level sensors while a more capable Linux computer provides higher-level networking, video, and operator functionality. The repository's history is also useful for studying how a real open hardware platform evolved through multiple board revisions.

OpenROV's associated [Cockpit repository](https://github.com/OpenROV/openrov-cockpit) is relevant to the wider Cockpit research. It describes a web-centric tele-robotic control system with browser-based video, configurable gamepad/joystick control, telemetry recording, plugins, multiple motor configurations, and support for embedded Linux plus microcontrollers. This is strong historical evidence for the direction of a browser-based, vehicle-agnostic operator interface.

### TechMonkeyBusiness OpenSource ROV

The [TechMonkeyBusiness OpenSource ROV](https://www.techmonkeybusiness.com/articles/OpenSource_ROV.html) is valuable less for its exact hardware and more for its engineering process. The project deliberately separates the control and video systems, uses two Arduinos over a long CAT5 tether for control data, monitors battery voltage, and documents experiments in long-cable serial communications, ESC calibration, sensor integration, thruster testing, pressure testing, wire sealing, and tether management.

Its pressure-vessel work is particularly useful: a uPVC pressure tube with O-ring end seals is analysed and pressure-tested, and the project includes dedicated experiments for cable-gland and wire-sealing techniques. The project also records practical bath and pool trials rather than stopping at CAD and bench testing.

These are useful reminders to treat tether communications, sealing, pressure testing, propulsion testing, and subsystem integration as engineering test subjects in their own right.

### Blue Robotics control-board discussion

The [Blue Robotics control-board comparison discussion](https://discuss.bluerobotics.com/t/control-board-options-pros-and-cons/812) provides a useful historical comparison between OpenROV and Blue Robotics controller approaches. The discussion highlights the current limits of the OpenROV 2.8 controller's power/current capability and the consequences of trying to drive more or larger thrusters than the board was designed for.

The main lesson is to treat controller selection as a system-level electrical design decision. Motor/ESC count, continuous and peak current, power-distribution capability, I/O, sensor interfaces, and desired operating envelope must be considered together rather than selecting a controller solely on processor capability or software features.

### ArduPilot ROV project discussion

The [ArduPilot ROV project discussion](https://discuss.ardupilot.org/t/your-own-remotely-operated-vehicle-rov-project/7951) contains a useful long-form example of a hybrid ROV evolving through several hardware configurations. The project combines OpenROV controller hardware, Blue Robotics T100/BlueESC propulsion, BlueROV2 mechanical components, Raspberry Pi, Pixhawk, Fathom-X, external power distribution, leak sensing, and pressure testing.

The discussion is particularly useful for the practical integration details: controller current limits can become the limiting factor even when the mechanical platform supports additional thrusters; power distribution may need to move outside a pressure housing; cable routing and watertight power connections can become major integration tasks; and vacuum testing of watertight compartments should precede water testing.

This provides a useful real-world comparison with RovMaker's separate power/electronics volumes and with the intended separation between ROV Control, onboard computing, and Cockpit.

## Relevance to the current ROV

The strongest areas for further comparison are:

- six-thruster vector layout and control allocation;
- separate battery and electronics pressure housings;
- modular penetrator and connector strategy;
- vacuum leak testing;
- adjustable ballast and trim;
- propulsion characterisation before vehicle integration;
- thermal management of ESC electronics;
- Raspberry Pi plus dedicated control hardware;
- controller current capability versus the actual propulsion envelope;
- separation of video and vehicle-control paths where appropriate;
- long-tether communications and power-distribution design; and
- documenting mechanical dimensions and service procedures sufficiently for reproduction.

The projects are particularly useful as a group because they provide several different approaches to the same engineering problem. OpenROV demonstrates an integrated embedded-controller/Linux architecture and an early browser-based Cockpit. TechMonkeyBusiness demonstrates low-cost, explicitly tested subsystem engineering. RovMaker demonstrates modular pressure housings, penetrators, ballast, and propulsion development. The Blue Robotics and ArduPilot discussions expose practical limits and integration problems encountered when combining these approaches.

These references should inform design reviews and test plans without turning the current ROV into a copy of any one historical platform.

## Engineering caveats

Although several of these projects are described as open-source, their documentation, licences, hardware availability, and maintenance status differ. Treat historical component specifications and performance claims as project data requiring independent engineering verification before reuse.

The RovMaker Edge Hackaday project currently shows limited uploaded project material and has not been actively developed for many years. OpenROV is also a historical platform, although its repositories remain useful for studying real hardware and software evolution. Forum discussions are valuable evidence of engineering experience but should not be treated as authoritative specifications.

## Status

**Research / ROV design inspiration.** No RovMaker, OpenROV, TechMonkeyBusiness, Blue Robotics, or ArduPilot hardware/software dependency is planned.

## Read later

- [RovMaker Edge — Hackaday.io](https://hackaday.io/project/27781-rovmaker-edge-open-source-underwater-robot)
- [RovMaker Edge gallery](https://hackaday.io/project/27781/gallery)
- [RovMaker Edge project logs](https://hackaday.io/project/27781/logs)
- [ROVMAKER community open-source documentation discussion](https://forum.rovmaker.org/t/topic/879)
- [RovMaker Edge CAD on GrabCAD](https://grabcad.com/library/rovmaker-edge-open-source-underwater-robot-1)
- [OpenROV electronics](https://github.com/OpenROV/openrov-electronics)
- [OpenROV Cockpit](https://github.com/OpenROV/openrov-cockpit)
- [TechMonkeyBusiness OpenSource ROV](https://www.techmonkeybusiness.com/articles/OpenSource_ROV.html)
- [Blue Robotics control-board discussion](https://discuss.bluerobotics.com/t/control-board-options-pros-and-cons/812)
- [ArduPilot ROV project discussion](https://discuss.ardupilot.org/t/your-own-remotely-operated-vehicle-rov-project/7951)
