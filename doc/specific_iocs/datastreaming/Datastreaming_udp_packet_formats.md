# Datastreaming: UDP packet formats

This page describes the UDP packet format for instruments which stream UDP from detectors (e.g. HRPD-X).

Translation between this UDP format and the {doc}`flatbuffers format <ADRs/000_kafka>` is done by [`event_udp_to_kafka`](https://github.com/ISISComputingGroup/event_udp_to_kafka), which initially get written to the `_rawEvents` Kafka topic.

The data comes in over UDP packets, each of which is made up of 32-bit words. All data is transmitted in big-endian
format. Multiple messages can be concatenated together into a single UDP packet. The data does not currently have
trailing zero-padding bytes, but these may be added in future and should be ignored.

## Header format

The header is 16 words (64 bytes). 

### Word 0: marker word

Always `0xFFFFFFFF`.

### Word 1: header information


- **Bits 0..7**: Length of header, in 32-bit words (max 255 *too many?*)
- **Bits 8..23**: Header Type (max 65535 *too many?*)
- **Bits 24..31**: Marker - Always `0xFF` *(think it will be useful to keep extra Fs to show start of header but not sure if necessary?)*

### Word 2: Header Information

- **Bit 0..=7**: Header Flags
    - **Bit 0**: End of run header marker (active low)
    - **Bit 1**: Veto frame packet header marker (active low)
    - **Bit 2**: Pause frame packet header marker (active low)
    - **Bit 3**: No frame sync (active low) (not implemented)
    - **Bit 4..=15**: Reserved for future use
- **Bits 16..=31**: PCB Board Number, encoded as an integer. e.g. for `PC1234M1S`, the board identifier would be `1234`. Ignore any `PC` prefix and any suffix such as `M1S`.

### Word 3: GPS timestamp

- **Bits 0..=3**: seconds (most significant bits; combine with least significant bits from word 5)
- **Bits 4..=9**: minutes
- **Bits 10..=14**: hours
- **Bits 15..=23**: days
- **Bits 24..=31**: years (as offset from year 2000)

### Word 4: GPS timestamp

- **Bits 0..=9**: nanoseconds
- **Bits 10..=19**: microseconds
- **Bits 20..=29**: milliseconds
- **Bits 30..=31**: seconds (least significant bits; combine with most significant bits from word 4)

### Word 5: Frame number

- **Bits 0..=31**: frame number as u32

### Word 6: period number

- **Bits 0..=15**: Period number
- **Bits 16..=31**: Frame repeat number

### Word 7: events in frame

- **Bits 0..=31**: number of neutron events in this frame.

:::{note}
This is not necessarily the same as the number of events in this UDP message, as the events may be split between
multiple UDP messages. This is the *total* number of events in the ISIS frame.

See header word 8 if looking for length of *this* message.
:::

### Word 8: packet length & protons-per-pulse

- **Bits 0..=7**: protons-per-pulse in this ISIS frame.
- **Bits 16..27**: number of 32-bit words from the beginning of this header to the start of the next header.
- **Bits 28..=31**: unused

To convert to {math}`\mu Ah` delivered during this ISIS frame, multiply by {math}`1.738{\times}10^{-6}`.

### Word 9: vetoes
- **Bits 0..=15**: Common vetoes
    - **Bit 0**: Data Overflow veto
    - **Bit 1**: SMP veto
    - **Bit 2**: TS2 pulse veto
    - **Bit 3**: Wrong pulse veto *-awaiting clarity what this is*
    - **Bit 4**: ISIS slow *-awaiting clarity what this is*
    - **Bit 5**: period overflow veto *-awaiting clarity what this is*
    - **Bit 6**: run sig veto *-not sure if this will be needed when not using DAE3*
    - **Bit 7**: pause veto
    - **Bit 8**: Status Packet CRC fault veto
    - **Bits 9..=12**: Fast chopper vetoes
    - **Bits 13..=15**: Reserved for future use
- **Bits 16..=31**: Instrument Specific Vetoes
    - **Bits 16..=19**: External vetoes
    - **Bits 20..=31**: Reserved for future use

### Word 10: next frame address

- **Bits 0..=31**: Address of the next frame, in bytes.

### Word 11: streamed frame number

- **Bits 0..=31**: streamed frame number.

### Word 12: checksum

- **Bits 0..=31**: Pre-DDR checksum

### Word 13: unused

- **Bits 0..=31**: Reserved for future use

:::{note}
Did consider adding information for how long the event data is and how long the time data is to make it easier to slice but think that might come from the packet type anyway
:::

### Word 14: unused

- **Bits 0..=31**: Unused

### Word 15: unused

- **Bits 0..=31**: Unused
