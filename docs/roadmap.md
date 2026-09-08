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

Detailed milestones will be migrated from the existing project roadmap and maintained here as the central project view.
