# Project memories

## 2026-11-17 — PyInfra pilot for Adeept Robot HAT examples

The user asked to apply the personal defaults from their Linux setup posts to the Adeept example Pi. The focused deployment in `examples/adeept-rpi-robot-hat-v3/pyinfra/` now upgrades APT packages, removes unused dependencies, installs `git`, `nano`, `zsh`, and `pipx`, configures Oh My Zsh with the `clean` theme, and runs Hyfetch at interactive login for the SSH account. It ensures OpenSSH is enabled, enables I²C/SPI in Raspberry Pi `config.txt` with a dated backup, installs demo dependencies in a virtual environment, and copies examples 01–13 under `/opt`. The user's sudoers post describes an Ubuntu VM; their basic Linux setup post says Raspberry Pi OS has passwordless sudo, so this deployment does not edit sudoers. It also does not add the public key from the post. A manual reboot may be required after interface configuration or OS upgrades. The setup has not been run against the Pi; inspect the dry-run output first, and retain the D1/power-path check before hardware testing. See the [demo-code index](pages/sites/chartroom/research/adeept-rpi-robot-hat-v3-demo-code.txt) and [PyInfra research note](pages/sites/chartroom/research/pyinfra-infrastructure-automation.txt).

## 2026-11-10 — ROV historical project evidence and propulsion research

The user's own ROV development history is documented on PhilipMcGaw.com and the legacy Skippy.org.uk site. Before repeating ROV design work, check the [[https://philipmcgaw.com/projects/rov/|ROV project index]] and its linked posts: the 2023 DIY ROV architecture, pressure vessel, viewport dome, and end-cap/feed-through design; the 2024 transparent development frame; and later control-electronics/software work including the 2025 Arduino Pro Micro serial issue and BlueOS investigation. The 2018 Skippy.org.uk ESC note records earlier setup/start-up difficulties. These sources document design and development history, but do not establish that the recently discussed 100 W 2418 motor and 12 A bidirectional ESC combination was previously tested.

A separate, third-party experimental reference is Hamish Trolove's TechMonkeyBusiness OpenSource ROV archive. It includes builder-reported brushless thruster/propeller comparisons, motor corrosion mitigation, ESC calibration, and pool trials. Do not attribute those experiments to the user or treat them as validation of the current motor/ESC candidate. The compact motor/ESC combination from the DIY ROV Facebook screenshot remains a research candidate only; the ESC model is unidentified and key electrical, thermal, thrust, depth, and immersion ratings remain unverified. See [the consolidated research note](pages/sites/chartroom/research/diy-rov-compact-brushless-motor-esc.txt) and [the TechMonkeyBusiness source assessment](pages/sites/chartroom/research/techmonkeybusiness-open-source-rov-and-robotics.txt).

## 2026-11-09 — Local file inspection inbox

The repository has a root-level `inbox/` for files the user wants inspected in the context of Chartroom work. Its contents are ignored by Git and remain local to the checkout; useful findings should be transferred to canonical project files, and temporary files removed when no longer needed. See `inbox/README.md`.

## 2026-11-09 — Research batch consolidation

The research catalogue contains four batch pages and many source-specific research notes. Consolidation should reduce repeated summaries while preserving source provenance and any useful material that has no standalone page. Keep standalone notes as detailed references and use thematic overviews to explain relationships between them. This is an editorial direction requested during repository review; it does not establish technical validation of the referenced projects. The follow-up action is tracked in [TODO.md](TODO.md).

## 2026-11-09 — Project record-keeping preference

Repository guidance records the user's standing preference that project-relevant decisions, corrections, research, and outcomes are written to the appropriate canonical repository files rather than left only in chat. Routine validated updates should be committed and pushed without a separate confirmation request. Preserve provenance and uncertainty; do not record unsupported claims. See `AGENTS.md` for the operational workflow.

## 2026-11-09 — Robotical learning resources assessed for SwarmBot

Robotical Marty is recorded as an educational robotics reference for SwarmBot and Test in a Box, not as a selected hardware platform or software dependency. The useful material is the staged progression from unplugged sequencing and visual blocks to Python, plus lessons on debugging, sensor-driven conditionals, loops, functions, and multi-robot programming. The V1/V2 distinction matters: the published “An Army of Martys” multi-robot tutorial is a useful beginner example of network discovery, lists, and command iteration, but it is not a swarm-control architecture. Older ROS documentation refers to ROS Indigo/Jade/Kinetic and must not be presented as ROS 2 support. Detailed assessment and selected reading links are in [the Robotical Marty research note](pages/sites/chartroom/research/robotical-marty-educational-robotics.txt).

