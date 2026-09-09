# BorgCube ROV research notes

**BorgCube ROV** is a long-running open ROV project by Tim Wilkinson. It is useful as a practical reference for integrating propulsion, buoyancy/stability, Raspberry Pi computing, watertight enclosures, servo-driven payloads, and operator software. The project explicitly targets manoeuvrability, a robotic arm, stereo vision, and an Oculus-compatible pilot interface. citeturn1search0

## Architecture and vehicle design

BorgCube uses a modular frame based on Actobotics aluminium channel rather than relying solely on round PVC tube. The project uses Raspberry Pi Compute Module hardware and multiple watertight enclosures, with waterproof servos for the eventual manipulator. citeturn1search0turn1search10

The project logs are especially useful because they expose real integration problems rather than only the finished vehicle. Examples include:

- motor-controller power distribution and protection;
- thruster resets caused by protection devices during higher-power operation;
- IMU-based PID stabilisation;
- poor initial mass distribution affecting neutral attitude;
- iterative controller PCB redesign;
- custom printed internal mounts; and
- modular tube and board mounting. citeturn1search0turn1search2

## Relevance to the ROV

BorgCube is a useful comparison for the existing ROV architecture, particularly:

- **Control:** closed-loop stabilisation should be treated as a control-system function, not merely a UI feature.
- **Electrical:** power distribution and protection need to be validated under realistic thruster loads.
- **Mechanical:** internal electronics mounting and service access deserve the same attention as the outer frame.
- **Payloads:** a common vehicle can support manipulators and imaging payloads without changing the core vehicle architecture.
- **Software:** operator software can expose stabilisation and camera/payload functions while the lower-level control system remains responsible for actuator behaviour.

## Stability and test lessons

The PID/balance work is particularly relevant. The project demonstrates that a vehicle can behave correctly in a nominal configuration yet expose problems when mass distribution and high-current actuator loads interact. The recorded motor resets and attitude-control tuning are good reminders to test:

1. static buoyancy and attitude;
2. actuator behaviour at realistic current;
3. control-loop response;
4. power-distribution voltage drop and protection behaviour; and
5. combined operation of propulsion and payload systems.

These are useful candidates for repeatable ROV bench and wet-test procedures.

## Mechanical/serviceability lessons

The move from simple laser-cut internal supports to purpose-designed 3D-printed mounts is a useful example of prototype evolution. Internal components should have positive mechanical retention, defined cable routing, and service access rather than relying on temporary mounting methods. citeturn1search2

## Caveats

This is historical project research, not a validated ROV design specification. Some components and techniques are dated, and the project should not be treated as evidence that a particular thruster, pressure housing, protection device, or control architecture is suitable for a modern vehicle.

## Sources

- [Hackaday.io — BorgCube ROV](https://hackaday.io/project/8343-borgcube-rov)
- [BorgCube project logs](https://hackaday.io/project/8343/logs)
- [BorgCube files](https://hackaday.io/project/8343/files)
- [BorgCube software repository](https://github.com/aanon4/borgcube-rov)

**Status:** Research / design inspiration.

**Read later:** Review the software repository, controller PCB history, PID/balance implementation, enclosure arrangement, and payload/arm integration.
