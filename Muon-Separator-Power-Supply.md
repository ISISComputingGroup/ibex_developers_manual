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


