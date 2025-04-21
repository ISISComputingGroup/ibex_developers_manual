# Git workflow

## Steps for Developing Code with existing Git Repos

If you are not sure what a git command does, you can take a look at [git commands](Git-Commands)

Development work
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Checkout the master branch (if not already in the master branch) `git checkout master`
* Make sure that the master branch is up to date (varies by repo) `git pull`
* Create a new branch: ``git checkout -b [branch-name]`` where `branch-name` is `TicketXXX_some_description` 
* Do the development work in the most appropriate editor (e.g. Eclipse for the GUI, notepad++ for .db changes)
* Update copyright notices on edited files to the current year to read ``Copyright (C) <first year> - <current year> ...``
* In Git Bash, add files to the branch (`git add <file>`, or `git add -u` to add all modified files, or `git add -A` to add all changed files) and commit (`git commit -m "commit message"`) as appropriate
* Note: if master has updated, 
    * ensure that the master branch is up to date: ``git fetch``
    * Merge in the latest master: `git merge origin/master`
    * Fix any merge errors (if required)
* Push changes using `git push` (if this is the first time the branch is being pushed, use `git push -u origin [branch-name]`)
* Go to GitHub and create the pull request, don't forget a test plan
* Bored of being asked for your username and password? Read [this](https://help.github.com/articles/caching-your-github-password-in-git/).
* If you are creating a new submodule for EPICS, find more info here: [Creating New Submodules in EPICS](/iocs/creation/Creating-New-Submodules-in-EPICS)

## Reviewing work for the GUI

* Navigate to the appropriate directory in Git Bash
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Open eclipse
* Import any new packages
* Refresh the packages
* Test the changes
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request. There will need to be at least one "approving" review before the merge button is enabled - as the reviewer, you can add your review by clicking on "files changed" and then "review changes".
* Click on the delete branch button on the merged page

## Reviewing work for the 'top' of EPICS (no other related changes)

* Useful checklist for reviewing java code: https://dzone.com/articles/java-code-review-checklist
* Check the list of files to be merged on the GitHub PR page - if one of them is `.gitmodules` then the PR **should not be merged** and needs to be either amended or recreated. 
* Navigate to the appropriate directory in Git Bash
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Test the changes, don't forget makes if required
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request. On most repositories, there will need to be at least one "approving" review before the merge button is enabled - as the reviewer, you can add your review by clicking on "files changed" and then "review changes".
* Click on the delete branch button on the merged page

{#git_workflow_reviewing_epics_submodules}
## Reviewing work for the subModules of EPICS

* Navigate to the appropriate directory in Git Bash
* If the submodule is not initialised, run `git submodule update --init` in the directory above
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Build, make, update access to the code as necessary. If changing something in support, don't forget to make IOC entries as well
* Test the changes
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request and delete the branch
* Get the merged pull request in repo: 
    * `git checkout master`
    * `git pull`
* Navigate to the 'top' EPICS module in Git Bash, note that these changes are undertaken in the master thread
* Update master in 'top' 
    * `git checkout master` 
    * `git pull`
* Stage the tested submodules with: ``git add [tested merged submodules]`` (example: ``git add ioc/master/`` to add ``EPICS-ioc``)
* Commit the updated submodules, with the comment as "Update submodules <list of submodules>": ``git commit -m "Update submodules <list of submodules>"``
* Push the changed submodules back to GitHub: ``git push --recurse-submodule=check``
NOTE: if you run `git config --global push.recurseSubmodules check` once, then the above becomes the default push action 

## Updating all Submodules

If you want a clean start then you can use a [[Developer-Server-Build]] rather than an in place git update

The following command used to be used in the project I leave it here for the minute. I believe that when run from the EPICS directory it updates all submodules by merging in the last commit from origin. This feels like you could have problems if your submodule is on a different branch

    git submodule update --remote --merge

A different command, which will get the latest versions of all submodules from github (without merging in any local commits) is:

    git submodule update --init --recursive --remote

Yet another command, which will leave some submodules like adsDriver and others which are forked and would cause a "modified content" warning if running `--remote`:

    git submodule update --recursive

## Updating the GUI

* Navigate to the appropriate directory in Git Bash
* Make sure you are in the master directory
* Get the latest version: ``git pull``
* Open eclipse
* Import any new packages
* Refresh the packages

## Updating EPICS

* Navigate to the appropriate directory in Git Bash
* Make sure you are in the master directory
* Get the latest version: ``git pull``
* Get the latest submodules to be used with the system: ``git submodule update --init --merge``
* Rebuild as appropriate
* If you only want the head files for the submodules leave off the ``--merge`` from the submodule update

## Cleaning up local installations (allowing yourself to see the wood, or branches, for the trees)

* In Git Bash, browse to any repo that might need cleaning up (the GUI is a prime example for this)
* Update all local branches set to track remote branches (does not merge any changes) : ``git remote update``
* Remove local listings of closed branches (can use --dry-run argument just to see what listings would be removed): ``git remote prune origin``
* Check the list of branches: ``git branch -a``
* Remove any out of date local branches: ``git branch -d [unused-local-branches]``

## Steps for Developing Code with new Git Repos

See [Adding new modules](Adding-new-modules-via-Git). If reviewing this you will need to checkout the branch on main EPICS and do `git submodule update --init` to initialise the newly created submodule into the tree. Everything else is as normal.

## Git Merge notes crib sheet

The basic outline of the git merge entries are:

```
  <<<< HEAD
  The code in the local branch
  =====
  The code in e.g. master
  >>>> master
```

If there are any common ancestors, there may be extra blocks in the area to merge.
