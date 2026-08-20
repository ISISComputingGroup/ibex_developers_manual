# Stanford SR850 Lock In Amplifier

The SR850 is a digital lock-in amplifier based on an innovative DSP (Digital Signal Processing) architecture. The SR850 boasts a number of significant performance advantages over traditional lock-in amplifiers—higher dynamic reserve, lower drift, lower distortion, and dramatically higher phase resolution.

A copy of the user manual is available here:  \isis\shares\ISIS_Experiment_Controls\Manuals\Stanford_Research_SR850_Lock-In_Amplifier

The manufacturer's web-site describes the [Stanford RS SR850](https://www.thinksrs.com/products/sr850.html)

## Troubleshooting

### Can't talk to device after it has been power cycled

Symptoms: commands are received and acted on by the box, but no replies come.

The device defaults to sending it's output to GPIB after a reboot. It still *listens* for commands via RS232, but no replies will be sent on RS232.

To fix:
- Stop IOC or pull serial cable from back of device (to prevent the device from being "stuck" in remote mode due to commands from IOC)
- Reboot physical device
- In device setup menu on the front of the box, choose "RS232" as the communication mode
- Plug serial cable back in / start IOC if it was stopped