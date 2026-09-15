---
title: "BlueOS and Adeept Robot HAT"
description: "Documentation page covering BlueOS and Adeept Robot HAT."
type: architecture
status: maintained
authority: Chartroom
tags:
  - architecture
---

# BlueOS and Adeept Robot HAT

## Status

**Status:** Planned / integration investigation

**Adeept hardware:** Bench-tested

**BlueOS integration:** Not yet implemented

## Summary

The current investigation is whether the **Adeept Robot HAT for Raspberry Pi** can provide the physical I/O layer for the ChartRoom ROV while **BlueOS** provides the onboard operating-system and service infrastructure.

The objective is to reuse BlueOS capabilities rather than recreate services that are already solved, while retaining the project's own control architecture and avoiding a dedicated flight-controller board unless it proves useful later.

The proposed approach is to implement the Adeept HAT as a **BlueOS Extension** rather than modifying BlueOS core.

## Existing Adeept hardware capability

The Adeept Robot HAT provides, among other interfaces:

- Raspberry Pi interface;
- PCA9685-based 16-channel PWM/servo output;
- I²C interface;
- an interface/socket for an external MPU6050 IMU module;
- 5 V servo supply;
- UART, ADC, GPIO, and other hardware interfaces.

The existing hardware setup has already been brought up using the Adeept example software. The `01_Servo.py` example was made operational after installing the required prerequisites and enabling the relevant interfaces.

**Multiple 9 g hobby servos have also been operated concurrently.**

Therefore, the basic hardware path is already demonstrated:

```text
Raspberry Pi
     │
    I²C
     │
 PCA9685
     │
 ├── 9 g servo
 ├── 9 g servo
 ├── 9 g servo
 └── 9 g servo
```

The BlueOS work is consequently an **integration exercise**, not a basic PCA9685 bring-up exercise.

