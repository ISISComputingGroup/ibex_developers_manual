> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [MERLIN and LET Oscillating Radial Collimators](MERLIN-LET-Oscillating-radial-collimators)

The oscillating radial collimator on MERLIN is similar but not quite the same as the one on LET.

# Starting it

Occasionally the oscillating collimator stops oscillating, you can tell because the `current angle` on the OPI will not be changing.

To restart this is sometimes tricky try the following:

1. On the OPI
1. Click Stop
1. Alter the `swept angle` and `operating frequency` to a **valid** and **different** values so it will resend the setting
   1. The valid values for the swept angle as currently 0-2 (you can see by right click on the input text box and `Show pv info`)
   1. The valid values of operating frequency are 0-0.5
1. Set the swept angle and operating frequency back to the required settings
1. Click start
1. The `Mode` should now read `Homing` then `Oscillating` and the current angle should start changing. 
    - this was fairly quick (less than 1 minute)

# Hardware quirks:
- The thread will die if zero is sent for distance and velocity. The driver must ensure that distance and velocity are not sent at IOC start.