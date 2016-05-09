> [Wiki](Home) > [Project tools](Project-tools) > [Working with git and github](Working-with-git-and-github) > Adding new modules

# Adding a new module

## initial import
In this example we will use the EPICS-danfysik8000 repository

First create a new GitHub repository - all EPICS modules should have an "EPICS-" prefix. Use the "new repository" button on https://github.com/ISISComputingGroup but make sure you create a blank repository i.e. without a README, licence or .gitignore file  Also decide on public or private repository, if you create it private one you can easily make it public later, but there is a limit on how many private repositories we can have at any one time. Also go into "add teams and collaborators" and add the ICP-Write group to write access to the repository

Software imported from outside should use a "vendor branch" so new versions are easy to merge in. First create new git repository in a directory on your computer away from your epics area, we'll add it to epics as a submodule later.

    mkdir danfysik8000
    cd danfysik8000
    git init

Often unpacking the code on Linux is preferred as there are less line endings issues. A vendor branch should contain unchanged original code i.e. don't add our own readme or .gitignore etc here, do that on master  However remove binaries from the unpacked original code if they have been left in and are not relevant
 
Now unpack the initial vendor code, if it unpacks to something like 1-11/... then move everything up a level. You want the top level directory to contain the usual EPICS configure and *App directory layout. Also delete any files that are not source files or directories e.g. O.Common, O.linux-x86 , top level bin and lib, db that might have got left in.  Also delete any .svn directories and files that end in a ~ (temporary files). Then add the files and push to GitHub
 
    git add .
    git commit -m "Imported danfysik 8000 version 1.11"
    git remote add origin https://github.com/ISISComputingGroup/EPICS-danfysik8000.git
    git push -u origin master

then create the vendor branch

    git checkout -b vendor
    git tag -a vendor_1_11 -m "Tag of danfysik 8000 import version 1.11"
    git push origin vendor
    git push --tags

now move back to master and make local changes

    git checkout master

and create readme.md to say where we got the code originally from. You can also add an initial .gitattributes and .gitignore

## Adding module as submodule

create a directory root for the submodule

    cd EPICS/support
    mkdir danfysikMps8000
    git add danfysikMps8000
    git commit -m "Add danfysikMps8000"

Then add new repository as a local directory called "master"

    cd danfysikMps8000
    git submodule add https://github.com/ISISComputingGroup/EPICS-danfysikMps8000.git master

You'll need a Makefile in the directory containing "master", copy it from e.g. ../calc/Makefile  Then add the files

    git add .gitmodules support/danfysikMps8000/Makefile support/danfysikMps8000/master
    git commit -m "Add danfysikMps8000 submodule"

now make sure it builds. You'll probably need to update   configure/RELEASE to be like e.g. ../calc/master/configure/RELEASE   Also check the Makefile for both *App and *app targets as well as iocBoot and iocboot - on windows this results in a double match due to case insensitivity, so remove the the *app and iocboot

    make
    git status

Then create/adjust .gitignore and .gitattributes  and check    make clean uninstall   all work. If everything OK, add new module to support/Makefile and to configure/MASTER_RELEASE

## Updating vendor branch

First checkout the vendor branch and remove all files

    git checkout vendor
    rm -fr *

Then unpack the new code into the directory in the same was as above. You'll have files added, removed and changed to handle. Type  git status  and remove unwanted files like like binaries and temporary files as described above. Then type  

    git add -u .

This will add changed files. Again check with a   git status  that all is looking right before using 

    git add .

to add new and remove deleted files. Then commit and tag the changes

    git commit -m "Imported danfysik 8000 version 1.12"
    git tag -a vendor_1_12 -m "Tag of danfysik 8000 import version 1.12"
    git push origin vendor
    git push --tags

Now you need to go back to master and merge in new version of vendor code

    git checkout master
    git pull
    git merge vendor_1_12

And resolve conflicts before committing



