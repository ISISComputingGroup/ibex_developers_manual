The EPICS build system allows you to have multiple architectures present in the same source tree, architecture independent files are built in O.Common and architecture dependent ones built in O.windows-x64 and O.win32-x86 etc. 

Running config_env selects a default EPICS_HOST_ARCH for builds, and typing "make" or running "build.bat" will use this. Any IOCs and start_ibex_server will also use this.

To build for another architecture without changing your default you need to:
- Open an epics terminal and run config_env in the normal way
- Pass a different architecture to build.bat e.g.
  * build.bat windows-x64-static
  * build.bat win32-x86

Note that this just compiles/builds the files, runIOC.bat will still use your default architecture. You can run IOCs manually if you wish to check the new architecture, I'll develop a better system for doing this but currently you can achieve it by temporarily resetting you default architecture (which is in epics_host_arch.txt at the top level) if you are careful.

If you need a 32 bit build but don't want to build it yourself, you can find the recent x86 builds in `\\ISIS\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_CLEAN_win10_x86`.
Rename or move your normal x64 EPICS folder, choose the latest suitable build, then manually copy the contents of `EPICS` across to your new x32 EPICS folder.
     