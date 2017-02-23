## Configurations & Components

When asking blockserver for Configuration

Use case 1:
Read Config (Load, dashboard)
1 PV containing all blocks, iocs etc.
Possibly change format to nested

Use case 2:
Edit Config
2 PVs: 1 with config(native elements and component names), 1 with all component details - match up in GUI
Same format for read & write 

Tickets:
- GUI: Separate Editing and Reading Configs
- GUI: Make Configuration- and (new)Component-class inherit from common superclass
- Create PV in blockserver with native only configs
