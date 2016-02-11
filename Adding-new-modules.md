# Adding a new module
In this example we will use the EPICS-danfysik8000 repository

First create a new GitHub repository - all EPICS modules should have an "EPICS-" prefix. Use the "new repository" button on https://github.com/ISISComputingGroup but make sure you create a blank repository i.e. without a README, licence or .gitignore file  Also decide on public or private repository, if you create it private one you can easily make it public later, but there is a limit on how many private repositories we can have at any one time. Also go into "add teams and collaborators" and add the ICP-Write group to write access to the repository

Software imported from outside should use a "vendor branch" so new versions are easy to merge in. First create new git repository in a directory on your computer away from your epics area, we'll add it to epics as a submodule later.

    mkdir danfysik8000
    cd danfysik8000
    git init

Often unpacking the code on Linux is preferred as there are less line endings issues. A vendor branch should contain unchanged original code i.e. don't add our own readme or .gitignore etc here, do that on master  However remove binaries from the unpacked original code if they have been left in and are not relevant
 
now unpack the initial vendor code, if it unpacks to something like 1-11/... then move everything up a level. You want the top level directory to contain the usual EPICS configure and *App directory layout. Also delete any files that are not source files or directories e.g. O.Common, O.linux-x86 , top level bin and lib, db.  Also delete any .svn directories
also files that end in a ~
 
git add .
git commit -m "Imported danfysik 8000 version 1.11"
git remote add origin https://github.com/ISISComputingGroup/EPICS-danfysik8000.git
git push -u origin master

create vendior branch

git checkout -b vendor
git tag -a vendor_1_11 -m "Tag of danfysik 8000 import version 1.11"
git push origin vendor
git push --tags

now move back to master and make local changes

git checkout master
create readme.md, file to say where we got it from, 


adding new version
checkout vendor branch
rm -fr *
unpack
git add -u .
git add .
git commit -m "Imported danfysik 8000 version 1.12"
git tag -a vendor_1_12 -m "Tag of danfysik 8000 import version 1.12"
git push origin vendor
git push --tags

an then merge

git checkout master
git pull
git merge vendor_1_12

resolve conflicts


cd EPICS/support
mkdir danfysikMps8000
git add danfysikMps8000
git commit -m "Add danfysikMps8000"

cd danfysikMps8000
 git submodule add https://github.com/ISISComputingGroup/EPICS-danfysikMps8000.git master
now add a MAkefile to the same directory as "master", copy it from e.g. 

cp ../calc/Makefile .

git add .gitmodules support/danfysikMps8000/Makefile  support/danfysikMps8000/master
git commit -m "Add danfysikMps8000 submodule"

now make sure it builds

configure/RELEASE like ../calc/master/configure/RELEASE
Makefile for *App and *app as well as iocBoot and iocboot

make
git status
add .gitignore and .gitattributes

make make celan uninstall   all work

if all OK, add it to support/Makefile

add to configure/MASTER_RELEASE

ioc/master

mkdir DANFYSIK8000

makeBaseApp.pl -t ioc -i DANFYSIK8000-IOC-03









