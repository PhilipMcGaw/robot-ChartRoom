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

Detailed milestones will be migrated from the existing project roadmap and maintained here as the central project view.
