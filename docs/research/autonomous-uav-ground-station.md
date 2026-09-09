# Autonomous UAV ground station research notes

The Hackster.io **Autonomous Drone / UAV Project For Plane** is a useful reference for the wider Robots software architecture, particularly the separation of a vehicle/flight-control system from a richer ground-station interface. The project is an open-source work in progress by The Architect, published in 2019, and describes an autonomous RC plane with more than 20 planned flight modes, experimental Raspberry Pi AI flight functions, environmental sensors, and a self-made dashboard. citeturn0search0

This is comparative research and design inspiration, not a specification or project dependency.

## Architecture

The project combines several processing platforms rather than relying on one computer:

- Arduino Mega;
- ESP8266;
- ESP32;
- Raspberry Pi 3;
- GPS;
- barometric pressure sensing;
- BME280 environmental sensing;
- three-axis magnetometer; and
- servo output.

The exact division of responsibility between these devices is not sufficiently documented on the Hackster page, so it should not be assumed to represent a sound final architecture. It is nevertheless useful as a reference for heterogeneous embedded systems and for asking where sensing, control, communications, and higher-level computation should live. citeturn0view0

## Ground-station ideas

The project explicitly describes building a ground station with a custom dashboard alongside the flight-control system. This is relevant to Cockpit because it demonstrates the value of treating the operator interface as a substantial system in its own right rather than merely exposing raw telemetry.

Potential lessons for Cockpit include:

- configurable operator views;
- multiple operating modes;
- presentation of vehicle state and environmental data;
- separation between operator-facing functions and low-level vehicle control; and
- designing the UI around the vehicle's available capabilities rather than around a fixed hardware screen.

The project page says the ground station was intended to support more than 20 flight modes and experimental AI flight, although the page does not establish that all of these features were completed. Treat these as project goals rather than validated capabilities. citeturn0search0

## Sensors and environmental data

The mixture of GPS, pressure, temperature/humidity, magnetometer, and other environmental sensors is relevant to the existing CTD and distributed-sensor research, even though the application is aerial rather than underwater.

Useful questions to compare with our architecture:

- Which measurements require local processing?
- Which sensor data should be retained as raw samples?
- Which values should be converted into higher-level state before transmission?
- How should sensor health and calibration state be represented?
- Which data belong in the vehicle controller versus the datalogger?

## Relevance to the Robots ecosystem

The strongest value is architectural rather than hardware-specific.

For **Cockpit**, it is another example of a custom ground-station/operator interface associated with an autonomous vehicle.

For **MarsBot**, it provides a useful comparison for autonomous vehicle modes, environmental sensing, telemetry, and operator supervision.

For **SwarmBot**, the idea of explicit operating modes and a capability-driven operator/programming interface may be relevant to how student programs are presented and constrained.

For the **ROV**, the project reinforces the general principle that the operator interface, vehicle control, sensor acquisition, and autonomous functions can be separate responsibilities. It should not, however, be taken as evidence that the project's multi-MCU architecture is preferable to the existing NATS-based design.

## Design cautions

The Hackster page is a work-in-progress project and its schematic is explicitly marked as incomplete. The available documentation does not establish the final control-loop architecture, safety behaviour, timing guarantees, or successful completion of the advertised autonomous modes. citeturn0view0

Therefore:

- do not copy the architecture without further investigation;
- do not treat the advertised AI/autonomy functions as validated;
- use the project primarily for interface, integration, and systems-engineering inspiration; and
- investigate the linked source repository and videos before drawing conclusions about implementation quality.

## Sources

- [Hackster.io — Autonomous Drone / UAV Project For Plane](https://www.hackster.io/user53873/autonomous-drone-uav-project-for-plane-5d8894)
- [Hackster.io — Planes projects](https://www.hackster.io/projects/tags/planes)

**Status:** Research / design inspiration. No dependency or architecture decision has been adopted from this project.

**Read later:** Review the project's source repository, dashboard implementation, schematic, and progress videos if the autonomous-mode or ground-station architecture becomes relevant to Cockpit or MarsBot.
