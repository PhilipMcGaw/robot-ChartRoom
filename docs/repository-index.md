---
title: "Robots project repository index"
description: "Documentation page covering Robots project repository index."
type: index
status: maintained
authority: Chartroom
tags:
  - index
  - repositories
---

# Robots project repository index

This index records the attached repositories inspected on 14 September 2026.
It is a navigation aid and cross-repository understanding record; the source
repositories remain authoritative for their own implementation and evidence.

## Authority map

| Repository | Authority |
|---|---|
| `robot-ChartRoom` | Cross-project architecture, engineering rationale, reusable guidance, decisions, and overall roadmap |
| `robot-CuttleOS` | Robot-side Cockpit, Control, Datalogger, robot profiles, and application-facing software contracts |
| `robot-SquidLink` | ROS 2/Gazebo simulation, SiL/HiL integration, scenarios, and simulation-side evidence |
| `robot-NautiPi` | Physical electronics, PCB/CAD work, embedded hardware, wiring, commissioning, and hardware evidence |

The evidence hierarchy is: current code and physical bench evidence, then
current status and roadmap, then authoritative architecture and context, then
older documentation or recollection. Designed, simulated, or software-tested
behaviour must not be described as physically or production validated.

## Master context files

### CuttleOS

- [`robot-CuttleOS/MASTER_CONTEXT.md`](https://github.com/PhilipMcGaw/robot-CuttleOS/blob/main/MASTER_CONTEXT.md)
  is the consolidated and authoritative CuttleOS context.
- [`robot-CuttleOS/docs/MASTER_CONTEXT.md`](https://github.com/PhilipMcGaw/robot-CuttleOS/blob/main/docs/MASTER_CONTEXT.md)
  is a redirect notice and should not be treated as a second source of truth.

Key points: Cockpit, Control, and Datalogger run as isolated services on one
Raspberry Pi and communicate through NATS Core. The browser reaches Cockpit
over HTTP/WebSocket and never talks directly to NATS or hardware. Control owns
command validation, actuator mixing, limits, timeouts, hardware drivers,
sensors, networking, and emergency-stop/neutral behaviour. Datalogger records
changed NATS values to SQLite without becoming a control dependency. Robot
profiles are versioned JSON under `configs/profiles/`.

The production target is Raspberry Pi OS Trixie Lite 64-bit on Raspberry Pi 3B+
or newer. The documented development targets are Windows, macOS, and Linux.
The staged validation path runs from static checks and protocol/sensor tests
through actuator bench, dry integration, and wet testing.

### SquidLink

- [`robot-SquidLink/MASTER_CONTEXT.md`](https://github.com/PhilipMcGaw/robot-SquidLink/blob/main/MASTER_CONTEXT.md)
  is authoritative for simulation architecture, conventions, and validation
  status.

Key points: SquidLink is independent of the robot runtime and physical
hardware. Its application boundary is the same CuttleOS NATS contract, adapted
behind a NATS/ROS 2 bridge to ROS 2 and Gazebo. ROS 2 and Gazebo must remain
inside SquidLink; safety-critical CuttleOS Control logic must not be duplicated
in the simulator. The authoritative workspace is `ros2_ws/`, and generated
`build/`, `install/`, and `log/` directories must not be committed.

The documented environment is Ubuntu 24.04 LTS AMD64, ROS 2 Jazzy, and Gazebo
Harmonic. The repository currently provides scaffolding and a provisional
`testbot_description` example; complete ROV simulation, production-quality
bridge execution, repeatable end-to-end scenarios, and physical HiL remain
unverified unless explicit evidence says otherwise.

### NautiPi

NautiPi has no root-level `MASTER_CONTEXT.md`. Its equivalent authority is
[`docs/hardware-architecture.md`](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/docs/hardware-architecture.md),
supported by the root [`README.md`](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/README.md).

Key points: NautiPi owns the physical implementation and evidence, including
schematics, PCBs, CAD, embedded projects, component and assembly records,
wiring, calibration, photographs, commissioning, and physical tests. CuttleOS
defines the application contract; NautiPi must not silently redefine it. The
hardware architecture uses identifiable distributed nodes where appropriate,
with permanent manufacturer identity separated from configurable bus address.
RS-485 and Modbus RTU are the intended field-bus approach where applicable,
but physical design and commissioning evidence are still required.

## Repository inventory

Counts are tracked-file-oriented navigation figures from the inspection; large
binary/reference collections are included in the totals.

| Repository | Files | Main areas |
|---|---:|---|
| `robot-ChartRoom` | 73 | `docs/`, `scripts/`, MkDocs configuration |
| `robot-CuttleOS` | 393 | `cockpit/`, `control/`, `datalogger/`, `frontend/`, `assets/`, `configs/`, `tests/`, `docs/`, deployment scripts |
| `robot-SquidLink` | 57 | `ros2_ws/`, `vehicles/`, `configs/`, `scenarios/`, `tests/`, `docs/` |
| `robot-NautiPi` | 6,226 | ROV CTD, ROV lighting, ROV main body and navigator, K9, Testbot, MarsBot, weather station, traffic light, CAD/PCB/reference media |

### ChartRoom (`/Users/skippy/Git/robot-ChartRoom`)

The central documentation site is organised into architecture, robot-specific
pages, HiL/SiL and ROS 2 course material, development guidance, decisions,
research, and the roadmap. `mkdocs.yml` is the navigation source.

### CuttleOS (`/Users/skippy/Git/robot-CuttleOS`)

The consolidated runtime repository contains three services, a frontend,
shared and robot-specific assets, deployment/configuration files, static-demo
material, and automated tests. Its root context and service documentation are
the right starting points for implementation questions.

### SquidLink (`/Users/skippy/Git/robot-SquidLink`)

The simulation repository contains ROS 2 packages under `ros2_ws/src/`,
vehicle-specific material under `vehicles/`, configuration, scenarios,
simulation documentation, scripts, and documentation-policy tests. Its course
material is learning material, not an alternative architecture authority.

### NautiPi (`/Users/skippy/Git/robot-NautiPi`)

The hardware repository is substantially larger because it preserves KiCad
projects, generated bills of materials, PDFs, photographs, CAD/reference
archives, firmware, and historical material. Principal project areas are:

- `ROV - Conductivity Temperature and Depth Transducer/`
- `ROV - Light Module/`
- `ROV - Main Body/`
- `ROV - Navigator/`
- `K9 - Main Body/` and `K9 - Camera/`
- `TestBot - Main Body/`
- `MarsBot - Main Body/`
- `Weather Station/` and `Weather Station - Soil Moisture/`
- `Traffic Light/` and `HID/`

Presence of a design, firmware file, photograph, or reference document does
not establish manufacture, assembly, calibration, commissioning, or
integration.

## Cross-project working rules

1. Preserve the repository boundaries and consult the authority map before
   changing or interpreting an interface.
2. Treat NATS Core as the application-facing boundary; NATS JetStream is not
   part of the robot architecture.
3. Keep ROS 2 and Gazebo behind SquidLink's bridge boundary.
4. Do not infer hardware allocations or production wiring from NautiPi
   references alone.
5. Record explicit evidence for software tests, bench tests, physical tests,
   and production validation separately.
