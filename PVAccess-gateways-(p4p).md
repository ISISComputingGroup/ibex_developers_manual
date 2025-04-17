# Instrument gateways

Instrument PVAccess gateways are available as of [#8319](https://github.com/ISISComputingGroup/IBEX/issues/8309) for connecting to EPICS V4 PVs on the same subnet. In practice this means other PVs in r3 if you are in r3, and similarly for r55/r80/r2.

Generally it is recommended to run a single gateway process per machine, in contrast to the channel access gateways which often have multiple gateway processes per machine. In order to support this, the p4p gateway has good "client" and "server" options which allow specifying multiple gateway servers within the same process. 

The [`p4p` gateway documentation online](https://mdavidsaver.github.io/p4p/gw.html#quick-start) is generally quite good.

### Instrument gateway setup

- The gateway is started by `C:\Instrument\Apps\EPICS\gateway\start_pva_gw.bat` (called by `start_gateways.bat`)
- A script called `generate_p4p_config.py` dynamically generates a `p4p` config file, based on the current machine's network settings, and writes it to `C:\Instrument\Var\tmp\p4p_config.json` just before the gateway starts.
- PVAccess address lists are set in `config_env_base.bat`
- The `p4p` gateway logs to `C:\Instrument\Var\logs\gateway\pva`

### Access security

`p4p` is currently unable to parse our `.acf` file for access security. Therefore, the gateway has been set to be globally read-only instead.

In practice this limitation is unlikely to be relevant - the obvious use cases for PVAccess (e.g. areadetector arrays) are primarily read-only anyway.

### Block gateway

Under channel access, we use a block gateway to alias underlying PVs into blocks.

A PVAccess block gateway should be possible, but most of our block infrastructure does not currently support PVAccess anyway (e.g. archiving, `g.cget`, GUI blocks view, ...).

# Site gateways

Site PVAccess gateways, which would allow access between the r55, r80, r3 subnets are not currently available. They will be added in [#8419](https://github.com/ISISComputingGroup/IBEX/issues/8419).