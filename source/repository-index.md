---
title: "Robots project repository index"
description: "Cross-project repository authority and navigation for the Robots project."
type: index
status: maintained
authority: Chartroom
tags:
  - index
  - repositories
---

# Robots project repository index

This page is the cross-project navigation and authority map for the Robots
repositories. Each implementation repository remains authoritative for its own
code, hardware, simulation, and supporting evidence.

## Authority map

| Repository | Authority |
|---|---|
| `robot-ChartRoom` | Cross-project architecture, engineering rationale, decisions, reusable guidance, deployment and commissioning guidance, operational knowledge, and roadmap |
| `robot-CuttleOS` | Robot-side software implementation, Cockpit, Control, DataLogger, robot profiles, and application-facing software contracts |
| `robot-SquidLink` | ROS 2/Gazebo simulation, SiL/HiL integration, scenarios, and simulation-side evidence |
| `robot-NautiPi` | Physical electronics, PCB/CAD work, embedded hardware, wiring, commissioning, and hardware evidence |

The authority boundary is more important than repository location: do not copy
implementation detail into Chartroom when a link to the authoritative source is
sufficient.

## Repository entry points

### Chartroom

- Repository: https://github.com/PhilipMcGaw/robot-ChartRoom
- Published documentation: https://chartroom.philipmcgaw.com/
- Documentation source: `source/`
- Site generator: vendored Quartz under `quartz/`
- Build and deployment entry point: `scripts/deploy.sh`

Chartroom is the authority for information that spans repository boundaries or
records why an engineering decision was made.

### CuttleOS

- Repository: https://github.com/PhilipMcGaw/robot-CuttleOS
- Authoritative context: `MASTER_CONTEXT.md`
- Implementation documentation: repository `docs/`

CuttleOS owns the robot runtime and its implementation. Chartroom should link
to CuttleOS rather than reproduce detailed implementation instructions.

### SquidLink

- Repository: https://github.com/PhilipMcGaw/robot-SquidLink
- Authoritative context: `MASTER_CONTEXT.md`
- ROS 2 workspace: `ros2_ws/`

SquidLink owns ROS 2, Gazebo, simulation scenarios, and simulation-side
integration evidence. ROS 2 and Gazebo remain behind the simulation boundary
and are not CuttleOS runtime dependencies.

### NautiPi

- Repository: https://github.com/PhilipMcGaw/robot-NautiPi
- Hardware architecture: `docs/hardware-architecture.md`
- Repository overview: `README.md`

NautiPi owns physical hardware design and evidence, including schematics,
PCBs, CAD, embedded projects, wiring, commissioning, and physical testing.

## Evidence and status

Engineering status must distinguish between:

1. designed or planned behaviour;
2. implemented behaviour;
3. automated software testing;
4. bench testing;
5. physical integration testing; and
6. production validation.

The existence of a design, source file, simulation result, photograph, or
reference document does not by itself establish physical manufacture,
commissioning, calibration, integration, or production validation.

When evidence conflicts, prefer current directly observed evidence over older
documentation, recollection, or plans.

## Cross-project boundaries

1. Preserve the repository authority boundaries when changing or interpreting
   interfaces.
2. Treat NATS Core as the application-facing boundary. NATS JetStream is not
   part of the robot architecture.
3. Keep ROS 2 and Gazebo inside SquidLink's simulation boundary.
4. Do not infer physical hardware allocation or production wiring from
   reference material alone.
5. Record significant cross-project decisions in Chartroom and implementation
   details in the repository that owns them.

## Related guidance

The project-wide documentation conventions are defined by the
[Robots Project Documentation Standard](development/documentation-standard.md).
