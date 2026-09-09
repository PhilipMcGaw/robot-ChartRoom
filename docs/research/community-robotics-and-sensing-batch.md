# Community robotics and sensing references

A collection of small robotics, ROV, environmental-sensing, video, and embedded-development projects supplied for review. These are references and sources of design inspiration, not project dependencies.

## ROV and underwater systems

### The Neverending Projects List — ROVs

https://www.theneverendingprojectslist.com/rovs/

A long-running homebuilt-ROV collection with an unusually broad practical focus. The author describes more than 20 years of intermittent ROV building and explicitly favours mechanical aspects over electronics. The collection includes 3D-printed ROVs, Blue Robotics T100 bilge-pump conversions, 3D-printed Kort-nozzle thrusters, manipulators, magnetic-coupled thrusters, control-system wiring, and propulsion experiments.

**Relevance:** useful historical/practical reference for ROV mechanical construction, propulsion experiments, basic control wiring, manipulators, and repairable DIY approaches. It is particularly useful as a counterpoint to more polished commercial ROV ecosystems.

**Read later:** review individual projects for mechanical and propulsion ideas rather than adopting the older electrical/control architecture wholesale.

### Low-buck PVC ROV

https://hackaday.com/2021/12/02/low-buck-pvc-rov-is-definitely-a-mvp/

A deliberately minimal ROV using PVC pipe, an Ethernet tether, simple brushed motors, relays, and a camera. The system demonstrates a useful minimum-viable-vehicle principle: prove buoyancy, propulsion, tethering, and video before adding sophisticated control electronics.

**Relevance:** useful for the ROV development sequence and early subsystem tests. The simplicity is valuable as a validation strategy even though the final ROV should retain proper protection, fault handling, telemetry, and controlled propulsion.

## Educational robots and vehicle platforms

### Open Source Turtle Robot (OSTR)

https://www.instructables.com/OSTR/
https://github.com/aspro648/OSTR/

OSTR was designed as a 10-hour STEM workshop project for teenagers. The design targets low cost, easy construction, easy programming, and an immediately visible result. The robot uses simple turtle-style commands such as `forward(distance)` and `left(degrees)`. Version 2 moved towards easier USB debugging and Python-capable hardware, allowing the same turtle programs to be evaluated on a computer and then run on the physical robot. The design files use open-source KiCad, FreeCAD/OpenSCAD/TinkerCAD, and Arduino/CircuitPython.

**Relevance:** strong reference for Test in a Box and SwarmBot educational architecture. The computer/physical-robot equivalence is especially relevant: a constrained command model can be tested or previewed before execution on hardware.

### SparkFun HUB-ee Buggy

https://learn.sparkfun.com/tutorials/building-the-hub-ee-buggy

A deliberately simple two-wheel Arduino-compatible robot used to teach soldering, wiring, PWM, connector basics, motor control, sensors, and basic obstacle avoidance. The tutorial decomposes the robot into wheels/motors/drivers, controller, sensor, mechanical support, and power, then builds the system incrementally.

**Relevance:** good reference for a staged beginner robotics curriculum and for explaining subsystem ownership. The tutorial is retired, so it should be treated as educational/historical material rather than a current hardware recommendation.

### Skoobot

https://hackaday.io/project/75832-skoobot

A small educational robot designed around interaction with children, with an emphasis on manufacturability, software accessibility, and cooperative activities. It used an nRF52832, distance sensing, a programming companion board, and staged development from a more capable software-hacker platform towards simpler Arduino-oriented use.

**Relevance:** strong inspiration for SwarmBot's educational/product thinking, particularly staged abstraction, approachable hardware, programming accessibility, and robot-to-robot cooperative activities.

### UKMARSBOT

https://github.com/ukmars/ukmarsbot
https://github.com/ukmars/ukmarsbot-examples
https://github.com/ukmars
https://github.com/ukmars/ukmarsbot/issues

