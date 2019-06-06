> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) > [Configure Mini Inst](Configure-Mini-Inst)

To install a mini inst, you need to install the EPICS backend and add the following in the `\NDXxxxxx\configurations\` area.

- `startup.txt`: contains a list of the IOCs to start (use the IOC name as in the IOCs list)
- `globals.txt`: add macro values you want the IOCs in `startup.txt` to start up with. [To do this, add a line per macro of the format `<IOC_name>__<macro_name>=<macro_value>`](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Create-and-Manage-Configurations#editing-a-global-setting)

### Startup and shutdown

You can start up the mini inst using the normal `start_ibex_server` and stop it with `stop_ibex_server`. It will look for the `startup.txt` and start up the mini inst instead of the full IBEX server if it exists.

### Updating config

If you update a configuration in [globals.txt](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Create-and-Manage-Configurations#editing-a-global-setting) then don't forget to restart the IOC. This can be done either by running `start_ibex_server` but it is more efficient to console to the IOC and restart it using `ctrl+x`.


