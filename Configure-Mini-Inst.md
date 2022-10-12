> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) > [Configure Mini Inst](Configure-Mini-Inst)

To install a mini inst, you need to install the EPICS backend and add the following in the `\NDXxxxxx\configurations\` area.

- `startup.txt`: contains a list of the IOCs to start (use the IOC name as in the IOCs list)
- `globals.txt`: add macro values you want the IOCs in `startup.txt` to start up with. [To do this, add a line per macro of the format `<IOC_name>__<macro_name>=<macro_value>`](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Create-and-Manage-Configurations#editing-a-global-setting)

### Startup and shutdown

You can start up the mini inst using the normal `start_ibex_server` and stop it with `stop_ibex_server`. It will look for the `startup.txt` and start up the mini inst instead of the full IBEX server if it exists.

### Updating config

If you update a configuration in [globals.txt](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Create-and-Manage-Configurations#editing-a-global-setting) then don't forget to restart the IOC. This can be done either by running `start_ibex_server` but it is more efficient to console to the IOC and restart it using `ctrl+x`.

### Adding Devices

If you want to run an IOC in a mini-inst then:

1. Add the device name to the "startup.txt" (`C:\Instrument\Settings\config\NDX<instrument>\configurations\startup.txt`)
   - e.g. JSCO4180_01
1. Then set macros in "globals.txt" (`C:\Instrument\Settings\config\NDX<instrument>\configurations\globals.txt`)
   - e.g. JSCO4180_01__PORT=COM13
1. Run `make iocstartups` in the epics terminal. This adds the device to the allowed running devices.
1. Start IBEX server as normal `start_ibex_server.bat`
1. If you are running the IOC to allow a Vi in SECI to communicate then configure that vi (usually the pv prefix)
   - e.g. Run `C:\LabVIEW Modules\Drivers\Jasco PU-4180 HPLC Pump\Jasco HPLC Pump - System.llb` - Initialisation File change IOC Root to `IN:CRISP:JSCO4180_01:`
1. Run the Vi


### Running `ARINST` and/or `ARACCESS` in a mini-inst

ENGIN-X will run a mini-inst for the instron stress rig that needs to use both `ARINST` and `ARACCESS`. These need to be added to `startup.txt` and MySQL needs to be installed and running on the machine.






