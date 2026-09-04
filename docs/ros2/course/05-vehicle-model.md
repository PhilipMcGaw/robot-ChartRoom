# Vehicle model and actuation

## Objective

Create the first ROV-like vehicle and establish a simple, measurable command-to-motion loop.

## First model

Start with a hull, thrusters, simple collision geometry, and basic dynamics. Favour repeatability over realism.

```text
command
  ↓
thruster model
  ↓
vehicle motion
```

Verify progressively:

```text
forward command → forward response
turn command → yaw response
dive command → depth response
```

Do not claim physical validity from a visually convincing simulation.

## Increasing realism

Only after the simple model is repeatable, consider realistic mass/inertia, centre of mass, centre of buoyancy, buoyancy, drag, thruster curves, and actuator dynamics.

Simulated vehicles belong to SquidLink under its ROS 2 workspace; this lesson explains the engineering concepts rather than owning the implementation.

## Exit criteria

- [ ] Vehicle loads reliably.
- [ ] Thruster commands can be applied in ROS 2.
- [ ] Forward, turning, and vertical responses are measurable.
- [ ] Vehicle parameters are identified as justified values or placeholders.
- [ ] The model is ready for sensor integration.