UKMARSBOT is an inexpensive, multipurpose beginner robot platform supporting line following, wall following, drag racing, and mini-sumo. The hardware repository includes documentation, ECAD, mechanical design, sensor boards, alternatives, and a resources area for serial data/control/logging. The examples repository deliberately progresses through small exercises including battery handling, switches, PWM, sensors, encoders, faster analogue acquisition, distance moved, and other low-level topics.

The issue tracker is also useful evidence of the practical engineering issues that arise in an educational open-hardware project, including component suitability and making parts generic.

**Relevance:** particularly strong reference for a structured SwarmBot/robotics training path. The examples progression maps well to a Test in a Box curriculum: electrical fundamentals → actuator control → sensing → encoders → motion measurement → higher-level behaviour.

## Small autonomous and networked robots

### Raspberry Pi remote-controlled car

https://www.instructables.com/Raspberry-Pi-Remote-Controlled-Car-1/

**Relevance:** browser/network-based vehicle-control inspiration. Compare its control boundary and web UI approach with Cockpit rather than treating its implementation as an architectural dependency.

### Motor car toy with Arduino UNO and 3D printing

https://www.instructables.com/motor-car-toy-with-arduino-uno-and-3dprinting/

**Relevance:** useful as a very low-complexity mechanical/electronic build reference for beginner robotics and rapid prototyping.

### Do-it-yourself Autonomous Tiny Robot

https://www.instructables.com/Do-it-yourself-Autonomous-Tiny-Robot/

**Relevance:** small autonomous-robot reference for sensing, embedded control, and the transition from remote/manual control to autonomous behaviour.

### EWON Raspberry Pi-powered home robot

https://www.instructables.com/EWON-Raspberry-Pi-Powered-Home-Robot/

**Relevance:** useful reference for Raspberry Pi-based domestic/mobile robotics, particularly the relationship between onboard computing, sensors, actuation, and a higher-level user interface.

### Pi-powered 1:35 Panther tank

https://hackaday.com/2022/01/09/powering-up-a-135-scale-panther-tank/

A small scale tank was fitted with geared drive motors, batteries, motor controllers, regulators, a turret servo, and a Raspberry Pi Zero. Control was provided through a simple browser page served by the Pi, with independent control of the two tracks and turret. The intended future direction included onboard video and sensor data.

**Relevance:** strong small-scale example of browser-first robot control and a useful mechanical reference for tracked SwarmBot experiments. The simple browser interface reinforces the value of separating the operator UI from vehicle-control implementation.

## Video and remote operation

### ustreamer Docker for Raspberry Pi

https://github.com/beholder-rpa/ustreamer-docker

A Docker image packaging uStreamer for Raspberry Pi, exposing a browser-accessible HTTP video stream from a USB webcam or HDMI capture device. The container can be run directly or integrated with a service/orchestration environment.

**Relevance:** useful reference for modularising camera streaming as a service. It is particularly relevant to the Cockpit/video architecture because video can remain a replaceable subsystem rather than being embedded in the core control process.

Do not assume uStreamer is the final ROV video transport: compare latency, codec support, browser compatibility, recording, WebRTC requirements, and tether bandwidth against the existing video architecture.

## Environmental sensing

### Arduino Weather Station (AWS)

https://www.instructables.com/Arduino-Weather-Station-AWS/

**Relevance:** reference for a low-cost environmental station and for presenting weather/environmental measurements as a coherent system rather than a collection of independent sensors. Useful to compare with the Smart Buoy and weather-station work.

### Reed-switch anemometer

https://www.instructables.com/How-to-Build-Your-Own-Anemometer-Using-Reed-Switch/

A simple mechanical anemometer using a reed switch to count rotations.

**Relevance:** useful as a low-cost, inspectable sensor example for weather stations and Smart Buoy work. It is also a good teaching example for pulse counting, debouncing, calibration, wind-speed conversion, and uncertainty.

### Jigglypuff CO₂/dust environmental monitor

