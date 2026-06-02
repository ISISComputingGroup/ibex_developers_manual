# Datastreaming: UDP packet formats

This page describes the UDP packet format for instruments which stream UDP from detectors (e.g. HRPD-X).

Translation between this UDP format and the {doc}`flatbuffers format <ADRs/000_kafka>` is done by [`event_udp_to_kafka`](https://github.com/ISISComputingGroup/event_udp_to_kafka), which initially get written to the `_rawEvents` Kafka topic.

The data comes in over UDP packets, each of which is made up of 32-bit words. All data is transmitted in big-endian
format.

## Header format

The header is 16 words (64 bytes). 

### Word 0: marker byte

Always `0xFFFFFFFF`.

### Word 1: header information

- **Bit 0**: End of run header marker (active low)
- **Bit 1**: Veto frame packet header marker (active low)
- **Bit 2**: Sample environment packet header marker (active low)
- **Bit 3**: Not used
- **Bits 4..=31**: Always `0xFFFFFFF`

### Word 2: Information

- **Bits 0..=3**: Reserved for header type
- **Bits 4..=8**: Length of header
- **Bits 9..=10**: Not used
- **Bit 11**: Bad frame
- **Bit 12**: Run will continue
- **Bit 13**: No frame sync
- **Bit 14**: Frame Memory Full veto
- **Bit 15**: Frame data overrun
- **Bits 16..=31**: Not used

### Word 3: Frame number

- **Bits 0..=31**: frame number as u32

### Word 4: GPS timestamp

- **Bits 0..=3**: seconds (most significant bits; combine with least significant bits from word 5)
- **Bits 4..=9**: minutes
- **Bits 10..=14**: hours
- **Bits 15..=23**: days
- **Bits 24..=31**: years (as offset from year 2000)

### Word 5: GPS timestamp

- **Bits 0..=9**: nanoseconds
- **Bits 10..=19**: microseconds
- **Bits 20..=29**: milliseconds
- **Bits 30..=31**: seconds (least significant bits; combine with most significant bits from word 4)

### Word 6: period number

- **Bits 0..=15**: Period number
- **Bits 16..=31**: Not used

### Word 7: events in frame

- **Bits 0..=31**: number of neutron events in this frame.

:::{note}
This is not necessarily the same as the number of events in this UDP message, as the events may be split between
multiple UDP messages. This is the *total* number of events in the ISIS frame.

See header word 13 if looking for length of *this* message.
:::

### Word 8: protons-per-pulse

- **Bits 0..=7**: protons-per-pulse in this ISIS frame.
- **Bits 8..=31**: unused

To convert to {math}`\mu Ah` delivered during this ISIS frame, multiply by {math}`1.738{\times}10^{-6}`.

### Word 9: vetoes

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

### Word 10: next frame address

- **Bits 0..=31**: Address of the next frame, in bytes.

### Word 11: next frame address

- **Bits 0..=31**: Address of the next frame, in 64-bit words.

### Word 12: streamed frame number

- **Bits 0..=31**: streamed frame number.

### Word 13: packet length

- **Bits 0..=11**: number of 32-bit words from the beginning of this header to the start of the next header.
- **Bits 12..=31**: Unused

### Word 14: unused

- **Bits 0..=31**: Unused

### Word 15: checksum

- **Bits 0..=31**: Pre-DDR checksum
