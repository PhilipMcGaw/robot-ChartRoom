# Robot Profiles

Robot profiles define the configuration and capabilities that allow common software to operate different robot configurations.

## Shared embedded-node framework

The Light Module and CTD are intended to share one ATtiny1614 firmware framework and
the same physical board where practical. The common layer should provide node
identity, Modbus RTU framing, diagnostics, watchdog/reset handling, input-voltage
measurement, and automatic RS-485 direction control. Board profiles then select the
sensor and actuator features available on each node.

The physical pin numbers are reusable, but their roles are not identical on every
board. Firmware must therefore use a board profile rather than assuming that every
logical feature is present on the same pin. The KiCad schematics and PCB files in
NautiPi are authoritative for those mappings.

See [Embedded node profiles](embedded-nodes.md).

