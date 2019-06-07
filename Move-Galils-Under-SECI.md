> [Wiki](Home) > [Galils Under SECI](galils-under-seci)

The move is undertaken as a state machine, and as such the text below attempts to explain the behaviours


State Name | Actions in State | Condition for next state and Next State
---        | ---              | ---
`Init`       |                  | First Call --> `Idle` <br> New Setpoint --> `Send Setup` <br> Stop triggered --> `Stop` <br> Otherwise --> State passed from previous run
`Idle`       |                  | `Send Setup`
`Send Setup` | corrections = 0 <br> Calculate the setpoint <br> hardware set point = user set point - offset _ user offset, the user set point is coerced to the user max and min if appropriate, and the hardware set point to the soft max and min if appropriate <br> g_sp{axis} = motor steps per unit * hardware set point <br> If stepper motor (If encoder position NaN (Read Encoder Position, "TP" or "RP" based on setup), "PR = 0", "DP = Encoder Readback") <br> Send motor parameters <br> "SP" | Move call != "" --> `Galil Program Check` <br> Move Call == "" AND (Dual Position Stage OR (If setpoint > position?forward backlash != 0 : backward backlash != 0)) = True --> `Send Setpoint + Backlash` <br> Move Call == "" AND (Dual Position Stage OR (If setpoint > position?forward backlash != 0 : backward backlash != 0)) = False --> `Set Point`
`Send Setpoint + Backlash` | If Dual Position Stage --> "JG" at Speed, otherwise --> "PT = 1", Setpoint to use = Set Point + moving forward?forward backlash : backward backlash, "PA=Setpoint to use" <br> correction = 0 | `Begin Motion 1`









