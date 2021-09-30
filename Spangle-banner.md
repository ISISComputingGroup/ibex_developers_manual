# Spangle banner (GUI)


The spangle banner in the GUI looks at a set of PVs and displays them at all times, regardless of the current configuration. The set of PVs to serve is contained in the blockserver, in a PV called `TE:NDWxxxx:CS:BLOCKSERVER:BANNER_DESCRIPTION`. Use 
```
caget -t -S %MYPVPREFIX%CS:BLOCKSERVER:BANNER_DESCRIPTION | uzhex
[{"local": "false", "pv": "DAE:SIM_MODE", "name": "DAE Simulation mode"}, ...]
```

This description is served as hexed compressed JSON. The items in the list are:
- `local`: Whether the GUI should prepend the local instrument's PV prefix
- `name`: The name of the item to display in the GUI
- `pv` the PV to look at

The way that the PVs are displayed in the GUI depends on the alarm state of the PV.

This ticket introduces the ability to add custom buttons, as well as the original items which display a PV. For displays, a new parameter has been added:
- `width`: the width of the item in pixels when displayed in the GUI (limited to between 10 and 500)

Buttons have the following parameters:
- `name`: the name of the item to display as text on the button in the GUI
- `pv`: the PV that the button writes to
- `local`: whether the GUI should prepend the local instrument's PV prefix
- `pvValue`: the value that the button writes to the PV (must be an integer)
- `textColour`: the colour of the text on the button as a hex colour, for example `#e0e0e0`
- `buttonColour`: the colour of the button
- `fontSize`: the font size of the text on the button (maximum of 16)
- `width`: the width of the button in pixels (limited to between 10 and 1000)
- `height`: the height of the button in  pixels (limited to between 10 and 35)

See the `xml` example below for the full structure. The order that the items are placed in the `xml` determines the order that they are placed in the GUI. The items in the GUI are aligned right, so the item at the top of `banner.xml` will be displayed on the furthest right, and the second item will be to the left of that, and so on.
Banner elements that were previously hard coded have now been moved to `banner.xml`. A new PV for the current configuration name was added to the Block Server in order to do this. Since PVs defined with `pcaspy` do not have a `.SEVR` field, this had to be defined manually in order to stop it being coloured pink in the GUI, see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/BlockServer-Structure#channel-access) for details.

# Configuration

In the settings area, create `C:\Instrument\Settings\config\NDWxxxx\configurations\banner.xml` with the following example structure:

```
<?xml version="1.0" ?>
<banner xmlns="http://epics.isis.rl.ac.uk/schema/banner/1.0" xmlns:blk="http://epics.isis.rl.ac.uk/schema/banner/1.0" xmlns:xi="http://www.w3.org/2001/XInclude">
  <items>
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
  </items>
</banner>
```

Once this ticket is merged, all instruments should have a `C:\Instrument\Settings\config\NDWxxxx\configurations\banner.xml`, and the stop motors button will have been moved from the GUI code into `banner.xml`. A typical example of this file is as follows:
```xml
<?xml version="1.0" ?>
<banner xmlns="http://epics.isis.rl.ac.uk/schema/banner/1.0" xmlns:blk="http://epics.isis.rl.ac.uk/schema/banner/1.0" xmlns:xi="http://www.w3.org/2001/XInclude">
  <items>
    <item>
      <button>
        <name>Stop All Motors</name>
        <pv>CS:MOT:STOP:ALL</pv>
        <local>true</local>
        <pvValue>1</pvValue>
        <textColour>#000000</textColour>
        <buttonColour>#e0e0e0</buttonColour>
        <fontSize>9</fontSize>
        <width>100</width>
        <height>25</height>
      </button>
    </item>
    <item>
      <display>
        <name>Motors are</name>
        <pv>CS:MOT:MOVING:STR</pv>
        <local>true</local>
        <width>170</width>
      </display>
    </item>
    <item>
      <display>
        <name>DAE Simulation mode</name>
        <pv>DAE:SIM_MODE</pv>
        <local>true</local>
        <width>250</width>
      </display>
    </item>
    <item>
      <display>
        <name>Manager mode</name>
        <pv>CS:MANAGER</pv>
        <local>true</local>
        <width>250</width>
      </display>
    </item>
    <item>
      <display>
        <name>Config</name>
        <pv>CS:BLOCKSERVER:CURR_CONFIG_NAME</pv>
        <local>true</local>
        <width>360</width>
      </display>
    </item>
  </items>
</banner>
```