---
title: "GTG-1 — Glass-to-Glass Video Latency Measurement"
description: "Research reference for measuring end-to-end camera-to-display latency in robotic video systems."
type: research
status: reference
authority: Chartroom
tags:
  - research
  - video
  - latency
  - camera
  - teleoperation
  - test-and-measurement
---

# GTG-1 — Glass-to-Glass Video Latency Measurement

## Summary

ConstantRobotics' GTG-1 is a dedicated instrument for measuring **glass-to-glass latency** in daylight camera systems. A light source is positioned in front of the camera and a light sensor is placed on the display showing the camera feed. The device reports minimum, maximum, average, and instantaneous latency with **1 ms resolution**, measuring up to **999 ms**. The manufacturer states that minimum, maximum, and average values are calculated over a 10 s measurement window, with light pulses generated at 1 s intervals. citeturn0search0

This is relevant to the robot video system because it provides a practical way to measure the latency experienced by an operator rather than relying on individual camera, encoder, network, decoder, or display specifications.

## Published hardware details

The manufacturer's current product page states:

| Parameter | Published detail |
|---|---|
| Measurement | Glass-to-glass video latency |
| Intended camera type | Daylight cameras |
| Resolution | 1 ms |
| Maximum measured latency | 999 ms |
| Reported values | Minimum, maximum, average, instantaneous |
| Measurement window | 10 s for minimum, maximum, and average |
| Pulse interval | 1 s |
| Dimensions | 90 × 70 × 20 mm |
| Weight | 555 g with case |
| Power | Battery not included |
| Package | Plastic case, device PCB, light-source cable, light-sensor cable, user manual |
| Warranty | 1 year |
| Sales model | B2B |
| Published price | €500 + shipping |

These are manufacturer's published figures and should not be treated as independently verified performance specifications. citeturn0search0

## Datasheet

The official product page provides a **Download datasheet** link. The linked PDF is:

urlGTG-1 product pagehttps://www.constantrobotics.com/gtg-1

urlGTG-1 datasheet — GTG-1_Datasheet_v100.pdfhttps://www.constantrobotics.com/s/GTG-1_Datasheet_v100.pdf

The datasheet should be retrieved and reviewed before treating the GTG-1's detailed electrical, measurement-accuracy, operating, or environmental characteristics as established.

## Relevance to robotics

Glass-to-glass measurement covers the complete video path from light entering the camera to light being emitted by the operator display. The GTG-1 method is therefore useful for assessing the actual end-to-end display latency rather than constructing a theoretical value from individual component specifications.

For teleoperation, this can be used as an acceptance-test measurement for the operator video path. It is particularly useful because the measured result includes interactions between components that may each have apparently acceptable latency when considered separately.

The measurement should not be treated as the complete robot control-loop latency. It does **not**, by itself, measure:

- operator input latency;
- command transport latency;
- actuator response;
- vehicle dynamics;
- sensor-processing latency that does not affect the displayed image;
- the time between an operator action and a resulting physical response.

A complete teleoperation latency budget therefore needs separate measurements for the command path and physical response.

## Possible ROV application

A useful test would be:

1. Place the GTG-1 light source in the field of view of an ROV camera.
2. Display the camera feed through the complete production video chain.
3. Place the GTG-1 light sensor on the operator display.
4. Record minimum, maximum, average, and instantaneous glass-to-glass latency.
5. Repeat with representative transport conditions and video settings.
6. Record the measured latency alongside resolution, frame rate, codec, transport protocol, and display configuration.

This would give the ROV project an empirical video-latency figure rather than an estimate assembled from component datasheets.

## Alternative / DIY method

The same underlying principle can be implemented without a dedicated GTG-1. ConstantRobotics describes the conventional approach as putting a 1 ms-resolution stopwatch in front of the camera, displaying the camera image on a monitor, and photographing both the real stopwatch and its displayed image in the same frame. The difference gives an estimate of glass-to-glass latency.

The dedicated instrument is therefore interesting both as a possible test tool and as a reference design for developing a lower-cost in-house test fixture.

## Status

**Reference / research candidate.**

The GTG-1 is not currently specified as a project requirement or selected test instrument. Its measurement method should be considered when defining video-system validation and teleoperation latency testing.

**TODO:** Retrieve and review the official GTG-1 datasheet, then update this note with any additional electrical, accuracy, environmental, operating, and measurement-method specifications that are not present on the product page.
