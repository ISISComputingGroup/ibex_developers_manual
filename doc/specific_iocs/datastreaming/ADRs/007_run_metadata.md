# 7 - Run metadata

## Status

Accepted

## Context

In the ICP-based system, `ISISDAE` is responsible for serving PVs such as `TITLE` and `USERNAME`, which get fed into the ISISICP through asyn calls.

This has historically meant that if any other data acquisition hardware needed to be integrated, other than a DAE2 or DAE3, whichever service responsible for controlling the hardware should also serve PVs for run metadata.

`kafka_dae_control` was also started in this way, however as this is a distributed system it might make sense to split this functionality out into a soft IOC, which can handle the auto saving behaviour and so on.

## Decision

For both the ICP and streaming systems, we will pull out things like `TITLE` and `USERNAME`, and any other PVs which are not strictly related to the hardware, and put them in a soft IOC such as `INSTETC`.

## Consequences

- `kafka_dae_control` will get smaller in terms of responsibilities, which may make it easier to maintain
- If we need to write `kafka_dae_control_2` for whatever reason (ie. new streaming control boards with a different interface), its reponsibilities should be limited to just controlling the hardware and serving PVs to do so. 
- Some extra effort will be required to add these PVs to `INSTETC` and modify the ICP to suit, as well as removing them from `kafka_dae_control`
- `kafka_dae_control` will rely on CA/PVA for these items. This is already the case for the list of blocks which is required to form a run start message.
