# Speed Up Building

```{note}
This page documents an advanced compilation workflow.

These instructions are unnecessary for a "standard" build
```

On windows it takes some time to do the checkRelease part of the build, which in our case is duplicated work as we use a MASTER_RELEASE file. 

To disable this turn off the check release flag (DO NOT CHECK THIS CHANGE IN). Edit line 181 of `...EPICS\base\master\configure\CONFIG_site` and uncomment the line to read:

    CHECK_RELEASE_YES = noCheckRelease
