Scripts needed to be located in: `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade`
some instruments it might want instead if not default on cclrc.ac.uk
`\\isis.cclrc.ac.uk\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade`
# Steps:

1. Remote desktop in:NDXinstrumentName 
2. Start ibex sever so you can take a 'picture' of some configurations.
3. Run deploy script in the tools' dir, instrument_deploy.bat, double click.
4. Says what version it is deploying, say yes
5. Yes to record LabVIEW vis, use snipping tool to screenshot the groups of blocks (the top part with instrument and blocks) if instrument has motors, click on that and take another snipping of what's on that screen, save motor parameters yes, save block parameters yes, they are for more detailed comparisons, picture easier
6. Save to CSV file, say yes/no if motor panel on left side
7. Save block parameters to file
8. Save block server to file say yes
9. it'll now back up existing installation
10. Yes to update git, may ask for pw
11. Yes to everything till Java
12. Yes to Java - go to `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\latest_versions`, go to open Java 18 installer and run that, may need admin pw.
13. Do step backup dirs yes. May take 5 mins. Close any window that have it open. The dir. Find size of epics i apps dir and then find size of backup in data and then old to find out its stage
14. Verify backup yes
15. Do backup yes
16. Do truncate yes
17. Start ibex server install yes
18. Keep old Galil river yes
19. Do step update ICP yes
20. Do step upgrade found in LabView, type in admin password
21. Install genie python yes
22. Install MySQL yes
23. Install ibex client with built-in python yes
24. Update instrument config yes
25. Yes automatic config merge yes, enter db root pw
26. Update calibration repo yes
27. Apply release notes yes
28. Update release notes yes
29. Reapply hotfixes, yes if any to reapply.
	1. Go into git bash
	2. Outcome: Git diff between new ibex file and data/old file if same then someone merged it with new deploy so all okay
	3. Outcome: Git diff is different but there looks to be an open merge then check that the open merge file (GitHub URL and use curl) to compare with new, matches the old file, and thus merge the pull request. Copy the file over from old to new ibex, may need to remove read permissions from the db directory, if permission denied.
	4. Outcome: If its not in new deploy already and there's no open pull request for it that got forgotten to be merged, then ask a team member whether the hotfix is still needed or whether it got patched by something else somewhere etc. 
		1. If it is still needed then copy over the file to the normal ibex install and make a PR from a new branch, which may need to get a ticket created if it's a large difference or the PR might be enough and just message somewhere for someone to approve it.
30. Start ibex GUI yes
31. Restart vis yes
32. Client release test yes
33. Check version yes, go to help and about section in ibex
34. Confirm genie python works, go into scripting and run `g.cshow()` it'll output some stuff that should look correct
35. Confirm this also works in genie_python.bat, in `C:\Instrument\Apps\Python 3\`, run `g.cshow()` in that too
36. Confirm config is consistent with the pictures you took at the start say yes if ok
37. Check all web links work correctly
38. If instrument has NDX prefix, switch instrument to non-NDX prefix version. so set to no by which instrument
39. Verify the server is up, may need to refresh the PVS.

Backup and truncation can be done separately from deploy, for example if instrument in cycle:
1. Stop ibex server
2. In `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\truncate_database.db` just double click. Enter database admin password. If you have Keeper type, if not, ask someone. It'll do backup first.
3. Say yes to truncated, enter admin password.


