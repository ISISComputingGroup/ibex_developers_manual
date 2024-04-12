> [Wiki](Home) > [The GUI](The-GUI) > [Getting started](GUI-Getting-Started) > Building the GUI

Before building and running the GUI please make sure you have followed the steps from here: [First time installing and building (Windows)](First-time-installing-and-building-(Windows)). In particular make sure Git and genie_python are installed.

## Eclipse RCP resources

We have a book which should serve as a reasonable introduction to the Eclipse RCP platform: 'Eclipse Rich Client Platform' by McAffer, Lemieux and Aniszczyk. There is also a basic introduction at http://www.vogella.com/tutorials/EclipseRCP/article.html.

## Checking out the GUI

Create a directory for where you want your IBEX GUI to reside (e.g. `C:\Instrument\Dev`). From an appropriate Git console (e.g. Git Bash) navigate to your directory and run:

`git clone https://github.com/ISISComputingGroup/ibex_gui.git`

## Building via Eclipse ##

### Eclipse

You must use a version of eclipse >= 2019-06, earlier versions will fail to build the client. An appropriate version is available at `\\isis\inst$\Kits$\CompGroup\ICP\Developer Tools`, simply unzip the the latest version folder to your chosen location for Eclipse (e.g. `C:\Tools\eclipse`) and use the provided workspace. 

~You can choose to download Eclipse directly from [the eclipse website](http://www.eclipse.org/downloads/packages/), choose the package for "RCP and RAP developers". If you download from the website you should use version 4.26.~ Some people have had issues with the latest version of Eclipse not pulling in all dependencies, so use the version on the share mentioned above for now to be safe.

### Building

These are the steps needed to run the GUI via Eclipse:

1. First, create a new workspace (example name: ibex_workspace_E4).
1. Then `git checkout master` from where the IBEX code was cloned to (if it's a fresh clone, it should already be on this branch).
1. Install the [pre-commit hook](https://github.com/ISISComputingGroup/IBEX/issues/4786). To install this hook you must run `install_pre_commit_hook.bat` from the `\build` subdirectory.
1. Start Eclipse IDE and select the workspace and use "Browse" to create and select the new workspace folder.
1. From the menu bar choose File->Import->General->Existing Projects into Workspace. Choose "Select root directory" and browse to `<IBEX Clone Path>\base`. You should now see a list of plugins to import with names like `uk.ac.stfc.isis.ibex.*`. Eclipse should automatically select everything so you just need to click "Finish" to add them to the project. If a "Marketplace solutions available" dialogue appears, click cancel as these will be obtained later.
1. If there is a "Welcome" tab open in Eclipse, close it. From the "Project Explorer" tab on the left, expand the target platform folder (labelled as ``uk.ac.stfc.isis.ibex.targetplatform``), double click on the target file and choose "Set as Active Target Platform". This may take some time as parts of CS-Studio and DAWN are downloaded. It may also be required to update the Locations in use should some packages appear to be missing. 
1. Then select Project->Clean from the menu bar.
1. To run the application from within Eclipse: open "ibex.product" from the ``uk.ac.stfc.isis.ibex.e4.client.product`` folder, select "Launch an Eclipse application".
1. Next, From the menu bar choose Run->Run configurations and select "ibex.product" from the left hand list under "Eclipse Application".
1. In the "Main" tab in **Run configurations** tick the "Clear" tick box and in the "Configuration" tab tick the "Clear the configuration area before launching" tick box. Click "Apply" and select "Run". Untick "Ask for confirmation before clearing", otherwise a dialog box will pop up every time you run the client.

IBEX should now build but there will probably be some errors. You can clear them following the procedure below.

**Important Notes:** 
* you will need JDK 17 installed to launch the IBEX GUI successfully.
* you should also [set up the checkstyle](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Checkstyle-setup), do it sooner than later as it may prevent potential errors

### If you see a “Plugin execution not covered by lifecycle configuration” error
1. From the menu bar choose: Window->Preferences
1. Expand Maven and choose Errors/Warnings
1. Set "Plugin execution not covered by lifecycle configuration" to Warning or Ignore

### Configuring Eclipse to show current Git repository and branch in the Package Explorer

e.g. `uk.ac.stfc.isis.ibex.targetplatform [ibex_gui_e4 master]`

Not for new starters: this should already have been done by eclipse so unless you do not see `[ibex_gui_e4 master]` next to the name of a plugin/package you do not need to do any of the following.
1. Select all plugins (ctrl-a)
1. Right-click on any one plugin and select `Team -> Share Project`
1. Click `Finish`
1. The repository and branch names should now be displayed after each plugin as above


## Building via Maven ##

1. Ensure your maven version is >= 3.6.0, excluding 3.6.1 as that version has a bug
1. Double check that your maven is the correct version by running `mvn -v` in a new command window. Older versions will give you very hard to diagnose build errors
1. From the command line, navigate to the `.\build\` directory in the IBEX code (one directory under the root, which should be `ibex_gui\`).
1. Run `build.bat`
1. Wait for a few minutes while it builds
1. After the build finishes it can be found in `.\built_client\`

## Troubleshooting ##

If the GUI loads up but items are the wrong size, you may need to change your display settings. The exact settings that you need may vary from computer to computer. This is a common issue on Windows 10 machines due to the OS' scaling setting for text, icons etc. that is meant to ensure they do not look too small on high screen resolutions. 

Generally a resolution of 1920 x 1080 with a scaling factor of 100% should look correct on standard screens. You can increase both of those settings slightly if you feel like the display elements look uncomfortably small.

Errors can occur if the wrong version of Java is installed for your OS. For example, the `x86` version can differ from the `x64` version and can cause issues when building the GUI. 

## Eclipse troubleshooting ##

Sometimes eclipse will tell you that you have errors when you open it. The following operations (may) help.
- Refresh, clean and build all projects. Select all projects, press F5 to refresh, then go to `Project -> Clean` to clean all projects.
- Go to `Run -> Run Configurations -> Plugins` and press "Add required plugins". You can now validate/apply your choice.
- In `uk.ac.stfc.isis.ibex.targetplatform`, open `uk.ac.stfc.isis.ibex.targetplatform.target` and click "set as target platform". 
- If you have done all these steps and it still doesn't work, there is more troubleshooting information [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Common-Eclipse-Issues).
- If all else fails, delete all the projects from eclipse's workspace and reimport them.

Eclipse can automatically set the Java standard for some projects to `1.8`. If you are seeing errors such as `var cannot be assigned to a type` on certain projects, navigate to the project in the explorer, then right-click and choose Properties->Java Compiler->Configure Workspace Settings, and then set the required Java standard to `11`.

## Further Troubleshooting ##

Additional support can be found [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/GUI-Troubleshooting).