## 2026-11-10 — PiWars blog reading list

The user supplied 25 unique blog and team-site links associated with PiWars for future reading. They are recorded in [the PiWars team blogs index](pages/sites/chartroom/research/piwars-team-blogs.txt); the links are user-supplied discovery references, and their site contents were not reviewed as part of indexing them. The duplicated PiWars Reactor URL is listed once.

## 2026-11-11 — Self-hosted robot coding portal concept

The user is interested in adapting the three editor categories presented by Raspberry Pi Code Classroom — Blocks, Python, and Web (HTML/CSS/JavaScript) — into a self-hosted coding portal accessible from a phone, tablet, or laptop over Wi-Fi. This is a concept for the Robot Code projects, not a decision to adopt Code Classroom itself or evidence that its hosted classroom backend can be self-hosted. SwarmBot is the preferred initial educational use case, with PiWars as a possible later reuse. For SwarmBot, consider a single swarm portal/gateway that can discover and manage multiple robots; PiWars could use a simpler single-robot deployment.

The key architectural principle is to treat editors as front ends and expose a narrow, documented Robot API. User programs must not have unrestricted access to GPIO, motors, or the host OS. Execution should be isolated; the control layer must retain command validation, operating limits, arbitration, watchdogs, timeouts, and emergency-stop authority. Aim for the same application-facing API over simulated and physical backends so programs can be developed in simulation before hardware deployment. Offline-first operation is desirable. Hosting topology (robot access point, existing network, or shared swarm gateway), editor component choices, licences, and execution technology remain open research questions. The concept and provenance are recorded in [the self-hosted robot coding portal research note](pages/sites/chartroom/research/self-hosted-robot-coding-portal.txt); it is a research candidate, not an approved implementation.

## 2026-11-14 — Qwiic/STEMMA QT robotics interface research

The user considers the Qwiic/STEMMA QT connector ecosystem worth using as a common interface for suitable short-range, low-power I²C peripherals across K9, PiWars, and SwarmBot. The user is already aware of I²C signal-integrity constraints; the research is about connector standardisation, modularity, and accessible bus/debug connections, not a claim that I²C is suitable for arbitrary cable lengths or noisy environments. Qwiic and STEMMA QT share the JST-SH 1.0 mm four-pin connector and pin order, but electrical compatibility, supply voltage, logic levels, current budget, and device requirements still need checking. This is a proposed common design convention, not evidence of an implemented or validated hardware change. See [the Qwiic/STEMMA QT research note](pages/sites/chartroom/research/qwiic-stemma-qt-i2c-connector.txt).

## 2026-11-14 — Matter-enabled ESP32 environmental sensor reference

The user identified a Random Nerd Tutorials guide showing an ESP32 and BME280 reporting temperature, humidity, and pressure via Matter as a potentially useful addition to existing remote-sensor research. It adds a local IP-network/controller pattern alongside existing LoRa and LoRaWAN examples, and includes a periodic deep-sleep sketch. The tutorial's sleep and reporting timings are example settings, not measured power or field validation; network reconnection, controller availability, and energy per report remain open checks. This is a research reference, not a selected platform or implementation decision. See [the ESP32 Matter BME280 note](pages/sites/chartroom/research/esp32-matter-bme280-remote-sensor.txt).

## 2026-11-15 — Mobile solar weather station reference

The user identified Raspberry Pi's report on a self-powered mobile weather station as potentially useful to weather-station and buoy research. The article reports a modular, solar-powered Raspberry Pi Zero W station, a claimed IP65 enclosure, and a Gower field test. Its reported anemometer stall at low wind and temperature bias of roughly 1–2 °C from heat trapped in the sensor head are useful design cautions. Power autonomy is not quantified, and the land-based project does not establish marine or buoy suitability. See [the mobile weather station research note](pages/sites/chartroom/research/raspberry-pi-mobile-self-sufficient-weather-station.txt).

## 2026-11-15 — Shared ESP32 web-management concept

