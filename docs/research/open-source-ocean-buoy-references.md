# Open-source ocean buoy and environmental sensing references

A focused set of academic, student, and open-source buoy projects relevant to the Smart Buoy work. These are **research/read-later references**, not project dependencies. The purpose is to compare engineering approaches, deployment experience, measurement validation, power budgets, communications, and the transition from prototype to useful scientific instrument.

## T3chFlicks Smart Buoy

https://github.com/sk-t3ch/smart-buoy
https://magazine.raspberrypi.com/articles/smart-buoy
https://gitlab.com/t3chflicks/smart-buoy
https://hackaday.io/project/166572-smart-buoy/details
https://www.hackster.io/t3chflicks/smart-buoy-summary-7d1a7b

T3chFlicks developed an Arduino buoy with a Raspberry Pi base station and Vue dashboard. The prototype measured wave height/period/power/direction, water temperature, air temperature/humidity/pressure, GPS, and electrical status. It used solar power, battery-aware scheduled operation, nRF24 radio, local processing/storage experiments, and a shore/base-station dashboard. The original GitLab repository was created in March 2019 and later moved to GitHub.

The project was created by **T3chFlicks, a small UK technology education and services company**. Public company records identify **Stephanie Katherine Andrews** and **Sebastian Edward Kelly** as the two directors/people with significant control of T3CH FLICKS LTD. Contemporary project material generally refers to Stephanie as **Steph** and Sebastian as **Seb**.

The Smart Buoy originated from Steph's undergraduate dissertation work on the impact of sea-level rise in Grenada. The Raspberry Pi/MagPi and HackSpace coverage says she found it difficult to obtain reliable, continuous coastal data and that this motivated the team to build an inexpensive system capable of producing meaningful measurements. The buoy was subsequently built and deployed in Grenada, with the team also discussing the project with the Grenadian government.

Contemporary documentation is particularly valuable as a **case study/post-mortem**. The team openly documented problems with sensor accuracy, memory constraints, waterproofing, storage, wave-property algorithms, and deployment. They identified an inability to reprogram the sealed buoy as a major design mistake and proposed an open/resealable enclosure, a more capable ESP32-class controller, LoRa, and additional onboard processing for a possible version 2.

The Hackaday and Hackster material also shows a useful full-stack engineering chain: embedded acquisition → radio link → Raspberry Pi base station → database/server → Vue dashboard, with a fake-data generator for dashboard development. One T3chFlicks team member was specifically described as the web developer who built the Vue dashboard.

**Relevance:** direct historical baseline for Smart Buoy. Use it to understand what a low-cost prototype can achieve and, equally importantly, what prevents a prototype becoming a persistent scientific instrument. It is also a useful reference for the way a small multidisciplinary team can combine environmental research, electronics, mechanical design, software, data visualisation, and education.

**Open research question:** the public material establishes Stephanie Katherine Andrews as Steph and links Smart Buoy to her undergraduate dissertation, but the university and dissertation title have not yet been conclusively established. Do not infer them from unrelated name matches.

## OLB — Open LoRa Buoy

https://arxiv.org/abs/2601.05615
https://github.com/larswd/OpenLoraBuoy

Dreyer et al. developed an open-source coastal drifter using LoRa. The design targets reliability, low cost, modifiability, and power efficiency. Reported validation experiments achieved observed radio ranges up to approximately 2.3 km and an expected battery life of up to seven months. The authors plan to release firmware for the buoy, base station, and digital platform together with PCB designs and a maintained component list.

**Relevance:** highest-priority modern reference. It demonstrates a progression from hobby-scale IoT towards a deliberately deployable, open scientific instrument. Pay particular attention to radio duty cycling, energy budget, recovery, maintainability, and the relationship between buoy firmware and base-station software.

**Status:** Read later — high priority.

## Smart Buoy communications — 868 MHz LoRa baseline

Recent review of the radio choice suggests retaining **868 MHz LoRa as the baseline communications technology**, but treating the radio and antenna as a measured engineering subsystem rather than simply selecting a module.

