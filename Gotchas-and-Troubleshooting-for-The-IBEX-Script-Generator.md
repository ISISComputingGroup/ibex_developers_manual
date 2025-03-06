# Troubleshooting

## Script generator tab is not shown

By default the script generator is disabled in the IBEX GUI. To enable it [Follow this step](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/The-IBEX-Script-Generator#adding-the-perspective-into-the-client)

## Cannot open generated script in notepad++ from the FileMessageBox

Currently, we search for notepad++ in "Program Files" and "Program Files (x86)". It may be that notepad++ on the computer being used isn't stored in those two. For the time being copy and paste the file location to open with their preferred editor. 

## Warning: Could not load any script definitions from `<FileSystemLocation>`

This could be due to 4 things:

- The script definitions have not been loaded into the correct place in the filesystem
   - Indicated in the log by `Error loading from <FileSystemLocation>`
   - To fix simply move them into the location that is given in the warning message
- The IBEX preference is not pointing to the correct location in the file system
   - Indicated in the log by `Error loading from <FileSystemLocation>`
   - For a temporary fix you can move the script definitions into that location, but for a better fix (see gotcha below) ensure that the preference is pointing to the correct location (The preference can point to multiple locations by separating them with commas)
- The script definitions all have errors on them and cannot be loaded
   - Indicated in the log by `Error loading <ScriptDefinitionName>: <error>`
   - The script definitions are maintained by the instrument scientists, however, obviously provide support and guidance for this
- There is a chance that Python has crashed due to an error
   - This will likely be in the log

## Some of my script definitions have not loaded

- We can point a preference to where to load script definitions from. This can be a combination of different places separated by commas. One of these preferences may be slightly incorrect and the script definitions from that location not loaded.
   - Indicated in the log by `Error loading from <FileSystemLocation>`
   - Find out where the preference should point (see gotcha below), adjust it and reload the GUI
- Some of the script definitions may have errors in them and so failed to load
   - Indicated in the log by `Error loading <ScriptDefinitionName>: <error>`
   - The script definitions are maintained by the instrument scientists, however, obviously provide support and guidance for this

## The script generator renders as a blank view

- Delete the `workspace` folder (next to the executable for the script generator) and then retry launching it. If the workspace is owned by a different user, this can cause problems with file permissions.

## The script generator is constantly loading

- This is likely based on loading a dependency
    - Failing to load Python for some reason, check logs for Py4J exceptions (check if a C:\Instrument\Apps\Python3 is interfering)
    - Failing to load git, check log files (the possible solution is to install git separately so we pick up the system git)

# Gotchas

## Preferences

Currently, we cannot load the main ibex client preferences from the script generator. So the script generator has it's own plugin_customization.ini containing some duplicate preferences i.e. script_generation_folder and script_generator_config_folder. When editing the preferences these should be changed in both files.