# ZeroBot Raspberry Pi Zero FPV robot research notes

The Hackaday.io **ZeroBot** is a compact Raspberry Pi Zero W-based, browser-controlled FPV robot by Max.K. It is a useful reference for small terrestrial robots, particularly the relationship between onboard computing, browser-based operator control, video, telemetry, motor control, power management, and compact 3D-printed mechanical packaging. The project began in 2017 and evolved into a ZeroBot Pro revision with battery monitoring, headlights, camera controls, and safe shutdown. citeturn0view0

This is comparative research and design inspiration, not a specification or project dependency.

## Architecture

ZeroBot deliberately keeps the architecture simple:

- Raspberry Pi Zero W provides the main compute, Wi-Fi, camera interface, and GPIO;
- dual DC gearmotors provide differential drive;
- a dual-channel H-bridge provides motor control;
- the Pi hosts the browser-facing user interface;
- Node.js and Socket.IO provide the control/telemetry communication path; and
- the camera provides a low-latency MJPEG video stream.

The author initially considered adding an Arduino for motor-controller communication but rejected it in favour of direct Raspberry Pi GPIO control through Node.js. The project therefore provides a useful counter-example to the dedicated-MCU boundary being considered for the larger Robots ecosystem: it is appropriate to ask whether a given small robot actually needs another controller, rather than adding one automatically. citeturn0view0

## Cockpit and operator interface

The most relevant aspect for Cockpit is the idea of making the browser interface the robot's primary operator surface. The original interface combines the live camera view with an analogue joystick, with speed/direction commands sent to the robot and basic telemetry returned to the browser. The later Pro interface adds camera capture, headlights, battery-voltage display, and safe shutdown. citeturn0view0

Useful lessons include:

- video and control can be presented as one coherent operator experience;
- telemetry should be presented as useful vehicle state rather than merely exposing raw GPIO information;
- control interfaces should work across different screen sizes;
- robot-specific functions such as lights and photographs can be exposed as explicit capabilities; and
- safe shutdown is worth treating as a first-class operator function on a Linux-based vehicle.

This is conceptually close to the intended Cockpit direction, although Cockpit should retain the stronger separation between operator UI, vehicle control, communications, and logging.

## Communications and networking

ZeroBot originally used the Pi's Wi-Fi connection and a browser connection to a Node.js application. The project also documents configuring the Pi as its own wireless access point, allowing a phone or computer to connect directly to the robot without an external router. citeturn0view0

This is useful inspiration for future vehicle bring-up and field operation. In particular, a robot should be able to provide a predictable local control path when normal infrastructure is unavailable.

It is not a reason to replace the existing NATS architecture. A useful comparison is:

**Browser → Cockpit → NATS → Control → hardware**

versus ZeroBot's much simpler browser → Node.js → GPIO path.

## Video and latency

The project reports approximately 0.2–0.3 s latency for a 640 × 480 MJPEG stream in its original implementation. The author selected the Pi Zero W specifically because it provided enough processing power and I/O for camera-equipped robotics while remaining small and inexpensive. citeturn0view0

The exact video stack is now dated, but the engineering question remains relevant: measure end-to-end operator-to-camera latency rather than assuming that a nominally fast video transport produces a responsive vehicle.

This should inform future Cockpit video testing, particularly for manual driving and ROV operation.

## Power and vehicle state

The ZeroBot Pro revision moved to two 2,600 mAh cells in parallel, with boost converters providing 5 V for the Pi and an optional 6 V motor supply. An ADS1115 ADC was added for battery-voltage measurement. The project also added a controlled shutdown function intended to prevent filesystem corruption. citeturn0view0

Useful lessons for the Robots ecosystem include:

- measure vehicle supply voltage locally;
- expose power state to the operator;
- distinguish motor power from compute power where appropriate; and
- provide a deliberate shutdown path for Linux computers rather than simply removing power.

The exact power architecture is not suitable as a generic design recommendation, particularly for larger vehicles.

## Mechanical and serviceability lessons

The robot uses a compact 3D-printed shell and wheels, with flexible filament used for tyre surfaces. The original build deliberately minimised fasteners, with the two shell halves held together by four screws while many internal components were glued into the housing. The later revision also optimised the printed parts for easier assembly. citeturn0view0

This is useful for SwarmBot-scale hardware, but the permanent adhesive approach should be treated as a trade-off rather than copied. For maintainable engineering hardware, access to batteries, connectors, motor drivers, storage, and controller boards should be considered explicitly.

## Relevance to the Robots ecosystem

### SwarmBot

ZeroBot is particularly relevant as a compact educational/mobile-robot reference. Its low component count, browser interface, camera feedback, and 3D-printed construction demonstrate how much functionality can be delivered by a small Raspberry Pi platform.

Potential ideas include:

- browser-based driving and programming feedback;
- integrated video for classroom demonstrations;
- local Wi-Fi operation without infrastructure;
- simple battery telemetry;
- explicit lighting/capability controls; and
- a compact, serviceable printed chassis.

### MarsBot

The main value is as a small terrestrial prototype for operator-interface and video experiments. It is not a mechanical reference for a Mars-style rover chassis.

### ROV

The direct browser/video-control approach is a useful historical comparison for ROV Cockpit, particularly around latency, control feedback, and local networking. The project's simplicity should not be mistaken for suitability for an underwater vehicle where safety, communications resilience, actuator isolation, and logging have greater importance.

### K-9

The compact Raspberry Pi + motor-driver + camera pattern may also be relevant to K-9 prototyping, especially for early experiments where the objective is simply to prove drive, video, and remote-control behaviour.

## Engineering/process lessons

The project is also valuable because it documents evolution rather than presenting only a final design. The author built a prototype, refined the mechanical packaging, then added practical features such as voltage measurement, headlights, camera capture, and safe shutdown. citeturn0view0

This supports a useful project principle: establish a minimum working vehicle first, then add capabilities that address observed operational needs.

The project also illustrates a recurring robotics trade-off:

> fewer processing layers can make a very small robot easier to build, but a stronger architectural separation becomes valuable as vehicle complexity, safety requirements, and reuse increase.

## Design cautions

The software stack is based on an older Raspberry Pi OS/Node.js ecosystem. Later community discussion records compatibility problems with newer Raspberry Pi Zero 2 W hardware, camera software, Bullseye, and some Node/npm dependencies. citeturn0view0

Therefore:

- use the project primarily for architecture and UX inspiration;
- do not assume its supplied SD-card image remains suitable for current Raspberry Pi hardware;
- do not copy its old camera or Node.js stack into a new project without reassessment; and
- treat its direct GPIO motor control as appropriate only where the system-level safety requirements permit it.

## Sources

- [Hackaday.io — ZeroBot: Raspberry Pi Zero FPV Robot](https://hackaday.io/project/25092-zerobot-raspberry-pi-zero-fpv-robot/)
- [ZeroBot GitHub repository](https://github.com/CoretechR/ZeroBot)
- [Thingiverse ZeroBot designs](https://www.thingiverse.com/thing:2800717)

**Status:** Research / design inspiration. No ZeroBot software or hardware dependency is planned.

**Read later:** Review the ZeroBot source repository and mechanical files, particularly the browser control/video implementation, power telemetry, and compact chassis/serviceability decisions.