An experimental 868 MHz LoRa study specifically examining water-surface communication demonstrated feasibility and measured 160 m over-water communication with a buffered antenna arrangement, compared with 80 m for the unbuffered arrangement. The study reinforces that the air/water interface can significantly affect antenna performance. Water's high permittivity and conductivity make antenna placement and matching important. [1]

For the Smart Buoy concept, the practical design target should therefore be an antenna **above the waterline**, mechanically separated from conductive structures, with antenna height treated as a validation parameter. A nominal target of roughly **200–500 mm above mean water level** is a useful engineering starting point, not a guaranteed requirement. Testing should cover antenna height, buoy orientation, sea state, range, RSSI/SNR, packet delivery ratio, reconnection behaviour, and energy consumed per successful telemetry packet.

The communications architecture should remain transport-independent at the application layer. The buoy telemetry protocol should not depend on LoRa-specific features so that an alternative sub-GHz PHY can be evaluated without redesigning sensing, logging, or the backend.

### Alternative radio technologies to investigate

**868 MHz FSK/GFSK:** worthwhile alternative if higher data rate, shorter airtime, or simpler PHY behaviour becomes more valuable than LoRa's maximum link budget. It should be treated as an experimental comparison against LoRa rather than a replacement assumption.

**433 MHz LoRa/FSK:** potentially attractive because of the lower frequency and longer wavelength, and therefore worth investigating for difficult water-surface geometries. The larger antenna and UK regulatory conditions must be considered before selecting it.

**2.4 GHz Wi-Fi/BLE/802.15.4:** useful for local or high-bandwidth functions but not currently preferred for the primary buoy-to-shore telemetry link. The water-surface environment and free-space/link-budget requirements favour sub-GHz for the long-range low-data-rate link.

### UK regulatory constraint

The Smart Buoy is intended for UK use, so the radio design must be based on the **current Ofcom IR2030 conditions**, not simply the generic term "868 MHz ISM". Licence-exempt short-range devices operate on a shared, non-protected/non-interference basis, and permitted power, bandwidth, duty cycle, channel access, and other conditions depend on the specific sub-band and device category. [2]

In particular, the attractive higher-power 869.4–869.65 MHz provisions shown in Ofcom material have specific channel-access requirements and must not be treated as a blanket 500 mW LoRa allowance. The selected radio configuration must be checked against the current UK interface requirements and the applicable ETSI harmonised requirements before deployment or productisation. [2]

**Status:** Design direction — 868 MHz LoRa baseline; alternative PHY/frequency options remain **Read later / experimental**, pending measured link testing and regulatory review.

## Low-Cost, Modular Mooring Buoy — Brendon Chan

https://www.brendon-chan.com/projects-1/mooring-buoy

An undergraduate MEng individual project developing a roughly £500 modular mooring buoy for oceanographic research. The design uses reconfigurable sensor mounts and was manufactured and experimentally validated in a towing tank. Buoy motion was measured using a homemade Arduino IMU system.

**Relevance:** particularly useful for the engineering discipline around mechanical design, modular payloads, instrumentation, experimental testing, and validation. The towing-tank work is a good reminder that buoy behaviour should be characterised rather than assumed.

**Status:** Read later — high priority.

## Backcasting a Low-Cost Wave Data Buoy — Reconstrained Design

https://reconstrained.design/projects/low-cost-wave-data-buoy

An open-source DIY wave-data buoy developed in Madeira in support of community-scale marine renewable-energy planning. The buoy uses off-the-shelf components and locally sourced materials, with a microcontroller, sensors, data logger, radio transmitter, batteries, and solar panels. It measures significant wave height, period, and direction, and sends data through a shore gateway to an online system with near-real-time display. Test buoys were moored in 7–10 m of water.

**Relevance:** strong example of connecting inexpensive instrumentation to a real deployment and an actual decision-making application. Useful for considering calibration, deployment logistics, communications, and the value of open hardware in locations with limited resources.

