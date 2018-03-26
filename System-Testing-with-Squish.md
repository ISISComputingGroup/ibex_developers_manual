> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > [System testing with Squish](System-Testing-with-Squish)

# Set Up for local server

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

# Setup For Build Server

1. Install all the things needed for an instrument (Git, MySql, Java)
1. Install Jenkins build system but run it from a command line.
1. Install squish as above.
1. Add to `C:\Squish\etc` the key `GlobalScriptDirs = "C:\\Jenkins\\workspace\\squish_ui_system_tests\\global_scripts"`
1. Add applications under test to the server setup as above using the IDE
1. Switch off screen saver and power saving
1. Next remote desktop from another machine as the user stated in the password doc
    - We have tried making this auto-logon but it get stuck at the policy screen
    - We don't need VNC this seems to do the job without a problem
1. Then disconnect the session (i.e. don't log out)

# Creating a new Test Suite

1. Click File -> New test Suite ...
1. New Test Suite:
    1. Create a sensible name, `suite_<what>_tests`
    1. Make the test suite path the same as the system testing folder
1. Language: Make sure it is python
1. Select the application as eclipse (the ibex client in E4 was called eclipse)
1. Finish
1. Edit the test suite settings (select test suite in test suites tab. Then click on icon with blue spanner)
    1. Edit Object Map to be `..\objects.map`
1. Add a new step in the build pipeline for the new test suite (same as the others). I have kept then as separate steps so they can be easily timed.

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
