# Oxford Instruments Mercury Heliox

The mercury Heliox systems are a type of refrigerator which cools using Helium-3. Using this technique, temperatures of around ~300mK can be achieved. 

The heliox systems, like dilution fridges, are parasitic, which means they must sit in an outer cryostat or cryomagnet which provides the initial stage of cooling to low temperature (a few degrees Kelvin) before the heliox provides the final stage of cooling (to ~300mK). The outer cryostat is usually controlled by a standard Mercury ITC controller.

# Communications

### Settings

The Mercury can be physically configured to use serial, ethernet or GPIB as it's transport layer. As ISIS, we use serial. The serial settings can be changed on the physical device, but we typically use 57600 baud as this is usually an acceptable compromise of transmission speed against line length restrictions. If there is a very long connection from the moxa to the heliox unit, and there is noise on the line, it may be useful to reduce the baud rate to see if this helps.

### Command set

The Heliox systems are physically based on the mercury ITC temperature controllers, but they do not use the same command set and cannot be controlled by the same drivers. The mercury heliox systems have their own driver.

The devices use an SCPI-like command syntax. There are two approaches to getting data using this protocol:
- Ask for everything in one go, e.g. `STAT:DEV:HelioxX`. This will return a huge status string containing every measurement under that category (~30 items). This approach is used by the labview driver (although it only actually looks at the data for a few measurements). It is also useful for enumerating the valid pieces of data that you can ask for individually.
- Ask for one thing at a time, e.g. `STAT:DEV:HelioxX:TEMP:SIG:TEMP`. This will only return the one measurement which we asked for. This approach is what the IOC uses.

### Channels

The mercury ITC driver essentially reads data from 5 distinct channels:

| Channel name | Physical sensor location | Notes |
| --- | --- | --- |
| `HelioxX:HEL` | He3 Pot | This is the "main" heliox control channel. According to the OI manual this is the only channel which we should need to use to control the heliox's temperature. In the IOC and Labview driver, this is the only channel on which we allow setting setpoints. It is a hardware alias of either `HeHigh` or `HeLow` depending on temperature (see below). |
| `He3Sorb:TEMP` | He3 Sorption pump | Dedicated channel for the (helium-3) sorption pump. Monitoring only. Note: the He3 sorption pump and the He3 Pot are not the same! | 
| `He4Pot:TEMP` | He4 Pot | Dedicated channel for the (helium-4) 1K-pot cooling stage. Monitoring only. Note: the way that ISIS run the Mercury Heliox systems means that this channel will read a constant value all the time, as there is no actual hardware present on the heliox to read this. This hardware would only be present if a single Mercury ITC unit was used to control both the main cryostat and the sorption stage. | 
| `HeHigh:TEMP` | He3 Pot | Monitoring only. This is a "high" (~2-80K) temperature thermocouple, used for measuring the temperature of the He3 Pot when the temperature is in it's range of validity. This channel will give invalid temperatures if the heliox is running at "low" temperature. | 
| `HeLow:TEMP` | He3 Pot | Monitoring only. This is a "low" (~0.2-2K) temperature thermocouple, used for measuring the temperature of the He3 Pot when the temperature is in it's range of validity. This channel will give invalid temperatures if the heliox is running at "high" temperature. | 

# Regeneration

### Physical process - background

Sorption cooling stages can only dissipate a finite amount of energy before they must be "regenerated". This is contrast to dilution cooling, which can be run (essentially) continuously.

A regeneration follows the following physical process:
- Regeneration is started either manually (by the user) or automatically by the IOC/labview driver if that option is selected
- The He3 sorption pump is warmed significantly (to about 30K).
- This heat causes the pump to release all of the Helium-3 stored in it.
- At the same time, the 1K pot is run, which causes the helium-3 to recondense when it comes into contact with the 1K pot
- Once all of the helium 3 has recondensed, the sorption pump is cooled back down. This causes it to start "pumping" and therefore cooling of the He3 Pot resumes.
- This process will take approximately 30-90 minutes depending on the starting temperature of the heliox.

The heliox typically needs a regeneration after 8-12 hours of cooling. This depends on the sample and the external heat load.

In effect, this means that the users lose temperature control while a regeneration is in progress. TODO: do the scientists know this or will they be surprised by this behaviour? Are regenerations typically done automatically or manually or does this depend on the scientist/experiment?

### Detecting when a regeneration is required

The following is how the existing labview driver detects whether a regeneration is required:

A regeneration is captured by a boolean with the following inputs:
- Mode = "Low Temp"
- And Heliox temperature > 0.4K
- And He3 Sorb heater in automatic mode
- And He3 Sorb heater percent heat < 0.2%
- And no comms errors within the last 120 seconds
- And auto-recondense enabled on labview front panel
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