# Deploy script workflow

Scripts needed are in: `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade`
some instruments it might want instead if not default on cclrc.ac.uk
`\\isis.cclrc.ac.uk\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade`

## Pre-script
1. Use RealVNC Viewer to ensure that the instrument is not currently in use.
1. Remote desktop into the instrument
1. Open git-bash
    1. cd into `C:\Instrument\Apps\EPICS`
    2. Run `git status`
    3. Run `git diff`
    4. Ask senior team member if any of the deleted/new/modified files are of note and record the ones that are, to deal with later.
1. Run deploy script in the tools' directory, you can double click on `instrument_deploy.bat` but it is safer to create a command window and then run the command from there, if the process were to crash you see the last message in the window. The install does now write a log file so this may not be necessary, but i usually still do it this way in case. 

## During script

| Config step (in order of script) | Instruction (y/n) | Comment |
| ----------- | ----------------- | ------- |
| Confirm new version | y if correct | N/A |
| Record LabView VIs | y | Take screenshots of blocks and relevant information such as motors in some cases. (for future reference) |
| Save motor parameters | y | Saves into csv file at `C:\Instrument\var\deployment_pv_backups\motors\` not strictly necessary on a test deploy machine, but useful to do there as well to test the process is still working correctly |
| Save block params | y | Saves into csv file at `C:\Instrument\var\deployment_pv_backups\` |
| Save block server to file | y | It'll now save existing installation |
| Update Git | y | It will need an admin account password for the instrument |
| Update Java | y | This will be manual: go to `\\isis\shares\ISIS_Experiment_Controls_Public\third_party_installers\` and install the latest version of Java. You can find some more info here: https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Upgrade-Java |
| Backup directories | y | This might take a long time. Close any window that have it open. The dir. Find size of epics i apps dir and then find size of backup in data and then old to find out its stage |
| Manually check Python installation | y | `Python` will not exist but `Python3` will, which the script will realise and back up|
| Verify backup | y | N/A |
| Backup database | y | Find password in Keeper |
| Truncate database | y | N/A |
| Start ibex server install | y | N/A |
| Keep old Galil driver | y/n | Should automatically locate the version and proceed but if it requires a decision of which version to use then ask a team member |
| Update ICP | y | N/A |
| Upgrade ICP found in LabView | y | Needs admin password |
| Install genie_python | y | N/A |
| Install MySQL | y | N/A |
| Install ibex client with built-in python | y | N/A |
| Update instrument config | y | N/A |
| Automatic config merge | y | N/A |
| Update calibration repo | y | N/A |
| Apply release notes | y | N/A |
| Update release notes | y | N/A |
| Reapply hotfixes | yes if any to reapply | [See "Reapply Hotfixes" section](#reapply-hotfixes) |
| Update script generator script definitions | y | N/A |
| Remove Instrument Scripts `githooks` | y | N/A |
| Start ibex GUI | y | N/A |
| Restart vis | yes | N/A |
| Client release test | y | N/A |
| Check version | y | Navigate to Help - > About |
| Confirm genie python works | y | In scripting tab run `g.cshow()` correctly and run as well in `C:\Instrument\Apps\Python 3\genie_python.bat` |
| Confirm config is consistent | y | N/A |
| Check web links work | y | N/A |
| Switch instrument to one correct one without NDX prefix | y | N/A |
| Verify the server is up | y | May need to refresh the PVs |
| Client release tests | n | N/A | 
| Server release tests | y | N/A | 
| Confirm blocks logging as expected | y | Navigate to `C:\Data\[RUN NUMBER]` | 
| Confirm correct branch | y | Open git bash and cd to EPICS | 
| Check web dashboard | y | N/A | 
| Run config checker | y | N/A | 
| Save motor params if applicable | y/n| N/A | 
| Save block params | y | N/A | 
| Set username & password | n | N/A | 
| Set autostart script | n | N/A | 
| Inform scientists | n | You can if you want but generally done in release messages |

## Reapply Hotfixes

1. Open git bash.
2. For each file you noted in the pre-script hotfixes instruction
    1. Run `git diff` between the file in the NEW EPICS dir and the `C:\Data\Old\` dir
    2. Use the outcome and response table to evaluate the file

| Outcome for each file of note | Response | 
| ----------- | ----------------- | 
| Returns nothing | Must be part of release so nothing to do | 
| Different but you have checked the repo and found a forgotten pull request that matches (you `curl [URL]` the url of the raw file in the PR and run git diff between old and this PR file) | Merge the pull request. Update submodule (pull latest with merge completed), go to EPICS dir and git add .and push this version of EPICS with the updated submodule version | 
| Different but no open PR | Ask team member whether okay to leave or if it needs to be copied to new install and a PR (and potentially a ticket) to be made |


## Backup and truncation can be done separately from deploy, for example if instrument in cycle:
| Config step | Instruction (y/n) | Comment |
| ----------- | ----------------- | ------- |
|  Stop ibex server | y | N/A |
| Run `truncate_database.db` | y | In `\\isis\shares\ISIS_Experiment_Controls_Public\ibex_utils\installation_and_upgrade\` |
| Truncate db | y | The previous step was just the backup |


