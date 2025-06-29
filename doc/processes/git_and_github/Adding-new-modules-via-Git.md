# Adding new modules
 
There are two use cases for adding a submodule:

1. When the code is new, e.g. for a support module for a new device (Marked with **New** below)
1. When importing code from a 3rd Party e.g. a fork of another github project (Marked with **3rd party** below)
    > For most cases, this should be done by forking the repo, as it makes dependency updates *much* simpler to manage. However, there are instructions included on this page for how to do this without simply forking a repo, covered in 3a "3rd Party Initial Import". This should only be used in cases where forking is not possible for some extreme edge case. In most cases, forking a repo, creating an "IBEX" branch, and setting that branch as default in our ISISComputingGroup will suffice.


## 1 Create submodule in GitHub

1. Create a new GitHub repository using the "new repository" button on https://github.com/ISISComputingGroup. Name it and fill in a description. The naming conventions are:

    *  EPICS submodules should have an "EPICS-" prefix, e.g. for support modules. 

1. Decide on public or private repository, if you create it private one you can easily make it public later, but there is a limit on how many private repositories we can have at any one time. Repositories should be private if we do not wish to share the code.

1. Start choice:
    * **3rd Party** Create a blank repository i.e. without a README, licence or `.gitignore` file. 

    * **New** Create a repository with a readme, but no `.gitignore` or licence. When it is created Use ISIS `.gitignore` files.

1. Click `Create Repository`

1. Add team access

    - Select Settings tab
    - Manage Access (left)
    - Click "Invite teams or people" and add both `ICP-Write` (give this `Write` access) and `ICP-WriteAndMerge` (give this `Maintain` access) to the repository
    - If it is a private repository also add `ICP-Read` as `Read` access

## 2 Get the repository

1. Move to a new branch in the EPICS directory for your ticket. 
1. Create a directory root for the submodule, e.g. for Danfysik in support
```
    cd EPICS/support
    mkdir danfysikMps8000
```
1. Add a Makefile in the directory, copy it from e.g. ../calc/Makefile  
1. Adjust the Makefile in the parent directory to include the new module, e.g. add to `SUPPDIRS` in `...EPICS\support\Makefile`.
1. Add all changes to git.

## 3a *3rdParty* Initial import

Software imported from outside should use a "vendor branch" so new versions are easy to merge in. 

1. Create new git repository called master:
```
    cd EPICS/support/danfysik8000
    mkdir master
    cd master
    git init
```
1. Unpack the initial vendor code. Often unpacking the code on Linux is preferred as there are less line endings issues.
1. If it unpacks to something like 1-11/... then move everything up a level. You want the top level directory to contain the usual EPICS configure and *App directory layout. 
1. Delete any files that are not source files or directories e.g. O.Common, O.linux-x86 , top level bin and lib, db that might have got left in.  
1. Delete any .svn directories and files that end in a ~ (temporary files). Then add the files and push to GitHub
 ```
    git add .
    git commit -m "Imported danfysik 8000 version 1.11"
    git remote add origin https://github.com/ISISComputingGroup/EPICS-danfysik8000.git
    git push -u origin master
```
1. Create the vendor branch
```
    git checkout -b vendor
    git tag -a vendor_1_11 -m "Tag of danfysik 8000 import version 1.11"
    git push origin vendor
    git push --tags
```
1. Switch to the branch for your ticket (When you create the pull request it can be created from this branch to master):
```
    git checkout TicketXXX_description
```
1. Make local changes. 
    - Create a readme.md to say where we got the code originally from 
    - Add an initial `.gitattributes` and `.gitignore` (often using a copy from an older repo).

1. Make sure it builds. You'll probably need to update `configure/RELEASE` to be like e.g. `../calc/master/configure/RELEASE`. Also check the Makefile for both *App and *app targets as well as iocBoot and iocboot - on windows this results in a double match due to case insensitivity, so remove the the *app and iocboot

## 3b *New* Initial import

1. Clone the repository in to the correct directory with the directory name master:
```
    cd EPICS/support/danfysik8000
    git clone https://github.com/ISISComputingGroup/<repo name>.git master
```
1. Switch to the branch for your ticket (When you create the pull request it can be created from this branch to master):
```
    git checkout TicketXXX_description
```
1. Edit/Create a readme.md to say what the module does 
1. Add an initial `.gitattributes` and `.gitignore` (often using a copy from an older repo).

## 4 Adding module as submodule
This should be undertaken by the reviewer as part of the merge process to avoid issues with merge conflicts in epics top caused by IOC master.
1. Add the new repository as a submodule:
    ```
    cd EPICS/support/danfysik8000
    git submodule add https://github.com/ISISComputingGroup/EPICS-danfysikMps8000.git master
    ```
    note: if the default branch is not `master` e.g. `main` is now the default on github then you must specify this with `-b` e.g.
   ```
    git submodule add -b main https://github.com/ISISComputingGroup/EPICS-danfysikMps8000.git master
   ```
   The `master` at the end of the command is the local directory name, which we are keeping the same at the moment.
   If you forget to do this, then you can edit `.gitmodules` at the top level directly and add a `branch = main` line to the submodule entry (see other entries in the file for example), then commit and push this change.


