# 3D-printed tank takes on the elements

## Source

- [Hackaday: 3D Printed Tank Takes On The Elements](https://hackaday.com/2021/05/16/3d-printed-tank-takes-on-the-elements/)

## Summary

The 2021 Hackaday article describes a home-built tracked RC tank designed and printed by Let's Print and tested outdoors in mud and snow.

The propulsion system uses two brushed motors with two speed controllers and conventional RC hardware. The bespoke mechanical system includes 3D-printed gearboxes, chassis components, and tracks. The tracks were printed in PETG and reportedly required more than 80 hours of printing alone.

The build demonstrated that the printed tracked system could operate outdoors, although the vehicle could become high-centred in deep snow. The aggressive track teeth produced substantial traction and left deep impressions in mud.

## Relevance to SwarmBot and MarsBot

The most useful aspect is not the particular tank design, but the **rapid, low-cost mechanical experimentation** it demonstrates.

Potential lessons for SwarmBot include:

- 3D-printed drive modules can be practical for early terrestrial prototypes;
- tracked propulsion is worth keeping as an experimental option where terrain rather than efficiency is the priority;
- bespoke gearboxes can remove dependence on proprietary mechanical assemblies during prototyping;
- outdoor testing should expose failure modes that indoor floor testing will not reveal; and
- track geometry, ground clearance, and terrain interaction need to be evaluated together rather than optimising traction in isolation.

For MarsBot, the article is a useful counterpoint to the more sophisticated JPL Open Source Rover and Sawppy references. A small tracked platform could provide a relatively simple way to investigate rough-terrain mobility before committing to a larger six-wheel rocker-bogie design.

## Engineering/process lesson

The reported 80+ hour print time for the tracks is an important reminder that **prototype geometry and manufacturing time are part of the engineering trade-off**. A mechanically elegant printed design may be impractical if replacement parts are slow to manufacture.

For the Robots ecosystem, this supports designing wear components, tracks, wheels, brackets, and sensor mounts as replaceable modules, with consideration given to print time, material consumption, field replacement, and availability of non-printed alternatives.

## Limitations

This is a hobbyist build report rather than a validated vehicle-development programme. There are no useful quantitative durability, traction, motor-efficiency, ingress-protection, or environmental qualification data in the article.

It should therefore be treated as design inspiration and evidence that the concept is feasible, not as a specification for SwarmBot or MarsBot.

## Status

**Research / mechanical design inspiration.** No tank drivetrain or tracked chassis dependency is planned.
