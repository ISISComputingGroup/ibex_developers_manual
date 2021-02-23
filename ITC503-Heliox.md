Original implementation for use on MuSR 3He refrigerator. The device is a Heliox/ITC503 based refrigerator.

## Control Logic

## Comms

ITC503s are on an RS232 connection direct into the MOXA.

Set communication details using macros for each of the 4 ITC503s (`1KPOT`, `SORB`, `HE3POT_HIGHT`, `HE3POT_LOWT`). The required settings are the port for each ITC503 e.g. setting `SORB_PORT` to `COM1`. You can also set the baud rate, bits, parity and stop bit e.g. for the `SORB`: `SORB_BAUD`, `SORB_BITS`, `SORB_PARITY` and `SORB_STOP`, all of which have default values. For testing, you can set the emulator port with e.g. `SORB_EMULATOR_PORT`.
