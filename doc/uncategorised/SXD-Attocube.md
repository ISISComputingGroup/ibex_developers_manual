> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [SXD Attocube](SXD-Attocube)

The Attocube device is used on SXD and controlled by a Galil, the code running on the Galil can be found [here](https://github.com/ISISComputingGroup/IBEX/issues/6056#issuecomment-2102666963). It has been [migrated from SECI](https://github.com/ISISComputingGroup/IBEX/issues/6056). 

On initialisation the following commands should be sent (in this order):

```
VERBOSE=0
AB0
MO
XQ #SXD
MG "stop 1" {P2}
```

BUSY is determined by comparing the response to BUSY= with \s0.0000\r\n:, if they match the system is not busy.
ATANGLE= returns the Angle Position
Y= returns the Arc Position
If setting the angle send ATTO= with a double between +170 and -170, followed by ATGO=1
If setting the arc send ARK= with a double between -19 and +19, followed by ARGO=1
If stop has been requested send the same set of commands as on initialisation, AB0, MO, XQ #SXD, MG "stop 1" {P2}