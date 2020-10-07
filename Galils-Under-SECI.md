> [Wiki](Home) > [Galils Under SECI](galils-under-seci)

# General actions taken
- [Galil homing routines as used in SECI](Homing-Galils-under-SECI): A page explaining the homing methods for Galils under SECI
- [Galil move routines as used in SECI](move-galils-under-SECI): A page explaining the move method for Galils under SECI
- [Jogging a Galil axis in SECI](jog-galils-in-SECI): A page explaining the way an axis is jogged on a Galil under SECI

# Specific Examples
- [Move for `GPHI` on CRISP from 0 to 2.4](move-gphi): A page using the move information above to predict the values being sent for a move of `GPHI` which behaves very differently between SECI and IBEX

# Other:

Motor Setup Pane

   - Correct Motion tick box: will make the driver retry the motion if the position is not within the deadband of the setpoint; up to 10 times.

# Setup values in IBEX from SECI (a subset)

The notes below detail how some of the values used by the SECI Galil driver should be translated for use in the EPICS IOC for Galils.

Motor steps per unit and encoder steps per unit should be inverted (`1/value`).

Displayed Position

- This is the position reported in the datarecord/encoder steps per unit + offset + user offset

Home Offset

- Used to drive axis to a position before running the home position - this can be ignored

Homeval

- Applied if a homing routine is defined as completed successfully - assume that this is the case and this is then the '0' position, the use of this value needs to be considered alongside the other offset values

Offset and User Offset

- These are regularly added to or removed from the values being communicated.
- When dealing with values which need to be corrected by the offsets, the two offsets are added together to give the total offset value:
   - On sending a position: `Values sent to Galil = (user set point - (offset + user offset)) * motor steps per unit`
   - On readback: `Value displayed = (position reported in the Galil datarecord/Encoder steps per unit) + (user offset + offset)`

Offset to apply in IBEX

- As the home value in IBEX should be 0, this should likely be set to `SECI Homeval - (offset + user offset)`
- Note also that there is an option to not apply the home offset and so 0 is used in that situation for the `SECI Homeval`
- The SECI limits are in software only and not written to the device. When applying this offset

Backlash

- The two systems differ here - SECI will add the forward backlash to the value sent to the Galil if moving forward, or add the backward one if moving backwards.
- As such setting the Backlash acceleration to a proportion (1/10) of the standard acceleration and the backlash velocity to a proportion (1/10) of the standard velocity is probably wise.
- BDST (the backlash distance) likely needs to be set to whichever of the forward and backward backlashes are set. (Again there is a concern over sign, but just using whichever is propagated with the sign it has should be a reasonable start.) If neither are set, this value should be 0. If both are set, there is something very wrong with that stage, and it should be flagged, but as a default the backward backlash could be used.
- Sign thoughts: We think the sign in IBEX is opposite to the sign in SECI. The reasoning is easiest to see with a positive axis pointing up. Here the corrected movement we want is when it is going down, -ve direction, we want it to go past the set point and come back. To achieve this in SECI you need to add a -ve value to the backwards backlash (backlash is added to the setpoint). To achieve this in IBEX you must add a +ve backlash distance (in IBEX it is taken off the setpoint).

Auto On/Off
- This relates to the De-energise setting, it is also worth noting that when this is set to false then the motor off deadband has to be set to -1.

Deadbands
- `RDBD` is the retry deadband and equates to the `positional accuracy` - both are in the engineering units
- `SPDB` is the setpoint deadband, and equates to the parameter of that name - both are in the engineering units

Jog Values
- Both `JAR` and `JVEL` are set to the same values as standard move velocity and acceleration

Limits
- Within IBEX we will set the `HLM` and `LLM` fields
- SECI limits (user and soft limits) are software only, so are never sent to the controller.
- Where the soft limits are set, but the user limits are either set to infinity or 0, then the soft limits should be used
- Where the soft limits are set to infinity or 0 then the limits will be set to 0 and a message added to the 'things to be aware of' part of the system
- If the user limits are larger than the soft limits, but not infinite, then the soft limits will win as those are the final limits used within the move normally

