# Knauer Valve Unifier (VU4.1)

This is an updated version of the older {doc}`Knauer-k-6` - the older model is becoming unreliable
due to old age.

:::{important}
This device uses the `KNRK6` IOC and OPI, with:
- `COMMS_MODE` set to `ip`
- the relevant IP address provided using the `HOST` macro.
:::

Manufacturer manual is available at:
```
\\isis\shares\ISIS_Experiment_Controls\Manuals\Knauer Valve Unifier VU4.1
```

## Connection details

The device should be plugged in to the network using the "LAN 1" port. It should acquire an IP address
by DHCP, this can be verified using menus on the device.

Existing devices should have their IP reserved in DHCP for both R55 and R80 as these are movable devices.
These reserved IPs are written on labels on the device. A listing of known pumps and their reserved DHCP IP addresses is available in the manuals folder.

The device will respond to a `ping`.

![](knauer_valve_unifier.png)
