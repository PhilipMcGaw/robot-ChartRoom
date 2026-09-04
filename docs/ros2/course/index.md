# ROS 2 / Gazebo Course

This is the practical ROS 2 and Gazebo learning path developed for the Robots project.

The course is maintained in Chartroom because the knowledge is reusable across the Robots repositories. SquidLink owns the ROS 2/Gazebo implementation and simulation infrastructure; Chartroom owns the learning material.

## Course path

| Lesson | Result |
|---|---|
| [Workstation Setup](00-workstation.md) | Known-good Ubuntu, ROS 2 Jazzy, Gazebo Harmonic, RViz2, and colcon environment |
| [NATS Core Networking](01-nats-networking.md) | Working NATS Core network independently of the physical robot |
| [Robot Description](02-robot-description.md) | Xacro → URDF → TF → RViz2 |
| [ROS 2 Fundamentals](03-ros2-fundamentals.md) | Nodes, topics, services, parameters, launch, and QoS |
| [Gazebo](04-gazebo.md) | Simple model running through ROS 2/Gazebo integration |
| [Vehicle Model](05-vehicle-model.md) | Vehicle, thrusters, and progressively more realistic motion |
| [Sensors and Camera](06-sensors-and-camera.md) | IMU, depth, heading, and simulated camera |
| [NATS ↔ ROS 2 Bridge](07-nats-ros2-bridge.md) | Application contract mapped to ROS 2 without exposing ROS 2 to Cockpit or Control |
| [HiL/SiL Scenarios](08-hil-sil-scenarios.md) | Repeatable integration tests and evidence |
| [Testbot: Physical Build to ROS 2](09-testbot-physical-to-ros2.md) | Testbot working example from physical record to ROS 2 description |

## Completion principle

A lesson is complete when its practical checks pass. Reading the material is not itself evidence of a working system.

## Supporting material

The course may link to reusable ROS 2 concepts and the dedicated [Gazebo](../gazebo.md) reference page where appropriate.

Project-specific implementation belongs in [SquidLink](https://github.com/PhilipMcGaw/robot-SquidLink), not in this course.
