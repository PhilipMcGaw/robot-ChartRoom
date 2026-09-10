# UKMARS and Micromouse reference

**Status:** Research / read later  
**Added:** 2026-09-10

## Sources

- [UKMARS](https://github.com/ukmars)
- [UKMARSBOT](https://github.com/ukmars/ukmarsbot)
- [Joshua CCL Micromouse](https://github.com/joshuaccl/Micromouse)

## Why this matters

These projects are useful references for the small-robot side of ChartRoom, particularly Test in a Box, SwarmBot, and HiL/SiL. They show two complementary approaches:

- UKMARSBOT: a deliberately accessible, modular platform designed around progressive learning and multiple robotics challenges.
- Micromouse: a more performance-oriented embedded platform where sensing, calibration, state estimation, control, and deterministic timing are central engineering concerns.

## UKMARSBOT

The UKMARSBOT repository separates documentation, ECAD, hardware, mechanical design, and resources, while software is maintained in separate repositories. It supports line following, wall following, drag racing, and mini-sumo. citehttps://github.com/ukmars/ukmarsbot

The structure is a useful model for a repeatable educational robot because the physical platform and software exercises can evolve independently without losing the relationship between them.

### Useful ChartRoom ideas

- Keep hardware, mechanical, firmware/software, and exercises separately maintainable.
- Treat design decisions and constraints as documentation, not tribal knowledge.
- Use interchangeable sensor boards where possible.
- Build exercises progressively from basic electrical bring-up to closed-loop behaviour.
- Keep serial data, control, and logging available as diagnostic interfaces.

## Micromouse

The Joshua CCL Micromouse project is an autonomous STM32-based robot intended to navigate an unknown maze and find an efficient route. Its development workflow includes STM32CubeMX, Eclipse/GCC, ST-LINK, and STMStudio. The repository includes explicit branches for ADC calibration, gyro/encoder calibration, and wall tracking. citehttps://github.com/joshuaccl/Micromouse

### Useful ChartRoom ideas

- Calibration should be an explicit engineering activity.
- Make important internal variables observable during development.
- Separate generated hardware configuration from hand-maintained application code.
- Use version control to compare changes to generated configuration.
- Treat sensor calibration, encoder calibration, and wall-tracking validation as distinct test activities.

## Test in a Box / HiL relevance

A useful progression inspired by these projects would be:

1. Power and communications bring-up.
2. Direct actuator command.
3. Sensor readout and validation.
4. Calibration.
5. Open-loop motion.
6. Encoder/IMU feedback.
7. Closed-loop velocity control.
8. Sensor-based behaviour.
9. Navigation or task-level autonomy.
10. Repeat the same tests with simulated inputs and, where appropriate, real hardware.

The key lesson is that **diagnostics and calibration are part of the platform**, not temporary developer conveniences.

## Read later

- Compare UKMARSBOT's repository structure with the intended Test in a Box structure.
- Review the sensor-board and mechanical modularity for ideas applicable to SwarmBot.
- Extract calibration and observability patterns from Micromouse for `ROV - HiL-and-SiL`.
