> [Wiki](Home) > [The GUI](The-GUI) > [Eclipse](GUI-Eclipse) > [Check Style setup](Checkstyle-setup)

Check style is set up by:

## Install checkstyle plugin.
You may need to install an older version to be compatible with our checkstyle config in case our dependencies are not up to date. 
    
1. Help --> Install New Software
1. Add new site (Name: Checkstyle, Location: https://checkstyle.org/eclipse-cs-update-site)
1. Uncheck "Show only latest versions of available software"
1. Uncheck "Hide Items that are already installed"
1. Install the correct version of "Eclipse Checkstyle Plug-in"(at the moment this is v`10.0.0`). If you see another version in the list that is already installed, you need to uninstall it first: Go to `Help > About Eclipse IDE > Installation Details`, search for "checkstyle" in the list of installed software and click `Uninstall`

## Configure Checkstyle to use external file.

1. In Eclipse open checkstyle settings via `Window` > `Preferences` > `Checkstyle`
1. If you have an existing "IBEX Checks" entry using an internal configuration, remove it. If it complains about the configuration currently being used in projects, you may have to remove and re-import all projects before you remove this config.
1. Add a new check configuration by clicking `New...` next to the table
1. Set the following
    1. File: External configuration file
    1. Name: IBEX Checks
    1. Location: `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.client.tycho.parent\checkstyle.xml`
    1. `Additional Properties` button
        1. `Add...` button
        1. Set:
            - Name: checkstyle.suppressions.file
            - Value: C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.client.tycho.parent\suppressions.xml
1. Apply and close: you should now be setup
    1. If you have issues with the highlight colour on a dark theme you can go to: Window -> Preferences, General -> Editors -> Text Editors -> Annotations to change it.

## Useful links

https://checkstyle.org/eclipse-cs/#!/custom-config