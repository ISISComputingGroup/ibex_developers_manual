> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) 
> Configure Mini Inst

To install a mini inst, you need to install the EPICS backend and add the following in the `\NDXxxxxx\configurations\` area.

- `startup.txt`: contains a list of the IOCs to start (use the IOC name as in the IOCs list)
- `globals.txt`: add macro values you want the IOCs in `startup.txt` to start up with. To do this, add a line per macro of the format `<IOC_name>__<macro_name>=<macro_value>`

You can start up the mini inst using the normal `start_ibex_server`. It will look for the `startup.txt` and start up the mini inst instead of the full IBEX server if it exists.
