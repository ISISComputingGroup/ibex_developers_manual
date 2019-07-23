# Oxford Instruments Mercury Heliox

The mercury Heliox systems are a type of refrigerator which cools using Helium-3. Using this technique, temperatures of around ~300mK can be achieved. 

The heliox systems, like dilution fridges, are parasitic, which means they must sit in an outer cryostat or cryomagnet which provides the initial stage of cooling to low temperature (a few degrees Kelvin) before the heliox provides the final stage of cooling (to ~300mK). The outer cryostat is usually controlled by a standard Mercury ITC controller.

# Command set

The Heliox systems are physically based on the mercury ITC temperature controllers, but they do not use the same command set and cannot be controlled by the same drivers. The mercury heliox systems have their own driver.

The devices use an SCPI-like command syntax. There are two approaches to getting data using this protocol:
- Ask for everything in one go, e.g. `STAT:DEV:HelioxX`. This will return a huge status string containing every measurement under that category (~30 items). This approach is used by the labview driver (although it only actually looks at the data for a few measurements). It is also useful for enumerating the valid pieces of data that you can ask for individually.
- Ask for one thing at a time, e.g. `STAT:DEV:HelioxX:TEMP:SIG:TEMP`. This will only return the one measurement which we asked for. The IOC will initially attempt to use this approach but keep a protocol file for the above commands available, until we can do a hardware test to check which approach is better.

# Channels

The mercury ITC driver essentially reads data from 5 distinct channels:

| Channel name | Notes |
| --- | --- |
| `HelioxX:HEL` | This is the "main" heliox control channel. According to the OI manual this is the only channel which we should need to use to control the heliox's temperature. In the IOC and Labview driver, this is the only channel on which we allow setting setpoints |
| `He3Sorb:TEMP` | Dedicated channel for the (helium-3) sorption cooling stage. Monitoring only. | 
| `He4Pot:TEMP` | Dedicated channel for the (helium-4) 1K-pot cooling stage. Monitoring only. | 
| `HeHigh:TEMP` | Monitoring only. Currently unsure of purpose. | 
| `HeLow:TEMP` | Monitoring only. Currently unsure of purpose. | 

# Regeneration

### Physical process - background

Sorption cooling stages can only dissipate a finite amount of energy before they must be "regenerated". This is contrast to dilution cooling, which can be run (essentially) continuously.

I believe a regeneration follows the following physical process (note: this probably needs checking for correctness by cryogenics):
- Regeneration is started either manually (by the user) or automatically by the IOC/labview driver if that option is selected
- The He3 Pot is warmed significantly (from ~300mK to >1K?).
- This heat causes all of the Helium-3 in the sorption stage to evaporate
- At the same time, the 1K pot is run at maximum cooling power, which causes the helium-3 to recondense when it comes into contact with the 1K pot
- Once all of the helium 3 has recondensed, sorption cooling can restart which brings the temperature back towards base temperature

According to a manual I found online, the heliox may need a regeneration after 8-12 hours of use. I think this depends on the sample and the external heat load. Note: talk to cryogenics about this to make sure this timescale is semi-sensible at ISIS.

In effect I think this means that the users lose temperature control while a regeneration is in progress. TODO: do the scientists know this or will they be surprised by this behaviour? Are regenerations typically done automatically or manually or does this depend on the scientist/experiment?

### Detecting when a regeneration is required

The following is how the existing labview driver detects whether a regeneration is required:

A regeneration is captured by a boolean with the following inputs:
- Mode = "Low Temp"
- And Heliox temperature > 0.4K
- And He3 Sorb heater in automatic mode
- And He3 Sorb heater percent heat < 0.2%
- And no comms errors within the last 120 seconds
- And one or both of:
  * Either:
    * Rate of change of temperature over the last 200 seconds > 0.0005K/min (calculated by line of best fit)
    * AND variance of temperature over the last 200 seconds > 0.0005K
    * AND (Heliox temperature - TSet) > 0.25K
  * Or:
    * (Heliox temperature - TSet) > 0.05K continuously for 600 seconds

This boolean must then stay true continuously for 120 seconds. If it does, then a regeneration is triggered.

### Regeneration logic

When a regeneration is triggered, the existing labview driver simply sends a temperature setpoint of zero. There is logic to do something much more complicated, but it is "commented out" in an `if False` statement.

It appears to me as though the setpoint is never set back to the previous value in the labview code. There is lots of code relating to this, but it appears to all be hard-coded to False.

# Labview driver oddities

The following notes apply to the labview driver:
- The driver does not work with labview 2018. It works with 2014 - I am not sure in which intermediate version it stops working. The symptom is that it never even tries to send bytes to a serial port. I think it is crashing while trying to get a subVI by reference but I am not completely sure about this.