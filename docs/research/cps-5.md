# CPS 5 underwater drone research notes

The **CPS 5** (Custom Printed Submarine) is a useful ROV reference because it combines a compact 3D-printable vehicle, structured build documentation, a tether, enclosed electronics, camera integration, and an explicit progression through multiple prototypes. The current CPS material describes a vehicle approximately 230 × 384 × 102 mm, with five motors, self-stabilisation/depth-hold features, 1080p live video, and a tethered architecture. citeturn1search1

## Why it is relevant

CPS 5 is particularly relevant to the ROV project as a **buildability and documentation reference**. The project has been iterated through many prototypes and presents the vehicle as a modular platform that can be modified after the initial build. citeturn1search1turn1search3

The current course structure covers:

- frame;
- endcaps;
- camera;
- external components;
- tether;
- electronics pipe; and
- vehicle operation.

That is a useful documentation pattern because it follows the physical integration sequence rather than presenting the vehicle only as a finished assembly.

## Design lessons

- Design for straightforward manufacture and replacement.
- Keep the camera, tether, electronics, and external hardware as explicit subsystems.
- Make the BOM and CAD files part of the project documentation.
- Use prototype iteration to discover mechanical and operational problems before attempting a final design.
- Treat custom modules and upgrades as extensions of a stable core vehicle.

## ROV architecture

The compact tethered architecture is a useful comparison with the existing ROV design. It reinforces the value of a simple, reliable physical communications path for an underwater vehicle, while leaving higher-level operator software and vehicle control as separate concerns.

The CPS 5 also demonstrates that a small vehicle can provide useful stabilisation and depth-hold behaviour without becoming mechanically complex. These functions remain candidates for the existing Control architecture rather than Cockpit itself.

## Caveats

CPS 5 is a maker/educational platform and should not be treated as a certified pressure-vessel, tether, propulsion, or safety specification. Published performance figures are project claims and require independent validation before being used as engineering requirements. The commercial course and associated material should also be distinguished from an independently reproducible open-source engineering baseline.

## Sources

- [Instructables — Overview of the CPS 5 Underwater Drone](https://www.instructables.com/Overview-of-the-CPS-5-Underwater-Drone/)
- [CPSdrone — CPS 5 Course](https://www.cpsdrone.com/cps-5-course/)
- [CPSdrone — Underwater drone building course](https://www.cpsdrone.com/articles-cpsdrone/underwater-drone-building-course-cps-5-course/)

**Status:** Research / design inspiration.

**Read later:** Review the CPS 5 CAD/BOM structure, tether implementation, electronics-pipe arrangement, camera integration, and documentation workflow.
