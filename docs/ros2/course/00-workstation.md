# Workstation setup — Ubuntu, ROS 2, and Gazebo

## Objective

Create a known-good Ubuntu development and simulation workstation for ROS 2/Gazebo HiL/SiL work.

## Target stack

```text
Intel Mac
  ↓
VMware Fusion
  ↓
Ubuntu 24.04 LTS AMD64
  ├── ROS 2 Jazzy
  ├── Gazebo Harmonic
  ├── RViz2
  ├── ros_gz
  ├── colcon
  └── Git / SSH
```

The VM is the HiL/SiL workstation boundary. It does not host the Cockpit, Control, or Datalogger application runtimes.

## VM baseline

Start with approximately:

- 4 CPU cores;
- 6–8 GB RAM where the host permits;
- 60–80 GB dynamically allocated disk;
- bridged networking when direct LAN communication is required; and
- 3D acceleration enabled initially.

Do not allocate every host CPU core or all available RAM to the VM.

## Ubuntu

Use Ubuntu 24.04 LTS Desktop AMD64. This provides the graphical environment required for RViz2 and Gazebo.

Update the installation before adding project software:

```bash
sudo apt update
sudo apt full-upgrade
```

## VMware integration

Install the Ubuntu-packaged VMware tools:

```bash
sudo apt install open-vm-tools open-vm-tools-desktop
sudo reboot
```

If display rendering is poor, check VMware Fusion 3D acceleration and Ubuntu display scaling before changing the ROS installation.

## Development tools

```bash
sudo apt install \
  build-essential \
  cmake \
  curl \
  git \
  wget \
  python3-dev \
  python3-pip \
  python3-venv \
  software-properties-common
```

Enable Universe if required:

```bash
sudo add-apt-repository universe
sudo apt update
```

## ROS 2 Jazzy

Install ROS 2 Jazzy using the current official ROS 2 Debian-package instructions. The intended distribution is `ros-jazzy-desktop` because the workstation requires RViz2 and the standard graphical tools.

After installation, source ROS 2 from ZSH:

```zsh
source /opt/ros/jazzy/setup.zsh
echo 'source /opt/ros/jazzy/setup.zsh' >> ~/.zshrc
```

Verify:

```zsh
printenv ROS_DISTRO
ros2 --help
ros2 doctor
```

`ROS_DISTRO` should report `jazzy`.

## Base ROS test

Before debugging project software, prove that ROS itself works.

Terminal 1:

```zsh
ros2 run demo_nodes_cpp talker
```

Terminal 2:

```zsh
ros2 run demo_nodes_py listener
```

The listener should receive messages. Then inspect:

```zsh
ros2 topic list
```

## Gazebo and development tools

Install ROS/Gazebo integration and common workspace tools:

```bash
sudo apt install \
  ros-jazzy-ros-gz \
  python3-colcon-common-extensions \
  python3-rosdep \
  python3-vcstool
```

Initialise `rosdep` once:

```bash
sudo rosdep init
rosdep update
```

If `rosdep init` reports that it is already initialised, run only `rosdep update`.

Test Gazebo:

```bash
gz sim
```

## Workspace

The SquidLink ROS workspace lives inside the repository:

```text
robot-SquidLink/
└── ros2_ws/
    └── src/
```

Create it with:

```zsh
mkdir -p "$HOME/robot-SquidLink/ros2_ws/src"
```

Run `colcon` from `ros2_ws`, never from `ros2_ws/src`.

Generated `build/`, `install/`, and `log/` directories should not be committed.

## SSH and GitHub

If remote administration is required:

```bash
sudo apt install openssh-server
```

Use Ed25519 keys for SSH authentication. Keep private keys out of the repository.

## Baseline

Before project-specific ROS packages are added, verify:

- Ubuntu 24.04 LTS AMD64;
- VMware guest integration;
- correct display behaviour;
- ROS 2 Jazzy;
- ROS demo nodes;
- Gazebo Harmonic;
- RViz2;
- `colcon`, `rosdep`, and `vcstool`; and
- Git/SSH.

Then take a VMware snapshot. This provides a known-good workstation baseline.

## Exit criteria

- [ ] Ubuntu runs reliably in VMware Fusion.
- [ ] ROS 2 Jazzy is sourced successfully with ZSH.
- [ ] RViz2 starts.
- [ ] Gazebo starts.
- [ ] ROS demo nodes communicate.
- [ ] `colcon` is available.
- [ ] The SquidLink workspace can be created.
- [ ] The VM is suitable for a baseline snapshot.
