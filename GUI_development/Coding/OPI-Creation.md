> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > OPI creation

# Introduction
OPIs live in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`

 - Start CSS studio to create/edit an OPI (see `EPICS\CSS\master\start_css.bat`)
 - Load in the project in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`: File -> Import -> General -> Existing Projects into Workspace.

 - Set the correct path for the Fonts and Colours files: Edit -> Preferences -> CSS Applications -> Display -> BOY. For the colour file choose `/resources/Share/isis_colours.def`; for the font file choose `/resources/Share/isis_fonts.def`.

 - Create a new OPI with File -> New  BOY -> OPI File
 - Change to the "OPI Editor" perspective to allow easier editing.
 - You need to use "OPI Editor" to edit your files, **not** "Display Editor". The later creates a display builder file and not an OPI.
 - Edit the OPI.
 - Also add an entry to the `opi_info.xml` file which can be found in `resources\opi_info.xml`. Note that some Macros are provided (See below).

## OPI Editor vs Display editor
When editing an existing OPI or creating a new one, it is important to use OPI editor over Display editor, as the display editor is not currently compatible with the rest of IBEX. If you have opened an OPI and can't find the ISIS colour and font schemes, this possibly indicates that you are using the wrong toolset. You may also find that the file extension is being changed to a .bob file when the file is saved in a Display editor window. Re-opening the file in an OPI editor window (right click OPI -> Open With -> OPI Editor) may solve these issues.

