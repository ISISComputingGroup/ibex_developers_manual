# Introduction
OPIs live in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`

Start CSS studio to create/edit an OPI (see `EPICS\CSS\master\start_css.bast`)
Load in the project in `ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`

Create a new OPI with File -> New  BOY -> OPI File
Change to the "OPI Editor" prespective to allow easier editing.



# Macros
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

# Developer Testing

## Start the IOC

Make sure the instrument is running with the `EPICS\start_inst.bat` command
Open an epics terminal a list all running instruments with

    console -M< localhost -x

