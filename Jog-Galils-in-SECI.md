> [Wiki](Home) > [Jogging a Galil axis in SECI](jog-galils-in-SECI)

The move is undertaken as a state machine, and as such the text below attempts to explain the behaviours.
Double line breaks are used to help see the different sets of instructions more easily.
Letters in double-quotes are commands sent to the Galil.
The condition is explained on the left of the --> and the state on the right-hand side.
Items in `code highlights` in the "Condition for next state and Next State" column are code items that happen when those conditions are met.
An external stop will interrupt the state machine and go to the Stop state.

| State Name | Actions in State | Condition for next state and Next State |
| --- | --- | --- |
| Idle | | Send Setup Params |
| Send Setup Params | Set motor position to encoder position <br><br> Send motor parameters | Begin motion speed zero |
| Begin motion speed zero | "JG" at minimum of Axis Setup Speed (from the setup information) and the Present Motion Speed (from the control on the VI - defaults to zero and is populated to +/- the Axis Setup Speed) <br><br> "SH" <br><br> If this is a servo motor `"CP = -1"` <br><br> "BG" | Set Jog Speed |
| Set Jog Speed | If state hasn't been changed by an external factor (e.g. a stop) OR Present Motion Speed has changed, then "JG" at the minimum of the Axis Setup Speed and the Present Motion Speed | If any of the stop sceanrios have been met OR a move is not in progress --> Stop, otherwise --> Jog Speed |
| Stop | "ST" | Wait Until Stop |
| Wait Until Stop | | Move in progress = True --> Wait Until Stop <br><br> Move in progress = False --> Power Off |
| Power Off | If De-energise = True, "MO" <br><br> Send Motor Params Init | End |
| End | | Send Setup Params |
