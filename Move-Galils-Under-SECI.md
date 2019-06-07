> [Wiki](Home) > [Galils Under SECI](galils-under-seci)

The move is undertaken as a state machine, and as such the text below attempts to explain the behaviours.
Double line breaks are used to help see the different sets of instructions more easily.
Letters in double quotes are commands sent to the Galil.
The condition is explained on the left of the --> and the state on the right-hand side.
Items in `code highlights` in the "Condition for next state and Next State" column are code items that happen when those conditions are met.
An external stop will interrupt the state machine and go to the Stop state.

State Name | Actions in State | Condition for next state and Next State |
--- | --- | --- |
Init | | First Call --> Idle <br><br> New Setpoint --> Send Setup <br><br> Stop triggered --> Stop <br><br> Otherwise --> State passed from previous run |
Idle | | Send Setup |
Send Setup | corrections = 0 <br><br> Calculate the setpoint <br><br> hardware set point = user set point - offset _ user offset, the user set point is coerced to the user max and min if appropriate, and the hardware set point to the soft max and min if appropriate <br><br> g_sp{axis} = motor steps per unit * hardware set point <br><br> If stepper motor (If encoder position NaN (Read Encoder Position, "TP" or "RP" based on setup), "PR = 0", "DP = Encoder Readback") <br><br> Send motor parameters <br><br> "SP" | Move call != "" --> Galil Program Check <br><br> Move Call == "" AND (Dual Position Stage OR (If setpoint > position?forward backlash != 0 : backward backlash != 0)) = True --> Send Setpoint + Backlash <br><br> Move Call == "" AND (Dual Position Stage OR (If setpoint > position?forward backlash != 0 : backward backlash != 0)) = False --> Set Point |
Send Setpoint + Backlash | If Dual Position Stage --> "JG" at Speed, otherwise --> "PT = 1", Setpoint to use = Set Point + moving forward?forward backlash : backward backlash, "PA=Setpoint to use" <br><br> correction = 0 | Begin Motion 1 |
Galil Program Check | | Move Call = "" --> Begin Motion 1 <br><br> Move Call != "" `"PA" to setpoint * motor steps per unit` --> Galil Program Complete |
Galil Program Complete | | Thread is executing --> Galil Program Complete <br><br> Thread not executing --> Delay before power off |
Begin Motion 1 | Motor Off (Axis status) is True OR Move in Progress (Axis Status) is False "SH", "BG" | Wait for stop 1 |
Wait for Stop 1 | | Dual Position Stage AND Move in Progress --> Wait for stop 1 <br><br> Dual Position Stage AND Move not in Progress --> Delay Before Power Off <br><br> Not a Dual Position Stage AND Move in Progress --> Wait for stop 1 <br><br> Not a Dual Position Stage and Move not in Progress --> Send setpoint + Backlash + Correction |