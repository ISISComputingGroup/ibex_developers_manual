> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > [System testing with Squish](System-Testing-with-Squish)

# Squish Licensing Information & Contact Details

[Details about our Squish License](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FSquish%20Information&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View={F2C33C51-70E6-4343-B937-2C59A2568306})

# Set Up for local server

Get a licence key (our license permits concurrent use by any 2 users from a list of 5 named users)

1. Download the SQUISH/JAVA WINDOWS from the [frog logic page](https://www.froglogic.com/squish/download/) using the account in the passwords page on sharepoint
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
    git clone  https://github.com/ISISComputingGroup/System_Tests_UI_E4.git
    ```
1. Open the test suites in the IDE
    1. Menu File -> Open Test Suite ..
    1. Open the root of the git clone you just made this will open all tests suites in the window
1. Set the Application under test (AUT)
    1. Ensure that the client has been built with build.bat
    1. Edit -> Server Settings -> Manage AUTs ...
    1. Select Mapped AUTs and click Add...
    1. Locate the executable from the built (built using the build.bat maven script) eclipse project (e.g. ibex-client in `ibex_gui\base\built_client\`)
1. To get access to global scripts right click in squish -> global scripts pane -> add -> global scripts directory and select the global scripts directory in the repository root.

# RDP to Server

It is possible to remote desktop to the squish server but when you disconnect you must use the "Disconnect from RDP" shortcut on the desktop. To do this you must be an Admin on the desktop.

# Setup For Build Server

1. Install all the things needed for an instrument (Git, MySql, Java)
1. Install Jenkins build system but run it from a command line.
1. Add the script for running the command to the startup.
1. Install squish as above.
1. Add to `C:\Users\<user>\AppData\Roaming\froglogic\Squish\ver1` the key `GlobalScriptDirs = "C:\\Jenkins\\workspace\\squish_ui_system_tests\\global_scripts"`
1. Add applications under test to the server setup as above using the IDE
1. Change the Application Behaviour to have a startup time of 120s.
1. Check that the global script directory has been set.
1. Switch off screen saver and power saving
1. Next remote desktop from another machine as the user stated in the password doc
    - We have tried making this autologon but it get stuck at the policy screen
    - We don't need VNC this seems to do the job without a problem
1. Then disconnect the session using the shortcut on the desktop
1. Leave the machine with an attached screen. I think this is needed to set the resolution when leaving remote desktop.

# Creating a new Test Suite

1. Click File -> New test Suite ...
1. New Test Suite:
    1. Create a sensible name, `suite_<what>_tests`
    1. Make the test suite path the same as the system testing folder
1. Language: Make sure it is python
1. Select the application as eclipse (the ibex client in E4 was called eclipse)
1. Finish
1. Edit the test suite settings (select test suite in test suites tab. Then click on icon with blue spanner)
    1. Edit Object Map to be `..\objects.map`. You may not be able to do this from the Squish client depending on your version, in which case you can directly edit `suite.conf` in `/<System tests folder>/suite_<something>_tests/` (it should say `OBJECTMAP=..\objects.map`)

# Creating a new Test

A test contains one test case.

1. Find the suite the test should be in
1. Click "Create new test case" (icon document with a plus in Test Suites tab)
1. Change name to `tst_<what the test does>`
1. A test suite should start:
    ```
    # -*- coding: utf-8 -*-
    import sys
    import os
    path = os.path.abspath(os.path.dirname(findFile("scripts", "test_running.py")))
    sys.path.append(path)

    from test_running import start_test
    <other imports> 
    
    def main():
    
        # Given application
        start_test()
    
        <rest of test>
    ```

# Writing tests

Hints, tips and gotchas for writing tests:

* Use `set_text_field` to set a text field because it deletes its contents before adding the new value.
* Use `menu` module to access menus because if a menu is interrupted then you want it to try again at the top level menu.
* Use `generate_config_name` to generate a config name so that it will be ignored by git and cleaned up by the system test
* If you open a dialogue capture it using a context manager. You could consider adding an option for OK and Cancel.
* If you need to select a perspective button the object picker will set it using the index (`occurrence`) however these buttons might change their positions it is better to select them based on their text. To do this:
    1. Open the object map.
    1. Click on the button object definition (you can use the search at the top to find it).
    1. In the properties tab change `occurrence` to `text` and the value to the text on the button.
    1. Save it and check it works by clicking highlight object; button should flash red.

# Creating/Reviewing a Test when I don't have a Licence

If you have done some GUI work but don't have a licence for squish and need to write a test. Then find someone who does have a licence and pair with them for that part of the ticket.
For a review, check the code and functionality then merge the ticket and let the build server do the testing.

# Other 

### Change Java that squish is using

To change java that squish is using:

```
cd squish directory
"bin/squishconfig" --java="C:\Program Files\Java\jdk<jdk version>\jre\bin"
```

This fixes the issue:

```
"Internal Error: don't know where to log: Squish for Java has not been configured for the current user yet. Please configure the (Java Runtime Environment) used for executing the AUT (Application Under Test) in the Squish IDE via Edit > Preferences > Squish > .... (Or use `SQUISH_DIR/bin/squishconfig --java=path_to_jre`. Replace "path_to_jre" as required.) (Starting application)"
```

and also the error message:

```
java.lang.NoClassDefFoundError: com/froglogic/squish/swt/CompositeResolver
	at com.froglogic.squish.swt.SWT.<clinit>(SWT.java:922)
	at org.eclipse.swt.widgets.Display.<init>(Display.java:419)
	at org.eclipse.swt.widgets.Display.<init>(Display.java:481)
	at org.eclipse.ui.internal.Workbench.createDisplay(Workbench.java:795)
	at org.eclipse.ui.PlatformUI.createDisplay(PlatformUI.java:160)
	at uk.ac.stfc.isis.ibex.e4.product.Application.start(Application.java:38)
```
when starting the GUI.

### Restart after a Power Cut

After a power cut you will need to log into the machine via RDP and then disconnect using the shortcut on the desktop.

### Diagnosing Error Screenshots

Screen shooting on error should be turned on in `start_test` in `test_running.py`. The screen shots are placed on the squish server in `... Jenkins\workspace\System_Tests_Squish\suite_configuration_tests\<test name>\errorImages` the will only be from the last build.

### Error in tests

To tack the error we find in squish please add any errors you see to this chart. Remove the error when you think it is fixed:

Frequency | Test | Error 
----  | ----- | ------
4         | tst_can_add_edit_and_delete_block_to_current_config | When getting blocks it failed to get all children of one of the components. `ValueError: need more than 0 values to unpack. ... tst_can_add_edit_and_delete_block_to_current_config\test.py: 73, instrument_blocks.py: 25`
2         | tst_can_create_lots_of_blank_configs | `RuntimeError: Error in activateItem() invocation: Menu not visible and/or enabled Called from: C:\Jenkins\workspace\System_Tests_Squish\suite_configuration_tests\tst_can_create_lots_of_blank_configs\test.py: 20`
2         | tst_can_add_edit_and_delete_block_to_current_config | `RuntimeError: Property read failed: exception: java.lang.reflect.InvocationTargetException () org.eclipse.swt.SWTException: Widget is disposed`  `Called from: C:\Jenkins\workspace\System_Tests_Squish\suite_configuration_tests\tst_can_add_edit_and_delete_block_to_current_config\test.py: 74`
1         | tst_user_names_can_be_set | `LookupError: Object ':Experiment Details_Text' not found. Could not match properties:    isvisible for object name: ':Experiment Details_Text' Called from: C:\Jenkins\workspace\System_Tests_Squish\suite_experiment_details_tests\tst_user_names_can_be_set\test.py: 19 C:\Jenkins\workspace\System_Tests_Squish\global_scripts\experiment_details.py: 19`

# Troubleshooting

### Squish fails to run tests with an error in the C runtime library

Error is:

```
Runtime Error! 

Program: C:\Squish\lib\_squishrunner.exe 

R6034 An application has made an attempt to load the C runtime library incorrectly. Please contact the application's support team for more information.
```

This issue is due to us loading the `uuid` library in Python. This library loads a conflicted C runtime library and means tests aren't able to run completely correctly.

Solution is to Rename `C:\Squish\python\msvcr90.dll` to `msvcr90_off.dll`, which removes the conflicting dependency version. See ticket [#4773](https://github.com/ISISComputingGroup/IBEX/issues/4773) for more details.

### Squish fails to begin run

Attempt to change your tcb file to a regular neutron tcb file and begin a run. You should see it beginning and then return to set up with the log message: `invalid tcb start - must be 0 not 5.00000 ns`. See the [DAE troubleshooting](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/DAE-Trouble-Shooting) "invalid tcb start" section.

### Sq