# Luke Ditria — Mini Raspberry Pi AI Wildlife Monitor

This project is a useful reference for compact, low-power edge-AI sensing systems, particularly where camera processing, local inference, data logging, and autonomous power management must operate without continuous cloud connectivity.

## Source

The project is by **Luke Ditria**, an engineer with a PhD in machine learning and BEng. His current work includes **AutoEcology**, which develops edge-compute and ecological-monitoring systems.

- **Video:** https://youtu.be/GxocHfgGO6o
- **Project repository:** https://github.com/LukeDitria/mini_ai_camera
- **AutoEcology:** https://www.auto-ecology.com/
- **Author:** https://www.auto-ecology.com/

The supplied social-media screenshots identify the video as a recent update to the author's **Mini AI Wildlife Monitor** and show the outdoor solar-powered installation.

## System summary

The current version combines:

- Raspberry Pi Zero 2 W;
- Raspberry Pi AI Camera using the Sony IMX500;
- a solar-powered supply using AutoEcology's PV Pi;
- local AI inference;
- a YOLO11n object-detection model;
- local identification of bird species; and
- long-duration outdoor operation.

The author's public project information states that the software has also been verified on a Raspberry Pi 5. The current repository uses Python 3.13 or later, Raspberry Pi OS Trixie, Picamera2, the IMX500 software stack, OpenCV, and uv for Python environment management.

## Relevant engineering features

### On-device inference

The AI inference is performed locally rather than sending image data to a remote service. This is directly relevant to robot systems where bandwidth, latency, privacy, or intermittent connectivity can make cloud inference unsuitable.

The current project uses the IMX500's neural-network capability and a YOLO-based detector. The repository includes a compiled model and configuration for limiting the classes that are detected.

### Event-based data handling

The current software does not simply save every frame. Its configuration includes:

- confidence and IoU thresholds;
- a maximum inference rate;
- an exponential moving average for detection confidence;
- activation and deactivation thresholds;
- a circular pre-capture video buffer; and
- optional image, video, and JSON-data output.

This is a useful pattern for CuttleOS sensor workloads: process continuously, but persist detailed data only when an event justifies it.

### Autonomous power

The outdoor installation combines the Raspberry Pi Zero 2 W and AI Camera with the PV Pi solar power-management hardware.

AutoEcology describes the PV Pi as providing solar battery charging and power management for Raspberry Pi and other single-board computers. Its stated capabilities include battery monitoring, controlled shutdown/restart behaviour, and scheduled operation.

This is particularly relevant to remote CuttleOS nodes and other autonomous sensing platforms.

### Service-based operation

The software includes an installation command that creates systemd services. This is relevant to the CuttleOS deployment model, where long-running robot services should be managed by the operating system rather than by an interactive shell.

## Relevance to the Robots project

This is **research/reference material, not an adopted design**.

Potentially useful ideas to investigate include:

1. **Edge AI:** local inference on constrained compute hardware.
2. **Event-driven recording:** retain detailed sensor data around meaningful events rather than continuously.
3. **Pre-event buffering:** retain a short period before an event trigger.
4. **Low-power scheduling:** operate high-power sensing or processing only when useful.
5. **Autonomous power management:** combine battery telemetry with controlled shutdown and recovery.
6. **Outdoor deployment:** compact enclosure, solar supply, camera, compute, and data storage as a single field node.
7. **Service supervision:** systemd-managed services for autonomous operation.

These concepts may inform future CuttleOS perception, remote-node, or autonomous-sensing designs, but they should not be treated as project requirements until separately evaluated.

## Related research

The project is especially relevant to the existing Chartroom research concerning:

- Raspberry Pi deployment;
- edge compute;
- cameras and video;
- autonomous/remote sensing;
- low-power systems; and
- field-deployed robotic or sensing nodes.

## Verification notes

The social-media screenshots supplied during research show the author's profile, the outdoor installation, and the statement that the monitor had been operating outside for approximately six months while detecting and identifying birds.

Independent public sources provide additional technical detail. The author's GitHub repository documents the current software and supported Raspberry Pi platforms. AutoEcology describes the wider edge-AI and ecological-monitoring work, including the PV Pi power-management system.

Specific hardware, model, power, enclosure, and environmental-performance claims should be verified against the original project documentation before being used as engineering requirements or design inputs.
