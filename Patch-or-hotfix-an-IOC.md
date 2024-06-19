To deploy a new IOC to an instrument, or patch an existing one, different levels of care need to be taken depending on what has changed

* OPI for new IOC

You do not usually need to deploy a new GUI, in fact it is best to avoid this as you may update other OPIs unintentionally, introducing changes that need IOC updates you are not deploying. So go for the minimal change approach if possible:
- keep existing GUI build
- copy across just the OPI changes you need and leave everything else as is
- if necessary (as in new rather than changed device), manually edit `opi_info.xml` to add new OPI to ibex list   

* Updating an exsiting IOC

again, change the minimum possible, don't copy a whole tree from build server unless you need to. If you do not need to update the EXE file you can probably just copy across the new db files or st.cmd changes etc.

* Deploying new IOC (or updating an existing ioc when EXE has changed)

An EXE depends on DLL files etc and these may change after a developer dependency update, so just copying an EXE from usual EPICS_CLEAN jenkins will not work. If you are sure that the dependencies on the build server and instrument are the same, you can do this, but it may be safer to copy a static build of an EXE across that includes all these DLL dependencies. If you copy an EXE you should also copy the ioc `dbd` file from the same build e.g. for INSTETC ioc this is the `INSTETC/dbd/INSTETC-IOC-01.dbd` file. So for a new IOC no the following:

* copy the new `support` directory from the `EPICS-CLEAN` jenkins build to the instrument e.g. `support\stanford_sr400_photon_counter`
* copy the `ioc` directory from `EPICS-CLEAN` jenkins build to the instrument e.g. copy all of `ioc\master\SR400`
* copy the just the ioc EXE files from the `EPICS-STATIC-CLEAN` build to replace those you copied from `EPICS-CLEAN` e.g. replace all of just `ioc\master\SR400\bin\windows-x64` with the files in `ioc\master\SR400\bin\windows-x64`
* copy the dbd files i.e. copy all dbd files in `ioc\master\SR400\dbd` from  `EPICS-STATIC-CLEAN` jenkins to equivalent location on local computer. We need to copy dbd files as they relate to records in DLLs that are embedded. We can't copy all of the `EPICS-STATIC-CLEAN` tree as some bits have the wrong `EPICS_HOST_ARCH` embedded. So we need to do this hybrid approach.
