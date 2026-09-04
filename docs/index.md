# Chartroom

**Chartroom** is the central engineering knowledge base for the Robots project.

It is the place for information that spans the individual robot repositories: system architecture, interfaces, engineering decisions, development guidance, simulation and test, tutorials, and the project roadmap.

## The Robots project

The Robots project is deliberately split into four related repositories. Each has a defined responsibility, while Chartroom records the engineering context that connects them.

| Repository | Role | Licence |
|---|---|---|
| **Chartroom** | Cross-project engineering knowledge and documentation | CC BY-NC-SA 4.0 |
| **CuttleOS** | Robot-side software, including Cockpit, Control, and DataLogger | PolyForm Noncommercial 1.0.0 for code; CC BY-NC-SA 4.0 for documentation |
| **SquidLink** | ROS 2/Gazebo simulation and SiL/HiL integration testing | PolyForm Noncommercial 1.0.0 for code; CC BY-NC-SA 4.0 for documentation |
| **NautiPi** | Physical hardware, electronics, PCBs, embedded projects, and hardware reference material | CC BY-NC-SA 4.0 for software/documentation/reference material; CERN-OHL-S 2.0 for hardware |

### Repositories

- [**Chartroom**](https://github.com/PhilipMcGaw/robot-ChartRoom) — this repository; the cross-project engineering record.
- [**CuttleOS**](https://github.com/PhilipMcGaw/robot-CuttleOS) — the robot-side software stack, including Cockpit, Control, and DataLogger.
- [**SquidLink**](https://github.com/PhilipMcGaw/robot-SquidLink) — the independent ROS 2 and Gazebo simulation and integration-test environment.
- [**NautiPi**](https://github.com/PhilipMcGaw/robot-NautiPi) — the physical hardware and embedded-project repository.

The repositories are intentionally separate. CuttleOS is authoritative for robot-side software implementation, SquidLink for simulation and simulation-side integration testing, and NautiPi for physical hardware design. Chartroom is authoritative for cross-project architecture, engineering rationale, significant decisions, reusable guidance, and the overall roadmap.

## People who have helped

The project has benefited from the practical help, ideas, testing, and encouragement of:

- **Philip 'Skippy' McGaw** — project author and engineer — [philipmcgaw.com](https://philipmcgaw.com)
- **Tamarisk 'NotQuiteHere' McGaw** — contributor and project support — [tamarisk.it](https://tamarisk.it)
- **Bob 'thinkl33t' Clough** — contributor and technical help — [thinkl33t.co.uk](https://thinkl33t.co.uk)

This list recognises people who have contributed to the wider project; individual repositories may contain more specific contributor or attribution information where appropriate.

## Licensing

The four repositories use deliberately different licences because they contain different kinds of engineering work. The licence attached to a repository does not automatically apply to material from another repository.

### Chartroom

Chartroom's documentation and original documentation content are licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

[Licence details and notice](https://github.com/PhilipMcGaw/robot-ChartRoom/blob/main/LICENSE-CC-BY-NC-SA-4.0.txt)

### CuttleOS

CuttleOS uses **PolyForm Noncommercial 1.0.0** for its software code and **CC BY-NC-SA 4.0** for its documentation.

[Licence information](https://github.com/PhilipMcGaw/robot-CuttleOS/blob/main/LICENSES.md)

### SquidLink

SquidLink uses **PolyForm Noncommercial 1.0.0** for its software code and **CC BY-NC-SA 4.0** for its documentation.

[Licence information](https://github.com/PhilipMcGaw/robot-SquidLink/blob/main/LICENSES.md)

### NautiPi

NautiPi uses **CC BY-NC-SA 4.0** for software, documentation, and reference material, and **CERN Open Hardware Licence Version 2 — Strongly Reciprocal (CERN-OHL-S 2.0)** for hardware design material.

[Licence information](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/LICENSES.md)

Third-party material, dependencies, libraries, standards, photographs, and other externally sourced material remain subject to their own terms and licences. Where a file or project has a more specific licence notice, that notice takes precedence for that material.

## Documentation principles

Chartroom is intended to be a living engineering record. Documentation should explain not only **what** the system does, but **why** it is designed that way.

Where a decision materially affects the architecture, it should be recorded as an engineering decision rather than relying on undocumented convention.

## Current status

The documentation structure is being established. Existing project documentation will be migrated into Chartroom progressively, with the source repositories remaining authoritative for implementation details.
