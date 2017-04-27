> [Wiki](Home) > [Project tools](Project-tools) > [Working with git and github](Working-with-git-and-github) > Git cribs

Steps for Developing Code with existing Git Repos
=====================================================

Development work
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Checkout the master branch (if not already in the master branch)
* Make sure that the master branch is up to date (varies by repo)
* Create a new branch: ``git checkout -b [branch-name]``
* Do the development work in the most appropriate editor (e.g. Eclipse for the GUI, notepad++ for .db changes)
* Update copyright notices on edited files to the current year to read ``Copyright (C) <first year> - <current year> ...``
* In Git Bash, add files to the branch and commit as appropriate
* Ensure that the master branch is up to date: ``git pull origin master``
* If the branch is only in the local copy of the repo: ``git rebase master``, otherwise ``git merge master``
* Fix any merge errors if required
* If the branch is only in the local copy of the repo: ``git push -u origin [branch-name]``, otherwise ``git push origin [branch-name]``
* Go to GitHub and create the pull request, don't forget a brief test plan
* Bored of being asked for your username and password? Read [this](https://help.github.com/articles/caching-your-github-password-in-git/).

Reviewing work for the GUI
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Open eclipse
* Import any new packages
* Refresh the packages
* Test the changes
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request.
* Check on the delete branch button on the merged page

Reviewing work for the 'top' of EPICS (no other related changes)
----------------------------------------------------------------------------------
* Check the list of files to be merged on the GitHub PR page - if one of them is _.gitmodules_ then the PR **should not be merged** and needs to be either amended or recreated. 
* Navigate to the appropriate directory in Git Bash
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Test the changes, don't forget makes if required
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request
* Check on the delete branch button on the merged page

Reviewing work for the subModules of EPICS
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
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
* Add in the tested submodules: ``git add [tested merged submodules]`` (example: ``git add ioc/master/`` to add ``EPICS-ioc``)
* Commit the updated submodules, with the comment as "Update submodules": ``git commit -m "Update submodules"``
* Push the changed submodules back to GitHub: ``git push --recurse-submodule=check``

Updating all Submodules
------------------------

The following command used to be used in the project I leave it here for the minute. I believe that when run from the EPICS directory it updates all submodules by merging in the last commit from origin. This feels like you could have problems if your submodule is on a different branch

    git submodule update --remote --merge

Updating the GUI
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Make sure you are in the master directory
* Get the latest version: ``git pull``
* Open eclipse
* Import any new packages
* Refresh the packages

Updating EPICS
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Make sure you are in the master directory
* Get the latest version: ``git pull``
* Get the latest submodules to be used with the system: ``git submodule update --merge``
* Rebuild as appropriate
* Occasionally add ``--init`` to the submodule update to get any new submodules
* If you only want the head files for the submodules leave off the ``--merge`` from the submodule update

Cleaning up local installations (allowing yourself to see the wood, or branches, for the trees)
------------------------------------------------------------------------------------------------
* In Git Bash, browse to any repo that might need cleaning up (the GUI is a prime example for this)
* Update the repo: ``git remote update``
* Remove local listings of closed branches: ``git remote prune origin``
* Check the list of branches: ``git branch -a``
* Remove any out of date local branches: ``git branch -d [unused-local-branches]``

Steps for Developing Code with new Git Repos
=====================================================

See [Adding new modules](Adding-new-modules). If reviewing this you will need to checkout the branch on main EPICS and do `git submodule update --init` to initialise the newly created submodule into the tree. Everything else is as normal.

Git Merge notes crib sheet
=====================================================
The basic outline of the git merge entries are:

```
  <<<< HEAD
  The code in the local branch
  =====
  The code in e.g. master
  >>>> master
```

If there are any common ancestors, there may be extra blocks in the area to merge.
