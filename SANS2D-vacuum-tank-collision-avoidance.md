> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [SANS2D vacuum tank collision avoidance](SANS2D-vacuum-tank-collision-avoidance)

SANS2D's vacuum tank contains 4 primary axes that can potentially collide with each other:
- Front detector
- Front baffle
- Rear baffle
- Rear detector

To reduce the risk of collisions, there is a collision avoidance system implemented in DB records in the `motorExtensions` module. These DB records monitor the gaps between pairs of axes next to each other, and will stop the axes in the following cases:
- The gap is too small and is becoming smaller
- There is a persistent (>5s) comms fault with one of the galil controllers

Collision avoidance can be switched on or off using the PV `%MYPVPREFIX%MOT:SANS2DVAC:COLLISION_AVOIDANCE` in case it is blocking a valid move (e.g. the motors have lost positions and think they are too close, when in reality they are not).

When the collision avoidance system stops axes, it will write the current time to `TE:NDW1799:MOT:SANS2DVAC:_LAST_STOP_TIME`, so that users can tell when an axis was stopped by this system.

The stopping distance can be controlled using the pvs:

- front detector to front baffle: `%MYPVPREFIX%MOT:SANS2DVAC:FDFB:MINIMUM_INTERVAL`
- front baffle to rear baffle: `%MYPVPREFIX%MOT:SANS2DVAC:FBRB:MINIMUM_INTERVAL`
- rear baffle to rear detector: `%MYPVPREFIX%MOT:SANS2DVAC:RBRD:MINIMUM_INTERVAL`

Note that this is not a hardware fail safe system it will try and stop the movement but if you keep forcing it the hardware will get closer and closer together. Also note that the stop issued is subject to the normal deceleration so will not stop at exactly this distance but some way inside of it.
