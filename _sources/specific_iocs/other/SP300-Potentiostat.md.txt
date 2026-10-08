# SP300 Potentiostat

Implemented before we documented on the wiki, readme says

> You will need a copy of the EC-Lab OEM Development package from http://www.bio-logic.info/potentiostat-electrochemistry-ec-lab/software/oem-package/ to build and use this software The ECLABSDK macro in the Makefile will then need to point to this root
> 
> Beside EPICS BASE, the ASYN module is also needed and its location must be added to configure/RELEASE
>
> Note: this driver is still in development, contact freddie.akeroyd@stfc.ac.uk for further details
>
> https://www.bio-logic.net/softwares/oem-package/

The underlying [oem package](https://www.bio-logic.net/softwares/oem-package/) seems to support these devices so the driver may too:

- SP50/SP-150/SP-200/SP-240/SP-300,
- VSP/VSP-300, VMP3/VMP-300,
- MPG-2 series, HCP-803/HCP-1005

The device supports multiple technique but out driver only support the following (new techniques can be implemented on request):

- OCV - Open Circuit Voltage technique
- CA - Chrono-Amperometry technique
- PEIS - Potentio Electrochemical Impedance Spectroscopy technique
- CV - Cyclic Voltammetry technique
- LASV - 
- LOOP - Loop technique
- TO - Trigger Out technique
- TI - Trigger In technique
- TOS - Trigger Out Set technique
- VSTEP - 
- DURSTEP -

**Unsupported techniques**

- Cyclic Voltammetry Advanced technique
- Chrono-Potentiometry technique
- Voltage Scan technique
- Current Scan technique
- Constant Power technique
- Constant Load technique
- Staircase Potentio Electrochemical Impedance Spectroscopy technique
- Galvano Electrochemical Impedance Spectroscopy technique
- Staircase Galvano Electrochemical Impedance Spectroscopy technique
- Differential Pulse Voltammetry technique
- Square Wave Voltammetry technique
- Normal Pulse Voltammetry technique
- Reverse Normal Pulse Voltammetry technique
- Differential Normal Pulse Voltammetry technique
- Differential Pulse Amperometry technique
- Ecorr. Vs Time technique
- Linear Polarization technique
- Generalized Corrosion technique
- Cyclic PotentioDynamic Polarization technique
- PotentioDynamic Pitting technique
- PotentioStatic Pitting technique
- Zero Resistance Ammeter technique
- Manual IR technique
- IR Determination with PotentioStatic Impedance technique
- IR Determination with GalvanoStatic Impedance technique
