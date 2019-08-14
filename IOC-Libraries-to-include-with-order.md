The following is a list of libraries to include and their order for different record types. These are added to the build.mak in the src directory of the ioc app. The order is important in the static build.

# In general
1. seq and pv should be listed last as any module may add sequencer support at some point
1. calc now depends on sscan so must be listed before sscan (it also depends on seq and pv too)

# specific rules

## Lib section

1. `scalc`: $(APPNAME)_LIBS += calc sscan

## DBD section
1. `scalc`: $(APPNAME)_DBD += calcSupport.dbd
