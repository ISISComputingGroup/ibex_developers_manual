From time-to-time, IBEX encounters problems determining the value of a PV (e.g. because of a communication error on a device).  The purpose of this page is to set out the conventions used by IBEX to indicate to the user that the value of a PV or block should be considered invalid.

Blocks are, essentially, aliases for PVs.  Therefore, if the value of a PV cannot be determined, the value of a corresponding block is equally invalid.

# Situations Giving Rise to Invalid Values
The following situations can cause process variables (PVs) to be considered invalid.
* communication error between a device and IBEX
* a device generates a value which is outside valid range of a calibration algorithm.
* device reports that a value is invalid (i.e. over range)

There may be other situations which can cause process variables (PVs) to be considered invalid.  If so, define them here.

## Communication Errors
When EPICS detects a communication error with a device, it does two things:
1. the PV continues to hold the last-known value
1. the alarm status of the PV is changed to `INVALID`

## Calibration Errors
Some devices return "raw" values from sensors.  Such values have to be converted into meaningful physical values via some kind of calibration algorithm (in most cases, the algorithm is merely a simple linear conversion or a table lookup plus linear interpolation).  For example, a Eurotherm returns the raw voltage returned from a thermocouple, which is converted into a temperature using a lookup table.

All calibration algorithms have a range of validity - if the "raw" sensor value falls outside that range the calibrated physical value should be considered invalid.  Calibration calculations are performed in the IOC, therefore, any out of range errors have to be signalled by the IOC.  In this situation, it is suggested that the IOC behaves as follows:
1. the PV holds the converted value (even though it might be invalid)
1. the alarm status of the PV is changed to `[can-we-invent-a-calibration-alarm?]`

# IBEX Conventions for Invalid Values
For each type of invalid value (described above), IBEX will behave according to the conventions described below.  There are specific conventions for different features of IBEX - the dashboard area of the IBEX GUI (i.e. the IBEX client), log files, genie_python, the Web Dashboard.

## Communication Errors:
In this situation IBEX cannot read a value from a device.  In practice, this means EPICS will signal an `INVALID` alarm on a PV.  On encountering an `INVALID` alarm, IBEX will behave as follows:
#### IBEX GUI
1. In the dashboard, blocks will display the text "N/A" and be surrounded by a purple border
1. In OPIs, readback fields (which display PVs, not blocks) will display the last-known-good-value and be surrounded by a purple border.  On hovering the mouse over a readback field, IBEX will display a pop-up box showing the PV name, the last-known-good-value and the alarm status.

#### Log & Data Files
1. In the NeXus data file, blocks will be logged with their last-known-good-value and the alarm status.
1. In the IBEX archive, PVs will be logged with their last-known-good-value and the alarm status.

Applications or scripts which process log & data files are responsible for checking the alarm status of a block or PV and taking appropriate action.

#### genie_python
In genie_python, `cget` is used to obtain the value of a block or PV.  `cget` always 
1. returns the value of a block or PV
1. returns the alarm status of the block or PV
1. prints a warning message if there is an alarm on the block or PV.

It is the responsibility of the script author to check the alarm status and take any subsequent actions required.

#### Web Dashboard
1. In the web dashboard, blocks will display the text "INVALID" and be surrounded by a red border

## Calibration Errors
At the current time, there is no agreed convention.

## Alternative Conventions
IBEX has adopted the conventions defined above.  Other systems and devices have adopted different conventions for signalling that a readback value might be invalid.  We have deliberately decided not to follow these conventions to avoid the risk of ambiguity or clashes in interpretation.

### Why haven't we used NaN?
NaN, which means "not a number", is a concept used in computing to represent the results of calculations that are somehow "indeterminate".  Superficially, therefore, it might seem that NaN is a good candidate for representing an invalid value. 
However, there are several reasons for not choosing NaN for this purpose:
1. Specifically, NaN, as defined by the IEEE-754 standard, applies only to floating-point numbers.  There is no concept of NaN for integer-valued variables.  Nor is there an equivalent concept for string-valued variables.  So, NaN is a only a partial solution, at best.
1. Some devices use NaN to signal that a value has not been defined or initialized.  Strictly speaking this is an abuse of the IEEE-754 standard.  Nevertheless, because some device manufacturers have adopted this convention, it means that there is a risk of confusion - if a device returns NaN does it mean that the value was never initialized, or has it become invalid (having previously been valid)?
1. In arithmetical expressions, NaNs behave as follows:
   * `anything + NaN = NaN` - i.e. NaNs propagate through arithmetical operations
   * all comparisons involving NaNs return `FALSE` (except the `!=` operator, which returns `TRUE`).
1. If NaNs appear in data or log files, then any code reading such files might need modification to take appropriate action on encountering a NaN.
