# Lakeshore 350 

The Lakeshore 350 is a temperature controller which is very similar to the [Lakeshore 340](Lakeshore340) but allows for 4 control loops with individual PID controls and heater ranges. The 340/350 IOC should cater for both of these and should detect based on whether the device is communicated with via ethernet or serial (340 is serial and 350 is ethernet) - this is done via a simple lua script in the IOC directory. 


