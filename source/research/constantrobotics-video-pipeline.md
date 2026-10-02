---
title: "ConstantRobotics — Video Pipeline and Low-Latency Research"
description: "Research into ConstantRobotics and RapidPixel video-capture, processing, encoding, streaming, tracking, recording, and Raspberry Pi examples relevant to the ROV."
type: research
status: research candidate
authority: Chartroom
tags:
  - research
  - video
  - latency
  - raspberry-pi
  - teleoperation
  - computer-vision
  - ROV
---

# ConstantRobotics — Video Pipeline and Low-Latency Research

## Summary

ConstantRobotics and its RapidPixel SDK provide useful reference implementations for real-time video capture, processing, hardware encoding, streaming, tracking, and recording. The material is relevant to the ROV video path because it exposes several of the individual stages that contribute to end-to-end latency.

This is **reference material**, not a proposal to adopt ConstantRobotics software. The commercial libraries should be treated as examples against which the project video architecture and measurements can be compared.

## Video capture

### VSourceLibCamera

[VSourceLibCamera](https://rapidpixel.constantrobotics.com/docs/VideoSource/VSourceLibCamera.html) provides C++ video capture and camera control through libcamera. It supports automatic selection of supported resolution, format, and FPS, with explicit configuration available.

### VSourceV4L2

[VSourceV4L2](https://rapidpixel.constantrobotics.com/docs/VideoSource/VSourceV4L2.html) provides V4L2 capture and control. Its current documentation explicitly describes a minimum-latency capture policy that delivers the newest captured frame and drops outdated frames.

That behaviour is particularly relevant to teleoperation: a delayed frame can be less useful than a dropped frame when the operator needs the current view.

**Research point:** compare a latest-frame policy against queueing behaviour in the ROV video path and measure the effect on glass-to-glass latency and motion smoothness.

## Hardware video coding

### VCodecV4L2

[VCodecV4L2](https://rapidpixel.constantrobotics.com/docs/VideoCoding/VCodecV4L2.html) provides Linux hardware H.264, HEVC, and JPEG encoding/decoding through V4L2. The current documentation reports testing on Raspberry Pi 4B, Raspberry Pi Zero 2W, and NVIDIA Jetson platforms.

The low-latency details are particularly useful. The implementation explicitly disables H.264/HEVC B-frames and, for H.264, can patch SPS VUI parameters to prevent unnecessary frame reordering in receivers. The documentation notes that some receivers can otherwise add approximately two frame periods of decoder buffering.

Published Raspberry Pi 4B encoding figures at 30 FPS and 3,000 kbps are approximately:

| Codec | 1,920 × 1,080 | 1,280 × 720 | 640 × 480 |
|---|---:|---:|---:|
| H.264 | 20.2 ms | 13.4 ms | 5.2 ms |
| HEVC | 24.9 ms | 10.5 ms | 3.7 ms |
| JPEG | 30.1 ms | 12.4 ms | 4.1 ms |

These are vendor-published benchmark figures, not measurements of project hardware or the complete video path.

**Research point:** measure capture → encode → transport → decode separately where practical, then compare the measured sum against GTG-1 glass-to-glass measurements.

## Streaming

### RtpPusher

[RtpPusher](https://www.constantrobotics.com/online-store/p/rtppusher) is a C++ library for H.264, H.265, and JPEG over UDP using RTP, with additional MPEG-TS transport modes and optional KLV metadata support. It is useful as a reference for packetisation and back-pressure behaviour, including a documented drop-oldest-frame strategy.

**Research point:** compare dropping old frames with the ROV requirement for current video rather than guaranteed delivery of every frame.

### VStreamerMediaMtx

[VStreamerMediaMtx](https://rapidpixel.constantrobotics.com/docs/VideoStreaming/VStreamerMediaMtx.html) provides a video-streaming interface around MediaMTX. The current documentation lists RTSP, WebRTC, HLS, RTMP, and SRT support.

This is useful for comparing transport choices and their latency/reliability trade-offs. It is not evidence that any particular transport should be selected for the ROV.

### MServer

[MServer](https://rapidpixel.constantrobotics.com/docs/VideoStreaming/MServer.html) supports RTSP, RTSPS, RTP, SRTP, UDP multicast, direct RTP push, and WebRTC, with H.264, H.265, and MJPEG. Its explicit no-B-frame design is another useful reference for avoiding decoder reordering.

## Raspberry Pi pipeline examples

### RpiStreamer

[RpiStreamer](https://www.constantrobotics.com/rpistreamer) is a Raspberry Pi 4B application that captures video, stabilises it, hardware-encodes it, and passes it to streaming frameworks including FFmpeg, GStreamer, and v4l2rtspserver.

It combines VSourceV4L2, VStabiliserOpenCv, VCodecV4L2, VOutputV4L2, and ChildProcess. This makes it useful as a concrete example of decomposing a Raspberry Pi video pipeline into replaceable stages.

### Zero2WFpv

[Zero2WFpv](https://rapidpixel.constantrobotics.com/docs/ExamplesTemplates/Zero2WFpv.html) targets Raspberry Pi 5 and Raspberry Pi Zero 2W and combines camera capture, tracking, format conversion, encoding, RTP output, and flight-control communications. The current documentation describes it as a software prototype/research example.

For the ROV project, the value is architectural: it demonstrates a complete low-power onboard video pipeline. The FPV flight-control interfaces are not relevant to the ROV.

## Tracking and perception

### CvTracker

[CvTracker](https://www.constantrobotics.com/online-store/p/correlation-video-tracker-lib) is a C++ object-tracking library intended for small or low-contrast objects and complex backgrounds. ConstantRobotics publishes benchmark results for Raspberry Pi Zero 2W, Pi 4B, Pi 5, Jetson, and other platforms.

For a 256 × 256 search window, published Raspberry Pi figures include approximately:

| Platform | Daylight | Thermal |
|---|---:|---:|
| Raspberry Pi Zero 2W | 18.7 ms/frame | 14.5 ms/frame |
| Raspberry Pi 4B | 8.16 ms/frame | 5.1 ms/frame |
| Raspberry Pi 5 | 2.76 ms/frame | 2.0 ms/frame |

These are vendor benchmarks. The daylight/thermal classification should not be interpreted as evidence that the algorithm is suitable for underwater imagery.

**Research point:** if visual target tracking becomes a requirement, test representative underwater imagery rather than extrapolating from these benchmarks.

## Image enhancement

### Dehazer and Denoiser

[Dehazer](https://rapidpixel.constantrobotics.com/docs/VideoFiltering/Dehazer.html) implements local contrast/dehazing algorithms, including CLAHE-derived approaches, with x86 SIMD and AArch64 NEON paths. RapidPixel also provides a [Denoiser](https://rapidpixel.constantrobotics.com/) filter for noise reduction.

These are interesting for underwater imaging, but atmospheric haze is not equivalent to underwater scattering, absorption, colour attenuation, and backscatter. Both should therefore remain research candidates until tested on representative underwater footage.

**Research point:** measure image quality and processing latency together; an enhancement that increases noise or operator-video latency may be counterproductive.

## Recording

### VideoRecorderMp4

[VideoRecorderMp4](https://rapidpixel.constantrobotics.com/docs/Service/VideoRecorderMp4.html) records H.264, H.265/HEVC, and MJPEG into MP4 files, with file/folder-size controls.

This is relevant to recording test evidence and operator footage. The architectural question is whether recording can consume the encoded stream without adding buffering to the live operator path. A slow storage device should not be allowed to increase control-relevant display latency.

**Research point:** test recording as a separate consumer of the encoded stream, with bounded buffering and explicit behaviour when storage cannot keep up.

## Reference pipeline

The ConstantRobotics material provides a useful conceptual pipeline:

Camera → capture → optional processing → hardware encode → transport → decode → display

with additional consumers such as recording and perception.

For the ROV, keep three concerns measurable and independently testable:

1. **Live operator video path** — optimise for current information and bounded latency.
2. **Recording path** — optimise for complete evidence without blocking the live path.
3. **Perception path** — optimise for useful machine vision without silently increasing operator-video latency.

Together with the [GTG-1 research note](gtg-1-glass-to-glass-latency.md), this provides a basis for building an empirical video-latency budget.

## What this research does not establish

This research does **not** establish a ConstantRobotics software dependency, selected camera, codec, streaming protocol, Raspberry Pi model, onboard tracking requirement, dehazing/denoising requirement, or target glass-to-glass latency.

Those decisions require project-specific requirements and measurements.

## Status

**Research candidate.**

The material is useful for designing experiments and identifying where video latency can be introduced. The next step is to build a measured ROV video-latency budget using representative hardware and the GTG-1 method, then compare it with individual subsystem measurements.

## Sources

- [ConstantRobotics — RpiStreamer](https://www.constantrobotics.com/rpistreamer)
- [RapidPixel — VSourceLibCamera](https://rapidpixel.constantrobotics.com/docs/VideoSource/VSourceLibCamera.html)
- [RapidPixel — VSourceV4L2](https://rapidpixel.constantrobotics.com/docs/VideoSource/VSourceV4L2.html)
- [RapidPixel — VCodecV4L2](https://rapidpixel.constantrobotics.com/docs/VideoCoding/VCodecV4L2.html)
- [ConstantRobotics — RtpPusher](https://www.constantrobotics.com/online-store/p/rtppusher)
- [RapidPixel — VStreamerMediaMtx](https://rapidpixel.constantrobotics.com/docs/VideoStreaming/VStreamerMediaMtx.html)
- [RapidPixel — MServer](https://rapidpixel.constantrobotics.com/docs/VideoStreaming/MServer.html)
- [RapidPixel — Zero2WFpv](https://rapidpixel.constantrobotics.com/docs/ExamplesTemplates/Zero2WFpv.html)
- [ConstantRobotics — CvTracker](https://www.constantrobotics.com/online-store/p/correlation-video-tracker-lib)
- [RapidPixel — Dehazer](https://rapidpixel.constantrobotics.com/docs/VideoFiltering/Dehazer.html)
- [RapidPixel — VideoRecorderMp4](https://rapidpixel.constantrobotics.com/docs/Service/VideoRecorderMp4.html)
- [RapidPixel — SDK documentation](https://rapidpixel.constantrobotics.com/)