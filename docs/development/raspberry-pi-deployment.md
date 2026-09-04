# Raspberry Pi deployment

This document defines the project-level procedure for deploying a robot computer based on Raspberry Pi OS. It is intentionally maintained in Chartroom rather than in the software package being deployed. The same procedure should be usable for CuttleOS and for future robot-side software stacks, with repository-specific implementation details linked from here.

The implementation of the CuttleOS provisioner remains in the [CuttleOS repository](https://github.com/PhilipMcGaw/robot-CuttleOS). Chartroom records the deployment architecture, operational procedure, commissioning checks, and lessons learned.

## Deployment objective

The target workflow is:

```text
Prepare SD card → configure deployment → boot robot computer → provision → verify → commission
```

The deployment should be repeatable, observable, and recoverable. A monitor and keyboard should not normally be required once the SD card has been prepared.

## Deployment routes

There are currently two supported starting points:

```text
Existing Linux system
        ↓
bootstrap_robot.sh
        ↓
robot software provisioner

Fresh Raspberry Pi OS SD card
        ↓
Raspberry Pi Imager
        ↓
first-boot configuration
        ↓
first-boot provisioning
        ↓
robot software provisioner
```

The first route is useful for an already-installed Raspberry Pi. The second is the preferred route for a new robot because the complete process can be prepared before the robot is powered for the first time.

## Raspberry Pi Imager

Use Raspberry Pi Imager to write a current Raspberry Pi OS Lite image appropriate to the approved robot baseline. Use Imager's customisation settings for the basic headless configuration:

- hostname;
- timezone and keyboard layout;
- username and password;
- network credentials; and
- SSH access.

These settings allow the Pi to join the network and accept a remote connection without requiring an interactive first-run setup.

A custom Raspberry Pi OS image is not required for normal deployment.

## First boot

Current Raspberry Pi OS releases use `cloud-init` for first-boot configuration. Raspberry Pi Imager creates configuration files on the card's boot partition, including `user-data`.

After Imager has finished writing the card on macOS:

1. Eject and reinsert the card so the boot partition appears in Finder.
2. Prepare the project-specific first-boot configuration.
3. Safely eject the card.
4. Install the card in the robot computer.
5. Apply power and allow first-boot provisioning to complete.

The cloud-config file must begin with:

```yaml
#cloud-config
```

The first-boot process may install packages, create configuration files, retrieve the software repository, select the robot profile, and invoke the robot software provisioner.

## Provisioning sequence

```text
Raspberry Pi Imager
        ↓
Network, user and SSH configured
        ↓
cloud-init starts on first boot
        ↓
Robot software repository retrieved
        ↓
Robot profile selected
        ↓
Robot software provisioner runs
        ↓
Required services and dependencies installed
        ↓
Deployment verification
        ↓
Commissioning
```

The robot profile identifies the configuration required by the particular vehicle. Profile selection belongs to the deployment configuration; detailed service and dependency installation belongs to the software repository being deployed.

## One-shot provisioning service

First-boot provisioning should hand off the actual installation work to a `systemd` one-shot service rather than leaving a long sequence of commands embedded directly in cloud-init.

The service should:

1. wait until networking is available;
2. run the provisioner as `root`;
3. write a completion marker on success;
4. avoid repeating completed work on subsequent boots; and
5. leave useful logs when provisioning fails.

The provisioner should be idempotent. Running it more than once must not duplicate configuration, unexpectedly overwrite local secrets, or start duplicate copies of robot services.

## Deployment readiness inspection

Before the first physical deployment of a new software baseline, perform a deployment-readiness inspection. The purpose is to identify assumptions that have not yet been demonstrated on the target hardware or a clean operating-system image.

At minimum, check:

- the supported Raspberry Pi and OS baseline is explicitly defined;
- the provisioning entry point can obtain the software it needs;
- required Debian packages are available from approved repositories;
- configuration and secret files are separated from source-controlled examples;
- secret files have restrictive permissions;
- systemd units use correct service names, paths, and dependencies;
- NATS is available before services that depend on it start;
- first-boot provisioning has a completion marker and useful logs;
- the robot profile is selected explicitly;
- the deployment does not depend on an interactive terminal; and
- the recovery path is understood if provisioning fails.

A readiness inspection is not evidence that the deployment has been physically validated. A clean-image deployment and hardware commissioning remain separate validation activities.

## Bench deployment and commissioning

For an initial deployment or software-baseline change, use a mechanically constrained test robot where practical. For TestBot, the initial deployment is performed with the wheels removed or the robot securely supported so that the wheels cannot contact the floor.

The initial commissioning sequence should be:

1. boot the Raspberry Pi and verify the network connection;
2. verify NATS starts;
3. verify Control starts and completes hardware initialisation;
4. verify Cockpit starts and is reachable;
5. verify Datalogger starts;
6. verify all expected services are healthy;
7. verify normal command and telemetry flow with the actuators mechanically constrained;
8. deliberately interrupt NATS and verify the documented safe-state behaviour;
9. verify NATS recovery does not automatically restore operational authority after a latched fault;
10. explicitly re-arm and verify fresh hardware initialisation; and
11. only then proceed to powered actuator testing appropriate to the robot.

Physical constraint is a risk control, not proof that an actuator cannot move unexpectedly. Keep people clear of moving mechanisms, retain a means of removing power, and treat exposed actuators as capable of unexpected motion or torque.

## Failure-injection checks

The first commissioning run should exercise the important deployment and runtime failure paths rather than testing only the nominal startup path.

For a CuttleOS robot, this includes at least:

- NATS unavailable during startup;
- a short NATS interruption below the configured fault threshold;
- a NATS interruption at or beyond the fault threshold;
- NATS recovery after a latched fault;
- attempted re-arm while NATS is unavailable;
- successful re-arm after NATS recovery; and
- failed hardware initialisation during re-arm.

Record the observed behaviour and update Chartroom with useful operational knowledge or troubleshooting guidance. The implementation-specific mechanism remains documented in the relevant software repository.

## Secrets

A reusable SD-card image, public example, or repository file must not contain real:

- Wi-Fi passwords;
- NATS credentials;
- private SSH keys; or
- other robot-specific secrets.

Secrets should be supplied during card preparation, retrieved from a protected private location during first boot, or entered through another controlled deployment step.

## CuttleOS implementation

CuttleOS contains the implementation-specific provisioning logic, including its Raspberry Pi provisioning scripts and first-boot helper. It remains the source of truth for the packages, Python and Node.js environments, Nginx, Motion, NATS, systemd units, Cockpit, Control, Datalogger, robot profiles, and robot-specific software dependencies.

See the [CuttleOS first-boot provisioning guide](https://github.com/PhilipMcGaw/robot-CuttleOS/blob/main/docs/raspberry-pi-first-boot-provisioning.md) for implementation details.

The CuttleOS repository should link to this page for the complete deployment procedure rather than reproducing the project-level procedure.

## Preparing a card from macOS

The preferred workflow is:

1. Use Raspberry Pi Imager to write Raspberry Pi OS Lite.
2. Configure hostname, user, network, and SSH in Imager.
3. Eject and reinsert the card so the `bootfs` volume appears in Finder.
4. Run the CuttleOS first-boot preparation helper from a CuttleOS checkout.
5. Safely eject the card.
6. Install the card in the robot and apply power.
7. Complete the deployment verification and commissioning checks above.

The current CuttleOS helper uses a command of this form:

```zsh
chmod +x scripts/prepare_first_boot.sh
scripts/prepare_first_boot.sh /Volumes/bootfs \
  --user philip \
  --profile k9 \
  --config-dir ~/robot-deployment/k9
```

The private deployment directory contains robot-specific configuration such as NATS and network settings. The exact files and command-line interface are implementation details of CuttleOS and may change independently of this document.

## Authority boundary

| Concern | Authority |
|---|---|
| Project deployment architecture | Chartroom |
| Robot deployment procedure | Chartroom |
| Deployment readiness and commissioning procedure | Chartroom |
| CuttleOS first-boot implementation | CuttleOS |
| CuttleOS package and service provisioning | CuttleOS |
| Robot software configuration | CuttleOS |
| Physical hardware and wiring | NautiPi |
| ROS 2/Gazebo simulation | SquidLink |

Chartroom describes the intended deployment process without becoming a second copy of the implementation. When commands, paths, service names, or provisioning behaviour change, the relevant software repository is the implementation authority and this page should be updated when the project-level procedure changes.
