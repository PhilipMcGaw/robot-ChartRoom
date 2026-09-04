# Raspberry Pi deployment

This document defines the project-level approach for deploying a robot computer based on Raspberry Pi OS. It records the repeatable deployment workflow and the boundary between operating-system provisioning and robot-specific software.

The implementation of the CuttleOS provisioner remains in the [CuttleOS repository](https://github.com/PhilipMcGaw/robot-CuttleOS). Chartroom records the deployment architecture and procedure as shared project knowledge.

## Deployment objective

The target workflow is:

```text
Write the SD card → configure the card → insert it into the robot → apply power → wait
```

The deployment should be headless, repeatable, observable, and recoverable. A monitor and keyboard should not normally be required once the SD card has been prepared.

## Raspberry Pi Imager

Use Raspberry Pi Imager to write a current Raspberry Pi OS Lite image. Use Imager's customisation settings for the basic headless configuration:

- hostname;
- timezone and keyboard layout;
- username and password;
- Wi-Fi credentials; and
- SSH access.

These settings allow the Pi to join the network and accept a remote connection without requiring an interactive first-run setup.

A custom Raspberry Pi OS image is not required for normal deployment.

## First boot

Current Raspberry Pi OS releases use `cloud-init` for first-boot configuration. Raspberry Pi Imager creates configuration files on the card's boot partition, including `user-data`.

After Imager has finished writing the card on macOS:

1. Eject and reinsert the card so the boot partition appears in Finder.
2. Prepare the project-specific first-boot configuration.
3. Safely eject the card.
4. Insert the card into the robot.
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
Wi-Fi, user and SSH configured
        ↓
cloud-init starts on first boot
        ↓
CuttleOS repository retrieved
        ↓
Robot profile selected
        ↓
CuttleOS provisioner runs
        ↓
Required services and dependencies installed
```

The robot profile identifies the configuration required by the particular vehicle. For example:

```text
ROBOT_PROFILE=k9
```

Profile selection belongs to the deployment configuration; detailed service and dependency installation belongs to CuttleOS.

## One-shot provisioning service

First-boot provisioning should hand off the actual installation work to a `systemd` one-shot service rather than leaving a long sequence of commands embedded directly in cloud-init.

The service should:

1. wait until networking is available;
2. run the provisioner as `root`;
3. write a completion marker on success;
4. avoid repeating completed work on subsequent boots; and
5. leave useful logs when provisioning fails.

The provisioner must be idempotent. Running it more than once must not duplicate configuration, unexpectedly overwrite local secrets, or start duplicate copies of robot services.

This makes recovery practical. If first boot fails because the robot is temporarily outside Wi-Fi coverage, the installation can be inspected over SSH and the provisioning service can be run again after connectivity is restored.

## CuttleOS implementation

CuttleOS contains the implementation-specific provisioning logic, including its Raspberry Pi provisioning script and first-boot helper. It remains the source of truth for Python and Node.js environments, Nginx, Motion, NATS, systemd units, Cockpit, Control, DataLogger, robot profiles, and robot-specific software dependencies.

See the [CuttleOS first-boot provisioning guide](https://github.com/PhilipMcGaw/robot-CuttleOS/blob/main/docs/raspberry-pi-first-boot-provisioning.md) for the current implementation procedure.

## Preparing a card from macOS

The preferred workflow is:

1. Use Raspberry Pi Imager to write Raspberry Pi OS Lite.
2. Configure hostname, user, Wi-Fi, and SSH in Imager.
3. Eject and reinsert the card so the `bootfs` volume appears in Finder.
4. Run the CuttleOS first-boot preparation helper from a CuttleOS checkout.
5. Safely eject the card.
6. Install the card in the robot and apply power.

The CuttleOS helper currently uses a command of this form:

```zsh
chmod +x scripts/prepare_first_boot.sh
scripts/prepare_first_boot.sh /Volumes/bootfs \
  --user philip \
  --profile k9 \
  --config-dir ~/robot-deployment/k9
```

The private deployment directory contains robot-specific configuration such as NATS and network settings. The exact files and command-line interface are implementation details of CuttleOS and may change independently of this document.

## Secrets

A reusable SD-card image, public example, or repository file must not contain real:

- Wi-Fi passwords;
- NATS credentials;
- private SSH keys; or
- other robot-specific secrets.

Secrets should be supplied during card preparation, retrieved from a protected private location during first boot, or entered through another controlled deployment step.

## Custom images

A custom operating-system image is not required for the current deployment model. It may become appropriate if the same prepared operating system is written to many robots, the repository should already be present on the image, or CuttleOS should eventually be integrated formally into Raspberry Pi Imager.

Until those requirements justify the additional maintenance burden, preparing a standard Raspberry Pi OS Lite card with the CuttleOS first-boot mechanism provides the better balance of repeatability and simplicity.

## Authority boundary

| Concern | Authority |
|---|---|
| Project deployment architecture | Chartroom |
| Raspberry Pi deployment procedure | Chartroom |
| CuttleOS first-boot implementation | CuttleOS |
| CuttleOS package and service provisioning | CuttleOS |
| Robot software configuration | CuttleOS |
| Physical hardware and wiring | NautiPi |
| ROS 2/Gazebo simulation | SquidLink |

Chartroom should describe the intended deployment process without becoming a second copy of the CuttleOS implementation. When commands, paths, service names, or provisioning behaviour change, CuttleOS is the implementation authority and this page should be updated when the project-level procedure changes.
