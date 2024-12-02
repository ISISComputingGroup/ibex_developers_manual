It is possible to use one of the intermediate outputs from a build server as the basis of your local development environment. This can provide you with either a normal `Release` build (EPICS_HOST_ARCH=windows-x64), or a `Debug` build (EPICS_HOST_ARCH=windows-x64-debug) or a different architecture such as 32bit (EPICS_HOST_ARCH=win32-x86)

> [!NOTE]  
> if you just want a recent EPICS build to run somewhere and do not need to be able to develop using it, you just need to run the `install_to_inst.bat` in the appropriate build on `kits$` when connected from the machine you want to install it on

## EPICS

You need to be using a Visual Studio compatible with the build server, currently `Visual Studio 2022` 



> [!TIP]
>### Quick Instructions  
> Run `install_developer_build.bat` in either `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS` (for 64bit builds, what you usually need) or `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS32` (for 32 bit builds, only if you have to build/test a specific driver needing 32bit versions). It will prompt you to choose from  normal/debug/static - in most cases `normal`
is what you want and is what is deployed to an instrument, `static` and `debug` are for special cases/testing 
 
 <details> <summary> Details (not normally needed) </summary>

If you wish to use a `debug` build, replace `x64` in paths below with `x64-debug`

The EPICS clean Windows 10 Jenkins build workspace is copied to  `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS` - this contains 
much more than an instrument installation e.g. it has all the local `.git` submodules and `*.lib` link libraries as well as temporary build (`O.*`) object file directories. It can thus be used as the basis for rapid further development work on your local computer. A standard instrument debug install for example would allow you to run an ioc in debug mode, but any further development would require re-generating the relevant `*.lib` files need to link the IOC and so take longer than using a developer debug build. 

CAUTION: updating an existing `C:\Instrument\Apps\EPICS` by the mechanism described here is the equivalent of deleting the directory, a full new `git clone --recursive` and then a build. You will lose all current changes to files and also any local git branches you created in that directory. Any changes there you want to keep you must push to Github and then re-checkout the branch after the update. Stashing changes to files is not enough as the local git repos are replaced - you need to push remotely.

you would need to find an appropriate build number in `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS\windows-x64` and then run e.g.
```
robocopy \\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\EPICS\windows-x64\BUILD-1 c:\Instrument\Apps\EPICS -MIR -NFL -NDL -NP -R:1 -MT -LOG:NUL
```
As an extra check you can re-run the robocopy without the LOG option. This should not take too long and should not print any errors or have any entries in the Mismatch/FAILED/Extras columns displayed at the end.  

you should have a compiled and ready to use distribution, with git pointing at current commit heads.
This may take a while to complete - at least 10 minutes, but longer if your disk is not an SSD for example.

**Alternative for slow network connection**

You can instead copy `EPICS-windows-x64.7z` from `\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\zips` and unpack this locally using
the [7-zip](https://www.7-zip.org/) program. Either drag the file using windows explorer, or if you have a very slow connection or one that might get interrupted you can try using `robocopy` in _restartable mode_. Open a cmd prompt, change to the relevant directory and type:
```
robocopy "\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\developer\zips" "." EPICS-windows-x64.7z /J /Z 
```
Note that this pre-allocates the full file space before starting the copy. I found that if I interrupt the copy with Ctrl-C and then type the command again, it picks up where it left off, so it looks hopeful it will handle network connection breaks.
 </details>

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