https://hackaday.com/2021/11/16/jigglypuff-sensor-breathes-co2-so-you-dont-have-to/

An environmental monitor using an MH-Z14A NDIR CO₂ sensor and GP2Y1010AU0F optical dust sensor with an Arduino Nano RP2040 Connect, Wi-Fi reporting, and an SSD1306 local display.

**Relevance:** useful comparison for environmental telemetry, local display versus remote reporting, and sensor modularity. The project reinforces the distinction between acquisition, local presentation, and communications. Its Telegram-based reporting should not become a project dependency.

## Embedded update and fleet-management inspiration

### Secure ESP32 OTA firmware updates

https://hackaday.com/2021/11/29/how-to-easily-set-up-secure-ota-firmware-updates-on-esp32/

Demonstrates a basic secure OTA update path for ESP32, including HTTPS and firmware deployment. The central engineering issue is that deployed embedded devices may be inaccessible for physical reprogramming.

**Relevance:** important future consideration for SwarmBot, Smart Buoy, distributed sensor nodes, and other deployed embedded modules. If OTA is implemented, require authenticated firmware, integrity verification, rollback/fail-safe behaviour, version reporting, and a recovery path. This is a future platform capability, not an immediate dependency.

## Open-source robotics engineering and manufacturing

### Freeburn Robotics

https://frobotics.com/
https://frobotics.com/robotics-design/
https://frobotics.com/pcb-design/

Freeburn Robotics provides robotics/mechatronics design, CAD, CNC, prototyping, small-scale manufacturing, PCB design, assembly, and embedded/software development. Its robotics offering explicitly covers open-loop through closed-loop control, while its PCB service covers analogue/digital design, component sourcing, assembly, testing, and small production runs.

**Relevance:** primarily a reference for the transition from prototype to repeatable hardware. It is useful when considering how ChartRoom projects could move from one-off experimental builds towards documented, testable, serviceable assemblies. It also provides a useful benchmark for the breadth of engineering disciplines that need to be represented in a serious small robotics project.

## Cross-project lessons

The strongest recurring themes from this batch are:

1. **Make the beginner path explicit.** OSTR, HUB-ee, and UKMARSBOT show the value of decomposing robotics into small, testable exercises.
2. **Keep simulation/preview and hardware execution aligned.** OSTR's turtle-command model is particularly relevant to Test in a Box: the same constrained program representation can potentially be previewed, simulated, validated, and executed.
3. **Keep operator interfaces separate from vehicle control.** The Panther tank, Raspberry Pi car, and OSTR all support the broader Cockpit direction.
4. **Use simple vehicles as engineering test platforms.** A small tracked or differential-drive robot can validate control, telemetry, video, and software architecture before those capabilities are transferred to the ROV or MarsBot.
5. **Treat sensing as a reusable subsystem.** The weather station, reed-switch anemometer, and CO₂ monitor are useful examples of acquisition, calibration, derived measurements, local display, and remote telemetry.
6. **Plan deployment lifecycle, not only first bring-up.** Secure OTA updates become increasingly valuable as the number of distributed robots/sensor nodes grows.
7. **Design for manufacture and service.** Freeburn Robotics and the long-running ROV projects reinforce the importance of CAD, wiring, assembly, test, serviceability, and repeatability rather than treating the first successful prototype as the finished design.

## Suggested ChartRoom relevance

**High priority:** OSTR, UKMARSBOT, Neverending Projects List ROVs, ustreamer-Docker, secure ESP32 OTA, Freeburn Robotics.

**Medium priority:** Skoobot, HUB-ee Buggy, Panther tank, low-buck PVC ROV, weather station, reed-switch anemometer, Jigglypuff monitor.

**General inspiration:** Raspberry Pi car, tiny autonomous robot, EWON home robot, motor-car toy.

These references should feed the existing **Test in a Box**, **SwarmBot**, **ROV**, **Smart Buoy/environmental sensing**, **Cockpit**, and **HiL/SiL** work rather than creating separate hardware projects for each reference.
