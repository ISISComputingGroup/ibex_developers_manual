> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > System testing with RCPTT

See [System Testing Proposals](System-Testing-Proposals) for a brief bit on the rationale behind the system tests.

## Getting Started

Checkout the ibex_system_tests repository by running:
```
git clone https://github.com/ISISComputingGroup/ibex_system_tests.git
```

The Eclipse IBEX Developer's Edition (version 3) comes with Eclipse RCPTT already installed. It is recommended to use a separate workspace for the system tests to the IBEX GUI, but it is not essential. Once you have started Eclipse you can select Window -> Perspective -> Open Perspective -> Other -> RCPTT to get to the RCPTT perspective.

You can also just download the latest testing tool from the [Eclipse RCPTT website](https://www.eclipse.org/rcptt/download/).

## Importing a Project

Importing the system tests works in the same way as for the GUI. In Eclipse choose File -> Import -> General -> Existing Projects into Workspace, then choose the RCPTT_Tests folder from the GitHub repository.

## Configure the Application Under Test (AUT)

In the bottom of the RCPTT window, under Applications, right click and add IBEX as the AUT. If you want to use a development version of the GUI the location will be something like `C:\Instrument\Dev\Client\ibex_gui\base\uk.ac.stfc.isis.ibex.client.product\target\products\ibex.product\win32\win32\x86_64`. If you have not done it before, you will have to build the client first by running `C:\Instrument\Dev\Client\ibex_gui\build\build.bat`
You can also use a version from the build server instead, just point RCPTT at the folder containing the executable.

The name should be filled out automatically as `uk.ac.stfc.isis.ibex.product.product`. Click 'Finish'.

## Create Some Tests

**Don't forget to add new tests to the All_tests test suite so that it'll be run by Jenkins. More details later in the paragraph**

Create a new 'Test Case'. Click the record button in the top right to start using IBEX and record some behaviour. Use `Shift+Alt+7` to switch to verification mode. In verification mode you can click on items to get access to their properties. The desired assertions can be selected.

Below is an example of a recorded script to create a new block.

```java
get-menu "Configuration/Edit Current Configuration..." | click
with [get-window "Edit Configuration"] {
    get-tab-folder | get-tab-item Blocks | click
    get-button "Add Block" | click
    get-window "Block Configuration" | get-button OK | click
    get-button "Save as ..." | click
    with [get-window "Save Configuration As"] {
        with [get-editbox -after [get-label "Name:"]] {
            set-text default
            key-type "TRAVERSE_TAB_NEXT"
        }
        get-editbox -after [get-label "Description:"] | set-text default
        get-button OK | click
    }
}

// Assert the new block exists
try -times 50 -delay 200 -command {
    get-view Blocks | get-label "NEW_BLOCK:" | get-property caption | equals "NEW_BLOCK: " | verify-true
}
```

Note the `try` was added manually, this is required as the BlockServer takes some time to respond to the request. Anything that depends purely on the GUI should not need to wait like this. It is better to use a `try` than a `wait` so that the test is not blocked longer than necessary. The `try` will try to pass the command every `-delay` milliseconds it will try up to `-times` times.

Finally, under 'All_Tests' choose 'Add Test Case' from the buttons on the right and add the newly created test. Add more tests here to run them one by one.

## Useful Concepts
* IBEX Server State: Because the state of the IBEX server is changed by the GUI some tests are not repeatable. For example if the test create a config called test then the next time it is run then it will try to create test again and fail. To avoid this the `CleanIBEXServer` context is run. This will delete any configuration, synoptic or component which starts with a known prefix. It will also delete the data for the DAE. After this it restarts both the block server and DAE with a blank configuration. To make sure anything created in the test is also deleted use the `test_prefix` procedure to add the prefix to any names. For example:

    ```
    let [val synoptic_name [test_prefix "test_synoptic"]] {
        ...
        get-editbox -after [get-label "Name:"] | set-text $synoptic_name
        ...
    }
    ```

* Updating the clean ibex script. The script to clean the server is stored in `RCPTT_Tests\cleanIBEXServer\cleanIBEXServer.py` but this is not run directly from the system tests. Instead the `CleanIBEXServerFiles` context copies it to a known location. To update the context remove the current folder and then add in the cleanIBEXServer folder. This updates the file.
* Procedures: this is RCPTT's equivalent of functions. A procedure is a named block of code, which can receive arguments and therefore is useful for code reuse. See RCPTT documentation for details. Defined like
`proc "proc_name"[val argument1] { <body> }`
* Contexts: RCPTT has the concept of test contexts, an artefact that can be loaded/executed before a test case, which can be used for test setup. There are a few different types of contexts, each targeted to a specific type of action, like setting up the workspace or copying files into directories outside of the workspace. Contexts can also contain ECL code, and so can contain reusable sequences of commands to be executed on the UI before the actual test. Contexts containing ECL code can be used to simply group a number of related procedures, so the procedures are available for all tests using that context (this is equivalent to importing a module in Python). See RCPTT documentation for details.

Note that we started writing contexts containing procedures that could be useful in a number of tests:
* The `InstrumentStatusProcedures` context contains procedures related to switching/asserting the current status of the instrument
* The `SwitchToViewProcedures` context contains procedures for switching perspective

## Tips, Warnings and Gotchas

### Tests

* Try to avoid waits (see next point). Instead look for a change in the UI and continue when the change happens. For example if waiting for a label to change use:

    ```
    try -times 10 -delay 200 -command {
        get-view Dashboard | get-control Any -index 1 | get-property "getChildren().Control[0].getText()" 
	    | contains $text | verify-true
    }
    ```
* Add wait XXXX when the GUI will be reading/writing to PVs and may take some time to respond
* The catch block in a try command is not called for each time. Therefore if you want to use the catch to tidy something up you will have to do the following:
    ```
    try -times 10 -delay 200 -command {
        try -command {
             // Open a dialog
             // Do a test
        } catch {
             // Close the dialog
             // Reraise error e.g. verify-true False
        }
    }
    ```
* The perspective switcher buttons do not get recorded properly, to manually switch just do e.g. `get-label "Log Plotter" | click`. Note that we started writing procedures for these actions in the `SwitchToViewProcedures` context, to maximise code reuse.
* If the test fail locally in clean Ibex server context check either the log file in `C:\Instrument\CleanIBEXServerFiles\cleanIBEXServer\cleanIBEXServer.log` or look at the exit error from the process and match it to the script in `C:\Instrument\CleanIBEXServerFiles\cleanIBEXServer\cleanIBEXServer.py` (this file is copied during the tests from the context).

### Writing locally

To speed up the tests when running locally you can do the following (do not check these back in though):

1. Remove the `clean ibex server` context from the project default contexts:
    - this will stop the server rebooting and getting a blank configuration but you need to delete new configurations and new synoptics by hand between each run
1. Remove the execution delay from the project default contexts

## Running tests automatically

The test runner can be downloaded from the [RCPTT download page, under 'Test Runner'](http://www.eclipse.org/rcptt/download/).

Below is an example Windows command script to run the tests automatically.

```bat
SET AUT=C:\Instrument\Dev\Client\ibex_gui\base\uk.ac.stfc.isis.ibex.client.product\target\products\ibex.product\win32\win32\x86_64
SET RUNNER=C:\Instrument\Dev\System_Test\runner
SET PROJECT=C:\Instrument\Dev\System_Test\IBEX_System_Tests

SET RESULTS=C:\Instrument\Dev\System_Test\Results

IF NOT EXIST %RESULTS% GOTO NORESULTS
RMDIR /S /Q %RESULTS%

:NORESULTS
md %RESULTS%

java -jar %RUNNER%/plugins/org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar ^
 -application org.eclipse.rcptt.runner.headless ^
 -data %RESULTS%/runner-workspace/ ^
 -aut %AUT% ^
 -autWsPrefix %RESULTS%/aut-workspace ^
 -autConsolePrefix %RESULTS%/aut-output ^
 -htmlReport %RESULTS%/report.html ^
 -junitReport %RESULTS%/report.xml ^
 -import %PROJECT% 
```

## Setting up a New RCPTT Project for Testing IBEX

In RCPTT create a new 'RCP Testing Tool Project' and give it a name.

Next create a new 'Test Suite' called All_Tests.

Next create a new 'Context' of type 'Workspace'. Under 'Workspace Options' tick 'Clear workspace'. Add 'isis.log, logs' to 'Do not clear'.

Create another 'Context' this time of type 'Launch'. Under options select 'Terminate existing launches' and 'Clear launch configurations'.

Create a third 'Context' this time of type 'ECL Script'. Add the following:

```java
// 200 ms between commands
set-q7-option eclExecutionDelay 200

// 5 s between tests
wait 5000
```

The first command here sets 200 ms between every command for the GUI test. This can slow the test down a lot, so this could be reduced with testing. Similarly the 5 seconds between each test will slow down the test execution, so this could be reduced too. RCPTT is clever at knowing when it should wait for pure GUI elements to finish updating, but knows nothing about the EPICS back-end, hence the need for the artificial delays.

Add all of these contexts to 'Default Contexts' under 'Project Settings'.

## Jenkins Notes

See [special notes on configuring Jenkins for the GUI tests](Adding-a-new-Windows-machine-to-Jenkins#jenkins_gui_tests).

## Useful links

API - possibly out of date? [http://download.xored.com/q7/docs/ecl-api/latest](http://download.xored.com/q7/docs/ecl-api/latest)

RCPTT Documentation - [http://www.eclipse.org/rcptt/documentation/](http://www.eclipse.org/rcptt/documentation/)

Tutorial on RCPTT - [http://eclipsesource.com/blogs/tutorials/rcp-testing-tool-rcptt-basic-tutorial/](http://eclipsesource.com/blogs/tutorials/rcp-testing-tool-rcptt-basic-tutorial/)