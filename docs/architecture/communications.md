# Communications

Documentation of communication paths, interfaces, and transport mechanisms used by the Robots ecosystem.

## RS-485 robot network

The robot field bus is a shared, half-duplex RS-485 multidrop network. It is intended
to connect the Raspberry Pi gateway to up to six Light Modules, motor controllers,
and other embedded nodes over the final ROV harness.

### Protocol and baud rate

The application protocol is **Modbus RTU over RS-485**. Modbus defines the messages
and addressing; RS-485 defines the electrical multi-drop transport. Keeping those
layers explicit allows the Pi-side bus code to be reused on other robots.

The default operating rate is **115200 baud, 8 data bits, no parity, 1 stop bit
(8N1)**. This is the baseline for commissioning and mixed node populations.

**500 kbit/s is an optional performance configuration**, to be enabled only after
testing the complete harness, termination, node count, switching loads, and clock
error. It is not the default design requirement.

### Loading target and telemetry

Normal sustained bus utilisation should be approximately **30% or lower**, measured
over a rolling window. The Pi gateway should calculate utilisation from transmitted
and received serial time, and publish the result through NATS for ChartRoom and
DataLogger recording. The telemetry should include baud rate, measurement window,
load percentage, peak load, transaction counts, timeouts, CRC errors, and the
maximum transaction duration.

### Termination and biasing

Termination resistors belong at the two physical ends of the bus. The USB/RS-485
control interface provides the single optional bias-resistor network; biasing must
not be fitted independently at every robot node. The harness should include a shared
signal reference conductor.

For the initial short-harness prototype, the bias network may remain unpopulated.
Populate it if testing shows false idle transitions, startup chatter, or susceptibility
to switching noise.

### Implementation status

These are system design targets, not physical validation results. Final support for
115200 and 500 kbit/s depends on bench testing with the intended harness and node
population. The existing embedded folders contain experiments; the KiCad designs
remain the authority for electrical pin assignments.

References:

- [ADM485 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/adm485.pdf)
- [ATtiny1614 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-16-17-DataSheet-DS40002204A.pdf)
- [Modbus over Serial Line Specification](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
