---
title: "BlueOS and Blue Robotics Cockpit SITL Test"
description: "A hardware-free test plan for BlueOS, ArduSub SITL, and Blue Robotics Cockpit."
type: test-plan
status: planned
authority: Chartroom
tags:
  - testing
  - blueos
  - cockpit
  - ardupilot
---

# BlueOS and Blue Robotics Cockpit SITL Test

## Purpose

Try the BlueOS and Blue Robotics Cockpit operator workflow against a simulated ArduSub vehicle. Observe vehicle discovery, telemetry, connection recovery, and operator controls to inform our own ROV test cases and Cockpit requirements.

This is an upstream-stack evaluation. It does not connect CuttleOS Cockpit to BlueOS, prove compatibility with our NATS contract, or adopt MAVLink as a project interface. CuttleOS, SquidLink, and NautiPi retain their documented authority boundaries.

## Test environment

- Raspberry Pi 4 Model B with the fitted Adeept ADM133 Robot HAT revision recorded before installation.
- The available 64 GB SD card, reserved for this BlueOS trial after confirming that it contains no data to preserve.
- The latest stable BlueOS image listed for Raspberry Pi 4B (currently the ARMv7, 32-bit Bullseye image); verify the download options immediately before flashing.
- Blue Robotics Cockpit running on a separate topside computer or in a browser.
- Network access for first-boot setup and BlueOS updates.
- No ESCs, thrusters, vehicle, or other powered actuators connected during the initial BlueOS/Cockpit test.

BlueOS is headless and is managed through its web interface. Flashing the image erases the selected SD card. Keep an existing Pi system card intact and use the reserved card for this trial.

## Preconditions and safety

1. Confirm the Raspberry Pi model and HAT revision. Photograph the assembly and record the SD card identity before flashing.
2. Confirm that the 64 GB card is the selected trial card and contains no data that needs to be retained before flashing.
3. Leave ESCs, thrusters, and other actuators disconnected. The HAT is not a BlueOS-supported controller by default; do not assume its outputs are safe or configured.
4. After BlueOS boots, confirm that no physical flight controller is attached before selecting a simulated ArduSub board.
5. Keep SITL disarmed throughout this first test. Do not test arming, motor output, mission execution, or real propulsion.
6. Record the Pi model, HAT revision, image, BlueOS release, Cockpit release, date, and network arrangement.

Stop if the selected board or connection could refer to physical hardware, if the operator interface indicates an armed/active vehicle unexpectedly, or if the HAT revision/pin mapping is uncertain before any I/O test.

## Deployment and first boot

