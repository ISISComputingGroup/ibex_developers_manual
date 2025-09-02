# Experimental Run Troubleshooting

Something Has Gone Wrong with my Experimental Run

## Script Failed to Finish and Take All Measurements

This is from a problem see on IRIS.

1. Get the script and configuration.
   In this case the important bits are:
    ```
    def set_sample_temp(temp, high, low, tlccr_offset):
        g.cset(Sample=temp, highlimit=high, lowlimit=low, runcontrol=True)
        g.cset(TLCCR=temp+tlccr_offset, runcontrol=False)
        
    def next_sample(temp, uamps):
        g.change(title="Fast Frozen Liver Cells transplant + Cryoprotectant + algae "+str(temp)+"K PG002")
        g.begin()
        g.waitfor(uamps=uamps)
        g.end()

    for i in range(47):
        temp += 5
        set_sample_temp(temp, temp+2, temp-2,-5)
        next_sample(temp, 20)
    ```
1. Find the PVs and plot them in log plotter
    1. Open IBEX GUI. Switch to the instrument in question
    1. If the config is loaded right click on PV and display block history (otherwise do this and edit)
    1. Look for the time in question (zoom out horizontally button in bar and use the hand to drag to the place)
    1. Add other plots which might be interesting (right click add PV)
        1. Block as `IN:<instrument>:CS:SB:<block name>`
        1. Other PVs `IN:<instrument>:<IOC>:PV.VAL` (these must be marked in the DB file with `info(archive, "VAL")`)
    1. Good blocks to choose might be SP and SP:RBVs in this case plotting the SP and SP:RBV showed that the SP had not be set in the machine. So run control hadn't been able to progress and it had hung.
![log plotter image](LogPlotter.png)

## Experiment stuck in `Waiting` state after beginning a run

There is now a new PV that you can write to from IBEX to force a resync of run control

    caput %MYPVPREFIX%CS:RC:SYNC:SP 1

## Experimental Files not being Archived and so not Appearing in the Journal

At the end of a run log file should be transferred from `C:\data` to the archive. For this to happen the files should be marked read only, then when the run ends it is copied thanks to a script in `<normal user>\Documents\Configurations\COMMON\end_of_run.cmd`. 
Double checking that the files are read only is a good first step when items are missing from the archive.
If this has failed:

* Make sure the network location d:\data\<cycle> is accessible. This can need connecting to manually after a restart, i.e. open the folder in explorer.

To archive files end a run.
Should you have runs ending and read only files, then check on the archive in `INST\instrument\logs\cycle_nn_n`, the log files there will provide some extra information. If the file `exception_copy.log` doesn't exist, or hasn't been updated for a long time, then the script above isn't running the code to clean up old files, or it has hung.

* Problems with the end of run script can be diagnosed by looking at the `post_command_<day>.log` file in the ICP logs area on the instrument. The ICP log files (in the same area) may also be instructive to check for other issues - for example, if the files are not being set read-only.
