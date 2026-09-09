# Learn Robotics — Raspberry Pi Robot Video Streaming

## Source

- [Learn Robotics — Video Streaming Raspberry Pi Robot & Camera](https://www.learnrobotics.org/blog/video-streaming-raspberry-pi-robot-camera/)

## Summary

This tutorial is a useful historical reference for browser-based FPV on small Raspberry Pi robots. It uses a Raspberry Pi Zero W or Raspberry Pi 3 B+ with a Raspberry Pi camera and uses WebRTC to stream camera video to a web browser. The tutorial explicitly targets low-latency browser video and demonstrates operation across separate networks using a TURN server.

The project combines the browser operator interface, video stream, and robot control path through the RemoteMe platform. The article describes browser commands being sent through the same transmission channel used by the video-oriented application, with the goal of keeping perceived control latency low.

## Relevance to the Robots ecosystem

### Cockpit video architecture

The strongest relevance is the use of **WebRTC for low-latency browser video**. This supports keeping video as a distinct transport from the vehicle command and telemetry middleware. For our architecture, this reinforces the existing principle that Cockpit should receive video independently while NATS remains the vehicle middleware rather than carrying the video stream.

The tutorial also demonstrates that WebRTC can operate when the browser and robot are on different networks, with a TURN server providing connectivity through NAT where direct peer-to-peer connectivity is unavailable.

### Small-robot reference

The hardware is intentionally simple: Raspberry Pi, camera, motor controller, battery, and a small mobile chassis. It is therefore a useful SwarmBot/MarsBot reference for demonstrating a complete browser-operated robot without requiring a substantial onboard computer.

### Operator-interface progression

The project is structured as a staged progression:

1. establish Raspberry Pi camera streaming;
2. control a camera pan/tilt mechanism;
3. combine video, camera control, and vehicle driving.

That is a useful pattern for Cockpit development and testing: validate the video path independently before integrating it with vehicle control and higher-level UI functions.

### Remote connectivity

The use of TURN is relevant to future remote-operation scenarios, but it should not be treated as a requirement for the ROV. Local-network and tethered operation should remain valid without an external service. Any future Internet-accessible operation also needs explicit consideration of authentication, authorisation, safety, bandwidth, and failure behaviour.

## What we should take from it

- Keep video transport separate from NATS control/telemetry traffic.
- WebRTC is a strong candidate for low-latency browser video where the deployment requires it.
- Test the video path independently before coupling it to vehicle control.
- Treat NAT traversal and TURN as infrastructure concerns rather than vehicle-control dependencies.
- Preserve a local-network operating mode that does not require third-party cloud services.
- Consider browser-based camera pan/tilt as a reusable Cockpit capability.

## Caveats

The tutorial relies on the RemoteMe platform, so its end-to-end architecture should not be adopted directly. It is also aimed at a small educational robot rather than a safety-conscious ROV. The WebRTC transport concept is the useful reference; the RemoteMe control architecture is not a replacement for the project's NATS-based design.

## Read later

- [Learn Robotics — Video Streaming Raspberry Pi Robot & Camera](https://www.learnrobotics.org/blog/video-streaming-raspberry-pi-robot-camera/)
