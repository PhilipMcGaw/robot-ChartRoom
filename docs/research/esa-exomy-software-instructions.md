# ESA ExoMy — Software Instructions

## Source

- [ExoMy Software Instructions](https://github.com/esa-prl/ExoMy/wiki/Software-Instructions)
- [ExoMy repository](https://github.com/esa-prl/ExoMy)

**Status:** Research / read later. The original ExoMy repository is archived and read-only; this note preserves the useful engineering and training ideas rather than treating the historical software stack as a project dependency.

## Why this matters

The ExoMy software instructions are particularly useful for the MarsBot and HiL/SiL work because they describe a complete robot software deployment rather than only individual ROS examples.

The original platform used a Raspberry Pi 4 running Raspberry Pi OS, with Docker providing a defined Ubuntu/ROS environment. The application code was primarily Python. The documentation explicitly describes ROS nodes as separate functions communicating through predefined messages.

The important architectural lesson is the separation between:

- host operating system and robot application environment;
- containerised development/runtime dependencies;
- ROS nodes and their interfaces; and
- physical robot hardware.

This is a useful precedent for making a robot software environment reproducible without requiring the host OS to exactly match the development environment.

## Relevant ideas for MarsBot

### Reproducible software environment

ExoMy used Docker to keep the ROS software environment defined independently of the Raspberry Pi host installation. This is useful for MarsBot because it suggests a practical boundary:

```text
MarsBot host OS
      |
      +-- containerised robot software
      |       +-- ROS 2 nodes
      |       +-- robot application
      |       +-- simulation tools where appropriate
      |
      +-- hardware interfaces
```

The exact historical ExoMy versions should not be copied. The principle of a reproducible, versioned software environment is the useful part.

### Raspberry Pi as accessible robot computer

ExoMy demonstrates a Raspberry Pi as the main onboard computer, with Wi-Fi, Bluetooth, USB power, and sufficient processing capability for its application. This reinforces the value of SBCs as accessible development targets for MarsBot and educational robotics.

### ROS node separation

The documentation describes ROS as separating functionality into nodes communicating through predefined messages. This maps well to the project's existing preference for explicit subsystem ownership and interface boundaries.

For MarsBot, this can support separation of:

- hardware drivers;
- sensor processing;
- state estimation;
- vehicle control;
- navigation/autonomy;
- telemetry; and
- operator interfaces.

The specific ROS version in the historical ExoMy material should not constrain the current project, which is using ROS 2 Jazzy.

## Relevant ideas for HiL / SiL

ExoMy is useful because its software is sufficiently separated from the physical platform to make simulation and alternative execution environments practical.

The broader pattern should be:

```text
             Common robot interfaces
                     |
          +----------+----------+
          |                     |
       Simulation            Hardware
          |                     |
      simulated             physical
       sensors               sensors
          |                     |
      simulated             physical
      actuators              actuators
```

The same higher-level control/navigation software should ideally operate against either side of this boundary.

This reinforces the existing `ROV - HiL-and-SiL` direction and should also inform MarsBot's simulation environment.

## Relevant ideas for training

The ExoMy instructions are useful as a teaching example because they expose the full chain from a blank Raspberry Pi to a functioning robot software environment:

1. prepare the operating system;
2. configure the host;
3. install the container runtime;
4. obtain the source from version control;
5. start the defined software environment; and
6. run the robot application.

That is a useful curriculum pattern in its own right. Students can see that a robot is not simply a collection of Python scripts: it is a reproducible system consisting of hardware, operating system, middleware, application software, configuration, and deployment procedures.

This is particularly relevant to **Test in a Box**, where a learner-facing environment should hide unnecessary deployment complexity while still exposing the underlying engineering concepts progressively.

## Things not to copy directly

The original instructions are historical. They refer to Raspberry Pi OS Buster, Raspberry Pi 4, ROS-era software, and commands specific to the original ExoMy implementation. Those versions should not be treated as current recommendations.

Likewise, Docker should not automatically become a requirement for every robot. It is most valuable where reproducibility, dependency isolation, or deployment consistency justify the additional complexity.

## Key takeaways

- **Reproducible environments are valuable** for robot development and testing.
- **Host OS and robot application should have a deliberate boundary.**
- **ROS interfaces should remain stable while hardware/simulation implementations change.**
- **A complete robot software deployment is itself a useful training exercise.**
- **MarsBot is a good candidate for demonstrating the same application across simulation and physical hardware.**
- **The historical ExoMy software stack should be treated as reference material, not a dependency.**

## Read later

- [ExoMy Software Instructions](https://github.com/esa-prl/ExoMy/wiki/Software-Instructions)
- [ExoMy repository](https://github.com/esa-prl/ExoMy)
