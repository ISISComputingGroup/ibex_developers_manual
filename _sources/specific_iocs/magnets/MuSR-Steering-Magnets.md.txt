# MuSR Steering Magnets

MuSR has two steering magnets, for horizontal and vertical steering of muons.

An OPI exists for this (`musr_steering.opi`) which takes two Kepco Power supplies as macros for the respective magnet. 

This OPI contains a `STOP` and `START` button as pictured - this sends a PV write to the `IN:NDXMUSR:MUSR_STEERING_OFF` PV. This gets loaded by `INSTETC` on MuSR from `custom_records.db` file in the configurations area. This is stored on the `NDXMUSR` branch. 

![musr_steering_opi](musr_steering_opi.jpg)

The OPI also offers "saving" and "loading" functionality for the steering magnets and their 'default' values - these point to fields specified in `custom_records.db`. These records effectively trigger a manual autosave for the Kepco current setpoint values and load them back in when the load button is pressed. The OPI shows the current defaults above the buttons used for loading and saving. 