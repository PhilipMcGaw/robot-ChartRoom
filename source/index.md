---
title: Chartroom
description: Cross-project engineering knowledge base for the Robots project.
type: hub
status: maintained
authority: Chartroom
tags:
  - chartroom
  - robots-project
---

# Chartroom

**Chartroom** is the central engineering knowledge base for the Robots project.

It records information that spans the individual robot repositories: system architecture, interfaces, engineering decisions, development guidance, simulation and test, tutorials, and the project roadmap.

## Live demonstration

The current **CuttleOS Cockpit** demonstration is available at:

**[Open the CuttleOS Cockpit demo](https://cuttleos.philipmcgaw.com/)**

The demonstration shows the operator-facing software interface. The implementation remains authoritative in the CuttleOS repository; Chartroom records the architecture, rationale, and cross-project context.

## The Robots project

The project is deliberately split into four related repositories. Each has a defined responsibility, while Chartroom records the engineering context that connects them.

For the detailed authority boundary, see the [Robots project repository index](repository-index.md).

| Repository | Primary responsibility |
|---|---|
| [Chartroom](https://github.com/PhilipMcGaw/robot-ChartRoom) | Cross-project engineering knowledge and documentation |
| [CuttleOS](https://github.com/PhilipMcGaw/robot-CuttleOS) | Robot-side software, including Cockpit, Control, and DataLogger |
| [SquidLink](https://github.com/PhilipMcGaw/robot-SquidLink) | ROS 2/Gazebo simulation and SiL/HiL integration testing |
| [NautiPi](https://github.com/PhilipMcGaw/robot-NautiPi) | Physical hardware, electronics, PCBs, embedded projects, and hardware reference material |

The repositories are intentionally separate. Chartroom should link to the authoritative implementation repository rather than reproduce implementation detail.

## People who have helped

The project has benefited from the practical help, ideas, testing, and encouragement of:

- **Philip 'Skippy' McGaw** — project author and engineer — [philipmcgaw.com](https://philipmcgaw.com)
- **Tamarisk 'NotQuiteHere' McGaw** — contributor and project support — [tamarisk.it](https://tamarisk.it)
- **Bob 'thinkl33t' Clough** — contributor and technical help — [thinkl33t.co.uk](https://thinkl33t.co.uk)

This list recognises people who have contributed to the wider project; individual repositories may contain more specific contributor or attribution information where appropriate.

## Licensing

The repositories use different licences because they contain different kinds of engineering work. A licence attached to one repository does not automatically apply to material from another repository.

- **Chartroom:** CC BY-NC-SA 4.0 for original documentation content.
- **CuttleOS:** PolyForm Noncommercial 1.0.0 for software code; CC BY-NC-SA 4.0 for documentation.
- **SquidLink:** PolyForm Noncommercial 1.0.0 for software code; CC BY-NC-SA 4.0 for documentation.
- **NautiPi:** CC BY-NC-SA 4.0 for software, documentation, and reference material; CERN-OHL-S 2.0 for hardware.

See each repository's licence files for the authoritative licence text and scope:

- [Chartroom licence](https://github.com/PhilipMcGaw/robot-ChartRoom/blob/main/LICENSE-CC-BY-NC-SA-4.0.txt)
- [CuttleOS licences](https://github.com/PhilipMcGaw/robot-CuttleOS/blob/main/LICENSES.md)
- [SquidLink licences](https://github.com/PhilipMcGaw/robot-SquidLink/blob/main/LICENSES.md)
- [NautiPi licences](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/LICENSES.md)

Third-party material, dependencies, libraries, standards, photographs, and other externally sourced material remain subject to their own terms and licences. Where a file or project has a more specific licence notice, that notice takes precedence for that material.

## Documentation principles

Chartroom is a living engineering record. Documentation should explain not only **what** the system does, but **why** it is designed that way.

Where a decision materially affects the architecture, record it as an engineering decision rather than relying on undocumented convention.

The project-wide documentation conventions are defined in the [Robots Project Documentation Standard](development/documentation-standard.md).
