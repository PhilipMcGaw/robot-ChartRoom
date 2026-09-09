# DFRobot EC library

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
