# Device notes

* The bulk of this driver was written by a third party (original repo [here](https://gitlab.com/LBCS-ELI-BL/epics-ioc-moxa-e12xx_pub)). The third party code, extended for the e1210 and minimally modified for use on IBEX lives in the moxa1210 support module.

* The IOC folder for this device contains records to map from the vendor PV naming convention to the IBEX PV conventions.
    * The code to assign aliases to channel inputs also lives here and not in the support module to keep the vendor-supplied driver clean.

* I could not get the hardware counter to work
   * I used the web interface to change the state of one of the inputs from DI (input mode) to Counter, but this request was rejected by the device `"invalid token"`.
   * PVs exist which _should_ interact with this functionality, but this is not tested as I couldn't get the device to enter this mode
   * The [original ticket](https://github.com/ISISComputingGroup/IBEX/issues/3269) for this hardware does not require this, so this hasn't been taken any further


# Emulation and testing

* This is a modbus device, which adds complications when testing and emulating.

* Recsim is difficult to get working as a modbus device works on I/O interrupts and 