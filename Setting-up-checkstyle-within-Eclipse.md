## Install the Checkstyle plugin

`Help` > `Eclipse Marketplace...`

## Configure Checkstyle to use external file.

1. Open checkstyle settings via `Window` > `Preferences` > `Checkstyle`

2. Click `New` and select `External Configuration File` for type and name it IBEX Checks.

Select the file at `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.client.tycho.parent\checkstyle.xml`

Click OK

It will find unresolved properties. Click Edit Properties

Click `Find unresolved properties`

It will find `$(checkstyle.suppressions.file` it wil lask if you want to add them click yes.

for it's value put `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.client.tycho.parent\suppressions.xml`

Now select all the folders on your project explorer view and click project > preferences >Checkstyle and select IBEX Checks for all and save.

## Useful links

https://checkstyle.org/eclipse-cs/#!/custom-config