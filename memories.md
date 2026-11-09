# Project memories

## 2026-11-09 — Local file inspection inbox

The repository has a root-level `inbox/` for files the user wants inspected in the context of Chartroom work. Its contents are ignored by Git and remain local to the checkout; useful findings should be transferred to canonical project files, and temporary files removed when no longer needed. See `inbox/README.md`.

## 2026-11-09 — Research batch consolidation

The research catalogue contains four batch pages and many source-specific research notes. Consolidation should reduce repeated summaries while preserving source provenance and any useful material that has no standalone page. Keep standalone notes as detailed references and use thematic overviews to explain relationships between them. This is an editorial direction requested during repository review; it does not establish technical validation of the referenced projects. The follow-up action is tracked in [TODO.md](TODO.md).

## 2026-11-09 — Project record-keeping preference

Repository guidance records the user's standing preference that project-relevant decisions, corrections, research, and outcomes are written to the appropriate canonical repository files rather than left only in chat. Routine validated updates should be committed and pushed without a separate confirmation request. Preserve provenance and uncertainty; do not record unsupported claims. See `AGENTS.md` for the operational workflow.

## 2026-11-09 — Robotical learning resources assessed for SwarmBot

Robotical Marty is recorded as an educational robotics reference for SwarmBot and Test in a Box, not as a selected hardware platform or software dependency. The useful material is the staged progression from unplugged sequencing and visual blocks to Python, plus lessons on debugging, sensor-driven conditionals, loops, functions, and multi-robot programming. The V1/V2 distinction matters: the published “An Army of Martys” multi-robot tutorial is a useful beginner example of network discovery, lists, and command iteration, but it is not a swarm-control architecture. Older ROS documentation refers to ROS Indigo/Jade/Kinetic and must not be presented as ROS 2 support. Detailed assessment and selected reading links are in [the Robotical Marty research note](pages/sites/chartroom/research/robotical-marty-educational-robotics.txt).
