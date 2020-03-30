> [Wiki](Home) > [The GUI](The-GUI) > [Eclipse](GUI-Eclipse) > [Check Style setup](Checkstyle-setup)

Check style is set up by:

1. In eclipse click Windows->Preferences
1. Select Checkstyle (if this option is not available you will need to install the checkstyle plugin through `Help->Eclipse Marketplace` and search for checkstyle
1. Click New (if you are updating the config select properties)
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
