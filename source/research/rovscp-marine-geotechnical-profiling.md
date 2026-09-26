---
title: "ROVSCP marine geotechnical profiling paper"
description: "Critical research notes on a proposed ROV-mounted penetrometer for soft marine deposits."
date: 2026-09-26
type: research
status: reference
authority: Chartroom
tags:
  - research
  - rov
  - marine-geotechnics
  - sediment
  - instrumentation
---

# ROVSCP marine geotechnical profiling paper

## Scope and source status

This note reviews the user-supplied 12-page paper *Subaqueous Geotechnical Forensics: A New Methodology for Mapping and Stability Analysis of Low-Shear Biogenic Deposits*, by Steve Haggitt of Haggitt Consulting, dated 2026-09-23. The PDF labels itself a technical white paper, “Industry Standard 2.0”, and states that US provisional patent application 64/159,253 is pending. Those are descriptions and legal claims printed in the supplied document; they have not been independently verified.

This is a critical research reference, not an engineering instruction, validated method, project decision, or accepted standard. The paper was read in full. It describes anonymised case studies but supplies no raw measurements, site metadata, apparatus drawings, complete bibliography, or reproducible test protocol in the supplied copy.

## Proposal described in the paper

The paper proposes a remotely operated vehicle static cone penetrometer (ROVSCP) for profiling soft, organic seabed deposits. It describes a neutrally buoyant platform, a “triple-mass inertial drive”, and a seven-item sensor suite: fibre-optic gyro/inertial navigation, Doppler velocity log, hydrostatic depth, tip pressure, triple-laser planar scaling, acoustic sonar ranging, and physical depth markings checked against video.

It further proposes interpreting resistance-time and extraction signatures as indicators of biogenic jamming, an interstitial “root zone”, basal gas-pressure effects, deposit maturity, and mass stability. Numerical claims include a 6 mm root zone, rapid refusal signatures, and a 2.4-fold increase in lateral shear resistance. These are claims made by the paper; the supplied document does not provide the underlying measurements or enough test detail to reproduce or assess them.

## Comparison with established work

The broad idea of using remotely operated or submersible-mounted in-situ penetrometers is established. A 2002 University of Plymouth thesis describes ROV-assisted nearshore geotechnical and hydrographic investigation, including a T-bar flow-round penetrometer and sediment coring. Earlier published work describes cone penetrometers and other miniature geotechnical instruments deployed from a submersible. More recent seabed CPT work describes controlled penetration, tip resistance, sleeve friction, pore pressure, and calibration/field testing as core parts of a defensible instrument and method.

Accordingly, the supplied paper may be a lead for a particular instrument concept or interpretation of organic deposits, but it does not establish that ROV-mounted penetrometry, low-disturbance in-situ probing, or the named generic mechanical effects are new. The specific ROVSCP apparatus and its claimed diagnostic signatures remain unverified from this source.

## Evidence and engineering questions

The paper does not show enough information to evaluate its “inertia-driven” or “neutrally buoyant” penetration mechanism. A probe entering sediment must have a defined reaction-force path; the paper copy does not quantify the forces, actuator, vehicle restraint, penetration-speed control, or how vehicle motion is separated from probe motion. Neutral buoyancy alone does not demonstrate stable static penetration.

Before treating its measurements as geotechnical properties or environmental evidence, the following would need to be documented and independently checked:

- cone or T-bar geometry, dimensions, materials, and intended sediment range;
- load path, actuator capacity, vehicle reaction or anchoring method, and safe recovery behaviour;
- penetration and extraction speed, position measurement, sampling rate, sensor calibration, filtering, and uncertainty;
- repeat tests and comparisons with accepted reference measurements such as cores, vane shear, or calibrated CPT results;
- site conditions, ground truth, full data traces, analysis methods, and independent replication; and
- a defined validation basis for the proposed classifications and any regulatory or stability conclusions.

The specific inferences about a 6 mm anchoring layer, gas-driven hydroplaning, storm “reset”, sand bedform angle as a guaranteed threshold, and certified benthic recovery should not be adopted from the supplied paper alone.

## Relevance to the Robots project

The useful project-level takeaway is a possible future payload-research direction: an ROV may carry an instrument for shallow sediment profiling, but such a tool needs a mechanically stable reaction system, calibrated force and depth sensing, and comparison with ground-truth samples. This is separate from the current BlueOS/Adeept HAT deployment and the Sensea camera/logger reference; neither provides a seabed penetrometer or validates these geotechnical claims.

For Chartroom’s existing underwater survey research, see [Vobster photogrammetry](vobster-photogrammetry.md), which concerns visual mapping and survey repeatability rather than sediment strength measurements. No ROVSCP hardware, software, sensor suite, or survey method is selected or validated for the project.

## References

- Haggitt, Steve. *Subaqueous Geotechnical Forensics: A New Methodology for Mapping and Stability Analysis of Low-Shear Biogenic Deposits*. Haggitt Consulting, 2026-09-23. User-supplied PDF; 12 pages; supplied copy states “US Provisional Patent #64/159,253 Pending”.
- Gillon, Rosemary Jayne Browning. *The Role of the ROV Within Integrated Geotechnical and Hydrographic Site Investigation*. University of Plymouth thesis, 2002. [Repository record](https://pearl.plymouth.ac.uk/fose-theses-other/290/).
- Guo et al. “Development and application of a 3,000-m Seabed Cone Penetration Test and Sampling System based on a hydraulic drive.” *Frontiers in Marine Science*, 2024. [Article](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2024.1377405/full).
- “Surf Zone Ground Investigation Using ROV-mounted CPT.” *Hydro International*, describing a project-specific commercial ROV/CPT deployment. [Article](https://www.hydro-international.com/content/article/surf-zone-ground-investigation-using-rov-mounted-cpt).
- Lambert, Douglas N., Richard H. Bennett, and others. “Submersible-Mounted In-Situ Geotechnical Instrumentation.” *AAPG Bulletin* 65(9), 1981, abstract. [DOI record](https://doi.org/10.1306/03B596E3-16D1-11D7-8645000102C1865D).

**Status:** reference only. The paper’s empirical claims, novelty, patent status, and proposed classifications have not been independently validated for the Robots project.
