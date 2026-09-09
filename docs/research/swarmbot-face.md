# SwarmBot optional face/display module

The SwarmBot project could support an optional small front-mounted face/display module. The module should be treated as a replaceable payload rather than a requirement for the robot to operate.

## Reference

[How to Build a Tiny ESP DeskBuddy with ESP32-C6](https://www.schematik.io/projects/build-an-esp-c6-touch-lcd-gadget)

The reference uses a self-contained ESP32-C6 display module with a 172 × 320 monochrome display, capacitive touch, and an onboard QMI8658 IMU. Its face uses simple geometric eyes and a mouth, with several expressions and IMU-driven eye movement. The implementation deliberately achieves expressiveness with simple graphics rather than a large animation system.

## Ideas worth evaluating for SwarmBot

- a small display mounted as an optional front-facing personality module;
- simple animated eyes and expressions;
- expressions linked to robot state, such as idle, running, stopped, error, charging, or waiting;
- IMU-driven or motion-driven eye movement to make the robot feel responsive to its physical movement;
- touch as an optional interaction mechanism;
- a local MCU responsible for rendering the face so the robot remains functional if the main computer or Cockpit is unavailable;
- a small diagnostic or status view available alongside the normal face; and
- a clean electrical/mechanical interface so the module can be fitted, removed, or replaced without changing the SwarmBot core.

## Architectural principle

The face should not become part of the SwarmBot control or safety path.

A useful separation is:

**SwarmBot core** → movement, sensors, communications, and safety

**Optional face module** → display, animation, local interaction, and personality

This preserves the modular-platform approach while giving the educational robot a visible and engaging means of communicating state.

## Educational relevance

A physical face could provide immediate feedback from student programs. For example, a program could deliberately change the robot's expression when an event occurs, giving learners a visible connection between their code and the physical robot.

The face should therefore be considered both a human-robot-interaction feature and a possible classroom programming target, rather than merely decoration.

## Status

**Status:** Read later / design inspiration. No display, controller, mechanical interface, or animation architecture has been selected for SwarmBot.
