# Lakeshore 336

The Lakeshore 336 is a temperature controller that has four input temperature readings (A, B, C, D) and four heater outputs (1, 2, 3, 4). The user can configure which heater output is paired up with which input.

This means that the temperature setpoint `TEMP1:SP` (and `TEMP1:SP:RBV`) could be matched to any of the temperature readings `TEMP_A`, `TEMP_B`, `TEMP_C` or `TEMP_D` depending on how the device is setup, and the user can change this dynamically.
This of course breaks our naming convention the blocks rely on to work. So the IOC has some extra PVs to deal with this, so the user can either rely on the names `TEMP_A`, `TEMP_A:SP`, `TEMP_A:SP:RBV`, or on the names `TEMP1`, `TEMP1:SP`, `TEMP1:SP:RBV`.


## IOC Setup
When connecting to the real device, the IOC requires its IP address, but the software installed on the device has a bug and does not return the correct IP address. Its network name, however, is correct.

To use the device, set the `IPADDR` macro to be the device hostname, e.g. `LKSH336_01__HOST=ls336-1`.

### Troubleshooting: device not reachable for IOC using hostname

The Lakeshore 336 has a strange issue where if it travels with some kit (for example the 3D Magnet) it needs to be forced to renew its DHCP lease. To do this, re-select "Ethernet" on the front panel of the device. If the address shown is 172.* then it has failed to connect to the network and defaulted to a private address, re-selecting ethernet should fix this. It may also be it is showing an old address, or one for the wrong experiment hall - reselecting ethernet should fix this. A third problem is that if somehow there are multiple Lakeshores with the same hostname on the network, reselecting will fix by overwriting the current DNS entry, but the other Lakeshore need to be located and renamed.    

If incorrect values are selected, it's likely the IOC has connected to another Lakeshore with the same hostname, change it on the front panel by pressing 6 (interface), selecting `modify ipconfig`, then scroll down to the hostname and edit it to something different with the arrow keys.

## Note on Implementation
The Lakeshore 336 IOC was originally taken from Diamond; the Diamond IOC is on a vendor branch of the support module and uses more functionality on the device than what we actually need (at least, at the time of writing). This means that in the support module you'll find some template files which we're not using: refer to the substitutions file in the ioc repo to see which templates we're using.

The template files we're using have been tweaked to fit our needs and have gone through a general PV renaming, to make them consistent with our naming convention. In the template files we're not using the PVs have NOT been renamed.

**NOTE**
The device has actually four outputs, two of one type and two of another type. In the original IOC, the functionality common to both types is in the `lakeshore336output.template` file, while the things that are specific to each output type are in separate files, `lakeshore336loop.template` and `lakeshore336analog.template`.

Now, some PVs (typically mbbi/mbbo) have their definition split in two files: the common fields in the common file, and the type-specific fields in the type-specific file.

So for example, this is the case for the PV `$(P):HEATER$(OUT):RANGE`: part of it is in `lakeshore336output.template` (for the fields common to both output types) and part in `lakeshore336loop.template` (for the fields specific to the output type we're using). The file `lakeshore336analog.template` still contains the fields specific to the other output type, it's just that there the PV appears with a different name because this file didn't go through our PV renaming!

