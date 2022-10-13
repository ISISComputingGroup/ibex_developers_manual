It is possible to use one of the intermediate outputs from a build server as the basis of your local development environment. This can provide you with either a normal `Release` build (EPICS_HOST_ARCH=windows-x64), or a `Debug` build (EPICS_HOST_ARCH=windows-x64-debug) 

If you wish to use a `Debug` build, replace `x64` in paths below with `x64-debug`

NOTE: if you just want a recent EPICS build for somewhere, you just need to run the `install_to_inst.bat` in the appropriate build on `kits$` when connected from the machine you want to install it on

## EPICS

### quick instructions

* You need to be using a Visual Studio compatible with the build server, currently `Visual Studio 2019` and from "help about" it needs to be `16.11.*` or later
* run `stop_ibex_server.bat` from `c:\Instrument\Apps\EPICS` (if this directory already exists)
* rename any existing `c:\Instrument\Apps\EPICS` to a different name. If you care about the contents, then keep this for a later rename back. If you don't care (all work pushed to github) then delete it. The reason for doing a rename first is that it confirms no EPICS processes remain running that may cause the robocopy below to not complete properly.     
* run `robocopy \\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS\x64 c:\Instrument\Apps\EPICS -MIR -NFL -NDL -NP -R:1 -MT -LOG:NUL` and wait
 
### details

The EPICS clean Windows 10 Jenkins build workspace is copied to  `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS\x64` - this contains 
much more than an instrument installation e.g. it has all the local `.git` submodules and `*.lib` link libraries as well as temporary build (`O.*`) object file directories. It can thus be used as the basis for rapid further development work on your local computer. A standard instrument debug install for example would allow you to run an ioc in debug mode, but any further development would require re-generating the relevant `*.lib` files need to link the IOC and so take longer than using a developer debug build. 

CAUTION: updating an existing `C:\Instrument\Apps\EPICS` by the mechanism described here is the equivalent of deleting the directory, a full new `git clone --recursive` and then a build. You will lose all current changes to files and also any local git branches you created in that directory. Any changes there you want to keep you must push to Github and then re-checkout the branch after the update. Stashing changes to files is not enough as the local git repos are replaced - you need to push remotely.

After running above robocopy command, you should have a compiled and ready to use distribution, with git pointing at current commit heads.
This may take a while to complete - at least 10 minutes, but longer if your disk is not an SSD for example.

**Alternative for slow network connection**

You can instead copy `EPICS-x64.7z` from `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer` and unpack this locally using
the [7-zip](https://www.7-zip.org/) program. Either drag the file using windows explorer, or if you have a very slow connection or one that might get interrupted you can try using `robocopy` in _restartable mode_. Open a cmd prompt, change to the relevant directory and type:
```
robocopy "\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer" "." EPICS-x64.7z /J /Z 
```
Note that this pre-allocates the full file space before starting the copy. I found that if I interrupt the copy with Ctrl-C and then type the command again, it picks up where it left off, so it looks hopeful it will handle network connection breaks.
 
### Using Files

After copying note that all submodules will be on a detached HEAD. 
 
If you wanted to temporarily use an updated distribution for e.g. a review then you can: 
- rename current `c:\Instrument\Apps\EPICS` to `c:\Instrument\Apps\EPICS-keep`
- use one of the above procedures to create a new `c:\Instrument\Apps\EPICS`
- checkout branches required for review, run make in just these directories if required
- when done delete `c:\Instrument\Apps\EPICS` and rename `EPICS-keep` back to `EPICS`

This scheme works as Visual Studio is binary compatible (even at object file level) from version 2015 onwards. Linking must be done with the most recent visual studio version used, the build server is currently running 2019, so any developer must also be using Visual Studio 2019.  
 
### NOTES

We now copy `CMakeCache.txt` across, if we later again have different developer and build server versions of visual studio then we will again need to not copy it as it is invalid if the visual studio version number is different (2017 v 2019). 

CMake is used in a few third party modules e.g. MySQL, gsl, OpenCV. Compatible binaries for these will always be copied across, so IOCs can be compiled and linked, but if `CMakeCache.txt` is missing a `make` in the top level will rebuild these modules, some of which do take a while.
