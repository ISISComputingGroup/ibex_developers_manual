# Spangle banner (GUI)

*Note: the following will apply once https://github.com/ISISComputingGroup/IBEX/issues/3010 is merged*

The spangle banner in the GUI looks at a set of PVs and displays them at all times, regardless of the current configuration. The set of PVs to serve is contained in the blockserver, in a PV called `TE:NDW1799:CS:BLOCKSERVER:BANNER_DESCRIPTION`. Use 
```
caget -t -S TE:NDW1799:CS:BLOCKSERVER:BANNER_DESCRIPTION | uzhex
[{"local": "false", "pv": "DAE:SIM_MODE", "name": "DAE Simulation mode"}, ...]
```

This description is served as hexed compressed JSON. The items in the list are:
- `local`: Whether the GUI should prepend the local instrument's PV prefix
- `name`: The name of the item to display in the GUI
- `pv` the PV to look at

The way that the PVs are displayed in the GUI depends on the alarm state of the PV.

# Configuration

In the settings area, create `C:\Instrument\Settings\config\NDWxxxx\configurations\banner.xml` with the following example structure:

```
<?xml version="1.0" ?>
<banner xmlns="http://epics.isis.rl.ac.uk/schema/banner/1.0" xmlns:blk="http://epics.isis.rl.ac.uk/schema/banner/1.0" xmlns:xi="http://www.w3.org/2001/XInclude">
    <item>
        <name>DAE Simulation mode</name>
        <pv>DAE:SIM_MODE</pv>
        <local>true</local>
    </item>
    <item>
        <name>Manager mode</name>
        <pv>CS:MANAGER</pv>
        <local>true</local>
    </item>
</banner>
```
