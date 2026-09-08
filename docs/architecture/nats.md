# NATS

NATS is the selected middleware for communication between Robots components.

## Embedded bus health

The Raspberry Pi gateway owns the Modbus RTU over RS-485 bus and publishes bus-health
telemetry to NATS. Live consumers should use Core NATS; persistence belongs in the
ChartRoom/DataLogger path where required.

Recommended subject:

`rov.bus.rs485.telemetry`

The payload should contain `bus`, `baud`, `window_ms`, `load_pct`, `peak_load_pct`,
`transactions`, `tx_bytes`, `rx_bytes`, `timeouts`, `crc_errors`, and
`max_transaction_ms`. A sustained load near 30% is nominal; rising load, retries,
timeouts, or CRC errors should be visible in ChartRoom as system-health data.

The bus protocol remains Modbus RTU. NATS is the robot-level software interface and
does not replace the field bus.
