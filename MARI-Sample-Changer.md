> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [MARI Sample Changer](MARI-Sample-Changer)

# MARI Sample Changer

MARI has two different sample changers. They are very similar in that they are both run by a Mclennan with the same settings for motor/encoder resolution. They are mounted on the end of sample sticks and each have 4 samples at 90 degrees from each other that can be placed into the beam. The sample holder is attached to both by screwing into the end of the sample stick. However, as this holder is rotating and is on this screw if it gets stuck during a rotation it will either tighten itself or loosen itself and fall off. Thus **the sample changer must always be rotated in the same direction to stop it falling off**, including during homing. If you are unsure which direction will result in it falling off you can start the device moving and then hold on to the sample holder and see if it starts tightening or loosening (you always want it tightening).

Unfortunately, although the sample changers are very similar they are mechanically different in that one is directly driven by a universal joint (UJ) and the other is driven by a belt. Due to these mechanics the sample changers run in different directions (e.g. a positive move on the Mclennan causes a clockwise rotation in one sample changer and anti-clockwise in the other). For both the belt and the universal joint the correct direction is **clockwise from the top** (the top being the side where the home datum is). See the videos below.

Confusingly there was an arrow on the bottom of each sample changer indicating which way it turns that was incorrect. The IS has corrected this arrow in blue marker pen. For the Mclennan this means that the belt must be driven in the positive direction and the UJ in the negative direction. The positions on the cans were originally incorrectly labelled, they have now been correctly labelled by the instrument scientist in pen.
 
There is currently an instrument script on MARI called `changer.py` which moves everything in the correct direction, including during homing, and selects the correct samples. Due to homing directions being different for both they can currently only be homed through that script, not the GUI. These issues will be corrected in https://github.com/ISISComputingGroup/IBEX/issues/5729.

Finally, because of inaccuracies between converting the motor resolution in the mclennan to one in IBEX the script does not move 90 degrees for each sample and instead has a small correction. To experimentally measure this correction there is a `test_sample_changer.py` script in C:\Scripts on MARI which will move the cans a number of full revolutions and ask the user to confirm they are still correctly aligned.

### Correctly moving universal joint sample changer
![](motors/mari_sample_changer_joint.gif)

### Correctly moving belt sample changer
![](motors/mari_sample_changer_belt.gif)

