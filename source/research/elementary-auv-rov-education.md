---
title: "Elementary AUV and ROV education reference"
description: "English synthesis of Russian ElementaryAUV and ElementaryROV teaching material for underwater robotics education."
date: 2026-09-22
tags:
  - research
  - underwater
  - rov
  - education
  - control
  - sensors
status: reference
authority: Chartroom
---

# Elementary AUV and ROV education reference

## Scope and translation method

This page is an English synthesis of user-supplied Russian teaching material for the ElementaryAUV and ElementaryROV platforms. It translates and preserves the useful technical, safety, curriculum, and assessment information without reproducing the complete third-party course pack.

The material is relevant to underwater-robotics education, mission-based learning, and the planned Test in a Box and ROV teaching work. It is not a Chartroom implementation authority, project requirement, safety case, or validation of the Robots project's physical hardware.

## ElementaryAUV platform

The supplied 2022 operating manual describes ElementaryAUV as an autonomous or remotely controlled educational underwater vehicle for demonstration, teaching, and competitions. The documented kit contains four thrusters, an electronics block with battery and sensors, a hull, antenna, charger, and wireless-charging adapter. The named payload and sensing functions include a laser sensor, electromagnet, and navigation-and-attitude sensor.

The vehicle is controlled through an Android application. The application provides device connection, remote control, projects, telemetry, and a visual programming environment. The left control stick drives the horizontal thrusters A and B; the right stick drives the vertical thrusters C and D. The application can display sensor and power information and can import and export projects.

## Safety and operating guidance

The source manual requires adult supervision for users under 18. It specifically states that operators must:

- keep hands away from propellers while the vehicle is powered;
- keep cables and foreign objects away from the thrusters;
- never charge the vehicle while it is in water;
- inspect cables, insulation, thruster connections, and battery state before use;
- start and test the vehicle on a level surface before entering the water;
- avoid dropping, striking, or strongly vibrating the vehicle;
- avoid temperatures above 40 °C and hot water;
- avoid opening or closing covers while the vehicle is on the water; and
- rinse thrusters with fresh water after salt-water use and remove trapped debris.

The manual says that waterproofing can be compromised by mechanical or thermal damage. These are source-manual operating instructions, not a substitute for a project-specific risk assessment, electrical isolation procedure, pool rules, emergency plan, or equipment inspection record.

The electromagnet has a maximum continuous-on time of two minutes and enters a cooling period after operation. This limit should be preserved in any exercise or software abstraction that uses the magnet.

## ElementaryAUV programming model

The supplied block reference documents the following groups.

### Movement and actuation

- Set movement on an axis, with paired-thruster control from −100 to 100 for forward/reverse, turning, and ascent/descent.
- Set thrust on an individual thruster A, B, C, or D, also from −100 to 100.
- Set and hold a heading, either relative to the initial heading or relative to the last commanded heading.
- Reset previously commanded thrusters.
- Switch the electromagnet on or off, subject to the two-minute operating limit.

### Sensors and conditions

- Wait for one or two impacts.
- Wait for a light or dark reading from the laser sensor.
- Detect an impact or colour/light condition without blocking.
- Read heading, pitch, or roll from the navigation-and-attitude sensor.
- Use `if`, `if/else`, comparisons, AND, OR, NOT, and conditional selection.

### Loops and data

- Wait for a time, read elapsed seconds, and run parallel processes.
- Use infinite, timed, counted, `for i`, and conditional loops.
- Break a loop or continue with the next iteration.
- Perform arithmetic, test number properties, take an absolute or opposite value, clamp a value, generate a random number, and normalise an angle from 0–360° to −180–180°.
- Control individual or all LEDs, choose named colours, generate random colours, and construct colours from red, green, and blue values.
- Create, assign, increment, and read variables.
- Create functions and functions that return values.

This is a useful compact capability model for an educational underwater-robot interface. Any Chartroom implementation should define its own safe command set, bounds, neutral behaviour, timeout handling, and authority boundaries rather than copying the vendor block names directly.

## Translated course sequence

The main course is presented as a one-year visual-programming module for school pupils. Competition-style “mission” lessons are used as formative assessment, although the source also permits tests, quizzes, and other assessment methods.

