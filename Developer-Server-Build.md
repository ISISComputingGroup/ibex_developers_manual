It is possible to use one of the checkouts from a build server as the basis of your local development environment.

## EPICS

The EPICS clean Windows 10 Jenkins build workspace is copied to  `\\isis\inst$\Kits$\CompGroup\ICP\developer\EPICS\x64` - this contains much more than an instrument installation e.g. it has all the local .git submodules and temporary build (object) files. It can thus be used as the basis for further development work on your local computer.

CAUTION: updating an existing `C:\Instrument\Apps\EPICS` is the equivalent of deleting the directory, a full new git clone and then a build. You will lose all current changes to files and also any local git branches you created. Any changes you want to keep you must push to github and then re-checkout the branch after the update. Stashing changes to files is not enough as the local git repos are replaced - you need to push remotely.

After running this command, you should have a compiled and ready to use distribution, with git pointing at current commit heads.
```
robocopy \\isis\inst$\Kits$\CompGroup\ICP\developer\EPICS\x64 c:\Instrument\Apps\EPICS -MIR -NFL -NDL -NP -R:1
```
If you wanted to temporarily use an updated distribution for e.g. a review then you can: 
- rename current `c:\Instrument\Apps\EPICS` to `c:\Instrument\Apps\EPICS-keep`
- run above `robocopy` command to create a new `c:\Instrument\Apps\EPICS`
- checkout branches required for review, run make in just these directories if required
- when done delete `c:\Instrument\Apps\EPICS` and rename `EPICS-keep` back to `EPICS`

If you wish to work with a debug build, replace `x64` with `x64-debug` in above `robocopy` command

This scheme works as Visual Studio is binary compatible (even at object file level) from version 2015 onwards. Linking must be done with the most recent visual studio version used, the build server is currently version 2017, so any developer using Visual Studio 2017 or 2019 can use this approach.  
 