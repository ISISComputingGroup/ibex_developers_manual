# Shared Instrument Scripts

The general instrument scripts are in this [repository](https://github.com/ISISNeutronMuon/InstrumentScripts). These scripts include:
- The ['old' scans library](https://pygenie-scans.readthedocs.io/en/latest/index.html); as of October 2025, this is used by SANS instruments and reflectometers, but is being gradually replaced by {doc}`Bluesky-based scans <Bluesky-scanning>`
- A shared SANS scripting framework. Contains definitions of `do_sans` and `do_trans`
- Shared utilities for Muon beamlines, for example including:
  * Background plot configuration (using {doc}`/specific_iocs/other/Background-Script-IOC` and {doc}`Matplotlib`)
  * {doc}`Zero-field system </specific_iocs/magnets/Zero-field-controller>` calibration routines
  * {doc}`DAE pre & post commands </specific_iocs/dae/DAE-Pre-and-Post-commands>`

## Deployment

During IBEX deployment, an optional step has been added to the deploy script (see [ticket](https://github.com/ISISComputingGroup/IBEX/issues/7914)
for details) to pull the latest master branch of the scripts repository and attempt an automatic merge with the local branch.
This step will immediately fail if the local branch is _not_ named after the machine (e.g. _NDXxxx_) it is being run on.
Following a successful check of the branch name, an automatic merge is attempted and should this fail, 
a set of instructions is presented to the user to perform a _manual_ merge.  No further action is taken by this deployment task.

At the time of writing, there is **no** automated task for this 'pull and merge' of the instrument scripts 
(i.e. is it not present in the CI system), it is **only** performed as an optional step during IBEX deployment.