The user wants a reusable browser-based configuration and maintenance interface shared by the LoRa sensor nodes and Internet gateway. The concept includes a device-hosted Wi-Fi access point for deliberate provisioning/configuration, possible access over trusted Wi-Fi, common dashboard and diagnostics functions, device-specific configuration pages, persistent settings (for example, NVS), and OTA as a separately secured future capability. Keep the management layer separate from LoRa application logic. The Random Nerd Tutorials ESP-IDF AP guide is a reference for the basic AP and HTTP-server mechanism only; it demonstrates a static page in AP-only mode, not the proposed management application, captive portal, AP+STA operation, or secure OTA. The ESP32 framework and detailed implementation remain undecided. See [the shared ESP32 web-management research note](pages/sites/chartroom/research/shared-esp32-web-management-for-lora-nodes.txt).

## 2026-11-15 — Tailscale as optional remote access for ESP32 management

The user already uses Tailscale. In the LoRa ESP32 web-management design, consider Tailscale as an optional remote-access path rather than a replacement for local ESP32 AP provisioning. The normal Tailscale client should not be assumed to run directly on the Heltec ESP32. A Linux/Raspberry Pi host on the same LAN could provide subnet routing to the ESP32 management endpoint, or a narrowly scoped reverse proxy could expose just that service. Local AP recovery should remain available independently. Apply explicit ESP32-side authentication and restrictive tailnet access controls; do not treat tailnet reachability alone as authorisation. Orion Robots' 2026-09-02 article demonstrates Tailscale and PyInfra on a Raspberry Pi, with useful deployment practices (secret hygiene, pinned versions, repeatable configuration), but is not an ESP32 implementation. See the Tailscale section in [the shared ESP32 web-management research note](pages/sites/chartroom/research/shared-esp32-web-management-for-lora-nodes.txt).

## 2026-11-15 — PyInfra research for robotics Linux deployment

The user asked to record PyInfra as a candidate for repeatable configuration and deployment of Linux-based Robots project computers. The user already uses Tailscale; the Orion Robots article demonstrates PyInfra automating Tailscale installation and enrolment on a Raspberry Pi, including secret handling, version pinning, and a warning not to alter Tailscale connectivity over the same connection being changed. PyInfra is not an ESP32 deployment tool and does not replace firmware build systems. It remains a research candidate; no tool choice or implementation has been made. See [the PyInfra research note](pages/sites/chartroom/research/pyinfra-infrastructure-automation.txt).

## 2026-11-15 — Underwater profiler and tether-management references

The user supplied a SeaMATE vertical-profiler presentation and a research presentation on underwater umbilical management. The profiler guide offers a single-motor, tethered water-column sampling concept with optional temperature sensing, but is an educational pool-oriented reference and does not validate marine deployment. The umbilical presentation reports research on camera-based cable-shape estimation between ROVs and a powered surface winch for an ROV tether; its supplied PDF date (2019-06-14) differs from the EMRA'19 programme date (2019-05-16), an unresolved source discrepancy. The user also supplied an OpenGrabber assembly guide; its build notes are recorded as source recommendations, not tested project behaviour. See the [profiler note](pages/sites/chartroom/research/mate-seamate-vertical-profiler.txt), [umbilical research note](pages/sites/chartroom/research/underwater-umbilical-management-two-robots.txt), and [RoboCenter note](pages/sites/chartroom/research/robocenter.txt).

## 2026-11-15 — Yellow gearmotor dimensions

The user has examples of the yellow gearmotor shown in the supplied drawing and wants its dimensions available as a reference because this motor size is common. The drawing identifies JL-12ZN20-43-06450 but does not identify its manufacturer; it also conflicts on output-shaft diameter. The physical motors should be measured before using the drawing for a bracket, coupler, or CAD model. See the [dimension and specification note](pages/sites/chartroom/research/jl-12zn20-43-06450-yellow-gearmotor.txt).

## 2026-11-15 — Weather-station calibration and irradiance references

