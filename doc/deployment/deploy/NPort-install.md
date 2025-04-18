# Moxa NPort

To install/upgrade NPort driver:

1. Use remote desktop because you need admin privileges
1. Open NPort admin and note the IP address, Com ports and moxa ports for the current config (NB there maybe be multiple moxas)
1. Uninstall NPort using windows add/remove programs
1. Install the latest nport software from `...\installs\Installs\Applications\LabVIEW\Other bits\LabVIEW related\MOXA\MOXA NPort`
1. Open NPort Admin
1. Click Add
1. Search for the nport (click stop when it times out)
1. Clear All, then select the moxa you are using
1. Click OK, do not activate ports
1. Select all ports
1. Click Settings
1. Under basic settings Click "Auto Enumerating COM Number for Selected Ports"
1. Set Com to correct port (probably port 5)
1. Click OK.
1. Click Apply.
1. Ignore the message about setting moxa to real port.
1. Close NPort administrator

If the upon clicking apply you are told the port is in use, you may need to move to using NPort Driver Manager instead, it can be found here `\\isis\inst$\Kits$\CompGroup\Utilities\MOXA Nport Software`