| Lessons | English topic | Main learning focus |
|---:|---|---|
| 1 | Introduction and remote control | Vehicle construction, remote control, moving objects, and the magnet |
| 2 | Basic movement with paired thrusters | Forward, reverse, turning, ascent, waiting, and simple trajectories |
| 3 | Independent thruster control: forward and reverse | Individual thrusters, impact wait, and straight-line races |
| 4 | Independent thruster control: turning | Single- and two-thruster turns and complex paths |
| 5 | Independent thruster control: ascent and descent | Vertical thrusters, parallel processes, and tilt observation |
| 6 | Robot dance mission | Combining movement blocks and LED control |
| 7 | LEDs, algorithms, and loops | Linear algorithms, loops, branching, and Morse-code signalling |
| 8 | Mathematics and branching | Arithmetic, display output, parity, and conditional algorithms |
| 9 | Variables | Store data, use an index loop, and vary LED or thruster output |
| 10 | Random numbers | Random values, random colours, and loop interruption |
| 11 | Electromagnet | Magnetic pickup, delivery tasks, and functions |
| 12 | Laser sensor | Light/dark detection, stopping on a line, and functions |
| 13–14 | Zebra mission | Count dark lines and choose actions from the count |
| 15 | Navigation-and-attitude sensor | Read heading, pitch, and roll and use heading turns |
| 16 | Heading control and complex movement | Set heading, heading turns, and impact-triggered operation |
| 17 | Two-vehicle relay | Coordinate two vehicles in a shared tank |
| 18–19 | Treasure mission | Plan, test functions, use parallel processes, and complete a mission |
| 20 | Boolean logic | AND, OR, and NOT |
| 21–22 | Impact counting | Count impacts, display the count, and change direction after impact |
| 23 | Line relay controller | Follow a dark line with a relay controller and timed stopping |
| 24 | Two-vehicle detection | Detect another vehicle with the laser sensor |
| 25–26 | Transporter mission | Move objects using heading control and a custom payload |
| 27 | RGB colour model | Set colours using red, green, and blue components |
| 28 | Relay controller | Build a relay controller independently |
| 29 | Proportional controller | Build a heading proportional controller independently |

## ElementaryROV course material

The separate ElementaryROV material adds a build-and-competition pathway around an open-frame remotely operated vehicle. The lesson headings cover introduction, electrical assembly, controller assembly, controller and thruster operation, frame construction, pool models, payload design, ballast, pool debugging, firmware changes, training, competition, and reflection.

The most transferable points are:

- ballast should be adjusted towards neutral or slightly positive buoyancy for controllability and recovery;
- ballast can be changed using distributed fasteners or other weights rather than treating buoyancy as fixed;
- payload design should begin with the task and strategy, and simple hooks or protrusions may outperform complex mechanisms;
- reduce unnecessary ascent and descent because vertical manoeuvres consume time and energy;
- test and debug in a pool before competition use;
- use an explicit pilot and assistant role during demonstrations and missions; and
- end a course with structured reflection on what worked, what was difficult, and what should be redesigned.

One lesson describes flashing an Arduino Leonardo controller with an `ElementaryROV.ino` program from the project's public repository. That is a source-specific workflow and should be rechecked before use; it does not establish a Chartroom firmware dependency.

## Relevance to Chartroom

This material is most useful in four places:

1. **ROV education:** staged progression from teleoperation to sensor-based control, closed-loop heading, payloads, and missions.
2. **Test in a Box:** a candidate structure for lessons that move from simulation or dry testing to controlled physical exercises.
3. **Safety and commissioning:** reminders to separate dry checks, water tests, battery charging, propeller safety, buoyancy, and post-salt-water maintenance.
4. **Control abstraction:** a compact example of bounded movement, sensor events, variables, functions, heading normalisation, relay control, and proportional control.

The material does not prove that the current ROV, SwarmBot, NATS, ROS 2, HiL/SiL, or Testbot systems implement these capabilities. Physical validation must remain tied to the project's own hardware, software, test evidence, and safety records.

## Provenance and limitations

- Sources: user-supplied Russian course and operating material for ElementaryAUV and ElementaryROV.
- Named ElementaryAUV manufacturer in the operating manual: Centre of Robotics, Vladivostok.
- Source materials reviewed: ElementaryAUV course plan, 29 lesson documents, operating manual dated 2022, programming-block reference, and the ElementaryROV lesson and build material.
- This page is an English technical synthesis, not a certified translation or a replacement operating manual.
- Original source files were reviewed for relevance and are discarded from the workspace after this synthesis; source copyright and publication permissions were not assessed.
