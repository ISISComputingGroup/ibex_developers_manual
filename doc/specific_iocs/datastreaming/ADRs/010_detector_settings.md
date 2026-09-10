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

### New process

We will add a separate process to read and write diagnostics from individual boards. The code will be in the same repository as
`kafka_dae_control` to allow re-use of shared infrastructure (for example, UDP comms logic), but will be a separate runtime
process.

This process is less critical than `kafka_dae_control`, in the sense that an instrument should be able to _run_ and perform all
routine DAE operations without this process available, albeit with reduced diagnostic visibility.

### Configuration

The new process would be configured using a `config.toml` in a similar style to the existing `kafka_dae_control` config file.
An example of a configuration file is:

```toml
# 'Parameter groups' define shared sets of parameters which may exist on
# multiple boards, to help reduce repetition.
[diagnostic_parameter_groups.temperature]
parameters = [
    { reg_id = "temp1", "pv_name" = "TEMP1", write = false },
    { reg_id = "temp2", "pv_name" = "TEMP2", write = false },
]

[diagnostic_parameter_groups.event_rate]
parameters = [
    { reg_id = "event_rate", "pv_name" = "EVENTRATE", write = false },
]

# Each board defines it's key parameters (ip, PV name).
# It then defines any parameters and parameter_groups which it uses; these are merged
# to form the list of parameters read by this board.
[diagnostic_modules.mod1]
ip = "192.168.1.21"
pv_suffix = "MOD1"
parameter_groups = ["temperature", "event_rate"]
parameters = [
    { reg_id = "super_special_parameter_for_mod1", "pv_name" = "SUPER_SPECIAL", write = true, init_value = 12345 },
]

[diagnostic_modules.mod2]
ip = "192.168.1.22"
pv_suffix = "MOD2"
parameter_groups = ["temperature", "event_rate"]
```

If the `write=` parameter is omitted, it will default to what is specified in the memory-map.

### Runtime

When the new process starts, it will:
- Update it's local cache of memory maps (e.g. `git pull`), with a timeout. If the pull fails or times out, the most recent set of memory maps will continue to be used, with a warning.
- Read register `0` of each configured diagnostic module to retrieve a memory-map identifier
- Use the retrieved mappings to map each configured register (in the `parameters` and `parameter_groups` sections of the `config.toml`) to a numeric address
- Attempt to poll each diagnostic register in turn, looping for the lifetime of the program.
- The updated numbers would be served in PVs of the form `IN:INST:DAE:DIAG:MOD1:SUPER_SPECIAL`. This allows them to be accessible to IBEX, monitored by Nagios, or consumed by DSG's monitoring infrastructure.

Every parameter would be exposed as an integer, with no parameter-specific logic.

### Writing

The new process would also create standard setpoint PVs for each writeable parameter, in the form `IN:INST:DAE:DIAG:MOD1:SUPER_SPECIAL:REINITIALIZE`, which writes
the value specified in the `config.toml` to the detector.

Every parameter would be written as an integer, with no parameter-specific logic.

We may also provide an `:SP` PV which writes an arbitrary value in future, though we need to be careful that this does not encourage _routine_ use of these settings as part of running an instrument.

## Alternatives

- In the first instance, we could avoid the architectural complexity of a central memory-map store and self-describing boards by requiring a `reg_address` in the `config.toml`.
  - Mapping via `reg_id` and self-description could still be added later if desired
- We could embed this within the `kafka_dae_control` process at runtime, for example as a separate thread.
  - This would increase the risk that a failure in 'diagnostic' functionality could affect the core 'control' functionality.

## Risks

Providing a route through to individual detectors from IBEX may encourage architectural shortcuts to be taken later. For example, a parameter that should conceptually be set via the SCB may get set on individual detectors instead of adding the relevant functionality to the SCB. Over time, these shortcuts may accumulate and increase system maintenance burden to an unsustainable level.

If instruments begin accumulating scripts or workflows which involve 'fiddling' with detector parameters directly, those instruments will become much harder to migrate to different detectors in future. It will reduce the commonality between instruments, which will increase system maintenance burden.

## Consequences

- It is possible to read and write a specified set of registers from individual detector modules from EPICS PVs. This set is statically configurable per-instrument.
- We increase the risk of architectural 'shortcuts' being taken later which, if taken, would adversely impact maintainability.
- The `kafka_dae_control` repository becomes more complicated, as it now hosts the source code for two independent processes, which happen to share some functionality and architectural approaches.
- Diagnostic functionality is isolated from core DAE control functionality through process-level separation, reducing the likelihood that detector diagnostic failures will impact routine instrument operations.
