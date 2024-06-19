To deploy a new IOC to an instrument, or patch an existing one, different levels of care need to be taken depending on what has changed

## OPI for new IOC, or changes to existing OPI

You do not usually need to deploy a new GUI, in fact it is best to avoid this as you may update other OPIs unintentionally, introducing changes that need updates to IOC that you are not deploying. So go for the minimal change approach if possible:
- keep existing GUI build on instrument
- the directory yopu will be updating on the instrument will be of the form `C:\Instrument\Apps\Client_E4\plugins\uk.ac.stfc.isis.ibex.opis_1.0.0.4670\resources` and if from your local machine then from somewhere like `C:\Instrument\Dev\ibex_gui\base\uk.ac.stfc.isis.ibex.opis\resources`
- copy across just the new/changed OPIs and leave everything else as is
- If adding a new IOC, then you may need to manually edit `opi_info.xml` to add new OPI to ibex list. Do not copy across a new `opi_info.xml` as it could refer to things that are not present.   

## Updating an existing IOC (no EXE changed)

again, change the minimum possible, don't copy a whole tree from the jenkins build server unless you need to. It is usually safer to use a clean jenkins build from `kits$` as a basis unless you are really sure your local build is consistent. If you do not need to update the IOC `EXE` file in `ioc/master` you can probably just copy across the new db files or st.cmd changes etc. Note that we often edit files in e.g. a `YYYApp\Db` and `YYYApp\protocol` and they get deployed to a top level `db` and `data` when make is run, IOC normally load these top level ones but copying both sets is safe just in case.

##  Deploying new IOC (or updating an existing ioc when EXE has changed)

An IOC EXE from `ioc\master\MYIOC\bin\windows-x64` depends on DLL files etc in `support` and these may change after a developer dependency update to our EPICS repositories, so just copying an EXE from usual EPICS_CLEAN jenkins will not work (c++ libraries expose functions from DLLs, these may change with a new version of e.g. EPICS base or asyn). If you are sure that the dependencies on the build server and instrument were the same, you can just copy a new EXE, but it may be safer to copy a static build of an EXE across as that includes all these DLL dependencies inside the EXE and so is self contained (if a lot larger). If you copy an EXE you should also copy the ioc's `dbd` file from the same build e.g. for INSTETC ioc this is copying `INSTETC/dbd/INSTETC-IOC-01.dbd` file as well as the `INSTETC/bin` EXE files.

So for a new IOC do the following:

* copy the new `support` directory from the `EPICS-CLEAN` jenkins build to the instrument e.g. `support\stanford_sr400_photon_counter`
* copy the `ioc` directory from `EPICS-CLEAN` jenkins build to the instrument e.g. copy all of `ioc\master\SR400`
* copy the just the ioc EXE files from the `bin` of the `EPICS-STATIC-CLEAN` build to replace those you copied from `EPICS-CLEAN` e.g. replace files on instrument in `ioc\master\SR400\bin\windows-x64` with the files from `EPICS-STATIC-CLEAN` jenkins directory `ioc\master\SR400\bin\windows-x64-static` (this will just be replacing exe, if a DLL is present in the original instrument directory don't worry about it)
* copy the dbd files i.e. copy all dbd files in `ioc\master\SR400\dbd` from `EPICS-STATIC-CLEAN` jenkins to equivalent location on instrument computer e.g. to `c:\instrument\apps\EPICS\ioc\master\SR400\dbd`. We need to copy dbd files as they relate to EPICS records in DLLs that are embedded. We can't copy all of the `EPICS-STATIC-CLEAN` tree as some bits have the wrong `EPICS_HOST_ARCH` embedded (as in windows-x64-static). So we need to do this hybrid approach.

# Notes

* on windows you cannot replace an EXE file if it is in use
* The list of IOCs to start is produced by a `start_ibex_server` and it also builds the list of ioc macros that the GUI reads. So you will need to run `start_ibex_server` for a new IOC or changed macros, and may have to restart the GUI afgter this too.