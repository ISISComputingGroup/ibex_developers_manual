# Mercury Heliox

The mercury Heliox systems are a type of refrigerator which cools using Helium-3. Using this technique, temperatures of around ~300mK can be achieved. The heliox systems, like dilution fridges, are parasitic, which means they must sit in an outer cryostat which provides the initial stage of cooling to low temperature (a few degrees Kelvin) before the heliox provides the final stage of cooling.

The Heliox systems are physically based on the mercury ITC temperature controllers, but they do not use the same command set and cannot be controlled by the same drivers. The mercury heliox systems have their own driver.

# Labview driver oddities

The following notes apply to the labview driver:
- The driver does not work with labview 2018. It works with 2014 - I am not sure in which intermediate version it stops working. The symptom is that it never even tries to send bytes to a serial port.