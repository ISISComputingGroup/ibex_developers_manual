> [Wiki](Home) > [The GUI](The-GUI) > [Getting started](GUI-Getting-Started) > Building the GUI

Before building and running the GUI please make sure you have followed the steps from here: [First time installing and building (Windows)](First-time-installing-and-building-(Windows)). In particular make sure Git and genie_python are installed.

## Eclipse RCP resources

We have a book which should serve as a reasonable introduction to the Eclipse RCP platform: 'Eclipse Rich Client Platform' by McAffer, Lemieux and Aniszczyk. There is also a basic introduction at http://www.vogella.com/tutorials/EclipseRCP/article.html.

## Checking out the GUI

Create a directory for where you want your IBEX GUI to reside (e.g. `C:\Instrument\Dev`). From an appropriate Git console (e.g. Git Bash) navigate to your directory and run:

`git clone https://github.com/ISISComputingGroup/ibex_gui.git`

## Building via Eclipse ##

### Eclipse IBEX Developer's Edition

If you are working on the IBEX GUI please use the IBEX Eclipse editor, which is available, within ISIS, via a zip file at `\\isis\inst$\Kits$\CompGroup\ICP\Developer Tools`, simply unzip the the latest version folder to your chosen location for Eclipse and use the provided workspace. You can choose to download Eclipse directly from http://www.eclipse.org/downloads/packages/eclipse-rcp-and-rap-developers/mars1, but you will need to alter settings to get the correct defaults for formatting.

### Building

These are the steps needed to run the GUI via Eclipse:

1. Start Eclipse IDE and select the workspace and use "Browse" to create and select a new workspace folder (example name: ibex_workspace)
1. From the menu bar choose: File->Import->General->Existing Projects into Workspace. Choose "Select root directory" and browse to where the IBEX code was cloned to, Eclipse should automatically select everything so click "Finish" to add them to the project
1. Expand the target platform folder (labelled as ``uk.ac.stfc.isis.ibex.targetplatform``), double click on the target file and choose "Set as Target Platform". This may take some time as parts of CS-Studio and DAWN are downloaded. It may also be required to update the Locations in use should some packages appear to be missing.
1. To run the application from within Eclipse: open "ibex.product" from the ``uk.ac.stfc.isis.ibex.client.product`` folder, select "Launch an Eclipse application"

**Important Note:** you will need JDK 1.8 or higher installed to launch the IBEX GUI successfully. You may be able to use JDK 1.7, but you will need to change the JDK compliance level in Eclipse from 1.8 -> 1.7, else the GUI will not launch.

**Additional Important Note:** you will need JDK 1.8 or higher installed to launch the **E4** IBEX GUI successfully.

### Building the E4 version of the GUI

These are the steps needed to run the E4 GUI via Eclipse:

1. First, create a new workspace (example name: ibex_workspace_E4).
2. Then `git checkout master_E4` from where the IBEX code was cloned to.
3. Start Eclipse IDE and select the workspace and use "Browse" to create and select the new workspace folder.
4. From the menu bar choose File->Import->General->Existing Projects into Workspace. Choose "Select root directory" and browse to where the IBEX code was cloned to, Eclipse should automatically select everything so click "Finish" to add them to the project
5. Expand the target platform folder (labelled as ``uk.ac.stfc.isis.ibex.targetplatform``), double click on the target file and choose "Set as Target Platform". This may take some time as parts of CS-Studio and DAWN are downloaded. It may also be required to update the Locations in use should some packages appear to be missing.
6. Then select Project->Clean from the menu bar.
9. To run the application from within Eclipse: open "ibex.product" from the ``uk.ac.stfc.isis.ibex.e4.client.product`` folder, select "Launch an Eclipse application". The first time you do this, it will fail.
10. Next, From the menu bar choose Run->Run configurations and select "ibex.product" from the lefthand list under "Eclipse Application".
11. In the "Main" tab tick the "Clear" tick box and in the "Configuration" tab tick the "Clear the configuration area before launching" tick box. Click "Apply" and select "Run".
13. When a dialogue box asking if you want to clear the run-time workspace data click "Yes". This dialogue box will appear every time you run the E4 build of IBEX from within Eclipse.

IBEX should now build but there will probably be some errors. You can clear them following the procedure below.

### If you see a “Plugin execution not covered by lifecycle configuration” error
1. From the menu bar choose: Window->Preferences
1. Expand Maven and choose Errors/Warnings
1. Set "Plugin execution not covered by lifecycle configuration" to Warning or Ignore

## Building via Maven ##

1. From the command line, navigate to the build directory in the IBEX code
1. Run the build.bat file
1. Wait for a few minutes while it builds
1. After the build finishes it can be found in `\base\uk.ac.stfc.isis.ibex.client.product\target\products\`

## Troubleshooting ##

If the GUI loads up but items are the wrong size, you may need to change your display settings. The exact settings that you need may vary from computer to computer. This is a common issue on Windows 10 machines due to the OS' scaling setting for text, icons etc. that is meant to ensure they do not look too small on high screen resolutions. 

Generally a resolution of 1920 x 1080 with a scaling factor of 100% should look correct on standard screens. You can increase both of those settings slightly if you feel like the display elements look uncomfortably small.

## Eclipse troubleshooting ##

Sometimes eclipse will tell you that you have errors when you open it. The following operations (may) help.
- Refresh, clean and build all projects. Select all projects, press F5 to refresh, then go to `Project -> Clean` to clean all projects.
- Go to `Run -> Run Configurations -> Plugins` and press "Add required plugins". You can now validate/apply your choice.
- In `uk.ac.stfc.isis.ibex.targetplatform`, open `uk.ac.stfc.isis.ibex.targetplatform.target` and click "set as target platform". 
- If you have done all these steps and it still doesn't work, there is more troubleshooting information [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Common-Eclipse-Issues).
- If all else fails, delete all the projects from eclipse's workspace and reimport them.