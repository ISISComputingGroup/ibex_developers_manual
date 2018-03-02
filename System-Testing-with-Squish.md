> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > System testing with RCPTT

# Set Up

Get a licence key (there are 5 floating licences that can be used by 2 people)

1. Download the SQUISH/JAVA WINDOWS from the [frog logic page](https://www.froglogic.com/squish/download/)
1. Read and accept the terms and conditions if still correct
1. Install download:
    1. Run download installer
    1. Licence Key: Enter licence key from download page
    1. Licence Agreement: Read and accept the licence
    1. Installation folder: Choose a folder I chose `c:\tools`
    1. JRE or JDK: Select the JDK we are currently developing with
    1. Shortcuts: use defaults
    1. Start Menu: use defaults
    1. Accept default except for location which I suggest you change to c:\tools
    1. Install
1. Clone the current tests to your machine (dev is where I put mine)
    ```
    git clone  https://github.com/ISISComputingGroup/ui_system_tests_trial
    ```
1. Open the test suites in the IDE
    1. Menu File -> Open Test Suite ..
    1. Open the root of the git clone you just made this will open all tests suites in the window
1. Set the Application under test (AUT)
    1. Ensure that the client has been built with build.bat
    1. Edit -> Server Settings -> Manage AUTs ...
    1. Select Mapped AUTs and click Add...
    1. Locate the executable from the built eclipse project (e.g. ibex-client in `ibex_gui\bas\uk.ac.stfc.ibex.client.product\target\products\ibex.product\win32\win32\x86_64\ibex_gui.exe`
1. Other application setting
    1. Under Edit > Preferences
    1. Under Squish-> Test Creation select Python as the default language


# Other 

### Change Java that squish is using

To change java that squish is using:

    cd squish directory
    "bin/squishconfig" --java="C:\Program Files\Java\jdk<jdk version>\jre\bin"

This fixes the issue "Internal Error: don't know where to log: Squish for Java has not been configured for the current user yet. Please configure the (Java Runtime Environment) used for executing the AUT (Application Under Test) in the Squish IDE via Edit > Preferences > Squish > .... (Or use SQUISH_DIR/bin/squishconfig --java=path_to_jre. Replace "path_to_jre" as required.) (Starting application)"

