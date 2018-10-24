# Existing script generators

### Muons

The muons have at least 3 different script generators. All of these are fundamentally table-based systems with varying degrees of functionality

### Inter

Inter has a script generator called MaxScript. It has fallen out of use because it is not easy to integrate with the SECI system. Scientists from Inter expressed the desire for the script generator to be able to talk to the script server directly, with feedback (for example, greying out completed rows where a row represents an experimental measurement).

The Inter script generator can also display the script in a "tree" view - this collapses each run into a short recognisable string, and the details can be seen by expanding out the tree item.

The Inter script generator provides a time estimate.

### Loq

LOQ uses a script generator "written by Matt Clarke in VB or C#". The scientists have expressed a desire for the script generator to be fairly simple from a user's perspective. However, their script generator is broadly

# Commonalities

### Spreadsheet / table based

Most of the existing script generators are table based. Some have additional alternative means of displaying equivalent information (such as a tree view)

### Parameters

All of the script generators I've seen have essentially been setting a small number (2-10) of parameters and then performing some kind of run. The functions to set parameters and do the runs are different for each beamline, so each beamline will need to be able to configure this. It would be advantageous for a scientist to be able to configure this by themselves, without necessarily requiring input from computing.

### Output

All of the existing script generators generate a plain text file. However, the overwhelming consensus is that a new script generator should be able to talk to the script server directly, without needing to explicitly generate and then load a script. However, the *option* to explicitly generate and load a script is still important.

### Feedback

All of the scientists that have been involved in this discussion at all have agreed that feedback from the script server to the GUI is important. Notably, rows should be greyed out in some way once the script server has finished executing that script.

A "nice to have" feature would be to have a dynamically updating countdown of estimated remaining script time. This might be more or less fine grained depending on the implementation.

# Suggested implementations

### Approach 1

One suggestion to implement the script generator is an eclipse application that can be run either within the IBEX GUI (as a perspective: similar to all the other perspectives) or standalone. Within the plugin, the script generator would be implemented as an MVVM stack in a similar style to the rest of the GUI, with the NICOS script server acting as the backend (if it is available).

The advantages that I can see with this approach are that:
- It facilitates integration within the GUI while not being too difficult to package as a standalone application.
- We can re-use some of the NICOS code from the GUI
- It is a UI technology which IBEX developers already use and are already familiar with

Some of the disadvantages are:
- Using Eclipse RCP might constrain us unnecessarily
- It might be easier to work with generating python code in python itself

### Approach 2

Another suggestion would be to implement the script server as a standalone Python program (using tkinter or a similar UI framework). As above this would be implemented as an MVVM stack.

Advantages are:
- It might be easier to interface with Nicos as nicos is written in Python
- It may be easier to generate python code using python than java (for example, access to the `ast` module)

Disadvantages are:
- IBEX developers are not currently familiar with Python UI toolkits. This would be another technology to learn.
- Some of the NICOS functionality which we've implemented in the GUI would need to be reimplemented in Python
- It would be more difficult or perhaps impossible to later integrate this into the main GUI