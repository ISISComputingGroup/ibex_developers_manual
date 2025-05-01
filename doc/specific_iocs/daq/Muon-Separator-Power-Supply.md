# Muon Separator Power Supply

The Muon Separator Power Supply is controlled by a National Instruments DAQ-Mx, since IBEX cannot communicate directly with the Separator PSU. The configuration for the DAQ is done in `EPICS\ioc\master\SEPRTR\iocBoot\iocSEPRTR-IOC-01\st-daq.cmd` There is further documentation on how the separator works [here](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Muon%20FE/Supporting%20the%20Muon%20Separator.pptx).


The DAQ uses 4 AI ports and 4 AO ports used as such:

| AI Port| Use               | --- | AO Port | Use |
| --- | ---                  | --- | --- | --- |
| 0 | Read Kicker Voltage    | --- | 0 | Not used |
| 1 | Read Kicker Current    | --- | 1 | Not used |
| 2 | Read Separator Voltage | --- | 2 | Set Separator Voltage |
| 3 | Read Separator Current | --- | 3 | Not used |

Each port sends or receives a voltage in the range 0-10V. The actual separator PSU operates between 0-200kV and 0-2.5mA, so some scaling is needed

The calibration (scaling) relationship is:
- Separator Voltage: 0-10V (DAQ) = 0-200kV (PSU)
- Separator Current: 0-10V (DAQ) = 0-2.5mA (PSU)

## Separator stability

The calculation of the stability of the muon power supplies is calculated in two stages. First, the number of data points which lie out of the current and voltage stability boundaries is calculated from a sample set of data from the cDAQ. The record which calculates this is updated with every update from the voltage from the device, both voltage and current aren't used to trigger this calculation as this could double count some data.

This data accumulates over one second until a timekeeper PV activates and sends the total number of data points which lie outside the stability boundary recorded in that second to a circular buffer. This buffer is kept in an aSub record, its default length is 600s (10 minutes).

To recover the amount of time which was spent outside of the stable boundary, multiply the number of samples collected by the time each sample represents, (1/sample frequency). This value is exposed in a PV for a nagios alarm to monitor.

The stability boundaries are defined as:
1. Voltage stability: `V_lower_limit < V_measured < V_upper_limit`
1. Current stability: `I_measured <= (I_stable + I_limit)`

**N.B**: When the stability limits are set so that the signal is always unstable, then the unstable time will sometimes not equal the buffer size due to data loss. This will be a large problem if the frequency is larger than the number of elements.

## Moving average Filtering
After installing the separator software on MUONFE, we found interference on the voltage input. To counter this, a filtering scheme was developed, described in the python notebooks here: https://github.com/ISISComputingGroup/separator-signal-analysis

This takes a moving average of two adjacent points, although a different stride length (number of indices between 
the two points) of 20 was also considered. The stride length is currently a constant (1) in the c++ source, and the python test libraries

An aSub record to perform this is now referenced in the separator's voltage db file. The data flow for voltage now looks like:

1. Raw data `$(P)DAQ:VOLT:_RAW`
1. Calibration `$(P)_APPLYVOLTCALIB`
    - Calibrated data `$(P)CALIBRATE:VOLT`
1. Filtering `$(P)_APPLYVOLTFILTER`
    - Filtered Data `$(P)FILTERED:VOLT`

To remove the filtering from the data flow, change the INAA field of `_STABILITYCHECK` in the separator stability db file to point at `$(P)CALIBRATE:VOLT`.

### Data loss at large stride lengths
As a consequence of performing a moving average, the shape of voltage input data is reduced by the stride length. This means that there will be fewer data points than the (unfiltered) current data, so the assumption of the separator stability calculation that there are the same number of points for both current and voltage is no longer valid. It was decided that a stride length of 1 does not 'stretch out' the voltage trace enough to break the assumption. A longer stride length (e.g. 20) would be a significant source of error and need to be addressed.