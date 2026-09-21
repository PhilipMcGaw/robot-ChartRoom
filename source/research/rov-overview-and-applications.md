---
title: "ROV overview and applications"
description: "Cleaned reference overview of remotely operated underwater vehicles."
date: 2026-09-21
tags:
  - research
  - rov
  - underwater
status: reference
authority: Chartroom
---

# ROV overview and applications

## Scope

This page records general reference material about remotely operated underwater vehicles. It is background research for the Robots project, not a project specification.

An ROV is an uncrewed underwater robot controlled from the surface, usually through a tether or umbilical. The tether can provide power, telemetry, video, and control, but introduces drag, entanglement, handling, and range constraints. Local automation, stabilisation, and safety functions do not make an ROV fully autonomous.

## Core subsystems

- structural frame or chassis;
- propulsion and manoeuvring actuators;
- power distribution and protection;
- tether, communications, and surface control;
- cameras and lighting;
- depth, attitude, temperature, leak, voltage, current, and health sensors;
- onboard compute and control; and
- optional payloads such as manipulators, samplers, sonar, or other instruments.

The structure must balance stiffness, impact resistance, buoyancy, mass, drag, corrosion resistance, serviceability, and access to internal equipment. The appropriate frame depends on vehicle geometry and loads; generic triangulation advice is not a project requirement.

## Propulsion and sensing

Propulsion design should record thruster number and placement, surge/sway/heave/roll/pitch/yaw authority, thrust directions, motor and driver ratings, neutral behaviour, command timeouts, emergency stop, loss-of-communications behaviour, and tether effects.

Common sensing includes cameras and lights, depth or pressure sensing, accelerometers and gyroscopes, magnetometers where the magnetic environment permits useful heading information, temperature and environmental sensors, vehicle-health monitoring, and sonar where required.

Payloads should remain separate from core vehicle safety and control responsibilities. Define interfaces for payload power, commands, telemetry, and failure handling.

## Applications

ROVs are used for scientific observation, marine biology, oceanography, environmental monitoring, infrastructure inspection, underwater archaeology, geological studies, search and rescue, salvage, aquaculture, fisheries monitoring, education, and intervention work.

## Classification

Common broad classes include micro, mini, observation or inspection, general or light-work, heavy-work, and trenching or burial ROVs. These labels are not universal engineering standards. For the Robots project, record actual mass, dimensions, buoyancy, depth rating, tether, power budget, thrust, payload capacity, and intended operating conditions instead of relying on a class label.

## Launch, recovery, materials, and maintenance

Launch and recovery are part of the vehicle system. Plans may involve manual lowering, an A-frame, davit or winch, a tether management system, a garage, or a protected launch path. Account for splash-zone impact, tether handling, weather, lifting points, connector protection, recovery loads, draining, and inspection.

Material selection should consider hydrostatic pressure, depth, buoyancy, impact, vibration, galvanic compatibility, seawater corrosion, seals, penetrators, and pressure housings. Being underwater does not eliminate corrosion. Seawater, dissimilar metals, electrical leakage, trapped moisture, and wet surface storage all create risks. Post-dive care should include appropriate rinsing, draining, drying, inspection, connector care, and controlled storage.

## Relevance to the Robots project

Cockpit and the operator remain separate from vehicle-side control. CuttleOS can own vehicle services, control, telemetry, and safety boundaries. NautiPi owns physical structure, electronics, sensors, and hardware evidence. SquidLink can model vehicle motion, sensors, and test scenarios. Chartroom records cross-project interfaces, rationale, validation, and operational guidance.

NATS is an application communications boundary. The physical tether and any serial, Ethernet, or RS-485 links are separate transport decisions.

This reference does not establish a project depth rating, battery duration, power class, propulsion arrangement, or payload capability. Barometers intended for air are not substitutes for underwater pressure transducers, and wireless control is not automatically a practical replacement for a tether.

## Sources and provenance

Prepared from user-supplied pasted reference text reviewed 2026-09-21. The pasted text identified:

- Marine Insight, [What is Remotely Operated Underwater Vehicle (ROV)?](https://www.marineinsight.com/tech/what-is-remotely-operated-underwater-vehicle-rov/)
- Linden Photonics, [Underwater Remotely Operated Vehicles (ROVs): Applications and Advancements](https://www.lindenphotonics.com/underwater-remotely-operated-vehicles-rovs-applications-and-advancements)

These are general reference articles. Numerical claims and classifications should be verified against primary manufacturer, standards, academic, or project-specific sources before being used for design decisions.

## Status

Reference material only. No project requirement or architecture decision is established by this page.
