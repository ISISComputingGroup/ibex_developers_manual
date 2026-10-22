# Ambrell EASYHeat Induction Furnace

:::{attention}
To date (18/07/2025) the IOC has **not** been tested with the device nor has the hardware itself in isolation.
:::

This is a new piece of equipment due to be used on ENGIN-X, and because of that, the scientists will initially control it manually via its local panel, using IBEX to read and log diagnostic data remotely (IOC is READONLY).  It is envisaged that the equipment will be configured for a particular experiment and left in that state during neutron data collection, while being monitored from IBEX.

There appear to be two models of induction furnace - the EKOHeat and EASYHeat, the latter of which has been purchased by ENGIN-X.

The communications manual for these devices, which is stored in the usual network shared area, is unclear as to which commands are supported by which model and exactly what the format is of the replies.

:::{note}
This device uses RS485, and will require a custom cable to be made up to connect it directly to a MOXA NPort (8P8C <-> 8P8C).
:::

**More information will be added to this page once the device has been tested along with its IOC.**
