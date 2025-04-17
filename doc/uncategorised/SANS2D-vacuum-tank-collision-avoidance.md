> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [SANS2D vacuum tank collision avoidance](SANS2D-vacuum-tank-collision-avoidance)

SANS2D's vacuum tank contains 4 primary axes that can potentially collide with each other:
- Front detector
- Front baffle
- Rear baffle
- Rear detector

There is a collision avoidance check implement in DB records in the `motorExtensions` module. These DB records does the following things:
- Checks if the `SP` between 4 primary axes are above the minimum threshold
- `.SPMG` is set to `Pause` after axis has stopped moving and after `STOP ALL` button is pressed
- `.DISP` is set to `1` in axis and motor layer during movement and set back to `0` after axis is no longer moving
- `.DISP` is set to `MOVE_ALL` pv if movement is not allowed due to potential collision

The minimum distance between axes can be controlled using the pvs:

- front detector to front baffle: `%MYPVPREFIX%MOT:SANS2DVAC:FDFB:MINIMUM_INTERVAL`
- front baffle to rear baffle: `%MYPVPREFIX%MOT:SANS2DVAC:FBRB:MINIMUM_INTERVAL`
- rear baffle to rear detector: `%MYPVPREFIX%MOT:SANS2DVAC:RBRD:MINIMUM_INTERVAL`

