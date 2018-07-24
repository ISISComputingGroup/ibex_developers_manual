> [Wiki](Home) > [The GUI](The-GUI) > [Information about Eclipse E3](E3-Dcoumentation)

This page contains information about the IBEX GUI as it was under eclipse 3. This information should be kept in the relevant heading until such time that we have retired the Eclipse 3 GUI. Heading link back to current page so it can be compared to E4 if needed.

# [Getting Started](GUI-Getting-Started)

## Building the GUI

These are the steps needed to run the GUI via Eclipse:

1. Start Eclipse IDE and select the workspace and use "Browse" to create and select a new workspace folder (example name: ibex_workspace)
1. From the menu bar choose: File->Import->General->Existing Projects into Workspace. Choose "Select root directory" and browse to where the IBEX code was cloned to, Eclipse should automatically select everything so click "Finish" to add them to the project
1. Expand the target platform folder (labelled as ``uk.ac.stfc.isis.ibex.targetplatform``), double click on the target file and choose "Set as Target Platform". This may take some time as parts of CS-Studio and DAWN are downloaded. It may also be required to update the Locations in use should some packages appear to be missing.
1. To run the application from within Eclipse: open "ibex.product" from the ``uk.ac.stfc.isis.ibex.client.product`` folder, select "Launch an Eclipse application"

# [Coding](GUI-Coding)
# [Testing](GUI-Testing)
* [System/UI testing with RCPTT](System-Testing-with-RCPTT)
# [Eclipse](GUI-Eclipse)
# [Control System Studio (CS-Studio)](GUI-CSS)
# [GUI Chats](GUI-Chats)
# [Other](GUI-Other)
