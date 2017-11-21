> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [Motors](Motors-Trouble-Shooting)

## General

### Position needs to be restored 

Positions of the motor can be restored/set without setting an offset. These can be needed if the motor power cycles for example on a power cut. The recommendation is to do a home if possible but if not the position can be set without this.

1. Find the latest value from the archive with:
    ```
    SELECT t.name, s.smpl_time, s.float_val FROM archive.sample s
    LEFT JOIN archive.channel t ON s.channel_id = t.channel_id
    WHERE t.name LIKE "%MOT:MTR0101%RBV%"
    AND s.smpl_time > "2017-11-16 00:00:00"
    ORDER BY s.channel_id, s.smpl_time DESC;
    ```
1. Open the motor details opi for given motor
1. Click on `Set` in `Calibration` area
1. Set the `User` `MoveAbs` to the value from the querry above
1. Click on `Use` in `Calibration` area

## Galil

### Can not communicate with the Galil

This is not shown well in the OPI it just has weird values. Look in the log file to check near `GalilCreateController` it says `sevr=info Connected to XXX t 1000 -mg 0, DMC2280 Rev 1.0o-CM, 46949, IHB IHD` not `sevr=major connect: 5004 OPEN ERROR.  Galil::Galil() failed to open Ethernet host`

If it isn't connected try to ping the control address. If this isn't alive check, via the serial cable, the Galil address. The command for this is `IA?`.
