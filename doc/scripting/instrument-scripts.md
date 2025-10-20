# Shared Instrument Scripts

The general instrument scripts are in this [repository](https://github.com/ISISNeutronMuon/InstrumentScripts) and include scripts like `do_sans` and `do_trans`, as well as the (old) scans library.

During IBEX deployment, an optional step has been added to the deploy script (see [ticket](https://github.com/ISISComputingGroup/IBEX/issues/7914)
for details) to pull the latest master branch of the scripts repository and attempt an automatic merge with the local branch.
This step will immediately fail if the local branch is _not_ named after the machine (e.g. _NDXxxx_) it is being run on.
Following a successful check of the branch name, an automatic merge is attempted and should this fail, 
a set of instructions is presented to the user to perform a _manual_ merge.  No further action is taken by this deployment task.

At the time of writing, there is **no** automated task for this 'pull and merge' of the instrument scripts 
(i.e. is it not present in the CI system), it is **only** performed as an optional step during IBEX deployment.
