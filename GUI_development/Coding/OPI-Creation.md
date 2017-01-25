> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > OPI creation

# Introduction
OPIs live in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`

Start CSS studio to create/edit an OPI (see `EPICS\CSS\master\start_css.bat`)

Load in the project in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`: File -> Import -> General -> Existing Projects into Workspace.

Set the correct path for the Fonts and Colours files: Edit -> Preferences -> CSS Applications -> Display -> BOY. For the colour file choose `/resources/Share/isis_colours.def`; for the font file choose `/resources/Share/isis_fonts.def`.

Create a new OPI with File -> New  BOY -> OPI File
Change to the "OPI Editor" prespective to allow easier editing.

Edit the OPI not that some Macros are provided.

## Consistency - Template OPI
In order to promote consistency in look and feel between different OPIs, we have created a template OPI in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources\template.opi`. Please follow the guidelines provided in this template, including ALL fonts and colours (is probably easiest to just copy the widgets from this template). If you're adding new widgets in your OPI which are not covered by this template, please add them to the template.

Please also make sure your OPI works well for colour blind users, following [these guidelines](Designing-for-Colour-Blindness).

If you are converting an existing OPI from the old to the new style, be aware of [these tips and gotchas](Converting-to-New-Style-Tips-and-Gotchas).

There is a script called `check_opi_format.py` in `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis` that can help you check certain aspects of a new OPI. This script does not replace checking the OPI visually, but should help catch some style errors in OPIs. This will iterate over all OPIs in the `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources` directory, and write logs to the `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\check_OPI_format_logs` directory.

Usage examples:
- `python check_opi_format` - Default behaviour, will iterate through `.opi` files in the `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources` directory
- `python check_opi_format Eurotherm.opi` - Will check a single file in the default directory which is `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`.
- `python check_opi_format Lakeshore336.opi C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources\Lakeshore336` - Will check a single file in the specified directory.

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
* `value.macro.macro.description`: description of macro value which appears in target details when user clicks on the macro. For the macro that contains the IOC name, please provide an example of actual IOC name in brackets.

You can specify which icon should appear in the synoptic with the file `ui/devicescreeens/ComponentIcons.java`.
If you need to add new icons for the synoptic, these are under `uk.ac.stfc.isis.ibex.ui.devicescreens/icons` (both big icons for the actual synoptic and thumbnails for the synoptic editor). Please follow [these guidelines](Synoptic-Icons) when creating new synoptic icons.

  
# Testing

To start and interact with a testing IOC see [Running (and testing) IOC](Running-IOCs)



