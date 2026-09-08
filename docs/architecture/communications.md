# Communications

Documentation of communication paths, interfaces, and transport mechanisms used by the Robots ecosystem.

## RS-485 robot network

The short robot RS-485 network is expected to use a shared, unshielded harness of
approximately 2 m maximum length. Nodes share the same power rails and communicate
over a controlled half-duplex multidrop bus.

### Baud-rate guidance

The protocol should use **250 kbit/s as its nominal baud rate**. This provides
approximately 25 kB/s of raw 8N1 payload throughput and leaves useful margin for
bus turnaround, control traffic, and noise from the robot's switching loads.

**500 kbit/s is the sensible validated maximum** for this physical arrangement.
It may be supported as an optional configuration after testing the complete harness
and node population. Rates around 1 Mbit/s should be treated as experimental rather
than as a design requirement.

The ADM485 transceiver is capable of higher data rates, but the transceiver rating
does not establish a suitable system baud rate for an unshielded robot harness.
The ATtiny1614 USART clock configuration and baud-rate error must also be checked
for the selected setting.

### Termination and biasing

Termination resistors are located in the harness at the two physical ends of the
bus. The USB/RS-485 control interface provides the single optional bias-resistor
network for the bus; biasing must not be fitted independently at every robot node.

For the initial short-harness prototype, the bias network may remain unpopulated.
It should be populated if testing shows false idle transitions, startup chatter,
or susceptibility to switching noise.

The bus should include a shared signal reference conductor in the harness.

### Implementation status

This is an engineering design target, not a physical validation result. Final
support for 250 kbit/s and 500 kbit/s depends on bench testing with the intended
harness, termination, bias network, node count, and switching loads.

References:

- [ADM485 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adm485.pdf)
- [ATtiny1614 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-16-17-DataSheet-DS40002204A.pdf)