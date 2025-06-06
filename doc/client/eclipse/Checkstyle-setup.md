# Checkstyle setup

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
            - Name: `checkstyle.suppressions.file`
            - Value: `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.client.tycho.parent\suppressions.xml`
1. Apply and close: you should now be setup
    1. If you have issues with the highlight colour on a dark theme you can go to: Window -> Preferences, General -> Editors -> Text Editors -> Annotations to change it.

## To skip checkstyle processing for a method or all elements of a class.

1. Suppose you run build.bat and there are checkstyle violations.
2. Open the file checkstyle-result.xml in the particular project you have issues, it will show you the error, for example: <error line="29" column="9" severity="warning" message="Missing a Javadoc comment." source=`"com.puppycrawl.tools.checkstyle.checks.javadoc.JavadocVariableCheck"/>`
3. In the example above the error is generated by the checker `JavadocVariableCheck which implies that the variable defined in line#29 doesn't have a javadoc`.
4. It is possible that for this variable javadoc isn't necessary. For examples it is a file with lots of constants identifying magic numbers and strings. It is impractical to provide javadoc for all of them.
5. In such case we might want to suppress the checkstyle inspection for this file. There are two ways of doing it:

    5.1 - Locate the suppressions.xml file and mention the file name or pattern to skip processing. This is useful when you have a class of files you wish to skip, for examples test files. Different patterns can be separated by '|' as it is a regular expression.

    5.2 It may be more relevant to only suppress for a specific file or method or variable. In this case we can use the annotation @SuppressWarnings("checkstyle:<SOMETAGHERE>"). Recall the example above where the error was from the checker `JavadocVariableCheck`. The tag to use in this case is `javadocvariable` - take the checker class name, remove the word Check at the end and replace all capital letters by small hand letters.

6. Run the build again, the checkstyle violations will be suppressed.

## Useful links

https://checkstyle.org/eclipse-cs/#!/custom-config