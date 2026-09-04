# Testbot: physical build to ROS 2 description

## Objective

Use Testbot as the working example for turning a physical robot record into a ROS 2 robot description. Begin with simple primitive geometry, then replace provisional values with measured dimensions and approved CAD from NautiPi.

This lesson creates a useful ROS 2 model for learning and visualisation. It does not yet claim a validated digital twin or a Gazebo physics model.

## Architecture boundary

- NautiPi owns Testbot's physical CAD, wiring, measurements, and hardware evidence.
- CuttleOS owns the `testbot` profile and application-facing commands and telemetry.
- SquidLink owns this ROS 2 description, later Gazebo behaviour, and simulation tests.

## Prerequisites

Complete the earlier course lessons and have the SquidLink ROS 2 workspace available. The target environment is Ubuntu 24.04 LTS with ROS 2 Jazzy and Gazebo Harmonic. The lesson uses ZSH.

## Inspect the Testbot package

```zsh
source /opt/ros/jazzy/setup.zsh
cd "$HOME/robots/robot-SquidLink/ros2_ws"
colcon list | grep testbot_description
find src/testbot_description -maxdepth 3 -type f | sort
```

The package should contain the authoritative Xacro model, a visualisation launch file, and documentation describing its provisional status.

## Build and validate

```zsh
colcon build --symlink-install --packages-select testbot_description
source install/setup.zsh

ros2 run xacro xacro \
  src/testbot_description/urdf/testbot.urdf.xacro \
  > /tmp/testbot.urdf

grep -E '<link |<joint ' /tmp/testbot.urdf
```

## View the model

```zsh
ros2 launch testbot_description display_testbot.launch.py
```

In RViz2, inspect `RobotModel` and `TF`. Move the camera-tilt joint and confirm that the camera link rotates about the intended axis.

## Replace provisional values carefully

Do not edit dimensions from memory. Take measurements from the physical Testbot record in NautiPi. Replace primitive visual and collision geometry with approved simplified meshes only after the physical CAD and licence position are clear. Use separate simplified collision meshes where practical.

## What this proves

- the Testbot description package can be discovered and built;
- Xacro expands into a valid URDF;
- the initial Testbot frame and joint structure can be visualised; and
- the physical-to-simulation source boundary is understood.

## What this does not prove

- that Testbot dimensions, mass, inertia, or joint limits are accurate;
- that Gazebo physics is stable;
- that motor controllers are simulated;
- that the camera stream is available; or
- that the model is a validated digital twin.

The next stage should add Gazebo physics and differential-drive control. Add the CuttleOS NATS bridge only after the local ROS 2/Gazebo loop is repeatable.
