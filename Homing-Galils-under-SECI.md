This is currently a stub as the information is added and later formatted

Home methods
- Home call script
- None
- Home signal
- Reverse Limit
- Forward Limit

Home call script
1. Send the script in the home call variable to the Galil, and `XQ` on a specified thread
1. Wait until `_XQ` for that thread is false
1. If motor is set to de-energise after move, send `MO`
1. Wait 0.6 seconds
1. If apply home position is true, apply the home position

None
1. Send `SH` and `BG`
1. Wait for the move in progress to be false
1. If there is a home offset, `PR` to the home offset*motor steps, send `SH` and `BG`, wait for the move in progress to be false
1. Send `ST`
1. Wait for the move in progress to be false
1. If motor is set to de-energise after move, send `MO`
1. Wait 0.6 seconds
1. If apply home position is true, apply the home position

Home Signal
1. Set speed to home speed
1. Send `HM`, `SH` and `BG`
1. Wait for the move in progress to be false
1. If there is a home offset, `PR` to the home offset*motor steps, send `SH` and `BG`, wait for the move in progress to be false
1. Send `ST`
1. Wait for the move in progress to be false
1. If motor is set to de-energise after move, send `MO`
1. Wait 0.6 seconds
1. If apply home position is true and the stop code is 10 (Stopped after homing), apply the home position

Reverse Limit
1. If the reverse limit is true, `JG` at home speed, send `SH` and `BG`, wait until the limit switch is off, `ST`, wait for move in progress to be false
1. Set `JG` to minus the home speed, send `SH` and `BG`
1. Wait for the move in progress to be false
1. If there is a home offset, `PR` to the absolute of the home offset*motor steps, send `SH` and `BG`, wait for the move in progress to be false
1. Send `ST`
1. Wait for the move in progress to be false
1. If motor is set to de-energise after move, send `MO`
1. Wait 0.6 seconds
1. If apply home position is true, the forward limit is false, the reverse limit is true, and the stop code is 3 (Decelerating or stopped by reverse limit switch or soft limit BL), apply the home position

Forward Limit
1. If the forward limit is true, `JG` at minus the home speed, send `SH` and `BG`, wait until the limit switch is off, `ST`, wait for move in progress to be false
1. Set `JG` to home speed, send `SH` and `BG`
1. Wait for the move in progress to be false
1. If there is a home offset, `PR` to the absolute of minus the home offset*motor steps, send `SH` and `BG`, wait for the move in progress to be false
1. Send `ST`
1. Wait for the move in progress to be false
1. If motor is set to de-energise after move, send `MO`
1. Wait 0.6 seconds
1. If apply home position is true, the forward limit is true, the reverse limit is false, and the stop code is 2 (Decelerating or stopped by forward limit switch or soft limit FL), apply the home position
