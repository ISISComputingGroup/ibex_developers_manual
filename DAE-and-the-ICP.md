> [Wiki](Home) > [The Backend System](The-Backend-System) > [System Components](System-components) > [DAE and the ICP](DAE-and-the-ICP)

## The DAE and the ICP

The Data Acquisition Electronics (DAE) is the physical hardware that reads the neutron events out of the detectors. IBEX communicates with this hardware via the Instrument Control Program (ICP)

For Troubleshooting the DAE see [here](DAE-Trouble-Shooting).

## Running the DAE in Parallel

In some cases you may want your DAE to mimic the state of a DAE on another machine. This is particularly useful when testing the DAE3 hardware as it will give comparable data files to the ones created by a DAE2.

To do this you must:
* Switch to the dae3_pull_dae2_data [branch](https://github.com/ISISComputingGroup/EPICS-isisdae/tree/dae3_pull_dae2_data)
* Add `dbLoadRecords("$(ISISDAE)/db/dae3_pull.db","P=$(MYPVPREFIX),Q=DAE:,O=XXX")` to the st.cmd of your DAE, where XXX is the prefix of the instrument which you wish to mimic.
* Copy across the wiring, detector and spectra tables from the other instrument.
* Set your DAE with the same tables and the same general settings.
* Wait until the other instrument is in SETUP
* Start your DAE

The DAE will mimic the run state, title and period of the DAE it is point to.