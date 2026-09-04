# Robots Project Documentation Standard

This document defines the documentation standard for the Robots project. It is the single source of truth for project-wide documentation conventions used by Chartroom, CuttleOS, SquidLink, and NautiPi.

## Single source of truth

Where practical, maintain a single authoritative source of truth and reference it from other repositories rather than duplicating information.

If information has one authoritative owner, document it there and link to it elsewhere. Duplicate information only when the copy serves a materially different purpose, and clearly identify which source is authoritative.

This principle applies to both technical information and documentation conventions.

## Repository authority

Each repository owns a defined class of information:

| Information | Authority |
|---|---|
| Project-wide architecture | Chartroom |
| Documentation standard | Chartroom |
| Engineering decisions and rationale | Chartroom |
| Cross-repository interfaces | Chartroom |
| CuttleOS implementation | CuttleOS |
| CuttleOS deployment implementation | CuttleOS |
| Physical hardware and electronics | NautiPi |
| ROS 2/Gazebo simulation | SquidLink |

Repositories should link to the authoritative documentation rather than maintaining competing copies.

## Writing style

Documentation should use clear, concise, precise technical English. Prefer active voice, concrete terminology, and short sentences where this improves clarity. Follow the principles of *The Elements of Style* by William Strunk Jr. where they improve readability without reducing technical precision.

Use British English throughout the project and use Oxford commas in lists.

Important technical information should be stated explicitly rather than left to inference from diagrams, filenames, badges, or surrounding context.

## Engineering status

Documentation must distinguish between different levels of evidence. In particular, do not describe planned or intended behaviour as though it were implemented.

Where relevant, distinguish between:

- implemented behaviour;
- automated tests;
- bench testing;
- production validation; and
- planned or unverified work.

Claims about testing or validation should identify the level of evidence available.

## SI units and notation

Use SI units and notation consistently, following the NIST SI style guidance.

- Put a non-breaking space between a numerical value and its unit.
- Use SI symbols rather than spelling out units unnecessarily.
- Use `°` for degrees.
- Use the micro sign `µ`, not the Greek letter `μ` or the word “mu”, when the SI prefix is intended.
- Use `Ω` for ohms.
- Use commas as thousands separators for large numbers.

Examples:

```text
20 V
75 °C
4,000 A
10 µm
2.7 mΩ
```

## Symbols

Use established technical symbols where they improve precision and readability, including:

`±` `µ` `Ω` `≤` `≥` `Δ` `θ` `§` `°` `τ` `‽` `·` `…` `⟪` `⟫`

Use symbols consistently and do not substitute visually similar characters when a specific technical symbol is intended.

When referring to another section of the same document, use the section sign, for example, “see § Authority boundary”.

## Markdown structure

Use semantic Markdown structure:

- one top-level heading per document;
- meaningful second- and third-level headings;
- numbered lists for ordered procedures;
- bullet lists for unordered information;
- tables where they improve comparison or expose an authority boundary;
- fenced code blocks for commands, configuration, and source code; and
- admonitions where a warning, note, or important constraint needs to stand out.

Do not use formatting merely for decoration. Structure should communicate meaning.

## Commands and procedures

Procedures should be reproducible by another engineer.

Commands should:

- use the correct shell language where relevant;
- show paths explicitly when they matter;
- avoid embedding secrets;
- distinguish commands executed on different machines; and
- state prerequisites when they are not obvious.

If a command is an implementation detail owned by another repository, link to that repository's authoritative procedure rather than maintaining a second full procedure.

## Architecture and implementation

Keep project architecture and implementation details at the appropriate authority level.

Chartroom should describe cross-repository architecture, interfaces, rationale, and project-level procedures. Implementation repositories should describe how their own software or hardware actually works.

A Chartroom document may include an implementation example when that example materially explains the architecture, but it should identify the implementation repository as authoritative.

## Links and references

Prefer links to authoritative sources. When a project component has its own repository, documentation should identify the repository and link to it where relevant.

Do not create a local copy of information solely to avoid linking to its source.

When external standards, specifications, or authoritative documentation are referenced, identify the source clearly.

## Machine readability

Documentation should be understandable to both humans and machines.

Use explicit names, semantic headings, stable terminology, meaningful link text, and structured metadata where appropriate. Important relationships should be stated in prose rather than encoded only in visual presentation.

JSON-LD, canonical URLs, `llms.txt`, and related metadata may support machine discovery, but they do not replace clear human-readable documentation.

## Documentation maintenance

When an authoritative implementation changes, review dependent documentation for accuracy.

Do not silently leave duplicated documentation stale. If duplication is unavoidable, identify the authoritative source and update the dependent copy when the material relationship changes.

The objective is not to eliminate every repeated sentence. The objective is to eliminate competing versions of the truth.
