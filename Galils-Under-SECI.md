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

Motor steps per unit and encoder steps per unit should be inverted (`1/value`).

Displayed Position

- This is the position reported in the datarecord/encoder steps per unit + offset + user offset

Home Offset

- Used to drive axis to a position before running the home position - this can be ignored

Homeval

- Applied if a homing routine is defined as completed successfully - assume that this is the case and this is then the '0' position, the use of this value needs to be considered alongside the other offset values

Offset and User Offset

- These are regularly added to or removed from the values being communicated.
- On sending a position: `Values sent to Galil = (user set point - offset - user offset) * motor steps per unit`
- On readback: `Value displayed = (position reported in the Galil datarecord/Encoder steps per unit) + user offset + offset`

Offset to apply in IBEX

- As the home value in IBEX should be 0, this should likely be set to `SECI Homeval - offset - user offset` (Please check my maths here - I'm not sure about that `-` it could be `+`)

Backlash

- The two systems differ here - SECI will add the forward backlash to the value sent to the Galil if moving forward, or add the backward one if moving backwards.
- As such setting the Backlash acceleration to a proportion (1/3?) of the standard acceleration and the backlash velocity to a proportion (1/3?) of the standard velocity is probably wise.
- BDST (the backlash distance) likely needs to be set to whichever of the forward and backward backlashes are set. (Again there is a concern over sign, but just using whichever is propagated with the sign it has should be a reasonable start.) If neither are set, this value should be 0. If both are set, there is something very wrong with that stage, and it should be flagged, but as a default the backward backlash could be used.




