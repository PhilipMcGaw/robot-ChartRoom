# SB Components MotorShield research notes

The **SB Components MotorShield** is a Raspberry Pi motor-control board providing four DC-motor channels, direction/speed control, indicator LEDs, and simple sensor interfaces. Its Python library exposes motors as objects and provides grouped motor control, while the accompanying GUI supports independent direction and speed settings. citeturn0search0turn0search10

## Relevance

This is useful primarily as a **SwarmBot prototyping reference**. It demonstrates a relatively clean software abstraction over low-level GPIO/H-bridge control:

- `Motor` objects represent motor channels;
- `LinkedMotors` groups mechanically related motors;
- sensor objects expose simple trigger behaviour; and
- the GUI demonstrates direct manual testing of four motor channels. citeturn0search0

That abstraction is worth considering for Test in a Box and early robot bring-up, even if the actual hardware is not adopted.

## Architectural lesson

The useful pattern is to keep the application layer from depending directly on GPIO pin numbers. A hardware abstraction can map logical functions such as `left_drive`, `right_drive`, or `thruster_1` to physical outputs.

For the Robots architecture, this supports a stronger boundary:

**vehicle/control logic → logical actuator interface → hardware driver → GPIO/PWM/H-bridge**

This is compatible with the existing principle that Control owns actuator behaviour and safety.

## Caveats

The board is a convenience/prototyping product, not a safety-rated motor controller. Its electrical limits, H-bridge characteristics, thermal behaviour, and fault response need independent assessment before use in a real vehicle.

## Source

- [SB Components MotorShield documentation](https://sbcshop.github.io/MotorShield/)
- [SB Components MotorShield Wiki](https://learn.sb-components.co.uk/Motorshield)
- [SB Components MotorShield GitHub](https://github.com/sbcshop/MotorShield)

**Status:** Research / prototype inspiration. No hardware dependency planned.

**Read later:** Review the driver implementation and determine whether the logical motor abstraction is useful for SwarmBot's hardware interface.
