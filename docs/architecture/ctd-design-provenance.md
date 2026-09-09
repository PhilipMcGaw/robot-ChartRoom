# CTD design provenance

## Conductivity probe

The CTD conductivity probe design is based on the work of Marco Carminati and Paolo Luzzatto-Fegiz, published as [Conduino](https://github.com/feslab/conduino). The Conduino design is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

The design was subsequently modified by the OpenCPD team, as documented in `Conduino-V01.pdf`. The OpenCPD material is also identified as licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Pressure transducer

The CTD pressure-transducer interface is based on the SparkFun reference design **MS5803-14BA Breakout PCB v10**. The referenced SparkFun design is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Additional reference material

The [OpenCTD Construction and Operation guide](https://oceanographyforeveryone.org/openctd/) is retained as background reference material and is identified as licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). This licence is separate from the CC BY-SA licence applying to the Conduino/OpenCPD and SparkFun design references.

Manufacturer datasheets and product documents in the KiCad resources folder are retained for technical reference only; no additional licence is inferred from their inclusion.

## PCB development reference

PCB design development was informed by the DFRobot Gravity EC Sensor DFR0300.

## Turbidity sensor design

The initial turbidity prototype should use a fixed 860 nm near-infrared LED and a silicon photodiode arranged at 90 degrees to the incident beam. The LED and photodiode optical axes should intersect at a defined measurement volume.

Recommended starting geometry:

- 10 mm from the LED optical window to the measurement volume.
- 10 mm from the photodiode optical window to the measurement volume.
- Approximately 14 mm between the LED and photodiode optical centres.
- Provide black internal baffles and limit the photodiode field of view to reduce stray light and ambient-light pickup.
- Begin with a 5-20 mm adjustable range during prototype calibration.

A shorter optical path is preferable for highly turbid water because it reduces detector saturation. A longer path can improve sensitivity in clearer water. The final geometry must be calibrated as a complete mechanical and optical assembly using known turbidity standards.

The first implementation should report a calibrated project-specific turbidity value or FNU where the calibration supports it. NTU and FNU should not be treated as interchangeable without documenting the measurement method. For very high turbidity, a future revision could add a forward/transmission detector at 180 degrees.

Reference guidance commonly limits the combined incident and scattered optical path to no more than approximately 100 mm. See the [EPA turbidity guidance](https://www.epa.gov/sites/production/files/2021-05/documents/user-manual-freshwater-2021.pdf) and the [Analog Devices turbidity reference design](https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x/turbidity).
## Further reading

These projects and studies are useful for follow-up work on conductivity excitation, analogue feedback, temperature compensation, pressure measurement, probe construction, calibration, and field validation:

- [jwlauer/CTD](https://github.com/jwlauer/CTD) - MicroPython CTD using an MS5803 pressure sensor, NTC temperature measurement, two- or four-electrode conductivity, pseudo-AC excitation, and probe calibration.
- [CTDizzle](https://github.com/IanTBlack/CTDizzle) - Arduino-based open CTD with practical guidance on probe construction, waterproofing, logging, calibration, and deployment.
- [OpenCTD](https://github.com/OceanographyforEveryone/OpenCTD) - Open hardware and software CTD with extensive construction, calibration, and field-use documentation.
- [OpenCTD research paper](https://tos.org/oceanography/article/the-openctd-a-low-cost-open-source-ctd-for-collecting-baseline-oceanographic-data-in-coastal-waters) - Background on the OpenCTD architecture and field objectives.
- [Open-source four-pole EC/CTD validation study](https://research.fs.usda.gov/treesearch/66053) - Useful comparison of four-electrode conductivity measurement, calibration, temperature effects, and validation against a commercial instrument.
- [Cost-efficient oceanographic CTD study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11207868/) - Useful reference for pressure housings, sensor integration, and deeper-water design constraints.
These references describe design provenance; the Cuttlefish/ROV implementation may include further electrical, mechanical, firmware, and packaging modifications. Licence obligations should be reviewed before redistributing any derived design files.




