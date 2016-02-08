************************
Rules for Configurations
************************

A record of the rules for the various parts of a configuration.

--------------
Configurations
--------------

#. A configuration can be contain multiple components
#. A configuration cannot contain other configurations
#. A configuration can be converted to a component only if it does not contain any components

------
Blocks
------

#. Blocks are uniquely named and case is ignored (i.e. Block1 is the same as BLOCK1)
#. Block names can only include alpha-numeric chars and '_', and must start with an alpha-numeric char
#. Blocks must not be named "lowlimit", "highlimit", "runcontrol" or "wait"
#. Blocks do not know which group they are in
#. Blocks can only belong to one group
#. Blocks know which component they are in with null (None in Python) meaning they are not in a component
#. If a block appears more than once in a configuration the subsequent occurances are ignored (raise warning)
#. If a block is duplicated in a component then the component instance is ignored (raise warning)
#. If a block appears in multiple component the first one read is used, the rest are ignored (raise warning)

------
Groups
------

#. Groups are for grouping and ordering how the blocks are displayed in GUIs
#. Groups are uniquely named and case is ignored (i.e. Group1 is the same as GROUP1)
#. Group names can only include alpha-numeric chars and '_', and must start with an alpha-numeric char
#. If a block listed in a groups does not exist it is removed from the group (raise warning)
#. Empty groups are not saved
#. Groups defined in the configuration can include blocks from components
#. If a group is in the configuration and component then the order of blocks is configuration then component.
   Any duplicate blocks in the component are ignored (raise warning)

----------
Components
----------

#. Components cannot contain other components
#. A component group cannot contain blocks that are not in that component
#. When a component is loaded as part of a configuration its IOCs are started if they are not already started
#. Components cannot be loaded on their own only as part of a configuration

----
IOCs
----

#. If an IOC's macros or pvsets changes then restart the IOC on a configuration change
#. It should be possible to force IOCs to restart on a configuration change even if the macros or pvsets have not changed
#. An IOC is only included in a configuration/component if its auto-start setting is true

