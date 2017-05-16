This page contains issues which we have had at some point and are unsure what the cause is. If we capture them here we can group them and work out what the causes and likely hoods are. Please follow the template:

## 

Where: Polaris
When: 15/05/2017
Version: 3.2.1
Description: GUI could no longer control the DAE tab. User writes

    ```
    Summary: "IBEX - DAE Control Program: Run Summary/Experiment Setup etc. frozen"

    After ending Polaris run 98766 (from a script) the "DAE Control Program" pane 
    did not give back proper control of the instrument.
        
    On the Run Summary tab only the "Cancel Abort" button was active meaning I 
    could not start a new run.
    
    On the Experiment Setup/Data Acquisition tab I could tick the "Veto 0" tick 
    box, but the "Apply changes" button was not active (I had restarted the chopper 
    so needed to re-enable the veto).    
```

Work around: Restart the GUI.
