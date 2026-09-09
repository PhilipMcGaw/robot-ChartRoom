# Vobster Photogrammetry Project

## Source

- [3dMB — Vobster Photogrammetry Project](https://3dmb.uk/project/vobster-photogrammetry-project/)
- [3dMB — Underwater Photogrammetry & Mapping](https://3dmb.uk/rov-underwater-photogrammetry-and-mapping/)
- [3dMB](https://3dmb.uk/)

## Summary

The Vobster Photogrammetry Project is a long-running attempt to create a complete 3D model of Vobster Quay, including areas above and below the waterline, using consumer-grade equipment. The project is particularly relevant to the Robots ecosystem because it demonstrates how a large underwater mapping problem can be decomposed into manageable capture objectives and progressively improved as the operator learns from each iteration.

Phase 1 (2017–2019) began with a Canon 5D Mk III and EF 8–15 mm fisheye lens. The quarry was divided into individual attractions, which were scanned separately. The scale of the task led to the camera being mounted on an underwater scooter after the Canon 5D Mk IV introduced an internal intervalometer. Underwater models were subsequently linked and aligned with aerial drone data. The resulting model used more than 76,000 images.

Phase 2 (2020–2022) restarted the modelling effort using a Canon R5 with the same fisheye lens. The objective expanded from individual attractions and connecting paths to include comparatively featureless silt areas. The project also explored more accessible ways of presenting and interacting with the resulting model data.

Phase 3 began in 2023 and is ongoing. Separately, 3dMB reports that it moved from diver-based underwater data capture to ROV-based capture in 2024, allowing larger sensor payloads, more efficient data collection, and reduced dependence on diver operations. Its current ROV mapping work describes six-degree-of-freedom camera movement and electronic integration with housed professional cameras.

## Relevance to the Robots ecosystem

### ROV camera and mapping payloads

The project is a strong reference for treating imaging as an engineering payload rather than simply attaching a camera to an ROV. Useful lessons include:

- divide large environments into repeatable, manageable survey objectives;
- design capture procedures around the requirements of the photogrammetry pipeline rather than treating video as sufficient data;
- use controlled camera motion and repeatable coverage to improve reconstruction;
- integrate camera operation with the ROV where useful, including remote triggering and camera/focus control;
- consider 6-DoF vehicle motion as an asset for survey and cinematic capture; and
- retain the raw imagery so that improved reconstruction methods can be applied later.

### Survey planning and repeatability

Vobster demonstrates the value of an iterative survey methodology. Phase 2 deliberately restarted the project rather than simply extending the first dataset, incorporating lessons from the first attempt. This is a useful model for ROV mapping experiments: establish a baseline dataset, identify reconstruction failures, change the capture procedure, and repeat the survey with improved coverage.

For the current ROV, this suggests treating mapping missions as explicit, repeatable test procedures with defined coverage, camera settings, vehicle speed, overlap, lighting, depth, and environmental conditions where practical.

### Multi-source spatial registration

The combination of underwater imagery with aerial drone imagery is particularly interesting. It demonstrates a route towards building a larger site model from datasets acquired by different vehicles and sensors. This is relevant to the broader Robots architecture because Cockpit, Datalogger, and future mapping tools may need to associate observations from different platforms and missions with a common spatial reference.

This should be treated as a future mapping/data-management capability, not as a requirement for the current ROV implementation.

### ROV as a data-collection platform

3dMB's move to ROV-based acquisition is especially relevant to the project's long-term direction. An ROV can carry multiple sensors and cameras and can operate without diver decompression constraints. This supports the wider idea of a modular survey vehicle in which cameras, CTD sensors, environmental sensors, lights, and other payloads share a common vehicle and telemetry infrastructure.

The key architectural lesson is that the ROV should expose a stable payload interface while allowing the sensing package to evolve independently.

### Data processing and presentation

The project also highlights a distinction between **data acquisition**, **reconstruction**, and **presentation**. A successful ROV mapping system therefore needs more than a camera and storage:

1. capture imagery with sufficient overlap and metadata;
2. retain mission and vehicle telemetry alongside the imagery;
3. reconstruct and register the datasets offline;
4. validate the resulting geometry; and
5. provide an accessible way to inspect or publish the model.

This aligns well with the existing separation between vehicle control, Datalogger, and Cockpit. A future mapping pipeline could consume Datalogger mission records and imagery without becoming part of the safety-critical control path.

## Potential future work

- Define a repeatable underwater photogrammetry test procedure for the ROV.
- Investigate camera triggering and metadata synchronisation with vehicle telemetry.
- Determine what vehicle state should be recorded with every image or image sequence.
- Evaluate lighting, camera baseline, altitude/stand-off distance, and vehicle speed as reconstruction variables.
- Investigate whether ROV and surface/drone datasets could eventually be registered into a common site model.
- Consider a future Cockpit survey mode showing planned coverage, camera state, depth, and mission progress.
- Keep raw imagery and mission metadata so that improved reconstruction software can be used later.

## Caveats

The Vobster project is a practical recreational/commercial photogrammetry project, not a specification for underwater surveying. Its camera equipment, processing workflow, and survey methodology should therefore be treated as inspiration rather than requirements. Photogrammetric accuracy, scale, georeferencing, and reconstruction quality need to be validated for the intended application.

## Read later

- [Vobster Photogrammetry Project](https://3dmb.uk/project/vobster-photogrammetry-project/)
- [3dMB ROV Underwater Photogrammetry & Mapping](https://3dmb.uk/rov-underwater-photogrammetry-and-mapping/)
- [3dMB](https://3dmb.uk/)