1. Add the files generated by adding the submodule
    ````
    cd EPICS
    git add .gitmodules
    git commit -m "Add danfysikMps8000 submodule"
    ````
1. Next make sure that the whole thing builds from the support level (this will only work for a vendor branch).
    ````
    cd ..\EPICS\support
    make danfysikMps8000
    git status
    ````
1. Adjust `.gitignore` and `.gitattributes` to make sure they don't contain file that you have just built. Check `make clean uninstall` works. 

Once all the changes in the submodule are merged, create a commit in EPICS top using `git commit -m "add submodule <module name>"`, and then pushing `git push --recurse-submodule=check`.

## Updating vendor branch

Here we will update the vendor branch with new code, tag this revision, and then use a separate branch to merge new upstream changes into master 

First create your update branch
```
    git checkout master # or main
    git pull
    git checkout -b TicketXXX_update_to_danfysik_1_12
```

now checkout the vendor branch and remove all local files. You need to remove all current files before you unpack the new files or else you will either not pick up files removed in the latest version, or a file that is renamed will not get tracked properly by git as the original will still exist in your local source.  
```
    # If in git bash shell:
    git checkout vendor
    git pull
    rm -fr *
    ls -a
    # now remove any file or directory starting with a `.` but _do not_ remove `.git`
```
Then unpack the new code from the zip/tar into the directory in the same way as above. You'll have files added, removed and changed to handle. Type  `git status`  and remove unwanted added files like binaries and temporary files as described above. Then type:  
```
    git add -u .
```
This will add changed files. Again check with a   `git status`  that all is looking right before using: 
```
    git add .
```
which adds new and removes deleted files. As a final check run:
```
    git status --ignored
```
This will show files in the directory currently ignored by git via a `.gitignore`. As you started from an empty directory, and unpacked a clean vendor release, consider carefully whether these files should actually be added. If they should, you will need to use `git add -f` to force an add. There are several reasons why files may get ignored when they should be added:
- Windows/Unix case sensitivity difference. A `.gitignore` may contain `db` or `db/` as a directory to ignore. The top level `db` directory is usually a top level install directory to be ignored, the real files are in the `*App/Db` subdirectory. However as the windows file system is case insensitive git treats `db` and `Db` as the same so just `db` in a `.gitignore` will incorrectly exclude `*App/Db` files and cause us to miss adding them. We usually change a `db` to something more selective in our local `.gitignore` version post merge e.g. `/db/` means only match `db` at top level and not in subdirectories. There may be other case sensitivity issues, but this is the most common one.
- a `.gitignore` pattern may be too selective for importing. For example it may exclude `*.local` to ignore files like `RELEASE.local` created later during development, but the distribution has an `EXAMPLE_RELEASE.local` that should be imported by us.

Unless a new file is obviously included by error in the distribution, it is probably best to import everything in the vendor release distribution zip/tar file. 
    
Finally commit and tag the changes e.g.
```
    git commit -m "Imported danfysik 8000 version 1.12"
    git tag -a vendor_1_12 -m "Tag of danfysik 8000 import version 1.12"
    git push origin vendor
    git push --tags
```
Now go back to your ticket branch that was branched from the old master/main and merge in new version of vendor code via tag
```
    git checkout TicketXXX_update_to_danfysik_1_12
    git pull
    git merge vendor_1_12
```
And resolve conflicts before committing. Now create a PR to merge `TicketXXX_update_to_danfysik_1_12` branch into main/master

### IMPORTANT: checking a vendor branch update
First, you need to be sure your tar/zip contained what you expected. If it came from an official release web page, probably fine. If it was just an auto-created github tagged version then it may be missing a lot of files. github will zip up a repository for you, if the repository contains submodules however these will not get included in the auto generated zip. In this cases if you just take the zip file from github you will end up remove lots of files you really wanted to update. If you do a `git status` and see loads of files being removed, this may have happened. The epics motor and areaDetector modules are cases where care need to be taken.       

You should confirm the number of changes in your new update branch when compared to the new vendor it is based on looks reasonable. For example if our current master when compared to its original old vendor branch had changed 5 files, then after updating vendor and merging you would expect to see something like the same number of file changes. You can do this via git branch compare: compare current master with old vendor tag, and new update branch with new vendor branch tag. The number of changes will not always be identical in the new vendor branch as we do feed some of our changes back upstream if they are not locally specific hence those changes will not need re-applying and no longer show up as a changed file. If you see a large increase in files differences, this likely indicates a merge issue. 
