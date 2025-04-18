# Gateways

## Introduction

There are two files involved in the gateway, an ACF and a PVLIST. When the start_gateways.bat is run it copies the default files, appends any custom rules for the server stored in `settings\config\serverName\AccessSecurity`, and uses the standard macro expander for IBEX.

The ACF is the rules for the access, while the pvlist specifies which rules to follow for what.

## ACF Files

The default.acf used by both the external gateway and the IOCs is stored in `AccessSecurity` - these could be diverged if necessary.

The rules for the groups are enacted from bottom to top

It is possible to have lists of users:

` UAG(listname) { user1, user2 }`

and lists of hosts/computers:

`HAG(listname) { comp1, comp2 }`

Within the defaults for IBEX there is:

`HAG(instmachine) { localhost, $(ACF_IH1=localhost), $(ACF_IH2=localhost), $(ACF_IH3=localhost), $(ACF_IH4=localhost) }`

The macros would be set via globals.txt and would list the machines which are allowed full control of a server via the external gateway

A security group is set up with a number of rules, an example would be:
```
ASG(securityGroupName) {
	INPA("PVNAME")
	RULE(1, READ)
	RULE(1, WRITE, TRAPWRITE)
	{
		HAG(listname)
		CALC("A=0")
	}
}
```
The above security group would allow the PVs which use it (more on that later) to read from anywhere, but could only be written to by the machines in the list with listname when the specified PV is at 0, any other value for that PV and the write won't be allowed.

There are 5 ASG lists within IBEX by default at present and they are as follows, note that a write is always a write, trapwrite:

ASG Name | Read Rule | Write Rule
--- | --- | ---
`DEFAULT` | 1 | 1
`GWEXT` | 1 | 1 for `instmachine`
`READONLY` | 1 |
`WASL0` | 1 | 0 for `instmachine`
`ANYBODY` | 1 | 1

There is a standard record always available within IBEX to control via a CALC as per the example above within INSTETC_01. The db entry for that record is:
```
# used for access security on the fly changes
record (bo, "$(P)CS:EXCLUSIVE") 
{
	field(DESC, "Restrict access to localhost")
	field(SCAN, "Passive")
	field(DTYP, "Soft Channel")
    field(PINI, "YES")
    field(VAL, "0")
    field(OMSL, "supervisory")
    field(ZNAM, "All access")
    field(ONAM, "Restricted access")
}
```

It is also possible to generate 4 more (they have the name $(P)CS:EXCLUSIVE$(ID) in the db entry) using macros EXCLUSIVE1, EXCLUSIVE2, EXCLUSIVE3 and EXCLUSIVE4 which can be set via globals.txt. Note that these entries will need to include a : to use in the ID name, this has been left to implement there as otherwise if for some reason there was an expectation in an ACF for such a macro and it didn't exist we don't end up with a PV with nothing after a :.

Should an IBEX server require specific security group settings, then creating a file called `gwext.acf` in the `Settings\config\servername\AccessSecurity` folder will ensure that the gateway loads up with both the default groups, and any groups specified in `gwext.acf`.

An example of a custom acf file would be:
```
HAG(testing) { computerName }

ASG(TESTING) {
    INPA("$(MYPVPREFIX)CS:EXCLUSIVE$(EXCLUSIVE1=)")
    RULE(1, READ)
    RULE(1, WRITE, TRAPWRITE)
    {
        HAG(testing)
        CALC("A=0")
    }
}

```

Please note, these specific groups will only be required when WRITE access is needed beyond the standard named machines, and/or must be limited in some fashion. All systems will allow READING of any PV.

## PVLIST files

These lists allow the gateway to enact rules separately to the security rules being enacted by the IOCs, as well as providing an ability to ALIAS records as well.

As with the ACF there is default file.

It is possible to alter the evaluation order of the pvlist rules, by default within IBEX they are ordered ALLOW, DENY which makes deny rules override allow rules. This should not be changed.

Within the default pvlist there is a rule for all PVs to ALLOW them to a certain security group. The default for this is `GWEXT`. However, there is a macro, `$(ACF_PV)`, which can be used to alter that to a different security group. Please note, setting this macro could have serious repercussions on who has the ability to control (or not) an instrument, and it should generally be left alone.

Should an instrument need a specific pvlist file then there are a few behaviours and formats to be aware of. To provide access to a PV this has to be done via the original PV, you cannot provide access to an alias in these files if the underlying PV is not granted access. However, if the underlying PV has access then so too do any aliases (or at least that is what was observed). 

In order to alias a PV the format is:

`aliasPVname ALIAS originalPVname`

e.g. `$(MYPVPREFIX)KAUI:EXAMPLE  ALIAS $(MYPVPREFIX)SIMPLE:VALUE2`

In order to alias all PVs in an IOC:

`aliasIOCname\([.:].*\) ALIAS originalIOCname\1`

e.g. `$(MYPVPREFIX)MIRJANA\([.:].*\) ALIAS   $(MYPVPREFIX)SIMPLE\1`

The .* can be used as a wildcard in these files, and is used rather than specifying $(MYPVPREFIX) in the examples below for brevity.

In order to allow a security group access to a PV:

`.*pvName ALLOW securityGroupName 1`

e.g. '.*SIMPLE:VALUE2 ALLOW   TESTING 1'

To allow access to an IOC:

`.*iocName.* ALLOW securityGroupName 1`

e.g. `*SIMPLE.* ALLOW       TESTING     1`

If you are using `CS:EXCLUSIVE:` and a custom `.acf` file, you will also need to create a file called `gwext.pvlist` in `Settings\config\servername\AccessSecurity`. At the end of that file in order for the access security to work remotely, you will need to add:

`.*CS:EXCLUSIVE.*    ALLOW   securityGroupName`

e.g. `.*CS:EXCLUSIVE.*    ALLOW   TESTING`

If the aim is to deny, simply replace the ALLOW with DENY. Do remember that the standard security groups can be used when writing a pvlist file as well as custom ones.

## Troubleshooting

### Printing Reports
In general the gateways are set to low logging levels as they process a lot of PVs and so can be overly chatty. However, if there is an issue with a gateway you can get it to dump a report of it's state by doing `caput %MYPVPREFIX%CS:GATEWAY:BLOCKSERVER:report2Flag 1` and similarly for the external gateway. This will report information into `Instrument\var\logs\gateway`. There are 3 different reports that you can print, see [here](https://epics.anl.gov/EpicsDocumentation/ExtensionsManuals/Gateway/Gateway.html#Report) but generally report 2 gives a good overview of the state of the gateway.

## Links

More information can be found at:

[Gateway: The Process Variable Gateway](http://www.aps.anl.gov/epics/extensions/gateway/) - the main gateway page

[8.7 Channel Access Security](http://www.aps.anl.gov/epics/base/R3-14/12-docs/AppDevGuide/node9.html#SECTION00970000000000000000) - Access Security details for channel access

[caputRecorder 1.4](https://epics.anl.gov/bcda/synApps/caputRecorder/caputRecorder.html) - useful examples for the security groups

[Gateway Users Guide](http://www.aps.anl.gov/epics/EpicsDocumentation/ExtensionsManuals/Gateway/Gateway.html)
