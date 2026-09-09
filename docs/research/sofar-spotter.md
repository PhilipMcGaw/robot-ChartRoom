# Sofar Ocean Spotter research notes

The [Sofar Ocean Spotter](https://www.sofarocean.com/products/spotter) is a useful commercial reference for autonomous ocean sensing. It provides a professional comparison point for the [T3chFlicks Smart Buoy](https://github.com/sk-t3ch/smart-buoy) and for the project's own CTD and distributed-sensor architecture.

This is comparative research and architectural inspiration, not a specification or project dependency.

## Why it is relevant

Spotter demonstrates how a commercial system packages several related concerns into a common platform:

- autonomous ocean measurement;
- local sensing and time-series acquisition;
- onboard storage;
- solar power and battery management;
- satellite/cellular telemetry;
- remote configuration and firmware updates;
- a web dashboard and API;
- fixed, drifting, and mobile deployment models; and
- an extensible underwater sensor architecture.

The current Spotter platform supports a Spotter Buoy, Smart Mooring, and Spotter Scout, while presenting data through a common dashboard/API. The same platform can therefore span fixed-point, subsurface, and mobile sensing applications.

## Configurator

The [Spotter Configurator](https://spotter-configurator.sofarocean.com/) is particularly useful as a product-design reference. It exposes the idea of configuring a common sensing platform around the deployment rather than treating every application as a separate instrument.

The current configurator presents at least three deployment types:

- Spotter Buoy;
- Spotter Buoy with Smart Mooring; and
- Spotter Scout.

The configuration flow is organised around deployment, location, solution, sensors, data, and a final system summary.

This is worth studying as an example of turning a technically complex system into a structured configuration workflow.

## Measurement architecture

The Spotter Buoy records 3-D displacement time series at 2.5 Hz and derives wave parameters including significant wave height, period, direction, and spectral information. It also measures sea-surface temperature and barometric pressure and records position and system status.

An important design lesson is the retention of relatively raw measurement data. Spotter records the 3-D displacement time series onboard as well as providing derived wave products. This preserves the possibility of improved analysis without requiring another deployment.

The published specification gives a 0.03–0.8 Hz wave-frequency range, 0–360° wave-direction coverage, approximately ±2 cm wave-displacement accuracy, SST accuracy of ±0.1 °C, and onboard SD-card storage.

## Smart Mooring and sensor modularity

The Smart Mooring extends sensing below the surface and supports Bristlemouth-enabled sensor nodes. Current documented sensor options include temperature, conductivity/salinity, dissolved oxygen, turbidity, hydrophones, pressure, and current sensing.

This is particularly relevant to the project's CTD work. The useful architectural principle is a defined sensor interface which allows sensing capability to evolve without redesigning the complete buoy/controller.

The Smart Mooring documentation describes cable options up to 50 m and a two-conductor cable carrying power and data. This is also worth comparing with the project's distributed sensor-node and power/communications architecture.

## Power and communications

Spotter uses solar power and a rechargeable lithium-ion battery, with satellite and cellular connectivity. The platform supports remote configuration, alerts, firmware updates, and access to both current and historical data.

The engineering lesson is not to copy the particular communications technology, but to separate:

- measurement;
- local persistence;
- power management;
- telemetry;
- remote configuration; and
- user-facing data access.

## Software and data architecture

The Spotter Dashboard provides real-time and historical data, configuration, alerts, maps, and two-way communication. Sofar also provides a REST API and access to onboard SD-card data.

This is a useful commercial comparison for the project's **Cockpit → Control → Datalogger** separation:

- local hardware should acquire and protect measurement data;
- the control/data layer should expose well-defined state and telemetry;
- persistent storage should remain independently useful from the live UI; and
- the operator/application layer should consume data through an explicit interface rather than owning the hardware implementation.

## Comparison with T3chFlicks Smart Buoy

The Smart Buoy is the low-cost, educational/prototype reference; Spotter is the commercial reference for the same broad problem domain.

Useful comparison areas include:

- sensor acquisition and local processing;
- raw versus derived data retention;
- power budgeting and scheduling;
- waterproofing and serviceability;
- telemetry architecture;
- local logging versus cloud access;
- dashboard design;
- remote configuration;
- deployment and mooring;
- sensor modularity; and
- what changes when a prototype becomes a continuously deployable commercial instrument.

The Smart Buoy's documented V2 proposals — resealable access, ESP32/LoRa, and more local wave-data processing — provide a useful bridge between the educational prototype and the more integrated commercial architecture.

## Relevance to project architecture

For the CTD and other environmental sensor nodes, investigate whether the following pattern is appropriate:

```text
Sensor / analogue front end
          │
          ▼
Local acquisition + timestamping
          │
          ├── raw data / local buffer
          ├── calibration state
          ├── derived measurements
          └── health / diagnostics
          │
          ▼
Communications interface
          │
          ▼
Datalogger / higher-level processing
          │
          ▼
Cockpit / analysis / API
```

The sensor node should remain useful without requiring the Cockpit to be present, and the stored/raw measurement path should not be unnecessarily dependent on the live communications link.

For ROV use, the same principle may apply to payload and environmental sensors, although underwater power, communications, serviceability, and pressure-rated packaging impose different constraints.

## Questions to investigate

- Which parts of Bristlemouth's abstraction are useful for our own sensor-node interfaces?
- Should CTD nodes retain raw ADC data, processed measurements, or both?
- What calibration metadata should travel with a measurement?
- Where should timestamping and filtering occur?
- Which sensor health information should be treated as first-class telemetry?
- How should local persistence behave when communications are unavailable?
- Could a common sensor interface serve both ROV and buoy/terrestrial instrumentation?
- What aspects of the Spotter configurator could inform future vehicle/payload configuration tools?
- How much of the commercial architecture can be reproduced with open hardware/software while retaining serviceability and traceability?

## Status

**Research / commercial reference.** Spotter is not a project dependency and no decision has been made to reproduce its architecture or use Bristlemouth directly.

## Read later

- [Sofar Ocean Spotter](https://www.sofarocean.com/products/spotter)
- [Spotter Configurator](https://spotter-configurator.sofarocean.com/)
- [Spotter technical specifications](https://www.sofarocean.com/products/spotter/buoy/specs)
- [Smart Mooring specifications](https://www.sofarocean.com/products/spotter/smart-mooring/specs)
- [Sofar Ocean support and documentation](https://www.sofarocean.com/support)
- [Bristlemouth](https://bristlemouth.org/)
- [T3chFlicks Smart Buoy](https://github.com/sk-t3ch/smart-buoy)
