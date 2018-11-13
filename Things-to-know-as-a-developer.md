# Java licensing

See https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Understanding-Java-Licensing

# Update my Instrument

[Developer Updating](Developer-Updating)

# Make my Build Faster but less Safe

See [Speed Up Building](SpeedUpBuilding)

# A couple of other building tricks

## Run on one thread to clearly see the source of the error

Navigate to the directory for the module that is erroring during a build and run: `make -j1`

## Ignore any build errors

Do this when you know that you can safely ignore them, for example, you need a build of a specific IOC and one you won't be using will be is stopping your build - use with extreme caution! Navigate to the top of the directories and run: `make -i`

# Make Notepad++ Highlight DB Syntax

In Notepad++ Menu -> Language -> Define Your Language
Then import the file `...EPICS\editors\Notepad++\userDefineLang.xml`

# Python conventions

See [Python Conventions](python-conventions) for more information