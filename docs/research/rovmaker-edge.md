# RovMaker Edge research notes

RovMaker Edge is an open-source underwater robot project from ROVMAKER, created as an educational and exploratory ROV and based on ArduSub. It is a useful historical reference for the physical ROV architecture, pressure housing, buoyancy, penetrators, propulsion, and integration of Raspberry Pi and Pixhawk-class hardware.

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

## Relevance to the current ROV

The strongest areas for further comparison are:

- six-thruster vector layout and control allocation;
- separate battery and electronics pressure housings;
- modular penetrator and connector strategy;
- vacuum leak testing;
- adjustable ballast and trim;
- propulsion characterisation before vehicle integration;
- thermal management of ESC electronics;
- Raspberry Pi plus dedicated control hardware; and
- documenting mechanical dimensions and service procedures sufficiently for reproduction.

The project is particularly useful alongside the RoboCenter, Blue Robotics, and OOMWOO references. Together they provide several different approaches to the same question: where should mechanical, power, low-level control, high-level computing, communications, and operator-interface responsibilities sit?

## Engineering caveats

Although the project is described as open-source, the Hackaday project page currently shows no uploaded files and no formal instructions, and the project has not been actively updated for many years. Public discussions also indicate that users had difficulty obtaining some of the design files and control information. Treat the project as a research/reference source rather than assuming that it is a complete reproducible open-source design.

The published depth and component claims should likewise be treated as project claims requiring independent engineering verification before reuse.

## Status

**Research / ROV design inspiration.** No RovMaker hardware or software dependency is planned.

## Read later

- [RovMaker Edge — Hackaday.io](https://hackaday.io/project/27781-rovmaker-edge-open-source-underwater-robot)
- [RovMaker Edge gallery](https://hackaday.io/project/27781/gallery)
- [RovMaker Edge project logs](https://hackaday.io/project/27781/logs)
- [ROVMAKER community open-source documentation discussion](https://forum.rovmaker.org/t/topic/879)
- [RovMaker Edge CAD on GrabCAD](https://grabcad.com/library/rovmaker-edge-open-source-underwater-robot-1)
