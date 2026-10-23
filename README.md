# Chartroom

Chartroom is the central engineering knowledge base for the Robots project.

It records the architecture, engineering rationale, design decisions, development guidance, tutorials, deployment and commissioning procedures, hardware documentation references, test strategy, FAQs, troubleshooting knowledge, and project roadmap that span the individual Robots repositories.

## Documentation

The intended DokuWiki destination is the [`sites:chartroom` namespace](https://labbook.skippy.org.uk/doku.php/sites/chartroom/). The import has not yet been verified, so DokuWiki page text in `pages/sites/chartroom/` and retained media in `media/sites/chartroom/` remain the migration copy. Page files use `.txt`; nested paths map to namespaces under `sites:chartroom`, and `start.txt` is each namespace landing page. The former static site was available at <https://chartroom.philipmcgaw.com/>; this repository does not configure a redirect.

### Where to find information

- `pages/sites/chartroom/architecture/` — cross-project architecture, communications, NATS, and robot profiles.
- `pages/sites/chartroom/cuttleos/` — cross-project knowledge concerning CuttleOS; implementation-specific documentation remains in CuttleOS.
- `pages/sites/chartroom/cockpit/` — cross-project knowledge concerning Cockpit; implementation-specific documentation remains in CuttleOS where Cockpit is currently hosted.
- `pages/sites/chartroom/datalogger/` — cross-project knowledge concerning DataLogger; implementation-specific documentation remains in CuttleOS where DataLogger is currently hosted.
- `pages/sites/chartroom/hil-sil/` — hardware-in-the-loop and software-in-the-loop architecture and engineering guidance.
- `pages/sites/chartroom/ros2/` — ROS 2 and simulation knowledge relevant to the wider project.
- `pages/sites/chartroom/development/` — development environment, testing, deployment, hardware documentation, and documentation guidance.
- `pages/sites/chartroom/tutorials/` — reusable engineering and development tutorials.
- `pages/sites/chartroom/decisions/` — significant engineering decisions and their rationale.
- `pages/sites/chartroom/roadmap.txt` — cross-project roadmap.

Chartroom is the place to look when information applies across repository boundaries or when the reason for an engineering decision, deployment procedure, operational experience, or troubleshooting note is more important than the implementation detail.

## Documentation standard

The **[Robots Project Documentation Standard](pages/sites/chartroom/development/documentation-standard.txt)** is the single source of truth for project-wide documentation conventions. CuttleOS, SquidLink, and NautiPi should follow that standard rather than maintaining separate copies of the rules.

## Hardware documentation

Chartroom can hold references to manuals, datasheets, installation guides, configuration guides, and application notes for robot hardware.

For COTS components, the preferred source is the manufacturer's official documentation. Where documentation is publicly available from the manufacturer, Chartroom should link to that source rather than redistribute a copy. Hardware documentation entries should identify the manufacturer, part number or model, document type, and document revision or publication date where available.

Third-party documentation remains subject to its own copyright and licence terms. The Chartroom repository licence applies to original Chartroom content, not to manufacturer's documentation or other third-party material.

See the [hardware documentation policy](pages/sites/chartroom/development/hardware-documentation.txt) for the full guidance.

## Robots repositories

Chartroom documents the relationships between the current Robots repositories:

- [CuttleOS](https://github.com/PhilipMcGaw/robot-CuttleOS) — robot-side software, including Cockpit, Control, and Datalogger.
- [SquidLink](https://github.com/PhilipMcGaw/robot-SquidLink) — ROS 2/Gazebo simulation and software-/hardware-in-the-loop integration testing.
- [NautiPi](https://github.com/PhilipMcGaw/robot-NautiPi) — physical hardware, electronics, PCB designs, embedded projects, and hardware reference material.

The repositories are deliberately separate. Their interfaces, architectural relationships, and significant cross-project decisions are documented in Chartroom.

Each of the three implementation repositories should link back to Chartroom so that the documentation remains discoverable from the implementation and hardware repositories.

## Repository structure

```text
robot-ChartRoom/
├── pages/sites/chartroom/ # DokuWiki page text
├── media/sites/chartroom/ # DokuWiki media
├── AGENTS.md          # Repository working rules
├── MASTER_CONTEXT.md  # Project context
└── README.md          # Repository overview
```

## Scope and documentation boundary

Chartroom documents the system as a whole. It should not become a second copy of the implementation documentation held by the individual repositories.

- **CuttleOS** is authoritative for robot-side software implementation.
- **SquidLink** is authoritative for simulation, ROS 2, Gazebo, and simulation-side integration testing.
- **NautiPi** is authoritative for physical hardware design and embedded hardware-project material.
- **Chartroom** is authoritative for cross-project architecture, engineering rationale, significant decisions, reusable guidance, deployment and commissioning procedures, operational knowledge, hardware documentation references, FAQs, troubleshooting guidance, and the overall roadmap.

Where information belongs to a single repository, document it there and link to it from Chartroom where useful.

## Licence

Chartroom documentation and original documentation content are licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

See [`LICENSE-CC-BY-NC-SA-4.0.txt`](LICENSE-CC-BY-NC-SA-4.0.txt) for the licence notice and licence URL.

Unless explicitly stated otherwise, this licence applies to the documentation and other original content in this repository. Third-party material remains subject to its own licence.
