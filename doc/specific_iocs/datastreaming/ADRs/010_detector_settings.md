# 10 - handling low-level detector settings

## Status

- Provisional until agreed with DSG
- Requires prioritisation against other streaming work

## Context

`kafka_dae_control` primarily talks to the streaming control board (SCB). All user-facing operations are routed through this board, for example:
- Beginning and ending runs
- Configuring hardware vetoes
- Configuring time-sync source

We want all **user-facing** workflows to remain possible purely via the streaming control board. For example, we do **not** want to end up in a situation where we need to tell each individual detector to begin a run. The streaming control board should remain the common control interface to all streaming instruments.

However, for 'diagnostic' workflows, Detector Systems Group (DSG) would also like to be able to read and write some parameters on individual detector boards through IBEX. This may include workflows like:
- Configuring detector-specific parameters, for example discriminator thresholds or maximum event-rates before triggering a local 'overcount' veto.
- Verifying that a detector's configuration is as expected after a hardware reboot or a swap.
- Monitoring detector-specific diagnostic parameters, for example temperatures or local event rates.

The set of 'individual' detector boards is likely to be large, varied, and different on different instruments. For example, HRPD-X will have ~80 detector modules; SANDALS-2 will use an entirely different type of detector modules. For this reason, it is not sustainable for IBEX to individually cater for the quirks of every detector board on every instrument.

## Decision

### Detector board self-description

Individual detector boards which want to participate in this scheme will:
- Publish a UDP comms interface using the same request/response mechanism as the SCB
- In a register which is common across all detector boards, publish an identifier which uniquely identifies a specific memory map.
- This memory map will specify a mapping of `name <-> register` for all parameters this board can expose to IBEX.

### Configuration

We would add a section in [`kafka_dae_control`'s config file](https://github.com/ISISComputingGroup/kafka_dae_control/blob/main/config.example.toml), which looks like:

```toml
[diagnostic_modules.mod1]
ip = "192.168.1.21"
pv_suffix = "MOD1"
parameters = [
    { reg_name = "temp", "pv_name" = "TEMP", write = false },
    { reg_name = "event_rate", "pv_name" = "EVENTRATE", write = false },
    { reg_name = "super_special_parameter_for_mod1", "pv_name" = "SUPER_SPECIAL", write = true },
]

[diagnostic_modules.mod2]
ip = "192.168.1.22"
pv_suffix = "MOD2"
parameters = [
    { reg_name = "temp", "pv_name" = "TEMP", write = false },
    { reg_name = "event_rate", "pv_name" = "EVENTRATE", write = false },
]
```

### Runtime

When `kafka_dae_control` starts, it will create a thread dedicated to communication with 'diagnostic' modules.

It would then:
- Read register `0` of each configured diagnostic module to retrieve a memory-map identifier
- Look up that register map identifier in a central store to retrieve a 'full' memory map for this board
  - The central store could be cached locally on startup to ensure `kafka_dae_control` still boots correctly if the central store is offline.
  - In any case, a failure in the 'diagnostic' functionality should not prevent the critical functionality of `kafka_dae_control` from working.
- Use the retrieved mappings to map each configured register (in the `parameters` of the `config.toml` to a numeric address)
- A dedicated thread in `kafka_dae_control` would attempt to poll each diagnostic register in turn, looping for the lifetime of the program.
- The updated numbers would be served in PVs of the form `IN:INST:DAE:DIAG:MOD1:SUPER_SPECIAL`. This allows them to be accessible to IBEX, monitored by Nagios, or consumed by DSG's monitoring infrastructure.

### Writing

`kafka_dae_control` would also create standard setpoint PVs for each writeable parameter, in the form `IN:INST:DAE:DIAG:MOD1:SUPER_SPECIAL:SP`.

## Alternatives

- In the first instance, we could avoid the architectural complexity of a central memory-map store and self-describing boards by requiring a `reg_address` in the `config.toml`.
  - Mapping via `reg_name` and self-description could still be added later if desired
- We could make this an entirely separate process from `kafka_dae_control`, which happens to be implemented in a similar way.
  - Advantage: This would better insulate the *critical* functionality in `kafka_dae_control` from the non-critical functionality of providing diagnostics on individual detector modules.
  - Disadvantage: There would be some duplication between `kafka_dae_control` and this new process; both would be doing UDP comms to boards with a similar interface, and serving PVs over PVAccess.

## Risks

Providing a route through to individual detectors from IBEX may encourage architectural shortcuts to be taken later. For example, a parameter that should conceptually be set via the SCB may get set on individual detectors instead of adding the relevant functionality to the SCB. Over time, these shortcuts may accumulate and increase system maintenance burden to an unsustainable level.

If instruments begin accumulating scripts or workflows which involve 'fiddling' with detector parameters directly, those instruments will become much harder to migrate to different detectors in future. It will reduce the commonality between instruments, which will increase system maintenance burden.

## Consequences

- It is possible to read and write a specified set of registers from individual detector modules from EPICS PVs. This set is statically configurable per-instrument.
- We increase the risk of architectural 'shortcuts' being taken later which, if taken, would adversely impact maintainability.
- `kafka_dae_control` becomes more complicated.
