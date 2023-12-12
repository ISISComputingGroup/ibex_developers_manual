> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Reflectometry Configuration](Reflectometry-Configuration) > [Reflectometry Config Training](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Overview-&-Setup) > Exercise 6


# Beamline Parameters Misc

In this short section, I just want to briefly mention some other functionality BeamlineParameters provide:

- `autosave`: Parameters have an optional `autosave` flag which determines how SPs for those parameters get initialised on start-up. At this point in time **we probably just want to autosave every parameter by default** - read below for rationale
    - If `True`, they are read from a file in `/Instrument/var/refl/`. SPs get autosaved whenever a parameter is moved i.e. a new SP is applied as SP:RBV. 
    - If `False`, parameters are initialised to their current RBV. This option was implemented as a way for the reflectometry server to account for positions being changed outside of IBEX when swapping between SECI and IBEX for testing. This option is deprecated as not autosaving positions can lead to some ambiguity when initialising setpoints, and the workflow it supported is outdated as reflectometers are not going back to SECI anymore.


### [< Previous: Parking Components](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Config-Training-%E2%80%90-Exercise-5) || [Next: Beamline Parameters Misc](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Training-%E2%80%90-Exercise-7)>