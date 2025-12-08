# Mirion Lynx2 HPGe detector

The Lynx HPGe detector is a gamma detector, used on VESUVIO as a gamma detector. It may also be called
a "digital signal analyzer" or a "multichannel analyzer", and is made by a company called Mirion.

## Manual

A manual for the device is available at:
```
\\isis\shares\ISIS_Experiment_Controls\Manuals\lynx2-gamma-detector
```

## Hardware / Networking

We do **not** talk to this device from IBEX in any way.

The hardware is an ethernet device, which should be set up in DHCP mode to automatically acquire an IP address.

Configuration screens for the hardware are available by visiting its IP address in a web browser. Use:

```
http://x.x.x.x/mainex.asp
```

to access the configuration screens, as the _home_ page requires flash player, but the hardware configuration
screens do not.

If the device is (incorrectly) set to static IP mode, it will likely default to an IP of `10.0.0.3`. If the device has
forgotten its DHCP setting, then you may need to connect to the device directly (point-to-point) from NDCVESUVIO or
another computer, with netmask `255.255.255.0`.

The settings *should* look like this:

![expected settings](lynx/network_settings.jpeg)

## Software

The device is controlled using a program called "GENIE2K", which runs on **NDC**VESUVIO. This software is licensed to
a specific computer, so cannot be run on another computer. This software is unrelated to OpenGENIE - it is manufacturer
software. It does not integrate with IBEX in any way.
