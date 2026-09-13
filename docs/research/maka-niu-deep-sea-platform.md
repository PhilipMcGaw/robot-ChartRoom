# Maka Niu — low-cost deep-sea imaging and sensing platform

## Why it is interesting

Maka Niu is a compact, modular deep-sea imaging and sensing platform developed through work involving MIT and the Ocean Discovery League. It is particularly relevant to the ChartRoom because it demonstrates how commodity computing hardware can be packaged for extreme underwater pressure rather than relying on a large, expensive subsea vehicle.

The published system combines a Raspberry Pi Zero W, Raspberry Pi Camera Module V2, pressure-rated housing, batteries, and environmental sensors. The production/deployment design is approximately 261 mm long and 64–66 mm in diameter, with a mass of about 870 g in air and 150 g apparent weight in water.

## Depth and pressure

- Current published depth capability: **1,500 m**.
- The 1,500 m design corresponds to approximately **148 atmospheres** of pressure in seawater.
- The published design work describes an aluminium housing intended to extend the system to approximately **6,000 m**, potentially reaching about 99% of the seafloor.
- The 1,500 m housing uses Delrin/polyoxymethylene; the 6,000 m concept uses an aluminium pressure housing.

The 6,000 m figure should be treated as a **design target/capability**, rather than evidence that the 6,000 m configuration has been operationally validated to that depth.

## Electronics and sensing

The research paper describes:

- Raspberry Pi Zero W as the main computer, with development work considering the Pi Zero 2 W.
- Raspberry Pi Camera Module V2: 8 MP stills and 1080p video at 30 fps.
- Temperature and depth measurement using a Keller Series 7LD temperature/pressure sensor.
- GPS for position when the system is out of the water.
- 9-axis motion tracking.
- Optional modular payloads, including high-lumen lighting.
- Wireless communications with no electrical penetrators through the pressure housing.

The system can operate for approximately **18 hours of continuous video** on the reported battery configuration. The battery system uses three LG MJ1 3,500 mAh Li-ion cells in series, giving 11.1 V nominal and 12.6 V maximum; software shuts the system down below approximately 9 V.

## Communications and software

Maka Niu uses the Pi Zero W's Wi-Fi/Bluetooth capability for short-range communication. Modules can communicate over approximately 10–15 cm using native 2.4 GHz wireless links, with the mechanical structure acting as a waveguide where required. Longer-range underwater communications can instead use an acoustic modem.

The mission engine is Node.js-based and is accessed through a browser on a phone, tablet, or laptop. The device can operate as its own Wi-Fi access point or join an existing Wi-Fi network when available. A block-based mission system allows non-programmers to construct capture missions and triggers.

This is an interesting architectural precedent for a modular ROV/AUV ecosystem: computation, sensing, payloads, and communications are treated as reusable modules rather than building one monolithic vehicle.

## Mechanical design lessons

The most interesting aspect is not the Raspberry Pi itself but the pressure-housing strategy:

1. Keep the electronics in a sealed pressure vessel.
2. Avoid electrical penetrators where possible.
3. Use a small cylindrical pressure housing to reduce the pressure-loaded area and simplify manufacture.
4. Reuse the same housing, battery subsystem, and control electronics for different payload modules.
5. Treat the pressure boundary as a primary engineering system, rather than simply making an ordinary electronics enclosure waterproof.

For an ROV project, this is a useful reference when considering low-cost sensor pods, drop cameras, autonomous payloads, or sacrificial/deployable instruments.

## Relevance to ChartRoom / ROV work

Maka Niu is worth studying as inspiration for:

- compact subsea sensor pods;
- pressure-housed Raspberry Pi systems;
- modular payload interfaces;
- low-cost deep-water cameras;
- environmental data logging;
- autonomous mission scripting;
- wireless communication between sealed modules;
- separating a generic compute/control module from application-specific payloads;
- designing for recoverability and post-deployment data retrieval.

It is **not** a direct design for the current tethered ROV architecture: its wireless, autonomous, drop-camera model is fundamentally different from a tethered ROV using continuous communications. The useful lessons are primarily in subsea packaging, modularity, low-cost instrumentation, and autonomous payload design.

## Further reading

- Raspberry Pi: [Extreme Raspberry Pi: projects taking Raspberry Pi to its very limits](https://www.raspberrypi.com/news/extreme-raspberry-pi-projects-taking-raspberry-pi-to-its-very-limits/)
- Raspberry Pi / The MagPi: [Maka Niu deep-sea imaging system](https://www.raspberrypi.com/news/maka-niu-deep-sea-imaging-system-the-magpi-125/)
- Peer-reviewed paper: [Maka Niu: A low-cost, modular imaging and sensor platform to increase observation capabilities of the deep ocean](https://doi.org/10.3389/fmars.2022.986237)
- Peer-reviewed design study: [Low-Cost, Deep-Sea Imaging and Analysis Tools for Deep-Sea Exploration: A Collaborative Design Study](https://doi.org/10.3389/fmars.2022.873700)

## Status

**Further reading / research reference.** The 1,500 m capability is published and demonstrated; the 6,000 m configuration is described as a design capability rather than a demonstrated operational depth in the sources reviewed here.

## Sources

- Raspberry Pi, *Extreme Raspberry Pi: projects taking Raspberry Pi to its very limits*.
- Croff Bell et al., *Maka Niu: A low-cost, modular imaging and sensor platform to increase observation capabilities of the deep ocean*, Frontiers in Marine Science, 2022.
- Croff Bell et al., *Low-Cost, Deep-Sea Imaging and Analysis Tools for Deep-Sea Exploration: A Collaborative Design Study*, Frontiers in Marine Science, 2022.
