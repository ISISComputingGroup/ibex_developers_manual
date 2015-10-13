=============
Building IBEX 
=============

We have a book which should serve as a reasonable introduction to the Eclipse RCP platform: 'Eclipse Rich Client Platform' by McAffer, Lemieux and Aniszczyk.

Building via Eclipse
--------------------

This assumes you have got as far as cloning the GitHub repo.

These are the steps needed to run the GUI via Eclipse:

#. Start Eclipse IDE and select the workspace and use "Browse" to create and select a new workspace folder (example name: ibex_workspace)
#. From the menu bar choose: File->Import->General->Existing Projects into Workspace. Choose "Select root directory" and browse to where the IBEX code was cloned to, Eclipse should automatically select everything so click "Finish" to add them to the project
#. Expand the target platform folder (labelled as ``uk.ac.stfc.isis.ibex.targetplatform``), double click on the target file and choose "Set as Target Platform". This may take some time as parts of CS-Studio and DAWN are downloaded. It may also be required to update the Locations in use should some packages appear to be missing.
#. To run the application from within Eclipse: open "ibex.product" from the ``uk.ac.stfc.isis.ibex.client.product`` folder, select "Launch an Eclipse application"

**Important Note:** you will need JDK 1.8 or higher installed to launch the IBEX GUI succesfully. You may be able to use JDK 1.7, but you wil need to change the JDK compliance level in Eclipse from 1.8 -> 1.7, else the GUI will not launch.

Building via Maven
------------------

#. From the command line, navigate to the build directory in the IBEX code
#. Run the build.bat file
#. Wait for a few minutes while it builds
#. After the build finishes it can be found in \\base\\uk.ac.stfc.isis.ibex.client.product\\target\\products\\
