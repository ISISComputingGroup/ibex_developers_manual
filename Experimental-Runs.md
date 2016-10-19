Something Has Gone Wrong with my Experimental Run

# Script Failed to Finish and Take All Measurements

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
        1. Block as `IN:<instument>:CS:SB:<block name>
        1. Other PVs `IN:<instrument>:<IOC>:PV.VAL` (these must be marked in the DB file with `info(archive, "VAL")`)
    1. Good blocks to choose might be SP and SP:RBVs in this case ploting the SP and SP:RBV showed that the SP had not be set in the machine. So run control hadn't been able to progress and it had hung.
![log plotter image](troubleshooting/LogPlotter.png)

# Experiment stuck in `Waiting` state after beginning a run

This issue was encountered on Iris during the transition between Seci and Ibex. The cause was an experiment that had been left running in Seci, but which didn't appear either in Ibex or in the front panel LabView VI. The issue is most likely to occur on systems that are transitioning to Ibex that occasionally might fall back to Seci as a backup.

If the issue occurs, the following remedy worked in this case:

1. Go into `C:\data` and move all files beginning with `selog.sq3` to a backup location.
    1. If the files cannot be moved because they are in use, it may be that Seci or the `isisicp.dae` task is still using them. Make sure they are shut down (potentially requiring the task manager).
1. Make sure the Ibex server is stopped
1. Open Seci
1. End the run
    1. Note `End` and not `Abort`. The former worked in this case, we don't know if the latter would have the same effect.
    1. If there is no run in progress, it might suggest a different root cause for the issue.
1. Close Seci
1. Restart the Ibex server
1. Open the Ibex client
1. Try beginning the run