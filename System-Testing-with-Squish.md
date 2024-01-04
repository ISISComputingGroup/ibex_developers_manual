> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > [System testing with Squish](System-Testing-with-Squish)

# Squish Licensing Information & Contact Details

we have one floating tester subscription and one floating execution subscription licence. The execution subscription is used by a build server to run tests, the tester subscription is used by us to develop tests. We can have at most one developer writing tests at a time, but we can all install the software on our machines. I don't yet know how the license system works e.g. if one developer forgets to close squish on their system, does it block everybody until they do? Or is there some timeout? We will have to experiment. See `license server` below for more details. 
 
# Set Up for local server

1. Install SQUISH/JAVA WINDOWS from `<isis experiment controls share>\squish`
1. Read and accept the terms and conditions if still correct
1. Install download:
    1. Run download installer
    1. Floating license: Enter `control-svcs.isis.cclrc.ac.uk:49345`
    1. Licence Agreement: Read and accept the licence
    1. Uncheck `Test Center` from items to install, unless you really need it
    1. Select python version for script language (3.*)
    1. Installation folder: Choose a folder I chose `c:\tools` but  `c:\squish` is used on the build server
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
    1. Ensure that the ibex_gui client has been built with build.bat
    1. Edit -> Server Settings -> Manage AUTs ...
    1. Select Mapped AUTs and click Add...
    1. Locate the executable from the built (built using the build.bat maven script) eclipse project (e.g. ibex-client in `ibex_gui\built_client\`)
1. To get access to global scripts right click in squish -> global scripts pane -> add -> global scripts directory and select the global scripts directory in the repository root.
1. If not running in Python 3 follow [these](https://kb.froglogic.com/squish/howto/changing-python-installation-used-squish-binary-packages/) instructions, and point to the default `python3` directory in the squish installation root.

You may also need to install `psutil` and `mysql-connector-python==8.0.11` through the GUI (Edit -> Preferences -> PyDev -> Interpreters -> Python Interpreter then "Manage with pip") if running the experiment details tests. 

Once you have set up Squish via the steps above, you should be able to run a test suite to confirm everything is working. Note that you need the IBEX server running in the background, but not the client (which will be started by Squish when you run a test).

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

# System Testing The IBEX Script Generator with Squish BDD Tools

The way we use Squish for testing the script generator is a bit different to the way we test the IBEX client. The method for testing is documented on the [System Testing The IBEX Script Generator with Squish BDD Tools](System-Testing-The-IBEX-Script-Generator-with-Squish-BDD-Tools) page. Some of the hints and tips from this page still apply e.g. using utilities such as `set_text_field`.

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
* Often `test.compare` and `test.verify` in Squish provides logs that aren't very useful, please do add a `test.log` line to describe the error.

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

# License server

This was setup as per https://doc.qt.io/squish/setting-up-the-squish-floating-license-server.html on `control-svcs.isis.cclrc.ac.uk` in the directory `/usr/local/squish-licenceserver` the service is automatically started at boot time vis systemd, the file `squish-licenseserver.service` has the service details and is symbolically linked from the systemd `/etc/systemd/system` area. The log file is `/var/log/squish-licenseserver.log` and the service is running on the default port of 49345

To restart the licence server process use `sudo systemctl restart squish-licenseserver.service` on the licence server machine

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

### Squish Fails to Start the Application

Look at the `Runner/Server` Log tab see if you can diagnose the problem. 

* `Unrecognized option: --add-reads=javafx.base=ALL-UNNAMED` probably running it through java8 it is on your path too high up. 
    - I fixed this by copying the java from the shares into the directory from which it runs so that it picks this up as the default when it runs. E.g. copy `...\Kits$\CompGroup\ICP\ibex_client_jre` to `C:\Instrument\Dev\ibex_gui\built_client\jre` (note the name change to jre). Running `build.bat` should now do that for you.

### KeyError: `MYSQLPW` is missing

To remedy this error set `MYSQLPW` to the root password in your environment variables when running the tests. If the Squish IDE has not been restarted before this you will need to close and re-open it before running the tests again. 

### No licence available

If onsite/vpn you can access  https://control-svcs.nd.rl.ac.uk/squish/squish_stats.txt - look for something like
```
"clientAddress": "::ffff:a.b.c.d"
"licenseType": "tester"
```
Then from a command windows do `nslookup a.b.c.d` to see machine name using licence. Currently licences should auto-expire after 12 hours anyway, so you may just need to wait.  `licenceType` can be `tester` or `execution`, we have one of each type and `execution` is used by the jenkins squish test server (this licence type only allow running not editing of tests)  
