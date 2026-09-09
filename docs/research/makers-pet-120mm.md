# Maker's Pet 120 mm robot research

Maker's Pet's 120 mm Arduino/ROS 2 Self-Driving Robot Build Pack is a useful reference for **SwarmBot and MarsBot**, particularly for small differential-drive robotics, low-cost LiDAR, ROS 2 integration, modular 3D-printed mechanical design, and educational bring-up workflows.

It is much less relevant to the underwater ROV because the exposed 2D LiDAR and small wheeled chassis are inherently terrestrial. It should therefore be treated as a terrestrial robotics reference rather than a cross-project hardware target.

## What is interesting

The 120 mm robot combines a small round chassis, two N20 differential-drive motors, a 360° scanning 2D LiDAR, an ESP32 development board, and a dedicated motor-driver board. The published design includes downloadable 3D-print files, Fusion 360 source, board documentation, configuration, firmware, and ROS 2 software references. citeturn0search1turn0search0

The design is particularly interesting because the physical robot is deliberately small while still providing a useful autonomous-robot stack: obstacle sensing, mapping, SLAM, navigation, and autonomous exploration. citeturn0search1

### SwarmBot relevance

This is a strong reference for the **educational and small-robot side of SwarmBot**:

- compact differential-drive platform;
- inexpensive, accessible components;
- ESP32 as a low-level robot controller;
- dedicated motor-driver hardware;
- 360° 2D LiDAR as an optional autonomy/sensing payload;
- 3D-printable and modifiable mechanical parts;
- ROS 2 as an accessible higher-level robotics environment; and
- step-by-step bring-up and troubleshooting material aimed at learners.

The project's ability to run several robots from one ROS 2 PC is also worth studying for SwarmBot. Maker's Pet documents using a separate container and UDP port for each robot, which is a useful practical example of multi-robot development, even though our eventual SwarmBot architecture is expected to use our own communications/control boundaries rather than adopting this stack wholesale. citeturn0search0

The LiDAR should also be considered an **optional capability**, rather than something that every educational SwarmBot must carry. It could provide a useful advanced module for mapping, obstacle avoidance, localisation, or multi-robot experiments without making the basic classroom robot unnecessarily complex.

### MarsBot relevance

The 120 mm platform is an interesting small-scale reference for MarsBot, particularly for:

- differential-drive kinematics;
- wheel/encoder integration;
- 2D LiDAR mounting and scanning geometry;
- SLAM and navigation experiments;
- autonomous exploration;
- small-robot power and packaging;
- 3D-printable mechanical construction; and
- a staged progression from teleoperation to autonomous navigation.

MarsBot should not copy the 120 mm chassis. Its value is as a **small terrestrial test platform** for algorithms and interfaces that can later be exercised on a larger, more capable rover.

### Mechanical design lessons

The chassis demonstrates a useful approach to making a small robot easy to modify: the base, LiDAR posts/skirt, board posts, battery-holder components, wheels, and motor clamps are separately documented and available as printable/source models. citeturn0search1

This supports a general design principle worth carrying into SwarmBot and MarsBot: **define mounting interfaces so sensors and payloads can be replaced without redesigning the complete vehicle**.

The published build also demonstrates a practical way of putting a 360° LiDAR above the body while retaining a compact footprint. That is potentially useful inspiration for MarsBot, where a roof-mounted sensor mast or raised sensor pod may be more appropriate than trying to hide the LiDAR within the main body.

### Software and documentation lessons

Maker's Pet provides an unusually complete beginner-to-working-robot path: assembly, PC setup, firmware, configuration, bring-up, mapping, self-driving, troubleshooting, CAD/source files, and ROS 2 references. citeturn0view0turn0view1

This is relevant to the wider Robots ecosystem's educational goals. The useful lesson is not necessarily the particular ROS 2 distribution or Docker arrangement, but the **staged development experience**:

1. build the hardware;
2. establish low-level motor control;
3. verify encoders and motion;
4. bring up sensing;
5. teleoperate;
6. map the environment;
7. add localisation/navigation; and
8. progress to autonomous behaviour.

That progression is a useful candidate model for SwarmBot/MarsBot learning material and for HiL/SiL test milestones.

## Maker's Pet site — further research

The site is worth reviewing beyond the 120 mm kit. Its current material includes work on OOMWOO, low-cost LiDAR integration, ROS 2, and other robot-building resources. In particular, the OOMWOO project is already relevant to our existing research because of its Raspberry Pi, ROS 2, 2D LiDAR, 3D-printed, local-first approach. citeturn0search2

The site should therefore be treated as a **continuing source of robotics design inspiration**, rather than this being a one-off product reference.

## K-9 and 360° LiDAR

A 360° LiDAR is not obviously useful to the current K-9 concept. The major issue is not merely finding a mounting position but preserving a useful 360° horizontal field of view without making the sensor visually intrusive or mechanically vulnerable.

Do not force the Maker's Pet mounting concept onto K-9. If autonomous navigation or obstacle sensing becomes a K-9 requirement, investigate a dedicated sensor placement that fits the K-9 mechanical/aesthetic envelope, potentially using distributed or non-360° sensing instead.

## Status

**Status:** Research / design inspiration. Relevant primarily to SwarmBot and MarsBot; terrestrial only and not a requirement for either project.

**Read later:** [Maker's Pet 120 mm Build Pack](https://makerspet.com/product/arduino-ros2-self-driving-robot-120mm-build-pack/) and [BLD-120MM-PACK build instructions](https://makerspet.com/blog/BLD-120MM-PACK/).
