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
- **WILDLABS edge-AI discussion:** https://wildlabs.net/en/discussion/ai-edge-compute-based-wildlife-detection
- **Custom-model training video:** https://youtu.be/I69lAtA2pP0
- **Luke Ditria's deep-learning tutorials:** https://github.com/LukeDitria/pytorch_tutorials
- **Mothbox project:** https://digital-naturalism-laboratories.github.io/Mothbox/

**Technical authority:** `LukeDitria/mini_ai_camera` is the primary source for the monitor's software, configuration, installation, and supported Raspberry Pi platforms. `LukeDitria/RasPi_YOLO` is the related source for model training and deployment workflows.

The WILDLABS material provides useful project provenance and discussion of field constraints. The Hackster coverage provides secondary reporting on the later solar-powered revision.

## External resources and project provenance

There is evidence that Luke's work developed within the wider edge-AI and conservation community, but I have **not** found a statement from Luke identifying a particular project as the direct design inspiration for the Mini AI Wildlife Monitor.

The clearest provenance is WILDLABS. When Luke introduced his earlier edge-compute wildlife detector there in February 2025, he said that he had "just come across this site" and that it was exactly what he had been looking for. The discussion covers low-power object detection, field deployment, solar-battery operation, datasets, annotation problems, and model deployment. Luke subsequently used the discussion to exchange information with other wildlife-AI practitioners. In particular, he said he was looking for additional dataset sources and discussed annotation pollution and automated relabelling. [See WILDLABS discussion.]

Luke also points people to his own custom-model training material. In August 2025, when asked how to train a model for the Raspberry Pi AI Camera, he directed the questioner to his custom-model training video. His wider pytorch_tutorials repository provides additional background material on deep-learning implementation, although it is not specific evidence for the wildlife monitor's design.

The **Mothbox** project is particularly relevant to our research because it is another wildlife/insect-monitoring camera platform, and it was explicitly mentioned in discussion of Luke's project. However, the available evidence shows another participant raising Mothbox as a comparison; it does **not** establish that Luke based his design on Mothbox.

For that reason, these should be recorded as **related resources and provenance**, rather than described as confirmed design inspirations.

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

## Potential application to fish identification

The same general architecture could be investigated for species-level fish identification, but this remains a **research candidate, not an adopted design**.

Luke's public material supports the general concept of running object-detection and identification models locally for ecological monitoring. His later public description of the mini monitor states that the system uses YOLO11n to identify local bird species. [See Luke's 2026 project description.] I have not found evidence that Luke has already deployed this particular monitor for fish identification.

For an ROV application, the key question is whether the camera can consistently provide enough information for the model to distinguish the target species. Luke notes that the IMX500 processing path is limited to 640 × 480 pixels for this application and that the target therefore needs to occupy enough of the image to be discernible. He also notes that the required image detail depends on the species.

An ROV has a potentially useful advantage over a fixed wildlife camera: it can deliberately approach a target and control camera distance. That does not remove the underwater problems of turbidity, backscatter, variable illumination, colour attenuation, motion blur, occlusion, and visually similar species.

A sensible investigation would therefore be:

1. select a small number of visually distinguishable target species;
2. collect representative underwater imagery at the intended operating distance;
3. annotate fish bounding boxes and species labels;
4. train and validate a compact detector/classifier;
5. measure performance separately for detection and species identification;
6. test false positives and false negatives under varying visibility and lighting; and
7. compare IMX500-class inference with a higher-capacity platform such as Raspberry Pi 5 plus Hailo where the target occupies too few pixels.

This should remain a research input to future CuttleOS perception work rather than a dependency on Luke's implementation.

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
