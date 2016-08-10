On windows it takes some tome to do the checkRelease part of the build, which in our case is duplicated work as we use a MASTER_RELEASE file. To disable this edit base/master/configure/CONFIG_COMMON and change

     CHECK_RELEASE_YES = checkRelease

to

    CHECK_RELEASE_YES = noCheckRelease
 