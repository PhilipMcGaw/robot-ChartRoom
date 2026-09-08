# Frontend Libraries

This document records frontend libraries that have been selected, evaluated, or identified as potentially useful to the Robots project.

## Anime.js

[Anime.js](https://animejs.com/) is a JavaScript animation library for web interfaces. It is a candidate for the CuttleOS Cockpit presentation layer, particularly for custom instruments and SVG-based visualisation.

### Potential uses

Anime.js may be useful for:

- smooth interpolation of telemetry-driven instrument values;
- attitude, heading, and camera-pitch instrument movement;
- animated battery and network-status transitions;
- SVG instrument animation;
- motion paths and physically plausible spring-like movement; and
- controlled cockpit startup or warning animations.

The animation layer should remain separate from the telemetry and communications architecture. NATS, the Cockpit WebSocket, and application state must not depend on Anime.js.

### Status

**Planned evaluation.** Anime.js has been identified as a potentially useful presentation-layer dependency but has not yet been adopted as a project-wide dependency.

The first evaluation should use a single custom Cockpit instrument, preferably an SVG-based instrument, and assess visual quality, performance, bundle impact, TypeScript integration, and whether the dependency provides meaningful advantages over CSS or native browser animation APIs.

If adopted, prefer importing only the required Anime.js modules rather than adding unnecessary functionality to the Cockpit bundle.

### Authority

This page records the project-level evaluation and rationale. Any implementation-specific dependency configuration belongs to the CuttleOS repository.
