> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [SMC](SMC)

SMC100 Motor controller it has N axes which have different ports.

This is a newport motor controller. They have peculiar startup and homing behaviour, after powering up they must be homed and once homed they can not be homed again.

If running asyn trace, when it is working you may have nothing printed, so i guess It doesn't look to regularly poll

### Connection

DLS system: connected to laptop via a gender changer. It deos not seem to need a null modem, not tested if correct gender cable works, seems "traditional" to use a cable + gender changer.
