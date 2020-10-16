> [Wiki](Home) > [The Backend System](The-Backend-System) > [System Components](System-components) > [Inst etc IOC](Inst-etc-IOC)

PVs which are for instrument level, e.g. motors moving and security pvs


## User variables

There are a host of user variables which are autosaved for the users to set. The number of these is controlled with the macro `NUM_USER_VARS`. There are 3 types:

- Integer in `IN:<instrument>:PARS:USER:IX` (X is index)
- Reals in `IN:<instrument>:PARS:USER:RX` (X is index)
- Strings in `IN:<instrument>:PARS:USER:SX` (X is index), NB these are maximum of 40 characters

## User Buttons

There are a group of user buttons which can be setup using the [add buttons shared utility script](https://github.com/ISISNeutronMuon/InstrumentScripts/wiki/Button-Functions). The number of these is controlled with `NUM_USER_BUTTONS` macro.