See the existing hardware notes: [Adeept Robot HAT for Raspberry Pi](https://philipmcgaw.com/adeept-robot-hat-for-raspberry-pi/).

## Proposed BlueOS architecture

```text
                    BlueOS
                       │
             Adeept Robot HAT
                  Extension
                       │
                      I²C
                       │
                   PCA9685
                       │
          ┌────────────┼────────────┐
          │            │            │
        PWM 0        PWM 1       PWM 2 ...
          │            │            │
        Servo        Servo        Servo
```

The extension should initially expose the PCA9685 as generic PWM outputs rather than embedding ROV-specific semantics.

For example:

```text
CH 0  → PWM output
CH 1  → PWM output
CH 2  → PWM output
...
CH 15 → PWM output
```

The ROV Control layer can subsequently assign semantic functions to those outputs, such as thruster channels.

This maintains a clean separation between **hardware abstraction** and **vehicle control**.

## What BlueOS can provide

BlueOS is potentially useful for infrastructure that would otherwise have to be developed specifically for the ROV, including:

- onboard system management;
- networking;
- web-based administration;
- extension management;
- MAVLink infrastructure if required;
- camera management;
- WebRTC video infrastructure;
- serial interfaces and bridging;
- logging and other system services.

The intention is to reuse these capabilities rather than reproduce them in the project's own applications.

## Adeept HAT BlueOS Extension

A first `Adeept Robot HAT` extension should have a deliberately small scope:

1. Access the Raspberry Pi I²C interface.
2. Detect and initialise the PCA9685.
3. Configure the PWM frequency.
4. Set individual PWM outputs.
5. Report HAT/PCA9685 status.
6. Provide a simple BlueOS web interface for testing.
7. Later add MPU6050 support.
8. Add other HAT interfaces only when required.

A first test UI could expose the PWM channels directly:

```text
Adeept Robot HAT

PCA9685
Address: [detected]
Frequency: 50 Hz

CH 0    1500 µs
CH 1    1500 µs
CH 2    1500 µs
CH 3    1500 µs
...

[Centre all outputs]
```

The actual PCA9685 address should be detected or verified on the hardware rather than assumed.

## Relationship to ROV Control

The HAT extension should **not** become the vehicle controller.

```text
                 ROV Control
                      │
                 NATS / API
                      │
                      ▼
             Adeept HAT Extension
                      │
                     I²C
                      │
                  PCA9685
                      │
                     PWM
                      │
                     ESC
                      │
                  Thruster
```

`ROV Control` remains responsible for:

- joystick commands;
- thruster mixing;
- neutral;
- command timeout;
- E-stop;
- vehicle state;
- control loops.

The HAT extension is responsible for translating requested hardware outputs into PCA9685 PWM signals.

This is consistent with the existing ChartRoom principle that propulsion safety, timeout, neutral, and E-stop belong to the Control subsystem rather than the pilot UI.

## NATS

The existing architecture retains **NATS** as the chosen communication middleware. MQTT is not part of the design.

The proposed boundary is:

```text
ROV Control
     │
    NATS
     │
Adeept HAT Extension
     │
    I²C
     │
 PCA9685
```

This means the ROV control software does not need to know about the Adafruit/PCA9685 implementation details.

## MPU6050

The Adeept HAT provides an I²C interface for an external MPU6050 module. This creates a potential future path:

```text
                    Raspberry Pi
                         │
                        I²C
                         │
              ┌──────────┴──────────┐
              │                     │
           PCA9685               MPU6050
              │                     │
           PWM outputs          IMU data
```

MPU6050 integration should be added only after reliable PCA9685 operation through BlueOS has been demonstrated.

## Multiple PCA9685 devices

Multiple PCA9685 devices can share an I²C bus provided that each has a unique address and the electrical limitations of the bus are respected.

For the ROV, I²C should preferably remain **local to the Raspberry Pi/electronics assembly**. The planned RS-485 architecture remains the preferred physical layer for longer-distance connections to distributed external modules.

```text
                 Raspberry Pi
                      │
                 Local I²C
                      │
             ┌────────┴────────┐
             │                 │
          PCA9685           PCA9685
             │                 │
        local PWM          local PWM

                 Raspberry Pi
                      │
                 RS-485 PHY
                      │
        ═══════════ RS-485 ═══════════
          │             │             │
       LED node      sensor node   other module
```

## MAVLink and ArduSub

MAVLink and ArduSub remain optional parts of the architecture.

The project is deliberately investigating whether the Raspberry Pi can act as the central vehicle computer without a separate flight-controller board. BlueOS does not require that the project immediately adopt the conventional BlueROV2 architecture of BlueOS plus a dedicated autopilot.

A later experiment could investigate Raspberry Pi-based ArduSub and whether the PCA9685 and MPU6050 can be used as its output and sensor interfaces. This is **not a prerequisite** for the BlueOS/Adeept integration.

The preferred development sequence is to establish the BlueOS hardware abstraction first and only then evaluate whether MAVLink/ArduSub adds value.

## RS-485 external modules

The ROV is also investigating an RS-485 bus for distributed modules.

The intended separation is:

```text
BlueOS / Raspberry Pi
        │
        ├── Local I²C → PCA9685 / MPU6050
        │
        └── RS-485 → distributed modules
                         ├── LED
                         ├── sensors
                         ├── power monitoring
                         └── other payloads
```

RS-485 is the physical layer; the module protocol remains a separate design decision. Options include a project-specific protocol, Modbus RTU, or MAVLink where appropriate.

## Demonstration and development plan

The existing concurrent-servo test provides the hardware baseline. The next stages are:

### Stage 1 — BlueOS hardware access

Demonstrate that a BlueOS extension can access the HAT's I²C interface.

### Stage 2 — PCA9685 detection

Detect and initialise the PCA9685 from inside the BlueOS extension.

### Stage 3 — Single 9 g servo

Drive one 9 g servo at approximately 50 Hz through the extension.

### Stage 4 — Multiple servos

Reproduce the existing successful concurrent-servo demonstration through BlueOS.

### Stage 5 — Extension API and UI

Expose PWM channels through a clean extension API and provide a test interface.

### Stage 6 — MPU6050

Detect and read the external MPU6050 through the same I²C infrastructure.

### Stage 7 — ROV Control integration

Connect the extension to the existing ROV control architecture without transferring vehicle-control responsibilities into the hardware driver.

### Stage 8 — Optional MAVLink/ArduSub integration

Investigate whether the PCA9685 and MPU6050 can subsequently be used by a Raspberry Pi-based ArduSub configuration.

## Design principle

The objective is **not** to turn the Adeept Robot HAT into a Blue Robotics Navigator clone.

The intended division of responsibility is:

> **BlueOS provides the vehicle-computer infrastructure; the Adeept HAT provides inexpensive physical I/O; ROV Control provides vehicle behaviour.**

This should allow the project to reuse mature BlueOS infrastructure while retaining control of the parts of the ROV architecture that are central to the project.

## References

- [Adeept Robot HAT for Raspberry Pi — existing project notes](https://philipmcgaw.com/adeept-robot-hat-for-raspberry-pi/)
- [BlueOS documentation](https://blueos.cloud/docs/stable/)
- [BlueOS Extensions](https://blueos.cloud/docs/stable/development/extensions/)
- [BlueOS GitHub](https://github.com/bluerobotics/BlueOS)
- [Blue Robotics Cockpit](https://github.com/bluerobotics/cockpit)
