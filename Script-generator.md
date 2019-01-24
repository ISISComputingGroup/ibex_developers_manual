# Existing script generators

### Muons

The muons have at least 3 different script generators. All of these are fundamentally table-based systems with varying degrees of additional functionality on the side.

MACS is probably the most interesting muon script generator. A brief overview of functionality:
- Keeps a table-based view of operations on the screen. An "Operation" could be:
  * A run at a single combination of temperature/field
  * A scan over temperature or field (in three modes), counting at each point. These scans can be defined as linear or logarithmic.
  * An arbitrary block set to an arbitrary value
- Sends commands to OpenGENIE via the SECI API as it goes - means that scripts can be edited (up to the point when they have started running). This is similar in spirit to nicos script server.
- Includes some basic time estimation (it displays the total count time of everything in the script window)

Tom has a copy of MACS, but this can only run out of cycle and on a real instrument.

### Inter

Inter has a script generator called MaxScript. It has fallen out of use because it is not easy to integrate with the SECI system. Scientists from Inter expressed the desire for the script generator to be able to talk to the script server directly, with feedback (for example, greying out completed rows where a row represents an experimental measurement).

The Inter script generator can also display the script in a "tree" view - this collapses each run into a short recognisable string, and the details can be seen by expanding out the tree item.

The Inter script generator provides some time estimation.

Inter script generator is available at: `\\isis\shares\ISIS_Experimental_Controls\external_code\inter script generator` (copied from https://github.com/jonasgitt/ScriptMax with required DLLs and extra files added). Launch via the Qt IDE (download latest version from web; takes a while). I haven't been able to build it successfully to an exe, but only spent half an hour on it.

### Loq

LOQ uses a script generator "written by Matt Clarke in VB or C#". The scientists have expressed a desire for the script generator to be simple from a user's perspective.

# Commonalities of old systems / feature requests for new system

### Configurable

There is a clear need for the script generator to be highly configurable. Common actions that scientists want to take are:
- `cset` a block
- run an arbitrary instrument script (with parameters)

### Offline mode

Being able to use the script generator offline (in advance) as well as alongside/integrated with IBEX is important.

### Spreadsheet / table based

Most of the existing script generators are table based. Some have additional alternative means of displaying equivalent information (such as a tree view)

### Parameters

All of the script generators I've seen have essentially been setting a small number (2-10) of parameters and then performing some kind of run. The functions to set parameters and do the runs are different for each beamline, so each beamline will need to be able to configure this. It would be advantageous for a scientist to be able to configure this by themselves, without necessarily requiring input from computing.

### Parameter checking

All of the scientists have brought up a desire for parameters to be checked for implausible values (e.g. setting a dilution fridge to furnace temperatures). Many of the existing script generators already do this. Where the limits come from should be user-configurable.

### Output

All of the existing script generators generate a plain text file. However, the overwhelming consensus is that a script written using the new generator should be able to be executed "in one click", without requiring copying/saving a script and loading it explicitly.

However, the *option* to explicitly generate and load a script is still important, as some users like to edit the generated script before it is sent.

### Execution Feedback

Scientists have expressed a desire for live feedback visible in the script generator while the script is running. For example, rows should be greyed out once that part of the script has been executed.

### Time estimation

Some of the existing script generators already do some form of time estimation - given instrument-specific assumptions. This is a feature that is quite heavily requested by all the different groups.

### Dry runs

Some scientists have expressed an interest in dry runs/simulated runs of scripts to detect errors. None of the existing script generators that I've seen contain this functionality.

At a SAG meeting, the scientists suggested a graph of time (or rather, counts) against arbitrary parameters so that they can check the the graph looks as they expect.

### Scans

Some of the existing script generators already support "scanning" a parameter (that is, setting a parameter to a value and taking a measurement at each step. There is broad consensus that this is useful functionality.

There is slightly less consensus about nested loops - some groups see these as very useful, while others would prefer this "advanced" functionality to be handled by writing the python themselves.

Logarithmic scans (as opposed to linear) are important for the Muon group, but there was not substantial interest from other groups.

### Loading scripts

The script generator should be able to load/save scripts in it's own format. In addition, several groups expressed interest in loading from other formats, for example:
- Excel
- csv
- custom formats (e.g. ENGINX)
- Raw python code

# Suggested implementations

All of the implementations below assume that the NICOS script server will be used as the back-end, when the script generator is running on an instrument. Using the script server is logical as it already allows for queuing/re-ordering/editing scripts in a queue on an instrument.

### Approach 1

One suggestion to implement the script generator as a Java eclipse plugin that can be run either within the IBEX GUI or standalone. This plugin would be implemented as an MVVM stack in a similar style to the rest of the GUI.

Advantages:
- It facilitates integration within the GUI while not being too difficult to package as a standalone application.
- We can re-use some of the NICOS code from the GUI
- It is a UI technology which IBEX developers already use and are already familiar with

Disadvantages:
- Using Eclipse RCP might constrain us unnecessarily
- It might be easier to work with generating python code in python itself

### Approach 2

Another suggestion would be to implement the script generator as a standalone Python program (using tkinter or a similar UI framework). As above this would be implemented as an MVVM stack.

Advantages:
- It might be easier to interface with Nicos as nicos is written in Python
- It may be easier to generate python code using python than java (for example, access to the `ast` module)

Disadvantages:
- IBEX developers are not currently familiar with Python UI toolkits. This would be another technology to learn.
- Some of the NICOS functionality which we've implemented in the GUI would need to be reimplemented in Python
- It would be more difficult or perhaps impossible to integrate this into the main GUI later

### Approach 3

Approach 3 would be to attempt to adopt and adapt one of the existing script generators, and retrofit script server support to it and add any other features that are requested.

Advantages:
- Some functionality is already implemented in the other script generators.

Disadvantages:
- The quality of the existing code is largely unknown
- The existing script generators are written in technologies which were not necessarily familiar with, or which may be obsolete
- It is unknown how generic/extensible the existing script generators are. Most are fairly specific to a small number of beamlines.