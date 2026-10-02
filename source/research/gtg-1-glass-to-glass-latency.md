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

ConstantRobotics' GTG-1 is a dedicated instrument for measuring **glass-to-glass latency** in camera systems. It places a pulsed light source in front of the camera and a light sensor against the display showing the camera feed. The instrument reports minimum, maximum, average, and instantaneous latency with 1 ms resolution, with measurements up to 999 ms. citeturn0search0

This is relevant to the robot video system because it provides a practical way to measure the latency experienced by an operator rather than relying on individual camera, encoder, network, decoder, or display specifications.

## Relevance to robotics

Glass-to-glass measurement covers the complete video path from light entering the camera to light being emitted by the operator display. ConstantRobotics describes the method as covering optics, ISP, encoding, transport, decoding, and rendering. citeturn0search3

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

The same underlying principle can be implemented without a dedicated GTG-1. ConstantRobotics describes the conventional approach as putting a 1 ms-resolution stopwatch in front of the camera, displaying the camera image on a monitor, and photographing both the real stopwatch and its displayed image in the same frame. The difference gives an estimate of glass-to-glass latency. citeturn0search8

The dedicated instrument is therefore interesting both as a possible test tool and as a reference design for developing a lower-cost in-house test fixture.

## Source

ConstantRobotics — GTG-1:

urlGTG-1 product pagehttps://www.constantrobotics.com/gtg-1

Hackaday.io — GTG-1 project and measurement method:

urlGTG-1 project pagehttps://hackaday.io/project/204219-gtg-1-glass-to-glass-latency-meter

## Status

**Reference / research candidate.**

The GTG-1 is not currently specified as a project requirement or selected test instrument. Its measurement method should be considered when defining video-system validation and teleoperation latency testing.
