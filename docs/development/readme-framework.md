# README Framework

Meaningful project and module directories should contain a `README.md` when they form a useful documentation boundary.

A directory README should normally provide enough context for a reader to understand what the directory contains, why it exists, and where its authoritative information belongs.

## Recommended structure

Use the following sections where they are relevant:

- **Purpose** — what the directory or module is for.
- **Scope** — what is, and is not, covered by the directory.
- **Contents** — the files and subdirectories and their purpose.
- **Interfaces** — important electrical, mechanical, communications, and software interfaces.
- **Dependencies** — hardware, firmware, software, libraries, or external components that materially affect the module.
- **Status** — current evidence-based development or validation status.
- **Documentation** — where detailed engineering records are maintained.
- **Licence** — the applicable repository or project licence and any relevant exceptions.
- **Related repositories** — links to other Robots repositories when they are relevant to the directory.

Not every README needs every section. Small or narrowly scoped directories should remain concise.

## Boundaries

A directory README should describe the material it owns without duplicating documentation maintained elsewhere.

- **CuttleOS** is authoritative for robot-side software implementation.
- **SquidLink** is authoritative for simulation, ROS 2, Gazebo, and simulation-side integration testing.
- **NautiPi** is authoritative for physical hardware design and embedded hardware-project material.
- **Chartroom** is authoritative for cross-project architecture, engineering rationale, significant decisions, reusable guidance, deployment and commissioning procedures, operational knowledge, hardware documentation references, FAQs, troubleshooting guidance, and the overall roadmap.

Where a topic is authoritative elsewhere, provide a concise summary and link to the authoritative documentation rather than creating a competing copy.

## Status wording

Use explicit evidence-based terms such as `planned`, `implemented`, `tested`, `bench-tested`, and `production-validated`. Do not imply a higher level of validation than the available evidence supports.

## Style

Follow the [Robots Project Documentation Standard](documentation-standard.md), including British English, Oxford commas, clear technical prose, and consistent SI-unit formatting.