## Consistency - Template OPI
In order to promote consistency in look and feel between different OPIs, we have created a template OPI in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources\template.opi`. Please follow the guidelines provided in this template, including ALL fonts and colours (it's probably easier to just copy the widgets from this template). If you're adding new widgets in your OPI which are not covered by this template, please add them to the template.

Please also make sure your OPI works well for colour blind users, following [these guidelines](Designing-for-Colour-Blindness).

If you are converting an existing OPI from the old to the new style, be aware of [these tips and gotchas](Converting-to-New-Style-Tips-and-Gotchas).

There is a script called `check_opi_format.py` in `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis` that can help you check certain aspects of a new OPI. This script does not replace checking the OPI visually, but should help catch some style errors in OPIs. This will iterate over all OPIs in the `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources` directory, and write logs to the `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\check_OPI_format_logs` directory by default. Other behaviours are described below:

Usage:
`python check_opi_format.py [-h] [-file FILE] [-directory DIRECTORY] [-logs_directory LOGS_DIRECTORY]`

e.g. 
`python check_opi_format.py -directory resources/Lakeshore336 -file Lakeshore336.opi -logs_directory my_logs_directory`
will scan a single OPI in `resources/Lakeshore336/Lakeshore336.opi` and save the logs in `/my_logs_directory/`

## Macros
When an OPI is opened from the synoptic (via OpiTargetView.java) you get at least the following macros automatically set:

- `NAME`: the OPI title, as defined by the synoptic component editor (e.g. "Slit 2"). When setting up the OPI this acro should be in the Name property of the OPI.
- `OPINAME`: name of the OPI file opened (e.g. Slit.opi)
- `P`: the instrument pv prefix (e.g. IN:LARMOR:)
Others macros may also be available, passed down from higher screens (also defined via the synoptic editor component)

One convention we have used is to define a macro within the opened OPI called PV_ROOT which we then use to make full PV names. So at the top of the OPI XML would be something like

    <macros>
      <include_parent_macros>true</include_parent_macros>
      <PV_ROOT>$(P)$(EUROTHERM)</PV_ROOT>
    </macros>

here EUROTHERM would be a parameter passed from the synoptic and it is combined with P to create the prefix for all PVs referenced within the OPI screen. The macro name should be something like the un-shortened device name, and its value would typically be the IOC name used in the PVs, e.g. EUROTHERM_01.

### Other Standard Macro Names

| Name | Meaning |
| ---- | ------- |
| PV_ROOT | Root for all PVs within an OPI |

# Completing the OPI

Add the IOC name with appropriate information, including macros to the xml file

  ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources\opi_info.xml

In the xml file:
* `key`: unique name for component
* `value.type`: the component type, same as name of constant in ComponentType (uk.ac.stfc.isis.ibex.synoptic.model)
    This enables the correct component target details to be added when component details are selected
* `value.path`: the path to the opi file (relative to the resources folder)
* `value.description`: description which is shown in target details
* `value.macros.macro.name`: name of macro in OPI
* `value.macro.macro.description`: description of macro value which appears in target details when user clicks on the macro. For a macro that contains the IOC name please provide an example with the actual IOC name in brackets.

You can specify which icon should appear in the synoptic with the file `uk.ac.stfc.isis.ibex.ui.devicescreens/ComponentIcons.java`.
If you need to add new icons for the synoptic, these are under `uk.ac.stfc.isis.ibex.ui.devicescreens/icons` (both big icons for the actual synoptic and thumbnails for the synoptic editor). Please follow [these guidelines](Synoptic-Icons) when creating new synoptic icons.

  
# Testing

To start and interact with a testing IOC see [Running (and testing) IOC](Running-IOCs)
The easiest way to test this is to run IBEX-gui through the eclipse editor. Create a device screen and use this to test The device screen can be refreshed (right click -> refresh) to display the latest changes made in CSS editor.

# Debugging: No scrollbars

Check if you have stray widgets. An example of a stray widget might have:

```
<x>-2147483647</x>
<y>2147483496</y>
```

If you have a stray widget, it may prevent scrollbars from appearing on your OPI. It might be possible to solve the issue by selecting and copying the elements to a new OPI. You can then diff the old version and the copied version using the following tools:
- XML sorter e.g. [https://xmlsorter.codeplex.com/](https://xmlsorter.codeplex.com/)
- Diff tool e.g. notepad++, winmerge

# Writing to char waveform PVs

CSS text input fields can write to char waveform PVs but needs to be set up in a special way. If you don't do this, the `NORD` field of the waveform will not be set correctly on write and the PV value will only be written successfully if NORD already has a large enough value.
- Postfix the PV name with ` {"longString":true}` (note the space before the JSON). The final value in "PV Name" should look similar to the following: `$(PV_ROOT):ARBITRARY:SP {"longString":true}`
- Ensure "Format Type" is "String"

# Data browser Graph Creation

To make a databrowser graph on an OPI:

1. In CSS go to the data browser perspective
1. Click button "Add new databrowser plot" which is graph with a plus on in the tool bar
1. Right click -> Add a PV/PVs
1. PV should start with `$(PV_ROOT)` and end in `.VAL`, e.g. `$(PV_ROOT)POS.VAL`
1. Alter colours, remove/add title and legend, rename axis
1. Save in the resources folder, probably in a subfolder for the device (extension will be added automatically as .plt)
1. Add a `Data Browser` monitor to your opi
1. In properties in file set the file you have created

# Activate tab

If it's required to activate a tab from a synoptic via a macro: (See SKF G5 Chopper OPI as an example.)

1. Put macro in local PV
1. Create script that reads value
1. Set active tab on tab container using `setActiveTabIndex`

# Create a Local Enum

Create a local pv in an opi with labels (From Tech talk article not tested).

    loc://demo<VEnum>(2, "A", "B", "C", "D")

If you cannot use an actual enum PV because there are too many labels, and you can't use a local enum PV because that doesn't allow changes to the enum labels, then don't use an enum PV. Instead, on the combo box, un-check the option to get "Items from PV" and directly enter the items, as many as you want.
Or set the items from a script:
```
    from org.csstudio.display.builder.runtime.script import ScriptUtil
    combo = ScriptUtil.findWidgetByName(widget, "Name Of My Combo")
    combo.setItems( [ "Ene", "Mene", "Muh" ] )
```