1. Download the current stable Raspberry Pi 4B image from the official [BlueOS installation page](https://blueos.cloud/docs/stable/usage/installation/). Verify that the image is the Pi 4B ARMv7 build.
2. Use Balena Etcher to flash the image to the reserved SD card, then insert it into the Pi and power on the Pi with the ADM133 HAT fitted.
3. Allow first boot to complete, then open the BlueOS web interface from the topside computer using the host name or IP address shown by the network.
4. Complete the first-boot setup, record the installed BlueOS version, and apply the latest suitable stable update.
5. Confirm BlueOS remains reachable after reboot and that its system-health view reports normally.

This phase verifies the BlueOS installation on the Pi with the HAT physically fitted. It does not verify that BlueOS can access or operate the HAT.

## Procedure and expected results

### 1. Start the simulated vehicle

Use BlueOS's Autopilot Firmware service to select and start an ArduSub SITL instance, if the installed stable release offers it. Confirm that no real flight controller is connected. Verify that BlueOS reports the simulated autopilot as connected and that its MAVLink inspection/service view receives messages. Record the vehicle system/component IDs and the telemetry fields visible.

**Expected:** BlueOS identifies the SITL vehicle and receives changing heartbeat/telemetry data without a physical flight controller.

### 2. Connect Cockpit

Open Blue Robotics Cockpit and use vehicle discovery to connect to the BlueOS instance. If discovery is unavailable in the VM network, configure the BlueOS vehicle address and the documented MAVLink2REST backend address manually; record which method was used.

**Expected:** Cockpit identifies the ArduSub vehicle, loads an appropriate submarine interface, and displays live connection state and telemetry. Record fields, units, update behaviour, and any mismatch between Cockpit and BlueOS inspection.

### 3. Exercise view and telemetry behaviour

Observe attitude/depth or other available telemetry widgets while SITL values change. Switch between Cockpit views, open its MAVLink inspection view, and return to the vehicle view.

**Expected:** displayed values update, the connection state remains accurate, and Cockpit does not present missing or stale telemetry as live. Record any fields that are unavailable or misleading in SITL.

### 4. Check loss and recovery

Stop the SITL process from BlueOS while leaving Cockpit open. Observe the loss indication. Restart SITL and observe reconnection. Do not issue control input during the interruption.

**Expected:** Cockpit signals loss of vehicle communication and then recovers its connection and telemetry after SITL restarts. Record detection and recovery times, visible errors, and whether a manual reconnect is needed.

### 5. Optional disarmed input-path observation

Only if the SITL setup clearly confirms the vehicle remains disarmed, inspect incoming MAVLink messages while briefly moving a connected gamepad. Do not arm the vehicle or request actuator output. Stop moving the gamepad and observe how Cockpit indicates input loss or neutral state.

**Expected:** any emitted `MANUAL_CONTROL` messages are visible in the simulator-side MAVLink inspection. Record message presence and rate if measurable; this is an interface-path observation, not validation of safe control or actuator behaviour.

### 6. Separate HAT access follow-up

The BlueOS/Adeept extension and its I²C/PCA9685 access path are not yet implemented. Record this phase as **blocked** until an extension exists. Do not treat the BlueOS boot, SITL, or Cockpit results as evidence that the HAT works under BlueOS. The extension should first detect the PCA9685 and report status; any subsequent servo test should use one unloaded servo, with all motor/ESC outputs disconnected. Follow the [BlueOS and Adeept Robot HAT architecture](../architecture/blueos-adeept-robot-hat.md) and the [ADM133 interface reference](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/ROV%20-%20Main%20Body/docs/reference/adeept-robot-hat-adm133-interfaces.md).

## Evidence and result

Capture screenshots of BlueOS's simulated-board state, Cockpit's connected view, telemetry, and the disconnect/reconnect transition. Keep logs with the test date and software revisions. Mark each procedure **pass**, **fail**, **blocked**, or **not run**, and include the observed result rather than inferring success from a running UI.

The test can support conclusions about BlueOS/Cockpit SITL integration and useful operator-interface test cases. It cannot validate CuttleOS integration, our vehicle dynamics, the NATS/ROS 2 bridge, physical failsafes, or production readiness.

## Environment limitation and fallback

This test has not been run. It requires physical access to the Pi and a reserved SD card. If BlueOS cannot start ArduSub SITL on the Pi, Cockpit's documented ArduSub Docker Compose simulation can be used as a Cockpit-only fallback on a suitable Linux host; that does **not** satisfy the BlueOS-plus-Cockpit test. Record the missing BlueOS/SITL step as blocked.

## References

- [Blue Robotics Cockpit overview and simulation instructions](https://blueos.cloud/cockpit/docs/stable/usage/overview/)
- [BlueOS advanced usage: Autopilot Firmware and SITL](https://blueos.cloud/docs/stable/usage/advanced/)
- [BlueOS and Adeept Robot HAT architecture](../architecture/blueos-adeept-robot-hat.md)
- [Adeept ADM133 Robot HAT V3.1 interface reference](https://github.com/PhilipMcGaw/robot-NautiPi/blob/main/ROV%20-%20Main%20Body/docs/reference/adeept-robot-hat-adm133-interfaces.md)
