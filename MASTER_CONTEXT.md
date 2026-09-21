# Chartroom master context

## Identity

Chartroom is the central engineering knowledge base for the Robots project. It explains how the repositories fit together, why important engineering choices were made, and where shared guidance belongs.

Site: https://chartroom.philipmcgaw.com/
Repository: https://github.com/PhilipMcGaw/robot-ChartRoom

## Unavailable reference projects

The former TermiSoc reference project is not part of the current workspace. Do not recreate or add TermiSoc pages or reference content to Chartroom unless explicitly requested and supported by an available source.

## Repository boundary

Chartroom owns cross-project knowledge, not every implementation detail.

- CuttleOS owns robot-side software, runtime services, Cockpit, Control, and DataLogger implementation.
- SquidLink owns ROS 2, Gazebo, simulation, and software-/hardware-in-the-loop implementation.
- NautiPi owns physical hardware, electronics, PCB designs, embedded projects, and hardware reference material.
- Chartroom owns shared architecture, communications, NATS boundaries, engineering decisions, development guidance, deployment and commissioning knowledge, reusable tutorials, cross-project testing guidance, hardware-documentation references, troubleshooting, and the roadmap.

When a page concerns one repository, link to that repository rather than copying its authoritative implementation documentation.

## Current documentation areas

- Architecture: system overview, communications, NATS, robot profiles, embedded-node profiles, BlueOS/Adeept hardware boundaries, CTD provenance, and flight-controller options.
- Robots: CuttleOS, Cockpit, and DataLogger cross-project pages.
- Simulation and test: HIL/SiL and ROS 2/Gazebo course material.
- Development: environment, testing, deployment, Raspberry Pi deployment, hardware documentation, and documentation standards.
- Tutorials: reusable engineering and development material.
- Decisions: significant engineering decisions and rationale.
- Roadmap: planned research, engineering, and project work.
- Research: supporting reference and investigation notes; research must not silently become validated architecture.

## Technical and editorial principles

- State what is known, what is inferred, what is planned, and what has been tested.
- Use precise status terms: designed, planned, implemented, simulated, bench-tested, validated, and production-proven.
- Record important decisions with context, alternatives, consequences, and links to evidence or implementation.
- Prefer manufacturer and primary sources for hardware documentation.
- Use British English, Oxford commas, ISO dates, and SI units with appropriate spacing.
- Preserve third-party names, quotations, code, URLs, and official terminology.
- Do not invent test results, hardware revisions, repository behaviour, or deployment state.

## Build and publishing

The source of truth is source/. The established build path is scripts/deploy.sh, which uses the vendored Quartz checkout in quartz/ and writes generated output to site/.

- Edit source/ for content.
- Edit quartz/quartz.config.ts or quartz/quartz.layout.ts for Chartroom site configuration and visual presentation.
- Edit scripts/ only when build/deployment behaviour itself needs to change.
- Never hand-edit site/.
- Building locally is not publishing. Do not run production deployment unless explicitly requested.
- The deployment script contains rsync --delete behaviour; treat it as destructive and production-only.

## Working with the wider Robots project

Before documenting repository-specific behaviour, inspect the relevant implementation repository and identify its authoritative file or interface. Use Chartroom for the relationship, rationale, and shared operational meaning.

Important cross-project relationships include:

- shared messaging and communications boundaries;
- robot profiles and embedded-node responsibilities;
- CuttleOS runtime services and operator-facing surfaces;
- SquidLink simulation and ROS 2 integration;
- NautiPi hardware and sensor/electronics interfaces;
- HIL/SiL validation across physical and simulated systems.

## Change checklist

1. Read AGENTS.md.
2. Inspect the relevant source page and nearby conventions.
3. Check the authoritative implementation repository when the claim is repository-specific.
4. Preserve provenance, uncertainty, and existing links.
5. Validate Markdown/front matter and affected links.
6. Build or inspect the rendered site when practical.
7. Leave generated output to the established build process.
8. Report any build or deployment blocker clearly.
