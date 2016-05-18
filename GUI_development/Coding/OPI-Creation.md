> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > OPI Creation

# Introduction
OPIs live in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`

Start CSS studio to create/edit an OPI (see `EPICS\CSS\master\start_css.bat`)

Load in the project in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`: File -> Import -> General -> Existing Projects into Workspace.

Set the correct path for the Fonts and Colours files: Edit -> Preferences -> CSS Applications -> Display -> BOY. For the colour file choose `/resources/Share/isis_colours.def`; for the font file choose `/resources/Share/isis_fonts.def`.

Create a new OPI with File -> New  BOY -> OPI File
Change to the "OPI Editor" prespective to allow easier editing.

Edit the OPI not that some Macros are provided.

## Macros
When an OPI is opened from the synopic (via OpiTargetView.java) you get at least the following macros automatically set:

- `NAME`: the opt title, as defined by the synoptic component editor (e.g. "Slit 2")
- `OPINAME`: name of the OPI file opened (e.g. Slit.opi)
- `P`: the instrument pv prefix (e.g. IN:LARMOR:)
Others macros may also be available, passed down from higher screens (also defined via the synoptic editor component)

One convention we have used is to define a macro within the opened OPI called PV_ROOT which we then use to make full PV names. So at the top of the OPI XML would be something like

    <macros>
      <include_parent_macros>true</include_parent_macros>
      <PV_ROOT>$(P)$(EURO)</PV_ROOT>
    </macros>

here EURO would be a parameter passed from the synoptic and it is combined with P to create the prefix for all PVs referenced within the OPI screen

### Other Standard Macro Names

| Name | Meaning |
| ---- | ------- |
| PV_ROOT | Root for all PVs within an OPI |
| IOC_NUM | When there are multiple IOC of the same type this is the number, always 2 digits, e.g. 01 |

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
* `value.macro.macro.description`: description of macro value which appears in target details when user clicks on the macro
  
# Developer Testing

## Start the IOC

Make sure the instrument is running with the `EPICS\start_inst.bat` command
Open an epics terminal a list all running instruments with

    console -M localhost -x

To interact with an IOC use

    console -M localhost <IOC_NAME>

console will attempt to complete the name if you only give part of it and will give you possible options. Once in the console:
* `ctrl-x` : starts and stops thw IOC
* `crtl-e` `c` `.`: exits the console

TO switch an IOC to simulation mode the default is

    caput <IOC PV NAME>:SIM 1




