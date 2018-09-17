> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [DAQ](DAQ) > [Muon Separator Power Supply](Muon-Separator-Power-Supply)  

The Muon Separator Power Supply is controlled by a National Instruments DAQ-Mx, since IBEX cannot communicate directly with the Separator PSU. The configuration for the DAQ is done in `EPICS\ioc\master\SEPRTR\iocBoot\iocSEPRTR-IOC-01\st-daq.cmd`


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

The stability boundaris are defined as:
1. Voltage stability: `V_lower_limit < V_measured < V_upper_limit`
1. Current stability: `I_measured <= (I_stable + I_limit)`