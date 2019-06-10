> [Wiki](Home) > [Galils Under SECI](galils-under-seci)

The move is undertaken as a state machine, and as such the text below attempts to explain the behaviours.
Double line breaks are used to help see the different sets of instructions more easily.
Letters in double quotes are commands sent to the Galil.
The condition is explained on the left of the --> and the state on the right-hand side.
Items in `code highlights` in the "Condition for next state and Next State" column are code items that happen when those conditions are met.
An external stop will interrupt the state machine and go to the Stop state.

| State Name | Actions in State | Condition for next state and Next State |
| --- | --- | --- |
| Init | | First Call --> Idle <br><br> New Setpoint --> Send Setup <br><br> Stop triggered --> Stop <br><br> Otherwise --> State passed from previous run |
| Idle | | Send Setup |
| Send Setup | corrections = 0 <br><br> Calculate the setpoint <br><br> hardware set point = user set point - offset _ user offset, the user set point is coerced to the user max and min if appropriate, and the hardware set point to the soft max and min if appropriate <br><br> g_sp{axis} = motor steps per unit * hardware set point <br><br> If stepper motor (If encoder position NaN (Read Encoder Position, "TP" or "RP" based on setup), "PR = 0", "DP = Encoder Readback") <br><br> Send motor parameters <br><br> "SP" | Move call != "" --> Galil Program Check <br><br> Move Call == "" AND (Dual Position Stage OR (If setpoint > position?forward backlash != 0 : backward backlash != 0)) = True --> Send Setpoint + Backlash <br><br> Move Call == "" AND (Dual Position Stage OR (If setpoint > position?forward backlash != 0 : backward backlash != 0)) = False --> Set Point |
| Send Setpoint + Backlash | If Dual Position Stage --> "JG" at Speed, otherwise --> "PT = 1", Setpoint to use = Set Point + moving forward?forward backlash : backward backlash, "PA=Setpoint to use" <br><br> correction = 0 | Begin Motion 1 |
| Galil Program Check | | Move Call = "" --> Begin Motion 1 <br><br> Move Call != "" `"PA" to setpoint * motor steps per unit` --> Galil Program Complete |
| Galil Program Complete | | Thread is executing --> Galil Program Complete <br><br> Thread not executing --> Delay before power off |
| Begin Motion 1 | Motor Off (Axis status) is True OR Move in Progress (Axis Status) is False "SH", "BG" | Wait for stop 1 |
| Wait for Stop 1 | | Dual Position Stage AND Move in Progress --> Wait for stop 1 <br><br> Dual Position Stage AND Move not in Progress --> Delay Before Power Off <br><br> Not a Dual Position Stage AND Move in Progress --> Wait for stop 1 <br><br> Not a Dual Position Stage and Move not in Progress --> Send setpoint + Backlash + Correction |
| Send Setpoint + Backlash + Correction | | Encoder Present AND Correct Motion AND (setpoint + (setpoint > old setpoint?forward backlash:backward backlash) - position) < positional accuracy * 1000 `Set motor = Encoder, Set setpoint to setpoint + (setpoint > old setpoint?forward backlash:backward backlash` --> Begin Motion 2 <br><br> Encoder Preset AND Correct Motion AND NOT (Absolute of setpoint + (setpoint > old setpoint?forward backlash:backward backlash) - position) < positional accuracy * 1000 --> Delay Before Power Off <br><br> Encoder Present AND Correct Motion = False --> Set Point |
| Begin Motion 2 | Motor off or move not in progress "SH", "BG" | Wait for Stop 2 |
| Wait for Stop 2 | | Move in progress --> Wait for Stop 2 <br><br> Move not in progress --> Set Point |
| Set Point | "PT = 1" <br><br> "PA" setpoint | Begin Motion 3 |
| Begin Motion 3 | Motor off or move not in progress "SH", "BG" | Wait for Stop 3 |
| Wait for Stop 3 | | Move in progress --> Wait for Stop 3 <br><br> Move not in progress --> Set Point + Correction |
| Set Point + Correction | corrections + 1 | Encoder present = True and correct motion = False --> Delay before Power Off <br><br> Encoder Present and Correct Motion and absolute of setpoint - position is not greater than positional accuracy * 1000 --> Delay before Power Off <br><br> Encoder Present and Correct Motion and absolute of setpoint - position is greater than positional accuracy * 1000 `Set Mtr = Enc ("PR = 0", "DP" = "TP"), "PA" to setpoint, "AC" = quotient of Acceleration/10, "DC" = quotient of Deceleration/10, "SP" = greater of 1 and the quotient of speed/10` --> Begin Motion 4 |
| Begin Motion 4 | Motor off or move not in progress "SH", "BG" | Wait for Stop 4 |
| Wait for Stop 4 | | Move in progress --> Wait for Stop 4 <br><br> Move not in progress --> Check for Accuracy |
| Check for Accuracy | | If corrections < 10 AND correct motion AND Encoder Present AND ((Max of positional accuracy/2 and 1/encoder steps per unit) < the asbolute of set point - position)) AND (((Max of positional accuracy/2 and 1/encoder steps per unit) * 1000) > the asbolute of set point - position)) --> Set Point + Correction <br><br> Otherwise --> Stop |
| Stop | If used = True AND If Move Call not "", "HX" <br><br> If used = True "ST"| Wait until Stop |
| Wait until Stop | | Move in progress --> Wait until stop <br><br> Move not in progress --> Delay before Power Off |
| Delay before Power Off | If De-energise = True, "MO", else, "SH" <br><br> If Dual Position Stage, "PR = 0", "DP" setpoint, "DE" setpoint <br><br> Run any after move code | End |
| End | | Send Setup |
