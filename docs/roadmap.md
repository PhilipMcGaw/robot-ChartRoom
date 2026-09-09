# Roadmap

The roadmap records the intended evolution of the Robots ecosystem and its supporting development infrastructure.

## Frontend and Cockpit

### Evaluate Anime.js for cockpit instrumentation

Evaluate [Anime.js](https://animejs.com/) as a presentation-layer animation library for the CuttleOS Cockpit.

The initial evaluation should focus on a custom SVG-based instrument and assess:

- smooth telemetry-driven animation;
- physically plausible movement, including spring-like behaviour where appropriate;
- SVG and TypeScript integration;
- runtime performance;
- bundle size and modular imports; and
- whether it provides a meaningful advantage over CSS and native browser animation APIs.

**Status:** Planned evaluation. Anime.js is not yet a project-wide dependency.

The project-level rationale and evaluation criteria are recorded in [Frontend Libraries](development/frontend-libraries.md). Any resulting dependency configuration belongs to CuttleOS.

### Add Test in a Box programming interface for SwarmBot

Extend Cockpit to support a **SwarmBot classroom mode** using the Test in a Box programming interface, allowing school children to create and run programs against physical SwarmBot robots.

The intended direction is:

- use Cockpit as a generic robotic operator and programming interface rather than an ROV-specific UI;
- provide a beginner-friendly block-based programming environment, with a progression towards Python for more advanced users;
- support individual-robot programming first, followed by multi-robot and swarm experiments;
- expose robot capabilities through a constrained programming model rather than allowing student programs direct or arbitrary access to NATS;
- validate generated robot programs before execution, with bounded movement, timing, and available commands;
- provide live robot status and telemetry so students can see the effect of their programs on physical hardware; and
- use SwarmBot as a second vehicle/application to validate that Cockpit's architecture is genuinely vehicle-agnostic.

The architecture should preserve the separation between the educational programming layer, Cockpit, the robot-control implementation, and the robot communications layer. The ROV and SwarmBot should remain separate implementations behind shared Cockpit interfaces where appropriate.

**Status:** Planned concept. The educational programming interface, safe program representation, SwarmBot control interface, and classroom workflow have not yet been implemented.

### Cross-project Cockpit architecture

Continue evolving Cockpit towards a reusable operator/programming interface capable of supporting different robot types and operating modes, including ROV engineering operation and SwarmBot classroom programming.

### Blue Robotics Cockpit and community inspiration

Review Blue Robotics' Cockpit software and community discussions as a source of operator-interface, telemetry, vehicle-profile, logging, reliability, and educational robotics inspiration. The goal is to learn from an established marine robotics ecosystem without adopting its MAVLink/BlueOS architecture as a dependency.

Areas worth studying include:

- widget-based and configurable operator interfaces;
- vehicle/application profiles rather than a single fixed UI;
- telemetry as a reusable data source for instruments, logging, and overlays;
- video, recording, telemetry-overlay, joystick, connection, and control failure modes reported by users;
- digital-logbook and mission-history concepts;
- STEM and classroom robotics workflows; and
- community-driven build, modification, troubleshooting, and feedback practices.

The Blue Robotics community forum should be treated as a source of real-world UX and reliability lessons as well as feature inspiration. In particular, recurring discussions around joystick calibration, connection loss, video/recording reliability, telemetry overlays, and control behaviour should inform future Cockpit test cases rather than simply being copied as features.

**Status:** Research / inspiration. No Blue Robotics software dependency is planned.

**Read later:** [Blue Robotics Community Forums](https://discuss.bluerobotics.com/), [Cockpit discussions](https://discuss.bluerobotics.com/c/bluerobotics-software/8), and [STEM discussions](https://discuss.bluerobotics.com/c/stem/99).

### MarsBot — JPL Open Source Rover inspiration

Research the [NASA JPL Open Source Rover](https://github.com/nasa-jpl/open-source-rover) as a reference platform for MarsBot. The OSR is a six-wheel, build-it-yourself rover intended as a teaching and learning platform as well as a rugged-terrain research platform. Its use of consumer off-the-shelf components, Raspberry Pi computing, modular expansion, and detailed mechanical/electrical/software documentation make it a useful reference for both MarsBot hardware and project structure.

Areas worth studying include:

- rocker-bogie suspension and maintaining wheel contact over uneven terrain;
- differential pivoting and six-wheel Ackermann steering;
- modular mechanical and electrical expansion interfaces;
- Raspberry Pi as an accessible onboard computing platform;
- ROS 2 integration and the boundary between ROS 2 and the project's vehicle-control/application layer;
- cameras, IMUs, obstacle detection, mapping, environmental sensors, and robotic-arm expansion;
- battery, power, thermal, and rugged outdoor-operation considerations;
- staged build documentation covering wiring, electronics, mechanics, software, and commissioning; and
- the open-source/community modification model as an educational and research platform.

MarsBot should not become a copy of the JPL rover. Instead, use the OSR as a reference against which to test our own architecture, particularly the combination of NATS, Cockpit, CuttleOS, SquidLink HIL/SIL, and NautiPi hardware. MarsBot should provide a useful second terrestrial platform for evaluating autonomy, navigation, terrain handling, ROS 2 integration, telemetry, and simulation.

The JPL project is also a useful example of making a robotics platform approachable to people with different levels of mechanical, electrical, and software experience. This aligns with the educational direction of Test in a Box and the wider goal of making the Robots ecosystem suitable for experimentation and learning.

**Status:** Research / concept. No decision has been made to reproduce the JPL mechanical design or software architecture.

**Read later:** [NASA JPL Open Source Rover](https://github.com/nasa-jpl/open-source-rover) and [OSR rover code](https://github.com/nasa-jpl/osr-rover-code).

### RoboCenter ROV inspiration

Review the surviving RoboCenter/MUR material as a reference for a complete ROV development stack. The material is useful because it covers mechanical construction, open thrusters, payloads, embedded control, telemetry, operator UI, simulation, and practical air/pool testing. It should be treated as design inspiration and comparative research, not as a project specification or software dependency.

#### Mechanical

- study the OpenThruster projects as a reference for accessible, inspectable, modular propulsion hardware;
- evaluate replaceable thruster guards/ducts as part of the mechanical protection strategy;
- retain a modular frame with defined attachment points for propulsion, buoyancy, cameras, lights, and payloads;
- treat manipulators, cameras, and other payloads as replaceable modules; and
- include buoyancy, sealing, cable routing, and serviceability in the mechanical/electrical design loop.

#### Electrical and embedded

- compare RoboCenter's separation between high-level commands and low-level actuator/sensor control with the existing ROV Control boundary;
- expose useful actuator and driver state through the normal telemetry model rather than treating propulsion as a black box;
- define clear interfaces for additional sensors, lights, cameras, manipulators, and future payload electronics;
- compare their practical underwater power, Ethernet, sealed-electronics, and service-connection approach with the ROV electrical architecture; and
- explicitly document actuator fault handling, communications loss, limits, and safe-state behaviour.

#### Software architecture

The HighROV documentation describes a useful conceptual flow: receive operator commands; update sensors; update vehicle telemetry; control thrusters from current demand and state; publish actuator telemetry; control payloads; and return telemetry to the operator interface.

Use this as a comparison against the existing **Cockpit → Control → Datalogger** separation. The useful lesson is responsibility and ownership, not the specific RoboCenter implementation or protocol.

Also investigate the `PayloadTool` abstraction (`init`, `update`, `commit`) and MUR IDE as possible references for payload modules, vehicle profiles, and a common programming/simulation workflow.

#### Cockpit / operator UI

The HighROV UI provides a useful comparison for Cockpit: a central camera view surrounded by dedicated telemetry, diagnostic/message, thrust-limit, controller/regulator, and logging functions. Also study configurable gamepad control and the idea of a UI that can be adapted to a custom vehicle rather than being permanently tied to one hardware build.

Compare these ideas with Blue Robotics Cockpit and other ROV interfaces before making implementation decisions. The aim is to make Cockpit a generic robotics operator interface while retaining clear engineering/debug views.

#### HiL / SiL and testing

Use the RoboCenter simulator and MUR IDE as references for:

- running control software against a simulated vehicle before hardware;
- repeatable missions and operator workflows;
- testing telemetry and UI behaviour without a pool test;
- separating air/debug tests from wet/pool tests;
- keeping simulation and hardware models conceptually aligned; and
- recording sufficient state to reproduce test failures.

This supports the existing **ROV - HiL-and-SiL** direction and the goal of making simulation a normal engineering tool.

**Status:** Research / inspiration. No RoboCenter software dependency is planned.

**Read later:** [RoboCenter research notes](research/robocenter.md), which contains the surviving primary-source links, including the [RoboCenter materials index](https://robocenter.net/materials/), [HighROV manuals](https://robocenter.net/media/documents/HighROV_Manual_RUS.pdf), [MUR Thruster 200 specification](https://robocenter.net/documents/77/%D0%A1%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F_MUR_Thruster_200.pdf), [MUR simulator](https://simulator.robocenter.org/), [MUR firmware](https://github.com/murproject/rov_firmware), and [RovUI](https://github.com/murproject/RovUI).

### Documentation and technical communication design

Use Mayer's Principles of Multimedia Learning as a reference when producing technical information across the Robots ecosystem. Although the Raspberry Pi Foundation source is aimed at computing education, its guidance on cognitive load, information structure, visual signalling, and the relationship between words and diagrams is applicable to classroom material, engineering documentation, datasheets, presentations, and public-facing technical writing.

Areas worth applying include:

- **coherence:** remove information that does not support the document's purpose;
- **signalling:** deliberately direct attention to important information;
- **redundancy:** avoid unnecessary repetition of identical information in different forms;
- **spatial and temporal contiguity:** keep related explanations and visuals together;
- **segmenting:** break complex subjects into manageable stages;
- **pre-training:** introduce important terms, components, and relationships before complex material; and
- **modality:** use diagrams and demonstrations with concise explanation rather than dense blocks of duplicated text where appropriate.

Apply the principles according to the audience and document type rather than making every document look like a classroom lesson. In particular, use them when developing ROS 2/classroom material, engineering design and build documentation, datasheets and interface specifications, project READMEs, presentations, press releases, and architecture diagrams.

**Status:** Research / documentation design reference. These principles are not yet a formal ChartRoom documentation standard.

**Read later:** [Raspberry Pi Foundation — How to design and present clear computing lessons](https://www.raspberrypi.org/blog/how-to-design-and-present-clear-computing-lessons-mayers-principles/), [Designing Multimedia for Clarity](https://static.raspberrypi.org/files/curriculum/quickreads/QR32_Mayers_Principles_1_17_04_2026.pdf), and [Raspberry Pi Foundation Quick Reads](https://www.raspberrypi.org/teach/pedagogy/quick-reads).

### K-9 back-button screens and displays

Keep a small K-9-specific research track for the rear/back-button assembly, particularly the screens/displays associated with the buttons. Capture visual references before fixing the mechanical, electrical, or UI implementation.

**Status:** Read later / design research.

**Read later:** [K-9 Read Later](k9-read-later.md).

### Cross-project vehicle validation

Use substantially different vehicle types to validate whether Cockpit and the supporting software architecture are genuinely reusable rather than accidentally being an ROV-specific implementation.

The current reference vehicles are:

- **ROV:** vehicle control, telemetry, video, operator safety, and engineering test workflows;
- **SwarmBot:** education, constrained programming, multi-robot behaviour, and swarm experiments; and
- **MarsBot:** terrestrial planetary-rover-style mobility, autonomy, navigation, terrain interaction, and ROS 2 integration.

Where common interfaces are justified, share them at the Cockpit/application boundary rather than forcing the vehicles into a common internal implementation. Vehicle-specific control, hardware, and safety logic should remain owned by the relevant project.

**Status:** Planned architectural validation.

Detailed milestones will be migrated from the existing project roadmap and maintained here as the central project view.
