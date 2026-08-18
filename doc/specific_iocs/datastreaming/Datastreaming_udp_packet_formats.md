# Datastreaming: UDP packet formats

This page describes the UDP packet format for instruments which stream UDP from detectors (e.g. HRPD-X).

Translation between this UDP format and the {doc}`flatbuffers format <ADRs/000_kafka>` is done by [`event_udp_to_kafka`](https://github.com/ISISComputingGroup/event_udp_to_kafka), which initially get written to the `_rawEvents` Kafka topic.

The data comes in over UDP packets, each of which is made up of 32-bit words. All data is transmitted in big-endian
format. Multiple messages can be concatenated together into a single UDP packet. The data does not currently have
trailing zero-padding bytes, but these may be added in future and should be ignored.

## Header format

The header has an adjustable length with words 0 to 12 have fixed functionality and the final packet will be the DDR checksum.
Words in between these will be board specific and their functionality defined in the header type.

### Word 0: marker word

Always `0xFFFFFFFF`.

### Word 1: header information


- **Bits 0..7**: Length of header, in 32-bit words
- **Bits 8..23**: Header Type
- **Bits 24..31**: Marker - Always `0xFF` *(This will be useful to keep extra Fs to show start of header but not sure if necessary?)*

### Word 2: Header Information

- **Bit 0..7**: Header Flags
    - **Bit 0**: End of run header marker
    - **Bit 1**: Veto frame packet header marker - This show that the frame has been hard vetoed. If a mask is set to cover this corresponding bit this won't be set.
    - **Bit 2**: Pause frame packet header marker
    - **Bit 3**: No frame sync (not implemented)
    - **Bit 4..15**: Reserved for future use
- **Bits 16..31**: PCB Board Number, encoded as an integer. e.g. for `PC1234M1S`, the board identifier would be `1234`. Ignore any `PC` prefix and any suffix such as `M1S`.

### Word 3: GPS timestamp

- **Bits 0..3**: seconds (most significant bits; combine with least significant bits from word 5)
- **Bits 4..9**: minutes
- **Bits 10..14**: hours
- **Bits 15..23**: days
- **Bits 24..31**: years (as offset from year 2000)

### Word 4: GPS timestamp

- **Bits 0..9**: nanoseconds
- **Bits 10..19**: microseconds
- **Bits 20..29**: milliseconds
- **Bits 30..31**: seconds (least significant bits; combine with most significant bits from word 4)

### Word 5: Frame number

- **Bits 0..31**: frame number as u32

### Word 6: period number

- **Bits 0..15**: Period number
- **Bits 16..31**: Frame repeat number

### Word 7: events in frame

- **Bits 0..31**: number of neutron events in this frame.

:::{note}
This is not necessarily the same as the number of events in this UDP message, as the events may be split between
multiple UDP messages. This is the *total* number of events in the ISIS frame.

See header word 8 if looking for length of *this* message.
:::

### Word 8: packet length & protons-per-pulse

- **Bits 0..7**: protons-per-pulse in this ISIS frame.
- **Bits 16..27**: number of 32-bit words from the beginning of this header to the start of the next header or till the end of this UDP packet.
- **Bits 28..31**: unused

To convert to {math}`\mu Ah` delivered during this ISIS frame, multiply by {math}`1.738{\times}10^{-6}`.

{#ds_veto_bit_definitions}
### Word 9: vetoes
These values be even if there is a veto mark that corresponds to them
- **Bits 0..15**: Common vetoes
    - **Bit 0**: Data Overflow veto
    - **Bit 1**: SMP veto
    - **Bit 2**: TS2 pulse veto
    - **Bit 3**: Wrong pulse veto *-awaiting clarity what this is*
    - **Bit 4**: ISIS slow *-awaiting clarity what this is*
    - **Bit 5**: Run signal veto *-not sure if this will be needed when not using DAE3*
    - **Bit 6**: Pause veto
    - **Bit 7**: Period overflow veto pause veto
    - **Bit 8**: Dwell Period veto
    - **Bit 9**: Status Packet CRC fault veto
    - **Bits 10..15**: Reserved for future use
- **Bits 16..31**: Instrument Specific Vetoes
    - **Bits 16..19**: External vetoes
    - **Bits 20..23**: Fast chopper vetoes (Fermi)
    - **Bits 24..31**: Reserved for future use

### Word 10: next frame address

- **Bits 0..31**: Address of the next frame, in bytes.

### Word 11: streamed frame number

- **Bits 0..31**: streamed frame number.

### Word 12: Frame sync delay

- **Bits 0..31**: Delay of the frame sync from Time Of Flight pulse.

### Variable number of board-specific parameters

The interpretation of these words depends on the board number. There may be zero or more of these. The number of words of board-specific parameters is "length of header" (from word 1) minus 14.

See {ref}`ds_board_specific_header_parameters` for interpretation of these words for different board types.

### Last Word: checksum

- **Bits 0..31**: Pre-DDR checksum

---

{#ds_board_specific_header_parameters}
## Board-specific parameters

### `pc3544` / `pc3634` / `pc3877`

The scheme used by these boards is for 64-bit neutron events to look like:

```
1110000T TTTTTTTT TTTTTTTT TTTTTTTT
CCCxxxxx xxxxxxxx xxDDDDDD DDPPPPPP
```

Where:
- `1` is a bit that is *always* set to `1`
- `0` is a bit that is *always* set to `0`
- `T` is a bit that forms part of the raw timestamp
- `C` is a bit that forms part of the channel index
- `D` is a bit that forms part of 'diagnostic data' (for example pulse height)
- `P` is a bit that forms part of the 'position' (pixel) that this event corresponds to
- `x` is an unused bit

The example above has `pos_bits_per_ch = 6`, `diag_bits_per_ch = 8`, `channel_bits = 3`.

The detector ID sent to Kafka then needs to be `detector_id_offset + P + (C * (2^pos_bits_per_ch))`.

#### Word 13: board-specific parameters 0

- **Bits 0..7**: pos_bits_per_ch - how many positional bits needed for each channel (only need 5 bits for 32 bits)
- **Bits 8..15**: diag_bits_per_ch - how many bits needed diagnostic data for each channel (only need 5 bits for 32 bits) 
- **Bits 16..23**: channel_bits - how bits for channel (make this the most significant bits)
- **Bits 24..31**: board_address - which board in the system

#### Word 14: board-specific parameters 1

- **Bits 0..31**: detector_id_offset
