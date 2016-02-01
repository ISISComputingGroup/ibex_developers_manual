First create a new GitHub repository - all EPICS modules should have an "EPICS-" prefix. Use the "new repository" button on https://github.com/ISISComputingGroup but make sure you create a blank repository i.e. without a README, licence or .gitignore file     decide on public or private repository, if you create it privaste you can easily make it public later, but there is a limit on how many pivate repositories we can have at any one time. In this example we will use the EPICS-danfysik8000 repository

Go into "add teams and collaborators" and add the ICP-Write group to write access to the repository

Software imported from outside should use a "vendor branch" so new versions are easy to merge in.

First create new git repository in a directory away from your epics area, we'll add it to epics as a submodule later

mkdir danfysik8000
cd danfysik8000
git init

now unpack the initial vendor code, if it unpacks to something like 1-11/... then move everything up a level. You want the top level directory to contain the usual EPICS configure and *App directory layout. Also delete any files that are not source files or directories e.g. O.Common, O.linux-x86 , top level bin and lib, db.  Also delete any .svn directories
also files that end in a ~
 



