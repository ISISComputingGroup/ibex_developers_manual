# Deploy workflow

## Deploy script location

Scripts needed are in: `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade`
some instruments it might want instead if not default on cclrc.ac.uk
`\\isis.cclrc.ac.uk\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade`

## Steps

1. Remote desktop in:NDXinstrumentName 
2. Start ibex sever so you can take a 'picture' of some configurations.
3. Run deploy script in the tools' dir, instrument_deploy.bat, double click.

| Config step | Instruction (y/n) | Comment |
| ----------- | ----------------- | ------- |
| Confirm new version | y if correct | N/A |
| Record LabView VIs | y | Take screenshots of blocks and relevant information such as motors in some cases. (for future reference) |
| Save motor parameters | y | Saves into csv file at `C:\Instrument\var\deployment_pv_backups\motors\` |
| Save block params | y | Saves into csv file at `C:\Instrument\var\deployment_pv_backups\` |
| Save block server to file | y | It'll now save existing installation |
| Update Git | y | It will need an admin account password for the instrument |
| Update Java | y | This will be manual: go to `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\` and install the latest version of Java. You can find some more info here: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Upgrade-Java |
| Backup dirs | y | This might take a long time. Close any window that have it open. The dir. Find size of epics i apps dir and then find size of backup in data and then old to find out its stage |
| Verfy backup | y | N/A |
| Backup database | y | N/A |
| Truncate database | y | N/A |
| Start ibex server install | y | N/A |
| Keep old Galil driver | y/n | you can check at `ioc\master\GALIL\GALIL_OLD.txt` |
| Update ICP | y | |
| Upgrade ICP found in LabView | y | Needs admin passowrd |
| Install genie_python | y | N/A |
| Install MySQL | y | |
| Install ibex client with built-in python | y | N/A |
| Update instrument config | y | N/A |
| Automatic config merge | y | N/A |
| Update calibration repo | y | N/A |
| Apply release notes | y | N/A |
| Update release notes | y | N/A |
| Reapply hotfixes | yes if any to reapply | [See "Reapply Hotfixes" section](#reapply-hotfixes) |
| Start ibex GUI | y | N/A |
| Restart vis | yes | N/A |
| Client release test | y | N/A |
| Check version | y | Navigate to Help - > About |
| Confirm genie python works | y | In scripting tab run `g.cshow()` correctly and run as well in `C:\Instrument\Apps\Python 3\genie_python.bat` |
| Confirm config is consistent | y | |
| Check web links work | y | |
| Switch instrument to one correct one without NDX prefix | y| |
| Verify the server is up | y | May need to refresh the PVs |
| Client release tests | n | | 
| Server release tests| y | | 
| Confirm blocks logging as expected | y | Navigate to `C:\Data\[RUN NUMBER]` | 
| Confirm correct branch | y | Open git bash and cd to EPICS | 
| | | | 
| | | | 
| | | | 
| | | | 
| | | | 
| | | | 

## Reapply Hotfixes

1. Go into git bash
2. Outcome: Git diff between new ibex file and data/old file if same then someone merged it with new deploy so all okay
3. Outcome: Git diff is different but there looks to be an open merge then check that the open merge file (GitHub URL and use curl) to compare with new, matches the old file, and thus merge the pull request. Copy the file over from old to new ibex, may need to remove read permissions from the db directory, if permission denied.
4. Outcome: If its not in new deploy already and there's no open pull request for it that got forgotten to be merged, then ask a team member whether the hotfix is still needed or whether it got patched by something else somewhere etc.
    1. If it is still needed then copy over the file to the normal ibex install and make a PR from a new branch, which may need to get a ticket created if it's a large difference or the PR might be enough and just message somewhere for someone to approve it.


Backup and truncation can be done separately from deploy, for example if instrument in cycle:
1. Stop ibex server
2. In `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\truncate_database.db` just double click. Enter database admin password. If you have Keeper type, if not, ask someone. It'll do backup first.
3. Say yes to truncated, enter admin password.


