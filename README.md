# Chartroom

Chartroom is the central engineering knowledge base for the Robots project.

It records the architecture, engineering rationale, design decisions, development guidance, tutorials, test strategy, and project roadmap that span the individual Robots repositories.

## Documentation

The published documentation is available at **https://chartroom.philipmcgaw.com/**.

The documentation source is held in the `docs/` directory and is built with MkDocs. The repository's `mkdocs.yml` file defines the documentation site and navigation.

### Where to find information

- `docs/architecture/` — cross-project architecture, communications, NATS, and robot profiles.
- `docs/cuttleos/` — cross-project knowledge concerning CuttleOS; implementation-specific documentation remains in CuttleOS.
- `docs/cockpit/` — cross-project knowledge concerning Cockpit; implementation-specific documentation remains in CuttleOS where Cockpit is currently hosted.
- `docs/datalogger/` — cross-project knowledge concerning DataLogger; implementation-specific documentation remains in CuttleOS where DataLogger is currently hosted.
- `docs/hil-sil/` — hardware-in-the-loop and software-in-the-loop architecture and engineering guidance.
- `docs/ros2/` — ROS 2 and simulation knowledge relevant to the wider project.
- `docs/development/` — development environment, testing, deployment, and documentation guidance.
- `docs/tutorials/` — reusable engineering and development tutorials.
- `docs/decisions/` — significant engineering decisions and their rationale.
- `docs/roadmap.md` — cross-project roadmap.

Chartroom is the place to look when information applies across repository boundaries or when the reason for an engineering decision is more important than the implementation detail.

## Robots repositories

Chartroom documents the relationships between the current Robots repositories:

- [CuttleOS](https://github.com/PhilipMcGaw/robot-CuttleOS) — robot-side software, including Cockpit, Control, and Datalogger.
- [SquidLink](https://github.com/PhilipMcGaw/robot-SquidLink) — ROS 2/Gazebo simulation and software-/hardware-in-the-loop integration testing.
- [NautiPi](https://github.com/PhilipMcGaw/robot-NautiPi) — physical hardware, electronics, PCB designs, embedded projects, and hardware reference material.

The repositories are deliberately separate. Their interfaces, architectural relationships, and significant cross-project decisions are documented in Chartroom.

Each of the three project repositories should link back to Chartroom so that the documentation remains discoverable from the implementation and hardware repositories.

## Repository structure

```text
robot-ChartRoom/
├── docs/              # Documentation source
├── scripts/           # Documentation and deployment utilities
├── mkdocs.yml         # MkDocs configuration
└── README.md          # Repository overview
```

## Scope and documentation boundary

Chartroom documents the system as a whole. It should not become a second copy of the implementation documentation held by the individual repositories.

- **CuttleOS** is authoritative for robot-side software implementation.
- **SquidLink** is authoritative for simulation, ROS 2, Gazebo, and simulation-side integration testing.
- **NautiPi** is authoritative for physical hardware design and embedded hardware-project material.
- **Chartroom** is authoritative for cross-project architecture, engineering rationale, significant decisions, reusable guidance, and the overall roadmap.

Where information belongs to a single repository, document it there and link to it from Chartroom where useful.

## Licence

Chartroom documentation and original documentation content are licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

See [`LICENSE-CC-BY-NC-SA-4.0.txt`](LICENSE-CC-BY-NC-SA-4.0.txt) for the licence notice and licence URL.

Unless explicitly stated otherwise, this licence applies to the documentation and other original content in this repository. Third-party material remains subject to its own licence.
