The jenkins job `TestBuild` builds the branch `testbuild` in the top EPICS git repository and deploys it to a `TestBuild` directory in `kits$\EPICS`. The job is not run automatically on commit - you need to trigger it with `Build With Parameters` in Jenkins GUI at which point you could change e.g. the `EPICS_HOST_ARCH` from `windows-x64` (default) to `windows-x64-debug` if you wished.

To specify your build do the following:
- create and push branches in each submodule where you want to test changes. You do not need to create pull requests, and can call the branches any name you wish.
- in your EPICS top level, if you already have a `testbuild` branch delete this with `git branch -d testbuild`
- check if a `testbuild` branch exists on GitHub https://github.com/ISISComputingGroup/EPICS/branches - if it does, check the other developer has finished and then delete this GitHub remote branch. If they are still using it, then it is probably based on a quite recent commit and you may be able to add your changes to this branch and both use the same jenkins build. 
- If you deleted the remote branch, create a local `testbuild` branch with `git checkout -b testbuild` in your top level EPICS. If you are sharing `testbuild` with another developer, use `git checkout testbuild` which will get the current GitHub `testbuild` 
- now edit `.gitmodules` and for each of the submodules you created a separate  `my_branch_name` branch in add a corresponding `branch = my_branch_name` line to the relevant section of the file
- not commit your `.gitmodule` changes and push to `testbuild` on GitHub
- now start the jenkins build from the GUI

The jenkins job builds "tip of branch" i.e. it will use latest master of all submodules and also latest commits to any `branch =` lines you added. So you do not need to "git add" any submodule directories, and if you push new changes to any branch you can just start a new jenkins build and they will be picked.   


