Original implementation for use on MuSR 3He refrigerator. The device is a Heliox/ITC503 based refrigerator.

## Control Logic

## Comms

ITC503s are on an RS232 connection direct into the MOXA.

Set communication details using macros for each of the 4 ITC503s (`1KPOT`, `SORB`, `HE3POT_HIGHT`, `HE3POT_LOWT`).

Required macros for each ITC503:
- PORT e.g. `SORB_PORT` set to `COM1`

Macros with defaults for each ITC503:
- Baud rate e.g. `SORB_BAUD`
- Bits e.g. `SORB_BITS`
- Parity e.g. `SORB_PARITY`
- Stop bit e.g. `SORB_STOP`
