The OLD galil driver is build from a galil-old top level EPICS branch on ndhspare53, this is because it needs to be compiled with Visual Studio 2010. This build is then copied on a release to provide support/galil-old and  ioc/master/GALIL-OLD directories. A top level swap_galil.bat script is provided which swaps GALIL and GALIL-OLD, also when the release git repository is created a galil-old release files branch is created that matches the swapped branch.  

The galil-old structures needs to be kept in step to some extent with the main master tree, however some care is needed as not all changes are relevant, and because of the need to compile with VS2010 not all changes are possible to integrate e.g. a third party dependency like mysql may need a higher compiler version. Also not that we are replacing just one IOC of a main distribution, so we don;t need every change on galil-old just those relevant to building this ioc.    

Currently explicit galil-old branches exist for EPICS top, support/galil and ioc/master - other modules have just have pinned versions to EPICS that may not be the most recent (e.g. because newer versions do not compile with VS2010). Updating the to level galil-old EPICS branch should consider the following.
- if a change is made to support/galil master branch of EPICS-galil repository consider if this needs back-porting to the galil-old branch of this repository
- if a change is made to ioc/master/GALIL or ioc/master/GALILMUL consider if it needs back-porting to galil-old branch of this repositort
- some support modules get built into the galil ioc so the galil-old EPICS toplevel needs to be pinned to the most recent version of these e.g. sampleChanger, motionSetpoints. In general it is not a problem (but not necessary) to have all submodule repositories that are not on a separate galil-old branch to be at the most recent version, however in somes cases this is not possible due to compiler conflicts
      
   
