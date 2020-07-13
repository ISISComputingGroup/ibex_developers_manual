# Multi-Galil IOC

In some cases it is necessary for one IOC to talk to multiple galil motor controllers.

For example, this IOC is used for SANS2D, which have a jawset with oppositing jaw blades on different galil controllers.

### Configuration macros

The `GALILMUL` iocs are configured with `ADDR` and `MTRCTRL` macros as for a normal galil. A blank `MTRCTRL` macro specifies that no controller exists.

### Motor configuration files

The `GALILMUL` iocs load `.cmd` files from `C:\instrument\settings\config\<machine>\configurations\galilmul`, similar to the existing (single) galil controller IOC. The same files can be loaded as the usual, single, galil controller (for example `jaws.cmd` or `motorExtensions.cmd`). 

If multiple `GALILMUL` iocs are present on a beamline, use a macro guard like `$(IFIOC_GALILMUL_01=#)` to select the appropriate IOC