# What it is for

Access security, alternatively known as "manager mode", is used to prevent users from writing values to an IOC while letting instrument scientists assign values. 

# How to set it up

Here are the basic steps to follow:

- For each record in the IOC which should be protected, add an `ASG` field
- For instrument specific DB records, it is ok to hard-code the ASG (for example, `field(ASG, "MANAGER")`)
- For general IOCs, the access security group should be defined as a macro (e.g. `field(ASG, "$(ASG=DEFAULT)")`). Giving the `ASG` macro a default value of `DEFAULT` will mean that existing instruments using this IOC will be unaffected.
- The `ASG` macro can then be supplied from an `st.cmd`, or a `globals.txt` as appropriate. The two useful values for the ASG macro for setting up access security are `DEFAULT` (acts as normal) and `MANAGER` (with access security).
- OPIs that might be protected by access security should have the access security widget in them. This can be copy-pasted from the template OPI.
- The access security widget in the OPI depends on a PV provided from the IOC in the following way:
```
record(scalcout, "$(P)MANAGERMODE")
{
    field(ASG, "READONLY")
    field(DESC, "Non-zero if manager is required for this IOC")
    field(PINI, "YES")
    field(INPA, "$(PVPREFIX)CS:MANAGER CP")
    field(BB, "$(ASG)")
    field(CALC, "A = 0 && BB = 'MANAGER'")
    field(OOPT, "Every Time")
}
```
- Note that you will need to pass in `$(PVPREFIX)` from your `st.cmd` for this to work!

_(If you need a "real world" example, the jaw set on Polaris has been set up using access security.)_

# Further information

The access security rule is defined in `C:\Instrument\Apps\EPICS\support\AccessSecurity\master\default.acf`. 

This looks at a PV which is `$(P)CS:MANAGER`. If the PV is set to 1 then manager mode is enabled, if it is 0 then manager mode is disabled. The GUI simply sets this PV to 1 or 0 as you enter or exit manager mode.

To check whether access security is working properly it can be useful to use a `cainfo <pv>`, this tells you whether you currently have read, write, or both permissions.

# Even more information

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/EPICS-basics#Access-Security

https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Access-Gateway

# Past approaches / future extensions

In future it may be desirable to implement a "baton" system which allows users to request exclusive access to an instrument. There was a small amount of front-end code related to this removed in [this commit](https://github.com/ISISComputingGroup/ibex_gui/pull/615/commits/f3ea01d0cb4d192d5b6f22990540718c650bb8c2). The back end for this was never implemented.