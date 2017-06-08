# Java licensing

See https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Understanding-Java-Licensing

# Update my Instrument

[Developer Updating](Developer-Updating)

# Make my Build Faster but less Safe

    Turn off the check release flag (DO NOT CHECK THIS CHANGE IN)

    Line 46 of `...EPICS\base\master\configure\CONFIG_COMMON`

    EDIT THE SECTION TO READ

    ```
    # Check configure/RELEASE file for consistency
    CHECK_RELEASE_YES = noCheckRelease
    CHECK_RELEASE_NO = noCheckRelease
    CHECK_RELEASE_WARN = warnRelease
   ```
