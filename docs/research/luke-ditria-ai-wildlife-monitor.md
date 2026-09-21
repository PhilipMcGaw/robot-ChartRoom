# Luke Ditria — Mini Raspberry Pi AI Wildlife Monitor

This project is a useful reference for compact, low-power edge-AI sensing systems, particularly where camera processing, local inference, data logging, and autonomous power management must operate without continuous cloud connectivity.

## Primary sources

The project is by **Luke Ditria**, whose work includes edge-compute and ecological-monitoring systems.

- **Project repository:** https://github.com/LukeDitria/mini_ai_camera
- **Model training/export repository:** https://github.com/LukeDitria/RasPi_YOLO
- **Build video:** https://youtu.be/qhY_3XCSYsM
- **Video supplied for this research:** https://youtu.be/GxocHfgGO6o
- **AutoEcology:** https://www.auto-ecology.com/
- **WILDLABS author profile:** https://wildlabs.net/en/members/luked
- **WILDLABS project discussion:** https://wildlabs.net/en/discussion/mini-ai-wildlife-monitor

**Technical authority:** `LukeDitria/mini_ai_camera` is the primary source for the monitor's software, configuration, installation, and supported Raspberry Pi platforms. `LukeDitria/RasPi_YOLO` is the related source for model training and deployment workflows.

The WILDLABS material provides useful project provenance and discussion of field constraints. The Hackster coverage provides secondary reporting on the later solar-powered revision.

## System summary

The current project is based around:

- Raspberry Pi Zero 2 W;
- Raspberry Pi AI Camera using the Sony IMX500;
- solar-powered operation using the author's PV Pi hardware;
- local AI inference;
- YOLO-family object detection; and
- local wildlife/bird identification.

The project's README states that the software has been verified on a Raspberry Pi 5 and Raspberry Pi Zero 2 W with Raspberry Pi OS Trixie, and requires system-wide Python 3.13 or later. It uses Picamera2, the IMX500 software stack, OpenCV, and `uv` for Python environment management.

The project has evolved through several hardware configurations. Earlier versions used a Raspberry Pi 5 with a Hailo-based AI accelerator; later versions moved inference onto the Sony IMX500 in the Raspberry Pi AI Camera and used the smaller Raspberry Pi Zero 2 W.

## Relevant engineering features

### On-device inference

The AI inference is performed locally rather than sending image data to a remote service. This is directly relevant to robot systems where bandwidth, latency, privacy, or intermittent connectivity can make cloud inference unsuitable.

The related `RasPi_YOLO` repository documents training and export workflows for both the Sony IMX500 and Hailo accelerators.

### Event-based data handling

The current `mini_ai_camera` configuration includes:

- confidence and IoU thresholds;
- a maximum inference rate;
- an exponential moving average for detection confidence;
- activation and deactivation thresholds;
- a circular pre-capture video buffer; and
- optional image, video, and JSON-data output.

The default configuration documented by the repository includes a 3-second pre-capture buffer, an EMA smoothing factor of 0.2, an event-activation threshold of 0.8, and an event-deactivation threshold of 0.5.

This is a useful pattern for CuttleOS sensor workloads: process continuously, but persist detailed data only when an event justifies it.

### Autonomous power

The outdoor installation combines the Raspberry Pi Zero 2 W and AI Camera with solar power and the author's PV Pi hardware.

Secondary reporting on the latest revision describes a LiFePO₄ battery system and a PV Pi HAT with maximum-power-point tracking, battery charging, battery telemetry, a real-time clock, and power scheduling. These details should be treated as project-specific implementation information rather than requirements for the Robots project.

### Service-based operation

The software includes an installation command that creates systemd services. The repository documents using `systemctl` and `journalctl` to manage and inspect the services.

This is relevant to the CuttleOS deployment model, where long-running robot services should be managed by the operating system rather than by an interactive shell.

## Model provenance and versioning

There are multiple generations of the project, so model claims need to be tied to the relevant revision.

The current `mini_ai_camera` README documents a default compiled `yolov8n.rpk` model configuration. The related training repository also documents YOLOv8 workflows and contains a TODO noting that YOLO11 export to the IMX500 had not yet been tested in that repository revision.

Separately, Hackster's May/June 2026 coverage of the solar-powered revision reports that Ditria trained a YOLO11n model for 52 local species and exported the model for the IMX500. This is a useful description of the later field configuration, but it should not be conflated with the version/configuration currently documented in the repository README.

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

## Field constraints

The WILDLABS project discussion provides useful practical context. Ditria notes that the IMX500 processing path is limited to a 640 × 480 image size for this application, meaning that the target must occupy enough of the image to be discernible. He also distinguishes this from higher-resolution approaches using a Raspberry Pi 5 and Hailo accelerator.

This is an important engineering consideration for future robotic perception work: detector compute performance is only one part of the system. Target angular size, optics, sensor resolution, inference resolution, model capacity, illumination, and motion all affect detection and classification performance.

## Related research

The project is especially relevant to the existing Chartroom research concerning:

- Raspberry Pi deployment;
- edge compute;
- cameras and video;
- autonomous/remote sensing;
- low-power systems; and
- field-deployed robotic or sensing nodes.

## Verification notes

The supplied social-media screenshots show the author's profile, the outdoor installation, and the solar-powered wildlife-monitor concept.

The primary GitHub repository and related model repository have now been identified and checked. WILDLABS provides additional project history and discussion, while Hackster provides secondary reporting on the later solar-powered revision.

Specific hardware, model, power, enclosure, environmental-performance, and field-runtime claims should be verified against the relevant project revision before being used as engineering requirements or design inputs.
