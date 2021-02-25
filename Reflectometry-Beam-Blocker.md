> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Beam Blocker](Reflectometry-Beam-Blocker)

A beam blocker for the reflectometry server means that the blades of a slit stop acting like gap and centre and positions of blades are used. This is often used to block a part of the beam from the detector. In order to achieve this one blade is move out of the beam and the other, the blocker, is moved to intercept the beam. Currently there are two major cases:

1. S3 is on a component that tracks the beam. In this case new parameters are create in the server to set the positions of the two blades.
2. S3 tracks the beam by moving its centre. In this case in beam blocker mode the S3 offset parameter must be connected with the blocker blade so that it still tracking the beam while the other blade is free. So in normal mode the S3 offset controls the s3 vertical centre and in block mode it controls the blocker blade. This is achieved by an `pv_wrapper_for_parameter` which makes the motor control a different PV base on the value of the blocker parameter.

On top of this you can also invert the blade being controlled. This is useful for a south jaw where the position or offset would act in the opposite direction to all other heights; this is caused because the south blades position direction is away from the centre of the jaws (downwards). To invert the blade you need to add a user function engineering correction to invert the value sent to the motor.

So for instance on crisp we do something like this:

```
    def invert(value, block):
        """
        Multiply value by -1 if in South blocker mode, because the south jaw moves down but it should move up in
        beam blocker mode otherwise the offset won't work
        :param value: s3 offset
        :param block: blocker mode
        :return: 0 if in blocker mode None; otherwise -ve of value
        """
        if block == "South":
            return value*-2
        return 0

    # The offset should be the centre of jaw3 if in beam shapping mode in beam block mode the offset set is the inverted
    #   south motor.
    south_jaw_wrapper = MotorPVWrapper("MOT:JAWS3:JS:MTR")}), engineering_correction=UserFunctionCorrection(invert, s3_params["block"]),
                  synchronised=False)
    add_driver(
        IocDriver(s3_comp, ChangeAxis.POSITION, JawsCentrePVWrapper("MOT:JAWS3", is_vertical=True),
                 pv_wrapper_for_parameter=PVWrapperForParameter(s3_params["block"], {
                   "South": south_jaw_wrapper)
```

To find out what your blocker is set to see:

- [POLREF](Reflectomtery-IOC-POLREF#slit-3beam-blocker)
- [CRISP](Reflectomtery-IOC-CRISP#slit-3beam-blocker)
- [SURF](Reflectomtery-IOC-SURF#slit-3beam-blocker)
- [INTER](Reflectomtery-IOC-INTER#slit-3beam-blocker)


