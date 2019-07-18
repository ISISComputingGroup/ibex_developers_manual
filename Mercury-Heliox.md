# Mercury Heliox

The mercury Heliox systems are a type of refrigerator which cools using Helium-3. Using this technique, temperatures of around ~300mK can be achieved. The heliox systems, like dilution fridges, are parasitic, which means they must sit in an outer cryostat which provides the initial stage of cooling to low temperature (a few degrees Kelvin) before the heliox provides the final stage of cooling.

The Heliox systems are physically based on the mercury ITC temperature controllers, but they do not use the same command set and cannot be controlled by the same drivers. The mercury heliox systems have their own driver.

There are some older models of heliox which were being used, which were based on ITC503 temperature controllers. Those Heliox systems are **different** to this system and similarly we cannot control them using the standard ITC503 driver. I believe these older systems have now been phased out, but it is possible for old kit to turn up again sometimes...