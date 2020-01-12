# TDK Lambda Genesys

The TDK Lambda Genesys is a power supply for conventional (non-superconducting) magnets. It is on use on several muon beamlines as a transverse field magnet, as well as several magnets in the muon front end.

These power supplies can be daisy-chained in groups of up to 10 power supplies simultaneously; one IOC talks to the entire chain of power supplies.

# Macros

As well as the typical communication macros such as `BAUD`. `BITS`, `PARITY` etc, there are a number of specialist macros for each power supply in this IOC:

| Macro | Explanation |
| -- | -- |
| AMPSTOGAUSS | A factor which converts the Amps which are reported by the power supply to Gauss (a measure of magnetic field). This value depends on exactly which magnet the power supply is plugged in to. **Not all magnets use this factor; if it is set to the empty string, the "field" section will be hidden on the OPI. This is the case for all of the magnets on MUONFE (they just control on Amps/Volts for those magnets).** |
| MAX_VOLTAGE | The maximum allowable voltage (in Volts). |
| MAX_CURRENT | The maximum allowable current (in Amps). |
| READ_OFFSET | An offset, in Amps, which is added to the value reported by the power supply before being displayed on the OPI and used to calculate the field. |
| WRITE_OFFSET | An offset, in Amps, to add to any current setpoints before they are sent to the power supply. |
 

