If nagios is reporting a critical memory usage for labview (which will only be on a SECI instrument) then you need to do the following:

first check to see if the nagios service has been acknowledged (has a tick next to it), it it has then these steps have already been followed and you need do nothing

compose an email with the from address set to "ISIS Experiment Controls" and the following content with `yyyy` replaced by the instrument name e.g. `OFFSPEC`
```
subject: SECI/Labview memory usage on NDXyyyy computer

Hi,

The SECI/LabVIEW memory usage on the NDXyyyy instrument computer is getting very high and the process may crash in the next few days, it would be advisable to restart the SECI control system at the next convenient point

Regards,

ISIS Experiment Controls
```

Now send this email to the special instrument address alias

Then acknowledge the service in nagios: click on `LABVIEW memory` for the instrument in the nagios view, then on the right of the next page click on `Acknowledge this service problem` and then give a comment like "emailed scientists" and press `Commit`. If you now return to the nagios service view, you should see a tick mark next to the service name. 

