> [Wiki](Home) > [Project tools](Project-tools) > [Working with git and github](Working-with-git-and-github) > Git cribs

=====================================================
Steps for Developing Code with existing Git Repos
=====================================================
----------------------------------------------------------------------------------
Development work
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Checkout the master branch (if not already in the master branch)
* Make sure that the master branch is up to date (varies by repo)
* Create a new branch: ``git checkout -b [branch-name]``
* Do the development work in the most appropriate editor (e.g. Eclipse for the GUI, notepad++ for .db changes)
* In Git Bash, add files to the branch and commit as appropriate
* Ensure that the master branch is up to date: ``git pull origin master``
* If the branch is only in the local copy of the repo: ``git rebase master``, otherwise ``git merge master``
* Fix any merge errors if required
* If the branch is only in the local copy of the repo: ``git push -u origin [branch-name]``, otherwise ``git push origin [branch-name]``
* Go to GitHub and create the pull request, don't forget a brief test plan

----------------------------------------------------------------------------------
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

----------------------------------------------------------------------------------
Reviewing work for the 'top' of EPICS (no other related changes)
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Test the changes, don't forget makes if required
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request
* Check on the delete branch button on the merged page

----------------------------------------------------------------------------------
Reviewing work for the subModules of EPICS
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Update the repo: ``git remote update``
* Checkout the branch with the changes to review: ``git checkout [branch-name]``
* Build, make, update access to the code as necessary. If changing something in support, don't forget to make IOC entries as well
* Test the changes
* If the changes don't work, or you notice they break something else, talk to the developer and get it corrected
* Once the tests have been passed, go to GitHub and merge the pull request
* Navigate to the 'top' EPICS module in Git Bash, note that these changes are undertaken in the master thread
* Update the remote submodules to the latest version: ``git submodule update --remote --merge``
* Add in the tested submodules: ``git add [tested merged submodules]``
* Commit the updated submodules, with the comment as "Update submodules": ``git commit -m "Update submodules"``
* Push the changed submodules back to GitHub: ``git push --recurse-submodule=check``

----------------------------------------------------------------------------------
Updating the GUI
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Make sure you are in the master directory
* Get the latest version: ``git pull``
* Open eclipse
* Import any new packages
* Refresh the packages

----------------------------------------------------------------------------------
Updating EPICS
----------------------------------------------------------------------------------
* Navigate to the appropriate directory in Git Bash
* Make sure you are in the master directory
* Get the latest version: ``git pull``
* Get the latest submodules to be used with the system: ``git submodule update --merge``
* Rebuild as appropriate
* Occasionally add ``--init`` to the submodule update to get any new submodules
* If you only want the head files for the submodules leave off the ``--merge`` from the submodule update

------------------------------------------------------------------------------------------------
Cleaning up local installations (allowing yourself to see the wood, or branches, for the trees)
------------------------------------------------------------------------------------------------
* In Git Bash, browse to any repo that might need cleaning up (the GUI is a prime example for this)
* Update the repo: ``git remote update``
* Remove local listings of closed branches: ``git remote prune origin``
* Check the list of branches: ``git branch -a``
* Remove any out of date local branches: ``git branch -d [unused-local-branches]``

=====================================================
Steps for Developing Code with new Git Repos
=====================================================
This will only be applicable for new submodules on the whole, and needs completing by someone who knows this

=====================================================
Git Merge notes crib sheet
=====================================================
The basic outline of the git merge entries are:

::

  <<<< HEAD
  The code in the local branch
  =====
  The code in e.g. master
  >>>> master

If there are any common ancestors, there may be extra blocks in the area to merge.
