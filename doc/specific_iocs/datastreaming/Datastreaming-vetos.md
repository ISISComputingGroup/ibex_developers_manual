# Data streaming - Vetoes

Vetoes are essentially a way of telling either the detector acquisition hardware (with a `hard` veto) or downstream consumers of event data (`soft` veto) to ignore a set of events in a frame conditionally based on a signal (whether that's an internal state, electrical signal or a software-based condition).

Configuring these is handled with a bit mask where 1 signifies to ignore if `x` condition happens and 0 means always do something with the events. 

In the data streaming system, there are three states an individual veto can configured with: 
- `ignored` - the veto is not active and therefore all events are considered "good".
- `soft` - events will be streamed from the hardware, but downstream consumers should ignore these events if respecting vetoes.
- `hard` - events will not be streamed from the hardware at all. 

The only difference between soft and hard from a controls point of view is whether or not the corresponding bit is set on the hardware (the streaming control board) itself. With both `soft` and `hard` vetoes, these vetoes are emitted as a [`vc00`](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/vc00_veto_configuration.fbs) blob on the {ref}`veto config<vetoconfigtopic>` topic.

For every frame, there exists [a field](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/pu00_pulse_metadata.fbs#L12) in the header (which is always sent, even if no events are streamed) which is the frame's "active" veto information. This is whether or not a frame has been vetoed due to the condition. 

## Veto bit mask
This is the same for: 
1) the configured vetoes in the [`vc00`](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/vc00_veto_configuration.fbs) schema, emitted by `kafka_dae_control`
2) the streamed UDP frame packet's header in word 9, and in turn the `pu00` [active vetoes](https://github.com/ISISComputingGroup/streaming-data-types/blob/master/schemas/pu00_pulse_metadata.fbs#L12) that are sent every frame regardless of whether or not events are being vetoed.

Bits: 
- **Bit 0**: FIFO veto
- **Bit 1**: SMP veto
- **Bit 2**: TS2 pulse veto
- **Bit 3**: Wrong pulse veto
- **Bit 4**: Unused
- **Bit 5**: ISIS slow
- **Bits 6..=9**: External vetoes
- **Bits 10..=13**: Fast chopper vetoes
- **Bits 14..=15**: Reserved vetoes
- **Bits 16..=23**: Unused
- **Bits 24..=31**: Frame repeat number
TODO: this isn't quite right, and we should probably link these up with the docs on event_udp_to_kafka so there's only one place to change if we need to update them. 
