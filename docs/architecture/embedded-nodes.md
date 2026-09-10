# Embedded node profiles

This page records the common ATtiny1614 node interface. The ROV Light Module is the current definitive playground and reference implementation; CTD support is deferred. The hardware source of truth is the corresponding KiCad
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
| 5 | A3/D3 | PCB function-ID resistor strap (analogue read) |
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

## CTD profile (deferred)

KiCad mapping for the ATtiny1614 on the CTD:

| Pin | Board label | Function |
|---|---|---|
| 2 | A0/D0 | TDS excitation PWM, approximately 3.6 kHz at 50% duty |
| 3 | A1/D1 | CTD NTC / board-specific analogue input |
| 4 | A2/D2 | Built-in LED |
| 5 | A3/D3 | PCB function-ID resistor strap (analogue read) |
| 6 | D4/RXD | RS-485 receive |
| 7 | D5/TXD | RS-485 transmit |
| 8 | A6/D6 | Top-board SDA |
| 9 | A7/D7 | Top-board SCL |
| 10 | UPDI | Programming |
| 11 | A8/D8 | Input-voltage measurement |
| 12 | A9/D9 | TDS analogue feedback input |
| 13 | A10/D10/SCK | Expansion / available peripheral pin |

The CTD profile uses hardware PWM on A0/D0 for the TDS excitation waveform and
analogue sampling on A9/D9 for TDS feedback. The CTD profile uses the shared A3/D3 PCB function-ID strap. The RS-485 interface
uses automatic direction control, so no MCU direction GPIO is required or assigned.

## PCB function identification

All new devices based on the Light/CTD controller shall include a resistor network connected to `A3/D3` to identify the function of the populated PCB. Existing legacy boards may remain exceptions until their hardware is revised.

