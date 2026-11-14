# Project memories

## 2026-11-10 — ROV historical project evidence and propulsion research

The user's own ROV development history is documented on PhilipMcGaw.com and the legacy Skippy.org.uk site. Before repeating ROV design work, check the [[https://philipmcgaw.com/projects/rov/|ROV project index]] and its linked posts: the 2023 DIY ROV architecture, pressure vessel, viewport dome, and end-cap/feed-through design; the 2024 transparent development frame; and later control-electronics/software work including the 2025 Arduino Pro Micro serial issue and BlueOS investigation. The 2018 Skippy.org.uk ESC note records earlier setup/start-up difficulties. These sources document design and development history, but do not establish that the recently discussed 100 W 2418 motor and 12 A bidirectional ESC combination was previously tested.

A separate, third-party experimental reference is Hamish Trolove's TechMonkeyBusiness OpenSource ROV archive. It includes builder-reported brushless thruster/propeller comparisons, motor corrosion mitigation, ESC calibration, and pool trials. Do not attribute those experiments to the user or treat them as validation of the current motor/ESC candidate. The compact motor/ESC combination from the DIY ROV Facebook screenshot remains a research candidate only; the ESC model is unidentified and key electrical, thermal, thrust, depth, and immersion ratings remain unverified. See [the consolidated research note](pages/sites/chartroom/research/diy-rov-compact-brushless-motor-esc.txt) and [the TechMonkeyBusiness source assessment](pages/sites/chartroom/research/techmonkeybusiness-open-source-rov-and-robotics.txt).

## 2026-11-09 — Local file inspection inbox

The repository has a root-level `inbox/` for files the user wants inspected in the context of Chartroom work. Its contents are ignored by Git and remain local to the checkout; useful findings should be transferred to canonical project files, and temporary files removed when no longer needed. See `inbox/README.md`.

## 2026-11-09 — Research batch consolidation

The research catalogue contains four batch pages and many source-specific research notes. Consolidation should reduce repeated summaries while preserving source provenance and any useful material that has no standalone page. Keep standalone notes as detailed references and use thematic overviews to explain relationships between them. This is an editorial direction requested during repository review; it does not establish technical validation of the referenced projects. The follow-up action is tracked in [TODO.md](TODO.md).

## 2026-11-09 — Project record-keeping preference

Repository guidance records the user's standing preference that project-relevant decisions, corrections, research, and outcomes are written to the appropriate canonical repository files rather than left only in chat. Routine validated updates should be committed and pushed without a separate confirmation request. Preserve provenance and uncertainty; do not record unsupported claims. See `AGENTS.md` for the operational workflow.

## 2026-11-09 — Robotical learning resources assessed for SwarmBot

Robotical Marty is recorded as an educational robotics reference for SwarmBot and Test in a Box, not as a selected hardware platform or software dependency. The useful material is the staged progression from unplugged sequencing and visual blocks to Python, plus lessons on debugging, sensor-driven conditionals, loops, functions, and multi-robot programming. The V1/V2 distinction matters: the published “An Army of Martys” multi-robot tutorial is a useful beginner example of network discovery, lists, and command iteration, but it is not a swarm-control architecture. Older ROS documentation refers to ROS Indigo/Jade/Kinetic and must not be presented as ROS 2 support. Detailed assessment and selected reading links are in [the Robotical Marty research note](pages/sites/chartroom/research/robotical-marty-educational-robotics.txt).

## 2026-11-10 — PiWars blog reading list

The user supplied 25 unique blog and team-site links associated with PiWars for future reading. They are recorded in [the PiWars team blogs index](pages/sites/chartroom/research/piwars-team-blogs.txt); the links are user-supplied discovery references, and their site contents were not reviewed as part of indexing them. The duplicated PiWars Reactor URL is listed once.

## 2026-11-11 — Self-hosted robot coding portal concept

The user is interested in adapting the three editor categories presented by Raspberry Pi Code Classroom — Blocks, Python, and Web (HTML/CSS/JavaScript) — into a self-hosted coding portal accessible from a phone, tablet, or laptop over Wi-Fi. This is a concept for the Robot Code projects, not a decision to adopt Code Classroom itself or evidence that its hosted classroom backend can be self-hosted. SwarmBot is the preferred initial educational use case, with PiWars as a possible later reuse. For SwarmBot, consider a single swarm portal/gateway that can discover and manage multiple robots; PiWars could use a simpler single-robot deployment.

The key architectural principle is to treat editors as front ends and expose a narrow, documented Robot API. User programs must not have unrestricted access to GPIO, motors, or the host OS. Execution should be isolated; the control layer must retain command validation, operating limits, arbitration, watchdogs, timeouts, and emergency-stop authority. Aim for the same application-facing API over simulated and physical backends so programs can be developed in simulation before hardware deployment. Offline-first operation is desirable. Hosting topology (robot access point, existing network, or shared swarm gateway), editor component choices, licences, and execution technology remain open research questions. The concept and provenance are recorded in [the self-hosted robot coding portal research note](pages/sites/chartroom/research/self-hosted-robot-coding-portal.txt); it is a research candidate, not an approved implementation.

## 2026-11-14 — Qwiic/STEMMA QT robotics interface research

The user considers the Qwiic/STEMMA QT connector ecosystem worth using as a common interface for suitable short-range, low-power I²C peripherals across K9, PiWars, and SwarmBot. The user is already aware of I²C signal-integrity constraints; the research is about connector standardisation, modularity, and accessible bus/debug connections, not a claim that I²C is suitable for arbitrary cable lengths or noisy environments. Qwiic and STEMMA QT share the JST-SH 1.0 mm four-pin connector and pin order, but electrical compatibility, supply voltage, logic levels, current budget, and device requirements still need checking. This is a proposed common design convention, not evidence of an implemented or validated hardware change. See [the Qwiic/STEMMA QT research note](pages/sites/chartroom/research/qwiic-stemma-qt-i2c-connector.txt).
