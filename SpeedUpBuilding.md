On windows it takes some time to do the checkRelease part of the build, which in our case is duplicated work as we use a MASTER_RELEASE file. 


To disable this turn off the check release flag (DO NOT CHECK THIS CHANGE IN). Edit line 46 of `...EPICS\base\master\configure\CONFIG_COMMON` to read

    # Check configure/RELEASE file for consistency
    CHECK_RELEASE_YES = noCheckRelease
    CHECK_RELEASE_NO = noCheckRelease
    CHECK_RELEASE_WARN = warnRelease

