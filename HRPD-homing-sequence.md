There is a [special homing sequence for HRPD low temperature sample changer](HRPD-homing-sequence) because it doesn't work this is until ticket [5739](https://github.com/ISISComputingGroup/IBEX/issues/5739) is done

## Homing

Do not home in ibex

Goto the motor details page in ibex

- Drive the foil to the lower limit by setting a large negative value (within the limits) in the motor opi
-	Check the led is red next to the appropriate limit to indicate it is on the limit switch 

-	in the calibration section:
-	Don’t change the Off: value 
-	Set calibration to frozen
-	Push “set”
-	Type 0 into the Move Abs Dial column (the corresponding “user” column value should update automatically)
-	Push “use”
-	(it is ok to leave calibration as frozen – no need to set back to variable)
