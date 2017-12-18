TODOs For Eclipse 4 migration:

- Recommended synoptic code in config editor has been commented out
- CTRL + ALT + P preference menu does not work. The `preferencePages` extension point is not available anymore in E4. Someone developed a plugin which provides a preference page extension point for E4 applications which can be found [here](https://github.com/opcoach/e4Preferences)
- Switching perspectives is quite slow.
- Status bar is left justified?
- Menu bar items do not work (other than configuration related ones)
- To change the version for the about menu you must change it in e4.client/pom.xml
- `BeamStatusView.java`: The PVs haven't been connected to the beam status view because the archiver doesn't connect properly yet
- `BeamStatusView.java`: Using the `showToolbar(false)` command doesn't actually hide the toolbar in the beam status view. I've tried working around this but ran out of time. We should sort it out eventually but I've left it for the time being. We may want to change that entire part eventually to just be two databrowsers in different tabs rather than embedding the graph in a separate view. That relies on a later bit of work though.
- The MCR news and stats panel haven't been added to the Beam Status perspective. As per the Experiment Details perspective, these should ideally be in separate parts
- Right click on block menu is in something I touched but is probably best done as part of the blocks migration
- Reenable detecor diagnostics on tab changes PV is DAE:DIAG:ENABLE:FOR
- Log plotter within OPIs do not work. They need the changes to CSStudio from this pull request (https://github.com/ISISComputingGroup/CSStudio_3_3/pull/2/files). Currently the e4 gui just points at download.csstudio.org so doesn't have this change.
- Minimising views causes some very odd behaviour, we should capture what we actually want to happen and implement it.
- Perspectives currently cannot be hidden in the preferences. This is used for the NICOS perspective and the Script Generator.
- Verify that scripts within OPIs work properly. E.g. the HVCAEN is throwing errors.
    - Another example. Start a Eurotherm in RECSIM mode. The error messages on the OPI don't work and the console appears with messages of the form:
```
2017-10-25 14:42:26 ERROR: Error from pv connection layer: 
java.lang.IllegalArgumentException: Data source loc for loc://TE:NDW1695:EUROTHRM_01:A07_ramp_file_type("ramp") was not configured.
2017-10-25 14:42:26 ERROR: Error from pv connection layer: 
java.lang.IllegalArgumentException: Data source loc for loc://TE:NDW1695:EUROTHRM_01:A07_calibration_file_type("calibration") was not configured.
```
- Get genie_python talking to PVs. Currently it is getting `null` as it's `CA_ADDR_LIST` which causes issues.
- DAE perspectives need scrollbars
- DAE detector diagnostics are not being enabled properly
- Colour scheme is only read once when Motors view is initialised (cannot be changed afterwards)
- Switching to the scripting perspective is very slow. It's probably no better than e3 but there should be some feedback to the user that the perspective is being opened.
- The scripting perspective does not switch instruments properly
- The way the scripting perspective is created is confusing and messy, we should try and fix it 
- At the moment the log plotter branch will only display the empty view, need to actually display a plotter with a PV
- Need to sort out the access to the log plotter from OPIs and Blocks
- The script generator perspective has only been partially migrated. 
    - The different parts are not linked by an underlying model so the functionality will not work. 
    - The layout has not been updated to scale correctly. 
    - There are several buttons from the original view which no longer appear in the perspective.
- The synoptic perspective does not display correctly if it is opened too soon after the GUI is started.