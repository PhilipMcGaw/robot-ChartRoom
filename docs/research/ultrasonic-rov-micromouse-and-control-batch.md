# Ultrasonic, ROV, I/O expansion, and micromouse references

**Status:** Research / read later  
**Added:** 2026-09-10

## Sources

- [Modify Ultrasonic Sensors for 3 Volts Logic](https://www.instructables.com/Modify-Ultrasonic-Sensors-for-3-Volts-Logic-prepar/)
- [Build Your Own Underwater ROV From Scratch](https://www.instructables.com/Build-Your-Own-Underwater-ROV-From-Scratch/)
- [Stereo Vision and LiDAR Powered Donkey Car](https://www.hackster.io/bluetiger9/stereo-vision-and-lidar-powered-donkey-car-575769)
- [AB Electronics IO Pi Plus](https://www.abelectronics.co.uk/p/54/io-pi-plus)
- [Arduino forum — Arduino as an I²C expander](https://forum.arduino.cc/t/use-an-arduino-as-i2c-expander/886365/23)
- [OpenROV software](https://github.com/OpenROV/openrov-software)
- [OpenROV Cockpit](https://github.com/OpenROV/openrov-cockpit)
- [OpenROV Cockpit development guide](https://github.com/OpenROV/openrov-cockpit/blob/master/docs/DEV-HOWTO.md)
- [UKMARS](https://github.com/ukmars)
- [UKMARSBOT](https://github.com/ukmars/ukmarsbot)
- [Joshua CCL Micromouse](https://github.com/joshuaccl/Micromouse)

## Ultrasonic sensors and 3.3 V interfaces

The 3 V ultrasonic-sensor modification is useful as a practical interface-design reference. The important lesson is not the specific HC-SR04 modification, but the need to treat logic-level compatibility as an electrical design problem when inexpensive 5 V modules are connected to 3.3 V processors.

### Relevance

- Useful alongside the SonicDisc research already in ChartRoom.
- Relevant to small robots using Raspberry Pi, ESP32, or other 3.3 V logic.
- Provides a practical example of adapting inexpensive sensors rather than immediately replacing them.
- Any modification should still be electrically characterised and validated rather than assumed safe from a tutorial alone.

## DIY underwater ROV

The Instructables ROV project is useful as another practical, low-cost ROV reference. Its value is primarily in construction choices, integration, tethering, waterproofing, and the progression from individual components to a working vehicle.

### Relevance

- Add to the existing collection of OpenROV, Blue Robotics, RovMaker Edge, and other DIY ROV references.
- Useful for comparing mechanical construction and low-cost subsea integration strategies.
- Look specifically for ideas that remain serviceable and testable rather than merely inexpensive.
- Potential inspiration for ROV subsystem test fixtures and early prototypes.

## Stereo vision + LiDAR Donkey Car

The Donkey Car project combines stereo vision and LiDAR on a small autonomous platform. This is useful because it illustrates complementary perception modalities rather than treating a single sensor as the complete perception system.

### Relevance

- Relevant to MarsBot and terrestrial autonomy.
- Useful comparison with Maker's Pet's 2D LiDAR approach and the ultrasonic sensing references.
- Potential HiL/SiL exercise: provide simulated LiDAR/vision measurements to the same perception interface used by hardware.
- Useful reminder that perception should be separated from vehicle-control logic.

## AB Electronics IO Pi Plus

The IO Pi Plus uses two MCP23017 devices to provide 32 additional GPIO through I²C. It supports multiple I²C addresses, interrupts, and external 5 V power, and can be stacked to provide substantially more GPIO. The board is explicitly usable from Raspberry Pi-class SBCs and other 3.3 V I²C hosts. citehttps://www.abelectronics.co.uk/p/54/io-pi-plus

### Relevance

- Useful reference for expanding GPIO without adding another MCU.
- Potentially relevant to a vehicle peripheral controller or test fixture with many discrete inputs/outputs.
- External power and interrupt support are useful design features where an SBC needs to supervise real-world I/O.
- Do not confuse GPIO expansion with deterministic real-time control; safety-critical or timing-sensitive functions should remain in an appropriate controller.

## Arduino as an I²C peripheral / expander

The Arduino forum discussion is useful as an architectural reference for putting an MCU behind an I²C interface and exposing higher-level functions to an SBC. This is potentially more flexible than a pure GPIO expander when the peripheral needs local timing, sampling, filtering, control loops, or protocol handling.

### Relevance

- Possible pattern for SBC + MCU subsystem boundaries.
- Relevant to ROV Control hardware, Smart Buoy sensor nodes, and complex Test in a Box fixtures.
- Useful alternative to placing every peripheral directly on the Raspberry Pi's I²C bus.
- The interface contract should expose meaningful measurements/commands rather than raw implementation details.

## OpenROV software architecture

OpenROV's software repository describes a suite of projects covering the ROV, control system, and cloud services, with `openrov-cockpit` providing piloting and ROV control. The GitHub organisation also separates hardware, electronics, Cockpit, and Arduino software into distinct repositories. citehttps://github.com/openrov/openrov-software

The OpenROV Cockpit repository is particularly relevant. It describes Cockpit as a web-centric tele-robotic control system supporting mobile, desktop, and tablet browsers, configurable gamepad/keyboard/joystick control, video, telemetry recording, plugins, upgrades, and different motor configurations. citehttps://github.com/openrov/openrov-cockpit

### Strong relevance to ChartRoom

OpenROV provides historical evidence for several principles already emerging in the ChartRoom architecture:

- **Browser-first operator interface.** Cockpit does not need to be tied to one physical control console.
- **Separate operator UI from vehicle implementation.** This aligns with `ROV - Cockpit` → `ROV - Control`.
- **Mock hardware for development.** The OpenROV development guide explicitly supports developing without the embedded computer by replacing hardware interfaces with mock interfaces. citehttps://github.com/OpenROV/openrov-cockpit/blob/master/docs/DEV-HOWTO.md
- **Physical validation branch.** OpenROV historically distinguished development code from a stable branch that had actually been run through a physical-ROV testing checklist. This is a useful precedent for distinguishing software that runs from software that has been vehicle-validated.
- **Telemetry and video as first-class services.** The architecture treats operator video, telemetry, control, recording, and extensions as separable concerns.
- **Upgrade management.** Cockpit included system-upgrade notification/control, which is relevant to long-term maintainability of deployed robots.

This is probably the most valuable part of this batch for the existing ROV architecture. OpenROV should remain a historical reference rather than a software dependency, but its development/testing model is worth studying closely.

## UKMARS and UKMARSBOT

UKMARSBOT is a deliberately simple beginner's multipurpose robot platform supporting line following, wall following, drag racing, and mini-sumo. The repository separates documentation, ECAD, hardware, mechanical design, and resources, with software maintained separately. citehttps://github.com/ukmars/ukmarsbot

This is an excellent reference for the ChartRoom principle of keeping **hardware, firmware/software, documentation, and exercises separately maintainable while still describing one complete platform**.

The repository also contains serial-data/control/logging resources and design documentation covering processor selection, constraints, sensors, and design decisions. The existence of separate sensor boards and documented hardware iterations is particularly useful for Test in a Box.

### Relevance

- Strong Test in a Box reference.
- Useful small-robot hardware platform for teaching incremental control and sensing.
- Good model for documentation structure around a repeatable educational platform.
- Relevant to the staged learning path already identified: battery → PWM → sensors → encoders → closed-loop motion → higher-level behaviours.

## Micromouse

The Joshua CCL Micromouse project is a more advanced example of a self-contained autonomous robot. It uses an STM32-based development workflow, with STM32CubeMX for hardware configuration, Eclipse/GCC for development, ST-LINK for programming/debugging, and STMStudio for variable monitoring. The repository includes branches associated with ADC calibration, gyro/encoder calibration, and wall tracking. citehttps://github.com/joshuaccl/Micromouse

### Relevance

- Strong example of embedded calibration and debugging as explicit engineering activities.
- Useful reference for deterministic, low-level robot control where Linux is unnecessary.
- Relevant to SwarmBot only at the subsystem/algorithm level, rather than as a complete architecture.
- Potential HiL/SiL reference for encoder, IMU, wall-sensor, and control-loop validation.
- Demonstrates why calibration and diagnostic tooling should be treated as part of the engineering system rather than an afterthought.

## Cross-project lessons

1. **Interface voltage matters.** Cheap sensors can be retained, but 5 V/3.3 V boundaries must be explicitly engineered and validated.
2. **Use an MCU when local timing matters.** An I²C-connected MCU can provide a useful deterministic subsystem boundary; a GPIO expander is better suited to simpler discrete I/O.
3. **Perception should be modular.** Ultrasonic, LiDAR, vision, and other sensors should feed generalised perception interfaces rather than being embedded directly into vehicle-control logic.
4. **OpenROV is a particularly valuable architectural reference.** Its browser-first Cockpit, mock hardware, plugin model, telemetry/video integration, and physical validation workflow map well onto the direction of ChartRoom.
5. **UKMARSBOT is a strong Test in a Box reference.** Its separation of hardware, ECAD, mechanical, software, documentation, and exercises is close to the structure wanted for reusable robotics education.
6. **Calibration is part of validation.** The Micromouse project reinforces the value of explicit calibration modes, observable variables, and repeatable diagnostic procedures.
7. **Do not overfit to historical hardware.** The architectural patterns are more valuable than adopting old OpenROV, STM32, ultrasonic, or I²C-expander hardware unchanged.

## Read later

- Study OpenROV Cockpit's mock-interface development model and compare it directly with `ROV - HiL-and-SiL`.
- Inspect OpenROV's control/data boundaries and determine which ideas map cleanly onto NATS without importing its historical transport choices.
- Compare UKMARSBOT's documentation/ECAD/mechanical/software split with the intended Test in a Box repository structure.
- Compare ultrasonic, LiDAR, and stereo-vision interfaces for SwarmBot/MarsBot.
- Consider whether an MCU-as-I²C-peripheral pattern is useful for ROV peripheral hardware or Smart Buoy sensor aggregation.
- Extract calibration/diagnostic exercises from Micromouse for the HiL/SiL validation roadmap.
