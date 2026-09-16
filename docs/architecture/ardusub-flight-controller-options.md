---
title: ArduSub Flight Controller Options
description: UK sourcing options for Navigator and Pixhawk/Cube hardware.
type: architecture
status: maintained
authority: Chartroom
tags:
  - architecture
  - blueos
  - ardupilot
---

# ArduSub Flight Controller Options

## Decision summary

For a Raspberry Pi 4 running BlueOS, the **Blue Robotics Navigator** is the most direct fit. It is designed to turn the Raspberry Pi 4 into a BlueOS/ArduSub flight controller and provides the onboard IMU, compass, barometer, PWM outputs, ADC inputs, leak inputs, I²C, and serial expansion needed by the vehicle.

A conventional alternative is a **Cube Orange+** or **Holybro Pixhawk 4** running ArduSub, with the Raspberry Pi acting as the BlueOS companion computer. This keeps the autopilot control loop on a dedicated controller and is the lower-risk architecture for a vehicle intended to operate in water.

The prices below were checked on **16 September 2026**. They are supplier-listed prices and should be rechecked before purchase.

## UK suppliers and prices

| Controller | Supplier | Listed price (inc. VAT) | Availability noted | Comments |
|---|---|---:|---|---|
| Blue Robotics Navigator | [Buccaneer Marine](https://buccaneermarine.com/products/navigator-flight-controller) | **£219.99** | Listed for sale | Intended for Raspberry Pi 4 and BlueOS; Pi not included |
| Blue Robotics Navigator | [RobotShop UK](https://uk.robotshop.com/products/bluerobotics-navigator-drone-flight-controller) | **£203.08** | Restocking soon | Pi not included |
| Holybro Pixhawk 6C, aluminium case | [3DXR](https://www.3dxr.co.uk/products/holybro-pixhawk-6c-aluminium-case-11055) | **£175.99** | 43 in stock when checked | Controller only; verify power module and cable requirements |
| Holybro Pixhawk 6C | [Unmanned Tech](https://www.unmannedtechshop.co.uk/products/pixhawk-6c-flight-controller-aluminium-case) | **£139.99** | In stock when checked | Controller-only listing; check the selected variant |
| Cube Orange+ standard set | [3DXR](https://www.3dxr.co.uk/products/cubepilot-the-cube-orange-standard-set-with-sma-connector-cp-06344) | **£415.00** | 17 in stock when checked | Includes Cube and carrier board |
| Cube Orange+ standard set | [opAurea](https://glockenspiel-lanternfish-f8xj.squarespace.com/store/autopilots/cube-autopilot-and-combos) | **£375.00** | Stock to confirm | Includes Cube and carrier board |
| Holybro Pixhawk 4 | [Flying Tech](https://www.flyingtech.co.uk/product/holybro-pixhawk-4-px4-flight-controller/) | **£179.00–£194.90** | Sold out when checked | Strong ArduSub/BlueOS fit, but availability is poor |

## Recommendation for the CuttleOS/ChartRoom ROV

### Navigator

Choose the Navigator if the goal is to use the Raspberry Pi as the main onboard computer while retaining the normal BlueOS and ArduSub workflow. It also leaves the Navigator's expansion I²C and serial interfaces available for additional sensors.

The Navigator is the closest match to the proposed design, but the external IMU and Modbus depth sensor should not automatically replace its onboard control-state sensors. Any sensor used for stabilization or depth-hold needs to be integrated into ArduPilot's supported sensor path and validated under failure conditions.

### Cube Orange+ or Pixhawk 4

Choose a Cube Orange+ or Pixhawk 4 when reliability and a conventional separation of responsibilities matter more than reducing board count:

```text
Raspberry Pi 4
    └── BlueOS, video, networking, extensions
            │ MAVLink / USB or UART
            ▼
Dedicated autopilot
    └── ArduSub, IMU, attitude/depth control, PWM outputs
```

This is the architecture most closely aligned with the established ArduSub/BlueOS ecosystem.

### Pixhawk 6C

The Pixhawk 6C is a potentially good value modern ArduPilot board. However, Blue Robotics' specific ArduSub guidance recommends Navigator, Pixhawk 4, and Cube hardware; other ArduPilot-compatible boards are not necessarily tested with BlueOS. Treat the 6C as a test-and-integration choice rather than the lowest-risk purchase.

## Hardware checklist

Before ordering, confirm the complete system rather than the controller price alone:

- Raspberry Pi 4B and BlueOS-compatible storage;
- autopilot power module or suitable regulated power input;
- PWM/ESC cables and connector compatibility;
- underwater pressure/depth sensor and its electrical interface;
- USB-RS485 adapter or RS485 transceiver for Modbus sensors;
- leak detection and hardware motor-disable path;
- enclosure, vibration isolation, and power distribution;
- ArduSub firmware support for the exact board and selected sensor drivers.

## References

- [BlueOS flight controller guidance](https://blueos.cloud/docs/stable/integrations/hardware/required/flight-controller/)
- [BlueOS onboard computer guidance](https://blueos.cloud/docs/stable/integrations/hardware/required/onboard-computer/)
- [Blue Robotics Navigator](https://bluerobotics.com/store/comm-control-power/control/navigator/)
- [ArduSub autopilot hardware list](https://ardupilot.org/sub/docs/common-autopilots.html)
- [Existing BlueOS and Adeept Robot HAT architecture page](blueos-adeept-robot-hat.md)
