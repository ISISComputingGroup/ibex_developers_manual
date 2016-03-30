## Getting Started

Download the latest testing tool from the [Eclipse RCPTT website](https://www.eclipse.org/rcptt/download/).

Unpack the testing tool as you would for the Eclipse IDE.

## Configure the Application Under Test (AUT)

In the bottom of the RCPTT window, under applications, right click and add IBEX as the AUT. The location will be something like `C:\Instrument\Dev\Client\ibex_gui\base\uk.ac.stfc.isis.ibex.client.product\target\products\ibex.product\win32\win32\x86_64`. The name should be filled out automatically as `uk.ac.stfc.isis.ibex.product.product`. Click 'Finish'.

## Create Some Tests

In RCPTT create a new 'RCP Testing Tool Project' called IBEX_System_Tests.

Next create a new 'Test Suite' called All_Tests.

Next create a new 'Context' of type 'Workspace'. Under 'Workspace Options' tick 'Clear workspace'. Add 'isis.log, logs' to 'Do not clear'.

Create another 'Context' this time of type 'Launch'. Under options select 'Terminate existing launches' and 'Clear launch configurations'.

Add both of these contexts to 'Default Contexts' under 'Project Settings'.

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
wait 2000
get-view Blocks | get-label "NEW_BLOCK:" | get-property "toString()" | equals "Label {NEW_BLOCK: }" | verify-true
```

Note here the line `wait 2000` was added manually, this is required as the BlockServer takes some time to respond to the request. Anything that depends purely on the GUI should not need to wait like this.

Finally, under 'All_Tests' choose 'Add Test Case' from the buttons on the right and add the newly created test. Add more tests here to run them one by one.

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

## Useful links

API - possibly out of date? [http://download.xored.com/q7/docs/ecl-api/latest](http://download.xored.com/q7/docs/ecl-api/latest)
RCPTT Documentation - [http://www.eclipse.org/rcptt/documentation/](http://www.eclipse.org/rcptt/documentation/)
Tutorial on RCPTT - [http://eclipsesource.com/blogs/tutorials/rcp-testing-tool-rcptt-basic-tutorial/](http://eclipsesource.com/blogs/tutorials/rcp-testing-tool-rcptt-basic-tutorial/)