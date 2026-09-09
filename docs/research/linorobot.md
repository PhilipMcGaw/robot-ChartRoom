# LinoRobot — ROS robot platform research notes

LinoRobot is a useful reference for the ROS-based mobile-robot side of the Robots ecosystem. It is particularly relevant to the ROS 2 learning path, differential-drive vehicle architecture, reusable robot hardware/software boundaries, and the possibility of using a common control stack across small terrestrial robots.

This is comparative research and design inspiration, not a specification or project dependency.

## Why it is relevant

LinoRobot demonstrates the value of separating a robot platform into reusable hardware, ROS software, and configuration rather than treating each vehicle as an entirely bespoke system. That is closely aligned with the intended separation between the physical robots, the reusable Cockpit, and the `ROV - HiL-and-SiL` environment.

The strongest lesson is architectural rather than mechanical: a robot can remain physically simple while exposing a structured software interface for sensors, actuators, localisation, navigation, and operator tools.

## ROS relevance

The project is useful as a reference when progressing from the current ROS 2 Jazzy exercises:

- Xacro → URDF;
- `robot_state_publisher`;
- TF;
- RViz2;
- simulated sensors and actuators; and
- eventually navigation and autonomous behaviours.

It provides a useful comparison point for how a complete mobile robot is assembled around ROS rather than learning each ROS component in isolation.

## SwarmBot and MarsBot

For **SwarmBot**, the useful ideas are modular differential-drive hardware, standardised sensor interfaces, and a ROS-based software layer that can support experiments without requiring a completely new application for every hardware change.

For **MarsBot**, LinoRobot is more relevant to the software-learning path than to the final rover mechanics. The important inspiration is the progression from basic drive and sensing towards localisation, mapping, navigation, and autonomy.

## Cockpit relationship

LinoRobot should not replace the existing Cockpit architecture. ROS is useful for robot modelling, higher-level behaviours, simulation, and autonomy, while Cockpit remains the reusable operator-facing interface.

A useful future boundary to investigate is:

**Cockpit → vehicle interface → ROS 2 autonomy/control → hardware**

with NATS retained where it provides a useful cross-process or cross-computer interface in the existing Robots architecture.

This should be evaluated rather than assumed: ROS 2 and NATS solve overlapping but different integration problems, and adding both everywhere would increase complexity unnecessarily.

## Engineering lessons

- Keep robot description and hardware configuration explicit and reproducible.
- Separate reusable software from vehicle-specific configuration.
- Use simulation and visualisation to validate robot models before hardware bring-up.
- Treat sensor and actuator interfaces as stable boundaries.
- Build autonomy incrementally from reliable low-level motion and sensing.

## Caveats

LinoRobot is primarily useful as a ROS/mobile-robot reference. Its hardware and software choices should not automatically be adopted for the ROV, where underwater communications, safety, actuator isolation, and vehicle-specific constraints are different.

## Source

- [Hackaday.io — LinoRobot: Robot Operating System](https://hackaday.io/project/61347-linorobot-robot-operating-system)

**Status:** Research / design inspiration.

**Read later:** Examine the repository/project structure, ROS packages, robot description, sensor integration, and navigation examples for ideas that can be adapted to the ROS 2 Jazzy learning path.
