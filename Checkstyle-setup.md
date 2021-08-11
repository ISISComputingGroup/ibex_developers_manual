> [Wiki](Home) > [The GUI](The-GUI) > [Eclipse](GUI-Eclipse) > [Check Style setup](Checkstyle-setup)

Check style is set up by:

1. Install checkstyle plugin. You may need to install an older version to be compatible with our checkstyle config in case we have not updated our dependencies. 
    1. Help --> Install New Software
    1. Add new site (Name: Checkstyle, Location: https://checkstyle.org/eclipse-cs-update-site)
    1. Uncheck "Show only latest versions of available software"
    1. Install the correct version of "Eclipse Checkstyle Plug-in"(at the moment this is v`8.41.0`)
1. In eclipse click Windows->Preferences
1. Select Checkstyle 
1. Go to `Window > Preferences > Checkstyle`
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