**Status:** Read later — high priority.

## Open Source Ocean Data Buoy — Nick Raymond

https://opensourceoceanweatherbuoy.wordpress.com/about/

Nick Raymond started this project while a mechanical engineering graduate student at UC Davis. The original goal was a small, cheap 3D-printed buoy measuring wave height and period at a local surf spot. The project then expanded into the idea of networking many inexpensive buoys to produce higher-fidelity wave information over areas of interest.

**Relevance:** valuable conceptual reference for a distributed environmental-sensing network rather than a single sophisticated buoy. This aligns with the longer-term Smart Buoy idea of multiple inexpensive nodes feeding a common data platform.

**Status:** Read later — high priority.

## Low-Cost DGPS Water-Level Buoy — University of Western Australia

https://www.uwa.edu.au/projects/oceanworks-project-pages/riverlab-2020-s2/riverlab-2020-s2---hansen

A low-cost solar-powered water-level buoy concept using DGPS, Raspberry Pi/4G communications, and comparison against an existing tide gauge as ground truth. The project considers the effect of buoy pitch and roll on measurement accuracy.

**Relevance:** useful reference for the distinction between **sensing something** and **producing a defensible measurement**. Ground-truth comparison, motion compensation, calibration, uncertainty, and acceptance criteria are all directly relevant to a serious Smart Buoy design.

**Status:** Read later — medium/high priority.

## Development of a Small-Scale Wave-Powered Data Buoy — Iain McLeod

https://mural.maynoothuniversity.ie/id/eprint/21677/
https://coer.maynoothuniversity.ie/research-projects/

A 2026 PhD thesis from Maynooth University's Centre for Ocean Energy Research. It investigates powering a small data buoy from incident waves, including a small-scale triboelectric nanogenerator and a more conventional oscillating-water-column power take-off. It also develops a free-surface-elevation estimator rather than assuming that a wave-measuring buoy must behave as a perfect wave follower.

The wider research programme explicitly considers the whole system: hydrodynamic modelling, power-take-off modelling, control, optimisation, sensor design, data transmission, simulation, and experimental testing. The project was funded by the Marine Institute and involved partners including the Marine Institute, PLOCAN, Techworks Marine, Monterey Bay Aquarium Research Institute, Dundalk Institute of Technology, and Resolute Marine.

**Relevance:** secondary reference. The most useful parts for Smart Buoy are energy-budget thinking, the interaction between buoy dynamics and measurement, and holistic system optimisation. Wave-powered generation itself should not be treated as a requirement.

**Status:** Read later — secondary.

## Related contemporary research

### Small wave-buoy literature

A 2025 review of atmospheric and ocean measuring buoys explicitly lists the **T3chFlicks education-focused Smart Buoy** alongside Sofar Spotter, FZ-series buoys, MELODI, ADWSD, miniwave buoys, and other small wave-measurement platforms.

https://faculty.washington.edu/jmt3rd/Publications/Cavaleri_etal_2025.pdf

**Relevance:** useful evidence that the T3chFlicks project has value as a documented low-cost buoy reference beyond the maker community. It also provides a route into comparative literature on small wave buoys.

### Good Buoy / marine-mammal sensing follow-on

A 2025 ISEF project explicitly used a scaled version of the T3chFlicks **Good Buoy** design as a reference and performed structural stress analysis, 3D printing, buoyancy/stability testing, and environmental sensing. The implementation used an ESP32-class controller, battery, solar panels, and a planned LTE/hydrophone interface.

https://sciforum.net/manuscripts/27172/slides.pdf

**Relevance:** useful example of a later educational project taking an existing open buoy design and adding explicit structural analysis, deployment testing, and a new sensing application. It is a secondary reference rather than a design dependency.

## Cross-project lessons

### 1. Prototype versus instrument

T3chFlicks demonstrates how quickly a buoy can become a complex embedded system. OLB, Reconstrained, Brendon Chan, and UWA add the next step: deployment, measurement validation, power budgeting, and environmental characterisation.

