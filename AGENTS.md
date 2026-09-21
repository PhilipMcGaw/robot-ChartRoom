# Chartroom working rules

## Purpose

Chartroom is the cross-project engineering knowledge base for the Robots project. It records shared architecture, engineering rationale, significant decisions, development guidance, deployment and commissioning procedures, hardware documentation references, simulation and test knowledge, tutorials, troubleshooting guidance, and the project roadmap.

Chartroom is not the implementation authority for CuttleOS, SquidLink, or NautiPi. Those repositories remain authoritative for their own code, simulation, hardware, and repository-specific implementation details.

## Repository structure

- source/ — canonical Chartroom documentation source.
- source/architecture/ — cross-project architecture, communications, NATS, robot profiles, and system boundaries.
- source/cuttleos/, source/cockpit/, source/datalogger/ — cross-project knowledge for the robot software areas.
- source/hil-sil/ — hardware-in-the-loop and software-in-the-loop knowledge.
- source/ros2/ — ROS 2 and Gazebo learning and integration material.
- source/development/ — development, testing, deployment, hardware documentation, and documentation standards.
- source/tutorials/ — reusable engineering and development tutorials.
- source/decisions/ — significant engineering decisions and their rationale.
- source/research/ — research and reference notes where present; distinguish these from validated decisions.
- quartz/ — vendored Quartz build engine and Chartroom-specific Quartz configuration/layout.
- scripts/ — build and deployment scripts.
- site/ — generated static output. Regenerate it; do not hand-edit it.
- README.md — repository orientation and contribution guidance.
- mkdocs.yml — legacy/auxiliary documentation configuration; the established deployment script currently builds with Quartz.

## Unavailable reference projects

The former TermiSoc reference project is not part of the current workspace. Do not recreate or add TermiSoc pages or reference content to Chartroom unless explicitly requested and supported by an available source.

## Source-of-truth rules

1. source/ is the canonical source for Chartroom content.
2. The implementation repositories are authoritative for repository-specific behaviour: CuttleOS for robot-side software, SquidLink for ROS 2/Gazebo/simulation, and NautiPi for physical hardware and embedded projects.
3. Do not duplicate implementation documentation in Chartroom unless the cross-project view adds clear value.
4. When duplicating a fact for cross-project context, link to the authoritative repository or document.
5. Engineering decisions MUST distinguish proposed, designed, implemented, simulated, bench-tested, validated, and production-proven states.
6. Do not present an assumption or unverified research note as implemented or validated behaviour.
7. Preserve existing documentation unless the task explicitly requests correction, removal, or restructuring.
8. site/ is generated output and MUST NOT be hand-edited.
9. Do not add credentials, private keys, tokens, passwords, or private operational data.

## Documentation and evidence

New technical claims SHOULD identify their source where practical: repository path, issue, decision record, standard, manufacturer document, test result, or stable external reference.

When sources disagree, preserve the disagreement, identify the authoritative source, explain the decision or uncertainty, and do not silently choose a convenient interpretation.

Hardware documentation SHOULD identify the manufacturer, model or part number, document type, revision/date where known, and an official source link where available. Do not redistribute third-party manuals when a stable official link is sufficient.

Use Markdown footnotes for citations when source criticism or provenance matters. Use ordinary Markdown links for project navigation and external documentation.

## Markdown and house style

All newly authored project prose, comments, commit messages, and documentation MUST use British English, clear technical language, and consistent terminology.

Use British spellings such as organisation, behaviour, colour, centre, and licence; Oxford commas where useful; ISO dates (YYYY-MM-DD); and SI symbols with a non-breaking space between values and units, such as 10 mm, 5 V, and 25 °C.

Use precise status terms such as designed, planned, implemented, simulated, bench-tested, validated, and production-proven. Preserve quotations, code, identifiers, URLs, product names, and official third-party spellings exactly.

Keep front matter consistent with nearby pages. Do not invent dates, test results, or implementation details.

## Multi-agent collaboration

The repository is shared project memory and is model-agnostic. Agents MUST read applicable AGENTS.md files, inspect current files before changing them, preserve unrelated work, avoid copying private reasoning into project files, record concise conclusions and uncertainty, prefer small reviewable changes, and use Git history as the audit trail.

Do not overwrite another contributor''s work. If a shared file has changed during the task, re-read it and reconcile the update before writing.

## Scripts, build, and deployment

Inspect scripts/deploy.sh before changing build or deployment behaviour. The normal local build is scripts/deploy.sh, which builds Quartz from source/ into site/.

Building and publishing are separate operations. Do not deploy merely to test a content or styling change. Treat any rsync --delete or production-host command as a destructive production operation. Do not run production deployment unless explicitly requested.

Keep build scripts deterministic and narrowly scoped. Chartroom-specific Quartz customisation belongs in quartz/quartz.config.ts and quartz/quartz.layout.ts.

## Generated output

site/ may be committed because this repository keeps source and generated output together, but it remains build output. Never hand-edit generated HTML, CSS, JavaScript, search indexes, or images. Regenerate site/ from source/ using the established build process. If the build cannot run, report the blocker rather than patching generated files manually.

## Editing workflow

Before editing: inspect relevant source files and conventions; decide whether the change belongs in source/, quartz/, scripts/, README.md, or generated output; check links, front matter, diagrams, and repository paths; and consult the authoritative implementation repository for repository-specific claims.

After editing: validate Markdown/front matter; check affected links and media; run an appropriate local build or validation when safe; inspect rendered output for substantial layout changes; do not deploy unless explicitly requested; and summarise changes, validation, and uncertainty.

## Git workflow

Use focused changes with clear commit messages. Do not rewrite history, force-push, reset unrelated work, or include unrelated changes. The default branch is main unless the repository states otherwise.
