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

### Cross-project vehicle validation

Use substantially different vehicle types to validate whether Cockpit and the supporting software architecture are genuinely reusable rather than accidentally being an ROV-specific implementation.

The current reference vehicles are:

- **ROV:** vehicle control, telemetry, video, operator safety, and engineering test workflows;
- **SwarmBot:** education, constrained programming, multi-robot behaviour, and swarm experiments; and
- **MarsBot:** terrestrial planetary-rover-style mobility, autonomy, navigation, terrain interaction, and ROS 2 integration.

Where common interfaces are justified, share them at the Cockpit/application boundary rather than forcing the vehicles into a common internal implementation. Vehicle-specific control, hardware, and safety logic should remain owned by the relevant project.

**Status:** Planned architectural validation.

Detailed milestones will be migrated from the existing project roadmap and maintained here as the central project view.
