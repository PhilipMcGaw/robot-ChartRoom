---
title: "DFRobot EC library"
description: "Documentation page covering DFRobot EC library."
type: research
status: reference
authority: Chartroom
tags:
  - research
---

# DFRobot EC library
## DFR0300-H product reference

The DFR0300-H is DFRobot's laboratory-grade, analogue K=10 conductivity sensor kit for high-conductivity liquids. DFRobot positions it for seawater, concentrated brine, mariculture, aquariums, and wastewater/high-EC testing; it is not the low-conductivity K=1 variant.

### Published specifications

| Item | DFRobot specification |
|---|---|
| Signal-board supply | 3.0–5.0 V |
| Signal-board output | 0–3.2 V analogue |
| Signal-board size | 42 × 32 mm |
| Board probe connector | BNC |
| Board signal connector | PH2.0-3Pin Gravity |
| Signal-board accuracy | ±5% full scale |
| Probe type | Laboratory grade, K=10 |
| Cell constant | 10 ± 2 |
| Detection range | 10–100 mS/cm |
| Probe temperature range | 0–40 °C |
| Cable length | 100 ± 2 cm |
| Stated probe life | More than 0.5 year, dependent on use and environment |

The kit contains one probe, one signal-conversion board, four 12.88 mS/cm standard-buffer solutions, one Gravity analogue cable, two waterproof gaskets, a BNC connector cap, four M3 × 10 nylon pillars, and eight M3 × 5 screws.

The board pinout is: pin 1 = GND, pin 2 = VCC (3.0–5.0 V), and pin 3 = analogue output (0–3.2 V). Because the output is analogue, a Raspberry Pi deployment needs an external ADC; an Arduino-class board can use an analogue input directly.

### Use and maintenance constraints

The kit has no temperature sensor. DFRobot recommends adding a temperature sensor, such as a waterproof DS18B20, and passing both voltage and temperature to the EC10 library for compensation. The supplied laboratory probe should not be left immersed continuously. Its platinum-black electrode surface must not be touched and should only be rinsed with distilled water. The probe should be rinsed and dried between different test liquids to prevent cross-contamination.

DFRobot's current product page and setup guide describe single-point calibration with the supplied 12.88 mS/cm standard. Calibration commands are `ENTEREC`, `CALEC`, and `EXITEC`; the resulting parameters are saved in the controller EEPROM. The separate K=1 library and older documentation may refer to two-point calibration, so the K=1 and K=10 procedures must not be mixed.

**Official references:** [DFRobot DFR0300-H product page](https://www.dfrobot.com/product-1797.html), [DFRobot DFR0300-H Wiki](https://wiki.dfrobot.com/dfr0300-h), [DFRobot K=10 setup guide](https://wiki.dfrobot.com/dfr0300-h/docs/20395), and [DFRobot_EC10 library](https://github.com/DFRobot/DFRobot_EC10).

## Conductivity reference for the CTD sensor

The [DFRobot_EC](https://github.com/DFRobot/DFRobot_EC) Arduino library is a useful reference for the conductivity component of the CTD sensor. It implements the conversion from measured analogue voltage to electrical conductivity, temperature compensation, and probe calibration.

The library is written for DFRobot's Gravity Analog Electrical Conductivity Sensor / Meter Kit V2 (K=1.0, DFR0300). Its public interface deliberately separates voltage acquisition from the conductivity calculation through `readEC(voltage, temperature)`. This is relevant to the CTD architecture, where the embedded sensor electronics should acquire and timestamp the raw measurement and then apply the appropriate conversion and compensation.

### Points worth studying

- voltage-to-conductivity conversion and the associated analogue-front-end assumptions;
- probe cell constant (`K`) calibration;
- temperature compensation referenced to 25 °C;
- two-point calibration using 1,413 µS/cm and 12.88 mS/cm standards;
- storage of calibration parameters in non-volatile memory;
- range-dependent calibration constants in the K=1 implementation; and
- the separate K=10 implementation for higher-conductivity measurements, including marine applications.

The DFRobot implementation uses a temperature coefficient of 0.0185 / °C. This should be treated as a reference to investigate, not automatically adopted as the CTD's final seawater compensation model.

The K=10 library ([DFRobot_EC10](https://github.com/DFRobot/DFRobot_EC10)) is particularly relevant because it is intended for higher-conductivity solutions. Its implementation uses a single calibrated K value and the same basic temperature-compensation approach.

### Relevance to the CTD architecture

Use this project as a reference implementation rather than a drop-in dependency. Before selecting the final CTD conductivity implementation, investigate:

- the required conductivity range for freshwater and seawater operation;
- probe geometry and cell constant;
- excitation method and electrode polarisation;
- analogue signal conditioning and ADC requirements;
- calibration traceability and suitable conductivity standards;
- temperature-sensor accuracy and physical placement relative to the conductivity cell;
- temperature compensation appropriate to the intended seawater measurement range; and
- repeatability, drift, fouling, and long-term probe behaviour.

The useful architectural lesson is to keep raw acquisition, calibration, physical conversion, temperature compensation, and higher-level CTD data handling as separable functions. This also aligns with the existing goal of keeping low-level sensor acquisition local to the CTD electronics while exposing well-defined measurements to the higher-level system.

**Status:** Research / reference implementation. Not selected as the CTD implementation and not a project dependency.

**Read later:** [DFRobot_EC](https://github.com/DFRobot/DFRobot_EC), [DFRobot_EC10](https://github.com/DFRobot/DFRobot_EC10), and [DFRobot Analog EC Sensor K=10 documentation](https://wiki.dfrobot.com/dfr0300-h/).
