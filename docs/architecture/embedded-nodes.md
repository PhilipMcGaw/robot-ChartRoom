# Embedded node profiles

This page records the common ATtiny1614 node interface used by the ROV Light Module
and CTD where practical. The hardware source of truth is the corresponding KiCad
project in NautiPi.

## Common software contract

Each node should expose a stable identity and capabilities through Modbus RTU over
RS-485. The common framework should own serial framing, diagnostics, watchdog,
input-voltage measurement, status reporting, and the NATS-side gateway contract.
Feature modules implement the Light or CTD function set.

The shared power target is **12–18 VDC nominal**, with **24 VDC maximum design input**.
The 24 VDC value is an absolute maximum operating/design input and must not be
exceeded.

## Light Module profile

KiCad mapping for the ATtiny1614 on the Light Module:

| Pin | Board label | Function |
|---|---|---|
| 2 | A0/D0 | LED PWM |
| 3 | A1/D1 | Status LED / NTC feedback input |
| 4 | A2/D2 | Built-in LED |
| 5 | A3/D3 | Expansion |
| 6 | D4/RXD | RS-485 receive |
| 7 | D5/TXD | RS-485 transmit |
| 8 | A6/D6/SDA | I²C SDA |
| 9 | A7/D7/SCL | I²C SCL |
| 10 | UPDI | Programming |
| 11 | A8/D8/MOSI | Input-voltage measurement |
| 12 | A9/D9/MISO | Expansion |
| 13 | A10/D10/SCK | NeoPixel data |

The Light Module uses automatic RS-485 direction control, so no firmware direction
GPIO is required. D1 is the Cree CXA1304 9 V variant. Its AL8805 RSET is three
0.5 ohm 0805 resistors in parallel (approximately 0.167 ohm equivalent), targeting
approximately 600 mA LED current subject to final validation. Thermal management is
planned around water proximity/cooling and NTC feedback; it remains a commissioning
and thermal-test item.

## CTD profile

KiCad mapping for the ATtiny1614 on the CTD:

| Pin | Board label | Function |
|---|---|---|
| 2 | A0/D0 | CTD board-specific input |
| 3 | A1/D1 | CTD board-specific input |
| 4 | A2/D2 | Built-in LED |
| 5 | A3/D3 | RS-485 direction |
| 6 | D4/RXD | RS-485 receive |
| 7 | D5/TXD | RS-485 transmit |
| 8 | A6/D6 | Top-board SDA |
| 9 | A7/D7 | Top-board SCL |
| 10 | UPDI | Programming |
| 11 | A8/D8 | Input-voltage measurement |
| 12 | A9/D9 | Top-board temperature |
| 13 | A10/D10/SCK | Top-board TDS |

Unlike the Light Module, the CTD profile uses a firmware-controlled RS-485 direction
pin. A common framework must express that as a capability/profile setting.

## Address allocation

Modbus addresses are allocated in blocks of ten for operational clarity. The address
block is a convention; the factory unique ID and node-reported type remain the
authoritative identity.

| Address range | Node type |
|---|---|
| 10–19 | Light Modules |
| 20–29 | Motor controllers |
| 30–39 | CTD and environmental sensors |
| 40–49 | Thrusters and actuators |
| 50–59 | Cameras |
| 60–69 | Navigation |
| 70–239 | Future node types |
| 240–247 | Service and diagnostics |

This provides 23 complete ten-address type blocks while retaining a service range.
The current Light Module population should therefore use addresses `10–19`.
## Commissioning and robot transfer

The ATtiny1614 factory serial number is the permanent node identity. The Modbus
address is a changeable, robot-local assignment stored in EEPROM; it must not be
used as the node identity.

An uncommissioned node uses internal address value `0xFF` and does not answer normal
Modbus traffic. Modbus address `0` remains reserved for broadcast. The Raspberry Pi
gateway discovers nodes over the RS-485 bus using their factory unique IDs, assigns a
free address, writes the address with a version and CRC, and verifies the node after
reboot.

Discovery must also operate for already commissioned nodes. This allows a potted node
to move between robots without access to a button or jumper. When a node is moved,
it keeps its EEPROM address; the destination gateway checks the unique ID, detects
whether that address is already occupied, and reassigns the node if necessary.

If several nodes are uncommissioned or share the same default state, the gateway uses
collision-managed discovery: it queries progressively smaller portions of the unique-ID
space until one node responds, then assigns the next available address. The gateway
should retain a local mapping of unique ID, address, node type, and last-seen status,
and publish duplicate, missing, and uncommissioned-node conditions through NATS.
## Status

The interface is a design baseline. Firmware consolidation, bus testing, thermal
validation, sensor calibration, and full ROV integration remain separate verification
activities.


