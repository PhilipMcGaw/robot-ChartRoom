# Build and inspect a small ROS 2 robot

## Purpose

Create a deliberately simple two-wheel robot and display it in RViz2.

This is a learning exercise, not an ROV implementation and not a Gazebo or hardware-validation result.

The exercise proves the first part of the simulation toolchain:

```text
Xacro
  ↓
URDF robot description
  ↓
robot_state_publisher
  ↓
TF
  ↓
RViz2
```

It provides a small model for understanding links, joints, transforms, packages, builds, launch files, and visual inspection before adding underwater physics, NATS, or real hardware.

## Safety boundary

Use the independent Ubuntu HiL/SiL workstation. Do not connect the Raspberry Pi, NATS Core, motor controllers, propulsion hardware, or physical ROV hardware for this exercise.

Nothing in this exercise sends a command outside the local ROS 2 graph.

## Prerequisites

Complete [Workstation Setup](00-workstation.md) first. The target environment is Ubuntu 24.04 LTS AMD64 with ROS 2 Jazzy, RViz2, and colcon.

Install the packages if required:

```zsh
sudo apt update
sudo apt install \
  ros-jazzy-xacro \
  ros-jazzy-robot-state-publisher \
  ros-jazzy-joint-state-publisher-gui \
  ros-jazzy-launch \
  ros-jazzy-launch-ros \
  ros-jazzy-rviz2 \
  ros-jazzy-ament-index-python \
  python3-colcon-common-extensions
```

## 1. Create the package

From the workspace `src` directory:

```zsh
mkdir -p "$HOME/robot-SquidLink/ros2_ws/src"
cd "$HOME/robot-SquidLink/ros2_ws/src"
source /opt/ros/jazzy/setup.zsh

ros2 pkg create \
  small_robot_description \
  --build-type ament_cmake \
  --dependencies robot_state_publisher xacro ament_index_python launch launch_ros
```

Create the resource directories:

```zsh
cd "$HOME/robot-SquidLink/ros2_ws/src/small_robot_description"
mkdir -p launch urdf
```

Always run `colcon build` from the workspace root, not from `src`.

## 2. Robot description

Create `urdf/small_robot.urdf.xacro` containing a `base_link` and two continuous wheel joints. Use the standard ROS convention: `x` forward, `y` left, and `z` up.

The model should contain:

```text
small_robot
├── base_link
├── left_wheel
│   └── left_wheel_joint
└── right_wheel
    └── right_wheel_joint
```

Keep mass and inertia values explicitly marked as visualisation placeholders. Do not reuse them for Gazebo physics without proper mass-property calculations.

## 3. Validate Xacro

Generate a temporary URDF before building:

```zsh
cd "$HOME/robot-SquidLink/ros2_ws"
source /opt/ros/jazzy/setup.zsh

ros2 run xacro xacro \
  src/small_robot_description/urdf/small_robot.urdf.xacro \
  > /tmp/small_robot.urdf
```

This is a validation artefact. The Xacro source remains authoritative.

## 4. Install package resources

`CMakeLists.txt` must install the `launch` and `urdf` directories:

```cmake
cmake_minimum_required(VERSION 3.8)
project(small_robot_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY
    launch
    urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
```

The package must declare runtime dependencies on `ament_index_python`, `launch`, `launch_ros`, `robot_state_publisher`, `joint_state_publisher_gui`, and `xacro`.

## 5. Launch file

Create `launch/display.launch.py` and ensure it defines the required entry point:

```python
def generate_launch_description():
    ...
```

Use `get_package_share_directory("small_robot_description")` to locate the installed Xacro file. Do not depend on the current terminal directory.

## 6. Build and launch

```zsh
cd "$HOME/robot-SquidLink/ros2_ws"
source /opt/ros/jazzy/setup.zsh

colcon list
colcon build --packages-select small_robot_description
source install/setup.zsh
ros2 launch small_robot_description display.launch.py
```

A joint-state publisher window should open. Moving a wheel slider should change the corresponding joint state.

## 7. Inspect in RViz2

Open RViz2 and inspect the `RobotModel` and `TF` displays. Confirm that the chassis and both wheels appear correctly and that the transform tree is connected.

## What this proves

- Xacro can be expanded into a URDF;
- the package can be discovered and built;
- `robot_state_publisher` can publish the model's transforms; and
- the model can be inspected in RViz2.

## What this does not prove

- Gazebo physics;
- propulsion or motor control;
- hydrodynamics or buoyancy;
- sensor behaviour;
- camera behaviour;
- NATS integration; or
- physical ROV operation.
