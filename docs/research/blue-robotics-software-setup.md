# Blue Robotics BlueROV2 software setup

## Source

- [BlueROV2 Software Setup](https://bluerobotics.com/learn/bluerov2-software-setup/)

## Summary

Blue Robotics' current BlueROV2 setup guide is useful as a practical reference for vehicle software architecture, commissioning, networking, and operator workflow. It explicitly separates three major software responsibilities:

- **BlueOS** — onboard vehicle operating system and service/configuration layer running on the Raspberry Pi;
- **ArduSub** — vehicle-control/autopilot layer handling sensors, stabilisation, depth/heading hold, and translation of pilot commands into thruster outputs; and
- **Cockpit** — topside operator interface for piloting, video, telemetry, accessories, and custom interfaces.

The guide also documents the physical/network boundary between the vehicle and topside system. The Fathom-X Tether Interface presents the tether as a USB network adapter, with the topside system using a static address and the vehicle exposing BlueOS over Ethernet. BlueOS can then provide browser-based configuration, networking, video-stream, peripheral, and service management.

## Relevance to the Robots ecosystem

This is a strong reference for the **responsibility boundaries** already being developed for the ROV rather than a reason to adopt BlueOS, ArduSub, or MAVLink.

The most useful comparison is:

| Blue Robotics | Robots ecosystem |
|---|---|
| BlueOS | vehicle operating-system/service layer |
| ArduSub | `ROV - Control` |
| Cockpit | `ROV - Cockpit` / generic Cockpit |
| vehicle telemetry | common telemetry model |
| onboard services/extensions | future CuttleOS/NautiPi services |
| topside Ethernet/tether | transport/network layer |

The Blue Robotics implementation demonstrates that a clean separation between onboard services, real-time-ish vehicle control, and topside operator software is practical and understandable to users.

## Commissioning lessons

The setup process is particularly useful as a model for **vehicle bring-up and acceptance testing**. It includes:

- explicit network configuration;
- first-boot vehicle configuration;
- vehicle naming and mDNS;
- vehicle-specific parameter selection;
- accelerometer and compass calibration;
- thruster-direction verification;
- an automatic thruster-direction test that requires the ROV to float freely in calm water; and
- manual thruster-direction verification as an alternative when water testing is not possible.

The automatic motor-direction check is especially interesting: it turns a common integration error into an explicit commissioning test rather than relying solely on wiring inspection.

For the ROV, this supports a future **commissioning/test checklist** covering connectivity, sensor calibration, actuator mapping, neutral behaviour, control direction, failsafe behaviour, telemetry, and video before full water operation.

## Network and video architecture

The BlueROV2 guide reinforces the value of treating the tether as a network transport rather than coupling the operator application directly to individual serial devices. It also keeps video streams and vehicle-control/telemetry as distinct concerns within the software stack.

This aligns well with the current intention that Cockpit should consume telemetry through defined interfaces while the vehicle handles low-level control and hardware access.

## Design cautions

Blue Robotics' architecture is built around its own hardware and the MAVLink/ArduPilot ecosystem. The project should therefore borrow **architectural lessons and commissioning practices**, not reproduce its protocol stack.

The existing NATS-based communications architecture remains preferable for this project. In particular, NATS should not be replaced by MAVLink merely to resemble BlueOS/Cockpit.

## Status

**Research / architecture and commissioning inspiration.** No BlueOS, ArduSub, or MAVLink dependency is planned.
