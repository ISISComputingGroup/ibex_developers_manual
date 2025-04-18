# Moxa e12xx

## Device notes

* The bulk of this driver was written by a third party (original repo [here](https://gitlab.com/LBCS-ELI-BL/epics-ioc-moxa-e12xx_pub)). The third party code, extended for the e1210 and minimally modified for use on IBEX lives in the moxa1210 support module.

* The IOC folder for this device contains records to map from the vendor PV naming convention to the IBEX PV conventions.
    * The code to assign aliases to channel inputs also lives here and not in the support module to keep the vendor-supplied driver clean.

* I could not get the hardware counter to work
   * I used the web interface to change the state of one of the inputs from DI (input mode) to Counter, but this request was rejected by the device `"invalid token"`.
   * PVs exist which _should_ interact with this functionality, but this is not tested as I couldn't get the device to enter this mode
   * The [original ticket](https://github.com/ISISComputingGroup/IBEX/issues/3269) for this hardware does not require a functional counter, so this hasn't been taken any further

## Finding a moxa e1200 series device on the network

Moxa provides a tool, `ioSearch`, to find 12xx series devices which have DHCP allocated IPs on the network. For this to work you must be using a computer which is on the same subnet as the device. `ioSearch` is found in the manuals share under `<manuals share>\MOXA E1200 Series\moxa-iologik-e1200-series-iosearch-utility-v2.0.0.zip`. Extract this file and run the installer. When starting the program, UAC will ask for administrator privileges.

### Using the IP locate tool
Once loaded, click 'start search' in the top-right of the dialogue which opens. This will begin the search for any device on your subnet in the e1200 series. One can target a specific model by deselecting other models.

Once the search is completed, the IP addresses of any devices found will be displayed in the table. To perform another search, click the leftmost icon from the row of icons at the top of the screen. Once you have found the device you are looking for, you may access its web interface either by typing its IP address into a web browser or clicking the device's name in the list on the left hand side of the screen.

## Enabling DHCP
By default, the device should be connected using DHCP. If this is not the case, DHCP can be enabled through the device's web interface. First, go to `Network settings > Ethernet connection` from the menu in the web interface. Then select DHCP on the IP configuration drop-down box. The default static IP is written on the side of the device.

## Conversion of integer values to floating points

Some models in the ioLogik e12XX line provide floating point values. These include the e1240 which outputs a voltage; and the e1262 which outputs a temperature. These are encoded as unsigned integers in two consecutive registers. To combine these values into one floating point number using python one can follow [this stack overflow answer](https://stackoverflow.com/a/35603706):

```
import struct
register_values = (26214, 16878)
packed_string = struct.pack('HH', *register_values) # HH defines two unsigned ints.
                                                    # *register_values treats the values as a void
unpacked_float = struct.unpack('f', packed_string)[0]
print(unpacked_float) # Value should be 30.5. This is a Celcius measurement taken with an e1262.
```

## Emulation and testing

* This is a modbus device, which adds complications when testing and emulating.

* Recsim is difficult to get working as a modbus device relies on I/O interrupts and AsynInt/AsynFloat types, both of which make it much more difficult to get a record simulation to work. See [Record Simulation](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Record-Simulation)
   * Therefore, this device has no RECSIM tests.

* There is a crude DEVSIM/lewis emulator, but support for modbus in the lewis framework is minimal.
   * The workaround here is to include a line in the modbus interface to allow the device to hook in and access the data banks. See the modbus_interface.py in the moxa e1210 lewis emulator for an example.
   * This means that, unlike a stream interface device, the data will be held within the interface.
   * Any commands that the device will need to execute will need to be called directly through the backdoor
   * These commands will need to access the data through self.interface, rather than accessing the data directly on the device.