The latest inbox review added three weather-system references: the 2012 Weather SenseBox thesis' local logging and field-comparison lessons; the 2012 cup-anemometer study's finding that rotor geometry affects calibration; and Delta-T's SPN1 installation, logging, and calibration guidance. The SenseBox prototype's sensor comparisons were limited and exposed humidity, pressure, and wind-placement issues; they are not validation for current hardware. The SPN1 guide describes a low-power sensing head but a potentially high-current heater and the need for an external logger. A 2018 ESP8266 weather-station guide is recorded as a historical cloud-connected sensor/display pattern, not a current or offline deployment design. See the [SenseBox thesis note](pages/sites/chartroom/research/weather-sensebox-arduino-thesis.txt), [ESP8266 guide note](pages/sites/chartroom/research/esp8266-weather-station-getting-started.txt), and [SPN1 best-practices note](pages/sites/chartroom/research/delta-t-spn1-measurement-best-practices.txt).


## 2026-11-15 — Maker's Pet self-driving robot e-book

The user identified Maker's Pet's 209-page *Build, Program a Self-Driving Robot* e-book as a useful Chartroom reference. The expanded [Maker's Pet 120 mm robot research note](pages/sites/chartroom/research/makers-pet-120mm.txt) records the architecture, ESP32/Micro-ROS and ROS 2 host split, encoder calibration, LiDAR/frame diagnostics, SLAM/Nav2/frontier exploration, Gazebo simulation, Wi-Fi transport, multi-robot example, and relevance to SwarmBot, MarsBot, K9, PiWars, and SquidLink. The e-book source repository is available under makerspet/ebook and contains chapter Markdown; its root has an Apache-2.0 licence, but the exact redistribution scope for the generated PDF and its video-derived illustrations was not established. The PDF was therefore linked to the publisher rather than copied into Chartroom media. This remains research/learning material, not an adopted platform or validated project design.


## 2026-11-16 — MiddleAUV AUV kit and MUR software reference

The user identified MiddleAUV material associated with Dmitry Lyakhov as relevant to the ROV project. A dedicated [MiddleAUV research note](pages/sites/chartroom/research/middleauv.txt) records RoboCenter's Raspberry Pi-based AUV kit, its current Compute Module 4 configuration and older Raspberry Pi 3 specification, hardware and electrical ratings, MUR IDE, PYMURAPI, simulator, telemetry, and documented heading/depth regulation. The product is an AUV rather than a directly equivalent tethered ROV; its main potential value is as a software, control, telemetry, and simulation reference for the existing ROV and SquidLink work. RoboCenter's published figures are version-dependent and are not independent validation. The manufacturer's public materials do not establish Dmitry Lyakhov as the sole author, so attribution is kept cautious. No hardware or software platform has been selected or adopted.

## 2026-11-16 — Wider MUR Project and RoboCenter ecosystem

A wider review of RoboCenter/MUR Project identified useful references beyond the MiddleAUV kit: HighROV frame and buoyancy cutting patterns; HighBuoy, MiddleBuoy Surface/Bottom, and ElementaryBuoy firmware; the ElementaryAUV Android visual-programming application; MUR IDE, simulator, PYMURAPI, and lessons repositories; and Marine Robotics training and competition material. The training topics include tether calculations, serial communications, electrical fault-finding, frame/sealing/buoyancy work, PWM/ESCs, payload integration, computer vision, and simulator missions. These are research leads and educational references, not evidence of validated designs or adopted project dependencies. In particular, the separate MiddleBuoy repositories warrant source inspection before inferring how surface and submerged nodes communicate. See the [MUR Project ecosystem research note](pages/sites/chartroom/research/mur-project-ecosystem.txt), linked from the [research index](pages/sites/chartroom/research/start.txt) and [RoboCenter ROV note](pages/sites/chartroom/research/robocenter.txt).

## 2026-11-16 — EMF Roamer historical reference

The user recalled an internet-controlled robot roaming around EMF Camp, supplied a video showing the Roamer with GPS plots, and identified Chris Stubbs's `roamerpi` GitHub repository as a possible source. His blog provides 2018 build details and a 2022 queue post. The Hacky Racers CYBR TRK profile, available as indexed page text though its direct URL returned HTTP 403, identifies the 2022 vehicle as a larger follow-on and reports its hardware, browser-control/video stack, telemetry, steering evolution, and operating limitations. These details are source-reported, not independently verified. The repository's individual files also could not be retrieved; its “Roamer Pi Source” description and control, GPS, video, and LED folders strongly match the builder's 2018 Raspberry Pi account, but exact version and completeness remain unverified. See the [EMF Roamer research note](pages/sites/chartroom/research/emf-roamer.txt).

## 2026-11-16 — HTML5 UP as a Cockpit visual reference

The user asked whether HTML5 UP's responsive HTML/CSS website templates could help with Cockpit. The templates appear useful for responsive layout and visual prototyping, but they do not provide robotics data, controls, or Cockpit integrations. HTML5 UP states that its templates use CC BY 3.0 and require attribution; bundled assets need separate licence review. No template has been selected or adopted. See the [HTML5 UP research note](pages/sites/chartroom/research/html5up-responsive-templates.txt), linked from the [Cockpit page](pages/sites/chartroom/cockpit/start.txt).

## 2026-11-16 — Consolidated ultrasonic robotics reference batches

The two overlapping ultrasonic robotics batches have been consolidated into one thematic overview covering sensing/perception, ROV operator software, embedded interfaces, hardware, and education. Unique source links and relevant access limitations were retained; the former page IDs remain as short links to the overview because other research pages refer to them. The community robotics/sensing and robotics/electronics collections remain separate because they cover broader, distinct groups of references.


## 2026-11-17 — MPU-6050 breakout module photograph

The user supplied a photograph of the blue MPU-6050 breakout module used with the Adeept Robot HAT. The visible module PCB labels are VCC, GND, SCL, SDA, XDA, XCL, AD0, and INT. The photograph is retained in Chartroom media and embedded in the [BlueOS and Adeept Robot HAT architecture page](pages/sites/chartroom/architecture/blueos-adeept-robot-hat.txt). It is a user-supplied visual record, not a manufacturer schematic; the exact breakout-board model, fitted IC marking, and electrical implementation remain unverified.

## 2026-11-17 — Adeept Robot HAT V3.1 schematic label translation

The supplied schematic PDF now has the Chinese label 合金采样电阻 translated as “Alloy current-sense resistor”. Only that label was changed; the schematic has not been electrically reviewed. The original Chinese PDF remains beside the translated file. See the [Adeept Robot HAT architecture note](pages/sites/chartroom/architecture/blueos-adeept-robot-hat.txt).

## 2026-11-17 — Adeept Robot HAT V3 examples retained for testing

The user reports Adeept authorised redistribution of examples 02–13. Unmodified files 01–13 are retained under `examples/adeept-rpi-robot-hat-v3/`; `01_Servo.py` carries an MIT identifier in its source docstring, and the user's blog records it being used on channel 0. The supplied `setup.py` is archived for reference but not run because it installs system packages through privileged package commands. The complete source folder was moved out of `inbox/` after comparing all archived files with their supplied copies. No example was run. D1's suspected SS34 fault remains unverified; see the pending bench task in [TODO](TODO.md) and the [example index](pages/sites/chartroom/research/adeept-rpi-robot-hat-v3-demo-code.txt).

## 2026-11-17 — MPU-6050 breakout header still needs soldering

The user reports the MPU-6050 module header has not yet been soldered. Before fitting the module to Adeept HAT J1, confirm the chosen mounting orientation and align VCC, GND, SCL, and SDA with J1 pins 1–4. Soldering and installation are pending; see the [hardware TODO](TODO.md).

## 2026-11-20 — ROV single-pair Ethernet converter candidate

The user is considering two Microchip EVB-LAN8770M_MC boards (EV02N47A; RS 209-7642) for a control-PC-to-ROV link: 100BASE-TX at each host and 100BASE-T1 over a single twisted pair between the boards. The user proposes short pigtails from each T1 screw terminal to a more mechanically robust tether connector. Research also identified enclosed alternatives from PEAK-System, Datron Technology, and I-NOVATIVE. PEAK's PAE-Media Converter has H-MTD/MATEnet connectors but is IP20; I-NOVATIVE's Factory-Link-SPE-M manual says it is for development/testing, not series production. A 2026-11-20 retailer check recorded UK supplier/manufacturer pages and indicative stock/price information: PEAK via Control Technologies UK, TE-1000 via Datron Technology UK, and Factory-Link-SPE-M direct from I-NOVATIVE. Amazon UK searches found no listings for those alternatives, and RS listings were not found for them; RS listed the Microchip development board at £49.77 ex VAT, temporarily out of stock with dated incoming batches. No product is selected, and host compatibility, power, tether fit, environmental suitability, and testing remain open. See the [Chartroom research note](pages/sites/chartroom/research/microchip-evb-lan8770m-media-converter.txt).
