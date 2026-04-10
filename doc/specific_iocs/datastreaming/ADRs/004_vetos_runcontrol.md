# 4 - Vetos and Run control

## Status

Accepted 

## Context

**Vetos**  
Vetos are currently used by DAE2/DAE3 to mark neutron data as not useful - these are usually hardware signals fed into the DAE by other sources such as ISIS central timing systems and choppers. 

This will remain fairly similar for the streamed data and will be fed in via the VXI control boards, which has registers for viewing the status of vetos.

There are two ways that an event packet could be vetoed, configurable via the VXI streaming control board (and the WLSF modules individually):
- **Software veto:** Emit the frame, but mark it as invalid using veto flags
- **Hardware veto:** Do not emit the frame

Long term, we will likely need to allow for both modes. We also need to support each mode for each different type of veto - e.g. not emitting frames if one type of veto is active, while emitting frames marked as invalid for another type of veto.

**Run control** 

Run control is controlled by IBEX using the existing {doc}`/system_components/Run-control` IOC. The concept of 'suspending' data collection if sample environment is outside a desired range will still be required.

## Decision

There will be a register, in the streaming control VXI crate that `kafka_dae_control` can write to, which will be set via EPICS by the run control IOC. This register will act exactly like a hardware veto signal, except will be controlled by software. The runcontrol status will be monitored by `kafka_dae_control`, and when it changes, `kafka_dae_control` will write to the corresponding register in the streaming control VXI crate.

The overall concept of {external+ibex_user_manual:ref}`concept_good_raw_frames` will still be needed, as scientists will use {external+genie_python:py:obj}`genie.waitfor_frames` and similar functions to control their run durations.

WLSF modules may also emit their own detector-specific vetoes (for example, a local buffer overrun on a specific detector). These will be `OR`ed together with the vetoes emitted by the streaming control board, by `kafka_event_aggregator`

## Consequences

- The existing concept of {doc}`/system_components/Run-control` is retained. This means that commands such as {external+genie_python:py:obj}`genie.waitfor_frames` will work largely as before, minimising required changes to instrument scripts. 
- The existing concepts of {external+ibex_user_manual:ref}`concept_good_raw_frames` are retained.
- Existing vetoes will largely map across onto the new system.
- `kafka_dae_control` will need to monitor the run control [this PV](https://github.com/ISISComputingGroup/EPICS-RunControl/blob/master/RunControlApp/Db/gencontrolMgr.db#L54C28-L54C35) for changes. 
