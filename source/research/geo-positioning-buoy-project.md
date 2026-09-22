---
title: "Geo-Positioning Buoy Project reference"
description: "Reference notes on a small GPS/Bluetooth-controlled surface buoy and its mechanical construction."
date: 2026-09-22
tags:
  - research
  - buoy
  - surface-vehicle
  - gps
  - bluetooth
  - mechanical-design
status: reference
authority: Chartroom
---

# Geo-Positioning Buoy Project reference

## Scope

This page records reference information from the supplied *Geo-Positioning Buoy Project*, version 10.0, August 2025. The document describes the Chester Springs Model Yacht Club's Geo-Positioning Buoy (GPB), developed with Baker Creations, LLC, and is relevant as a small surface-buoy and mechanical-integration reference.

It is not a Chartroom design, implementation authority, bill of materials, safety case, or validated basis for an underwater or environmental buoy.

## System concept

The GPB is a small surface buoy intended to be placed from shore and controlled using a phone or tablet over Bluetooth Low Energy. The document describes waypoint and heading commands, an anchor-drop mechanism, and a fleet arrangement with a main hub buoy and secondary spoke buoys. It also describes an optional radio-control transmitter and receiver, but states that this mode cannot be used with the fleet solution.

The buoy uses a 3D-printed hull, lid, and flag components; two thrusters; electronic speed controllers; a control board; battery; and Bluetooth and GPS antennas. The document says that the electronics package came from Baker Creations and that hull parts were available from Autotiv Manufacturing.

The fleet arrangement is described as supporting a hub and up to five spoke buoys, with spoke buoys up to 185 m from the hub. These are claims made by the supplied project document, not independently verified Chartroom performance figures.

## Mechanical design references

The document provides examples of:

- ballast distributed into four hull compartments and encapsulated with epoxy;
- a removable bottom keel plug using a stainless screw, washers, rubber seal, and brass heat-set insert;
- port and starboard thruster placement, with clockwise and counter-clockwise propellers;
- thruster wire penetrations sealed with foam, O-rings, and sealant;
- a lid gasket seated in a machined or printed groove;
- a closed-cell foam rub rail for protection and additional stability;
- a removable or optional weighted keel; and
- a mast and colour-coded flag system for fleet identification.

These details are useful as design prompts for buoyancy, stability, sealing, service access, cable routing, and identification. They must not be copied into a project build without checking material compatibility, pressure and load cases, corrosion, battery safety, watertightness, and test evidence.

## Electronics and assembly lessons

The manual places the control board above the ballast, keeps the Bluetooth antenna vertical and away from metal, and warns against touching the GPS patch antenna because of the receiver's sensitive RF pre-amplifier. It recommends verifying thruster direction and port/starboard assignment before permanently joining the motor and ESC wires.

The described assembly sequence includes temporary wire connections, functional testing, solder-seal connectors, cable management, battery retention, and a final check of the control-board orientation. This is a useful example of separating provisional wiring checks from permanent sealing and installation.

## Power and fabrication references

The document describes a minimum operating voltage of 8.4 V for the thrusters and discusses 2S LiPo, LiFe, and NiMH battery options. It gives 5,000 mAh as a suggested minimum LiPo capacity for at least four hours of continuous use. Those figures are source-specific and must not be treated as a requirement without checking the actual controller, thrusters, battery protection, charging method, and measured load.

The documented print example uses PETG, a 0.4 mm nozzle, 0.2 mm layers, 100% infill, and a 300 mm × 300 mm × 130 mm minimum heated-bed volume. These are the authors' print settings, not a general Chartroom manufacturing standard.

## Relevance to Chartroom

The GPB is most useful as a comparative reference for:

- small surface-vehicle buoyancy and stability;
- modular hull and electronics integration;
- thruster sealing and service access;
- GPS and radio antenna placement;
- fleet identification and waypoint operations; and
- the relationship between mechanical assembly instructions and commissioning checks.

It should remain separate from the Smart Buoy environmental-sensing concept. The GPB is a model-yacht positioning platform, and its Bluetooth control, battery, thruster, hull, and operating assumptions do not establish suitability for environmental sensing, long-duration deployment, seawater, or underwater use.

## Provenance

- Source: user-supplied [csmyc-geo-positioning-buoy-project-v10.pdf](evidence/csmyc-geo-positioning-buoy-project-v10.pdf).
- Source title: *CSMYC Geo-Positioning Buoy Project*.
- Version/date shown in the PDF: version 10.0, August 2025.
- Organisation named in the PDF: Chester Springs Model Yacht Club.
- Contributors named in the PDF: Dave Baker, Jim Freeze, Tim Good, Steve LaBrenz, and John Stoudt.
- Related organisations named in the PDF: Baker Creations, LLC, and Autotiv Manufacturing.
- Source pages reviewed: PDF pages 1–23.
- Status: reference only; source copyright and publication permissions have not been assessed.
