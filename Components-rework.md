# Configurations & Components

Going forward, we intend to streamline the interactions between the GUI and the Blockserver regarding configurations and components, as well as reworking the class architecture in the GUI.

We distinguish between the following two types of interaction:

## Use Case 1: Reading a configuration
For example when switching to a different active configuration, or reading config data on the dataweb.

_What we expect to read from the Blockserver:_

One PV containing a configuration in it's entirety, i.e. all elements(iocs, blocks, groups ...) native to the configuration as well as ones imported from components.
GET_CURR_CONFIG_DETAILS currently holds this information. It might be beneficial to change the format to complete components nested within the config description (instead of blocks, groups, etc mixed in the respective lists and names of components separately)

## Use case 2: Editing a configuration
Edit Config
2 PVs: 1 with config(native elements and component names), 1 with all component details - match up in GUI
Same format for read & write 

Tickets:
- GUI: Separate Editing and Reading Configs
- GUI: turn EditableConfiguration into EditingModel
- GUI: Make Configuration- and (new)Component-class inherit from common superclass
- Create PV in blockserver with native only configs
