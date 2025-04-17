> [Wiki](Home) > [Project tools](Project-tools) > [Working with git and github](Working-with-git-and-github) > Github repo tools

# Git Hub Repository Tools

These are stored in [ibex_utils](https://github.com/ISISComputingGroup/ibex_utils) and there are install instructions and help. This is a list of common tasks run under epics terminal:

* List repositories belonging to ISISComputingGroup

   `python Scripts\change_repos.py -u John-Holt-Tessella -o ISISComputingGroup`

* For the standard repositories close all old milestones (with no issues), create new milestone, ensure labels exist (adding --dry-run to this, or any command, will show you what it will do without altering the repository)
 
     `python Scripts\change_repos.py -u John-Holt-Tessella -o ISISComputingGroup --repo-file standard_repos.txt --label-file standard_labels.txt --ms-from 2016-05-19 --ms-to 2016-06-15 --ms-close`


