> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Lakeshore 336

The Lakeshore 336 is a temperature controller that has four input temperature readings and two heater outputs. The user can configure which heater output is paired up with which input.

## IOC Setup
When connecting to the real device, the IOC requires its IP address, but the software installed on the device has a bug and does not return the correct IP address. Its network name, however, is correct.

To use the device, set the IPADDR macro in globals.txt to be the device network name, e.g. `LKSH336_01__IPADDR=ls336-1`.

## Note on Implementation
The Lakeshore 336 IOC was originally taken from Diamond; the Diamond IOC is on a vendor branch of the support module and uses more functionality on the device than what we actually need (at least, at the time of writing). This means that in the support module you'll find some template files which we're not using: refer to the substitutions file in the ioc repo to see which templates we're using.

The template files we're using have been tweaked to fit our needs and have gone through a general PV renaming, to make them consistent with our naming convention. In the template files we're not using the PVs have NOT been renamed.

**NOTE**
The device has actually four outputs, two of one type and two of another type, and we're only using one type. In the original IOC, the functionality common to both types is in the lakeshore336output.template file, while the things that are specific to each output type are in separate files, lakeshore336loop.template and lakeshore336analog.template.

Now, some PVs (typically mbbi/mbbo) have their definition split in two files: the common fields in the common file, and the type-specific fields in the type-specific file.

So for example, this is the case for the PV $(P):HEATER$(OUT):RANGE, which we're using: part of it is in lakeshore336output.template (for the fields common to both output types) and part in lakeshore336loop.template (for the fields specific to the output type we're using). The file lakeshore336analog.template still contains the fields specific to the other output type, it's just that there the PV appears with a different name because this file didn't go through our PV renaming!

