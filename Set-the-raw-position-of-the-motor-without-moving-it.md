> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Set the raw position of the motor without moving it](Set-the-raw-position-of-the-motor-without-moving-it)

### Setting the motor position/offset
*Note that this applies to multiple motor types.*

Sometimes it is desirable to change the reported position of the motor without it physically moving, effectively changing the origin of the axis. This can be achieved through EPICS by applying an offset to the reported motor position and by setting the position in steps in the motor. TO do this:

1. Start the motor IOC
1. Go into the `Motors` perspective in the client
1. Bring up the OPI for the desired motor by double clicking the relevant square in the table
1. Click on `More details...`
1. In the `Calibration` section, switch `Cal` from `use` to `set`
1. Either
    1. Change the `Off` field to apply an offset to the current position
    1. Change the current position directly by changing the `MoveAbs` `User` field in the `Drive` section
1. **Don't forget** to switch the `Cal` field back to `Use` once you're done or the motor won't move.