A resistor network connected to `A3/D3` identifies the function of the populated PCB. The shared firmware reads this analogue strap during startup and uses the decoded value to select the compatible feature profile or reject incompatible firmware. This approach follows the resistor-coded address-selection method described in [Choosing resistor values for setting ADDR on the MCP23018](https://philipmcgaw.com/choosing-resistor-values-for-setting-addr-on-the-mcp23018/).

The PCB function ID is a hardware capability/type identifier, not a Modbus address. The Modbus address remains a separate robot-local value stored in EEPROM. This allows the same firmware framework to support multiple node types while preventing an incompatible firmware image from operating a board under the wrong profile.

The resistor values and ADC acceptance bands must be selected with sufficient tolerance and noise margin. The function ID should be sampled before the pin is assigned to any feature peripheral, and an invalid or ambiguous reading should put the node into a safe diagnostic state.
## PCB function resistor codes

The initial function-code resistor assignments are:

| Function | Divider ratio | R1 | R2 |
|---|---:|---:|---:|
| Function 1 - Light | 1/16 (0.0625) | 4k7 | Open circuit |
| Function 2 - CTD | 3/16 (0.1875) | 910R | 3k9 |
| Function 3 - Reserved | 5/16 (0.3125) | 1k5 | 3k3 |
| Function 4 - Reserved | 7/16 (0.4375) | 2k4 | 2k4 in series with 430R |
| Function 5 - Reserved | 9/16 (0.5625) | 2k4 in series with 430R | 2k4 |
| Function 6 - Reserved | 11/16 (0.6875) | 3k3 | 1k5 |
| Function 7 - Reserved | 13/16 (0.8125) | 3k9 | 910R |
| Function 8 - Reserved | 15/16 (0.9375) | Open circuit | 4k7 |

The values and tolerance approach are based on [Choosing resistor values for setting ADDR on the MCP23018](https://philipmcgaw.com/choosing-resistor-values-for-setting-addr-on-the-mcp23018/). The final ADC acceptance bands must be checked against the ATtiny reference, resistor tolerance, supply variation, noise, and input leakage. The theoretical ratio for Function 8 is 15/16 = 0.9375; the source article gives 0.9357 in its table.

## Address allocation

Modbus addresses are allocated in blocks of ten for operational clarity and are written in hexadecimal. The address
block is a convention; the factory unique ID and node-reported type remain the
authoritative identity.

| Address range | Node type |
|---|---|
| `0x0A–0x13` | Light Modules |
| `0x14–0x1D` | Motor controllers |
| `0x1E–0x27` | CTD and environmental sensors |
| `0x28–0x31` | Thrusters and actuators |
| `0x32–0x3B` | Cameras |
| `0x3C–0x45` | Navigation |
| `0x46–0xEF` | Future node types |
| `0xF0–0xF7` | Service and diagnostics |

This provides 23 complete ten-address type blocks while retaining a service range.
The current Light Module population should therefore use addresses `0x0A–0x13`.
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
## Connector roles

For the three-PCB Light Module stack, `J4` plugs into `J7` and `J8` plugs into `J9`.
These are internal stack connections. `J1` is a diagnostic port used during design
and commissioning; it is not the production robot connection. `J6` is the final
interface to the rest of the robot.
## Light Module interface details

`J6` is the production interface to the robot. Its input voltage is **12–18 VDC
nominal**, with a **24 VDC maximum operating input**. Do not exceed 24 VDC.

`J1` is the AVR UPDI diagnostic/programming header. The built-in feedback LED is
not part of the standard UPDI header, but is placed on an otherwise unused header
pin to provide visual status/feedback from the microcontroller during design,
commissioning, and operation.

The Light Module input voltage is measured through a 51 kΩ / 12 kΩ divider:

`Vmeasure = V_in × 12 / (51 + 12)`

| Input voltage | Expected Vmeasure |
| ------------: | ----------------: |
|        12 VDC |            2.29 V |
|        18 VDC |            3.43 V |
|        24 VDC |            4.57 V |

These values assume ideal resistor values; component tolerance and supply variation
will introduce small differences.
## TH1/D11 multiplexed temperature feedback

A1/D1 is multiplexed between status indication and temperature feedback:

- Output low: D11 is on for status indication.
- Output high: TH1 is connected directly to the 5 V rail and may self-heat; this
  state should be avoided or limited to brief controlled intervals.
- High-impedance analogue input: TH1 sinks current through the R8 and D11/R14 paths,
  providing an indicative temperature measurement.

TH1 is located near the high-power LED D1. D11 provides local status indication for
RS-485 and other conditions that cannot be reported through the data link.

The following indicative response assumes R8 = 10 kΩ, R14 = 1 kΩ, a 5 V rail, TH1
= 10 kΩ at 25 °C with B = 3590 K, and a green D11 Vf approximately 2.1 V when forward biased. The D11 glow is expected and normal. Actual
values require calibration with the assembled board and the LED's measured Vf.

| Temperature | TH1 resistance | A1 voltage | 10-bit ADC | D11 state |
|---:|---:|---:|---:|:---|
| 0 °C | 30.1 kΩ | 3.75 V | 768 | off |
| 10 °C | 18.9 kΩ | 3.27 V | 669 | off |
| 20 °C | 12.3 kΩ | 2.88 V | 589 | glowing |
| 25 °C | 10.0 kΩ | 2.83 V | 580 | glowing |
| 30 °C | 8.20 kΩ | 2.78 V | 569 | glowing |
| 40 °C | 5.62 kΩ | 2.66 V | 544 | glowing |
| 50 °C | 3.94 kΩ | 2.51 V | 514 | glowing |
| 60 °C | 2.82 kΩ | 2.34 V | 478 | glowing |
| 70 °C | 2.06 kΩ | 2.15 V | 439 | glowing |
| 80 °C | 1.53 kΩ | 1.94 V | 397 | glowing |
| 90 °C | 1.16 kΩ | 1.73 V | 354 | glowing |
| 100 °C | 889 Ω | 1.53 V | 313 | glowing |
## CTD NTC and TDS

The CTD NTC is connected via `J1`, exposed to the water, and directly measures water temperature. Its
measurement is an input to the CTD total dissolved solids (TDS) calculation. This
is distinct from the Light Module NTC, which monitors the high-power LED temperature.
## CTD connector roles

The CTD connector design is distinct from the Light Module. `J6` is the UPDI
programming/diagnostic interface and `J7` is the external interface to the robot.
`J2` plugs into `J3`, and `J4` plugs into `J5`, forming the CTD board stack.
## Status

The Light Module is the current implementation target for firmware consolidation, commissioning, bus testing, and thermal validation. The CTD profile remains a documented future profile; CTD firmware work and sensor calibration are deferred.

## Transducer modularity

The CTD is intentionally a combined logical transducer because conductivity, temperature, and pressure are interdependent measurements: temperature compensates conductivity, pressure provides depth, and the three values support derived salinity and density calculations.

Other sensing functions should remain separate RS-485/Modbus nodes where practical. Optical absorbance, turbidity, pH, dissolved oxygen, and ORP should not be added to the CTD merely to reduce node count. The shared Arduino PCB, pin map, firmware framework, commissioning process, diagnostics, and Modbus interface should be reused across these modules, while sensor-specific analogue and conditioning circuitry remains local to each node.









