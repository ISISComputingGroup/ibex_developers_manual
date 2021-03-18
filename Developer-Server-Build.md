It is possible to use one of the checkouts from a build server as the basis of your local build.

## EPICS

The EPICS clean Windows 10 build workspace is copied to  `\\isis\inst$\Kits$\CompGroup\ICP\developer\EPICS\x64` - this contains much more than a distribution e.g. it has all the local .git submodules and temporary build files. It can be used as the basis for work on your local computer.

CAUTION: updating an existing `C:\Instrument\Apps\EPICS` is the equivalent of deleting the directory, a full new checkout and then a build. You will lose all changes to files and also any local git branches you created. Any changes you want to keep you must push to github and then re-checkout the branch after the update. Stashing changes is not enough as the local git repos are replaced - you need to push remotely.

After running this command, you should have a compiled and ready to use distribution
```
robocopy \\isis\inst$\Kits$\CompGroup\ICP\developer\EPICS\x64 c:\Instrument\Apps\EPICS -MIR -NFL -NDL -NP -R:1
```
If you wanted to temporarily use an updated distribution for e.g. a review then you can: 
- rename current `c:\Instrument\Apps\EPICS` to `c:\Instrument\Apps\EPICS-keep`
- run above `robocopy` command to create a new `c:\Instrument\Apps\EPICS`
- checkout branches for review, run make in these directories
- when done delete `c:\Instrument\Apps\EPICS` and rename `EPICS-keep` back to `EPICS`

if you wish to work with a debug build, replace `x64` with `x64-debug` in above `robocopy`

This scheme works as Visual Studio is binary compatible (even at object file level) from version 2015 onwards. Linking must be done with the most recent visual studio version used, the build server is currently version 2017, so any developer using Visual Studio 2017 or 2019 can use this approach.  
 