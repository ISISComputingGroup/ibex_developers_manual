Items we wish to capture for troubleshooting SECI.

### Motor stops before Limit for no Reason (has had IBEX on)

If an axis stops moving under SECI at a certain place which is not near the limits it is possible that the soft limits have got set in the controller. These can be set by IBEX so if you have swapped back from IBEX it is worth checking these.

To clear the limits:

1. open the low motor table
1. select tools and the motor in question 
1. click "clear axis limits"(approximate wording). 

This should allow the motor to go the whole range.