### 2. Measurement validation should be explicit

For Smart Buoy, acceptance criteria should distinguish:

- sensor functionality;
- calibration;
- derived measurement accuracy;
- motion effects;
- communications reliability;
- time synchronisation;
- data completeness;
- deployment endurance.

A future buoy should have a documented validation plan rather than relying on successful telemetry as evidence that the measurements are good.

### 3. Distributed sensing may be more valuable than a single advanced buoy

Nick Raymond's network concept and OLB's inexpensive drifter approach suggest a useful architectural direction: multiple modest nodes, a common communications/data model, and a shared backend can provide spatial information that a single sophisticated platform cannot.

### 4. Power is a system-level requirement

The useful comparison is not simply solar-panel wattage. The energy budget should include acquisition, processing, storage, radio receive/listen time, transmission, recovery/restart, battery state, environmental conditions, and update/recovery operations. OLB is especially relevant here because it explicitly targets long unattended endurance.

### 5. Mechanical behaviour affects measurement quality

Brendon Chan's towing-tank validation, the UWA work on pitch/roll, and McLeod's treatment of buoy dynamics all reinforce the same principle: the mechanical platform is part of the measurement system.

### 6. Communications should be chosen around deployment

The projects provide useful alternatives rather than a single prescribed solution: nRF24 for the T3chFlicks prototype, LoRa for OLB, and radio gateway architectures in the Reconstrained project. The current design direction is **868 MHz LoRa as the baseline**, with **868 MHz FSK/GFSK and 433 MHz LoRa/FSK retained as alternatives for measured comparison**. The radio choice should ultimately be based on range, energy, data rate, antenna behaviour at the water surface, regulatory constraints, infrastructure, cost, recovery, and deployment requirements.

For the LoRa baseline, the validation plan should explicitly include antenna height above water, antenna matching/counterpoise, buoy orientation, sea state, RSSI/SNR, packet delivery ratio, reconnect behaviour, and energy per successful telemetry packet. A nominal antenna position around 200–500 mm above mean water level is a starting design target, not a validated requirement.

### 7. Open hardware is most useful when it includes the complete engineering chain

The strongest references expose more than a PCB: mechanical design, firmware, data processing, communications, deployment method, validation results, and lessons learned. This should be the standard for any future ChartRoom Smart Buoy design documentation.

## Suggested Smart Buoy progression

A useful engineering progression emerging from these references is:

1. **Bench prototype** — sensor acquisition, timestamping, local storage, power measurement.
2. **Instrument validation** — calibration, derived measurements, repeatability, ground-truth comparison.
3. **Environmental test** — enclosure, buoyancy, motion, thermal behaviour, water ingress, recovery.
4. **Communications test** — range, duty cycle, packet loss, reconnection, local buffering, antenna height, and water-surface effects.
5. **Short deployment** — unattended operation with complete health telemetry.
6. **Extended deployment** — battery/solar endurance and environmental robustness.
7. **Fleet operation** — configuration management, authenticated firmware updates, rollback/recovery, fleet health, and common data/API infrastructure.

The goal is not to reproduce any one reference design. The references should be reviewed and either **incorporated into the Smart Buoy architecture with a source link/endnote, or discarded** after review.

## Read-later shortlist

**High priority:** OLB; Brendon Chan modular mooring buoy; T3chFlicks Smart Buoy; Reconstrained low-cost wave buoy; Nick Raymond open-source ocean buoy.

**Medium priority:** UWA DGPS water-level buoy.

**Secondary:** McLeod/Maynooth wave-powered data buoy; 2025 Good Buoy/ISEF follow-on; 868 MHz LoRa water-surface antenna study.

## Sources

[1] M. S. Al-Husainy et al., “Design, Implementation, and Measurement Procedure of Underwater and Water Surface Antenna for LoRa Communication”, *Sensors*, 2021. https://www.mdpi.com/1424-8220/21/4/1337

[2] Ofcom, “Short-range devices” and UK Interface Requirement IR2030. https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices
