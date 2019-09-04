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

## No rule to make target

This means a Makefile is trying to build something for which an external dependency has been listed and this dependency does not exist and it cannot find a way to generate it. This can be a typo/error in the Makefile itself, but if you have just done an update of many submodules it may mean that one of the auto-generated epics dependencies for the failing module refers to items in another module that now no longer exist. If for example the boost C++ library is updated, MySQL or ISISDAE may fail to build as they use headers from boost that may have been rearranged. If you "make clean uninstall" the failing module it should rebuild everything (including dependencies) and then work. You could also just remove the *.d files (which are auto-generated dependencies) and then make again.
      
# Make Notepad++ Highlight DB Syntax

In Notepad++ Menu -> Language -> Define Your Language
Then import the file `...EPICS\editors\Notepad++\userDefineLang.xml`

Alternatively, download VSCode and install the epics extension.

# Python conventions

See [Python Conventions](python-conventions) for more information