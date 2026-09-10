# VESUVIO Foil Homing

There is a special homing sequence for Vesuvio because it doesn't work this is until ticket [5739](https://github.com/ISISComputingGroup/IBEX/issues/5739) is done

## Homing left and right foils

Do not home in ibex
Drive the foil with Mclennan front panel to appropriate limit (upper limit for left foil, lower limit for right foil). 
Goto the motor details page in ibex

-	Check the led is red next to the appropriate limit to indicate it is on the limit switch 

-	in the calibration section:
-	Don’t change the Off: value 
-	Set calibration to frozen
-	Push “set”
-	Type 0 into the Move Abs Dial column (the corresponding “user” column value should update automatically)
-	Push “use”
-	it should be ok to leave calibration as frozen, but if you plan to later home in ibex you need to set it back to variable

The offset value in the Calibration section should not get altered by this procedure, as the dial position is zero both the user readback value and the offset should be the same and reflect the position you currently expect (42.5 right, -41.75 left). 

To test you could drive to the other limit and back etc. using the `Jog:` buttons. Whenever you drive to the appropriate homing limit the Dial value should end up being 0 (or very close to)

Note: Ibex stores the “offset” and high/low soft limits as part of the configuration, so if these are changed on the motor details they would also need to be changed on the config page or they will get reset on an ibex restart. I think I have adjusted the left ones to work on the above procedure, but we can check later.


