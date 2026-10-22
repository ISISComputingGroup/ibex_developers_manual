# Multi-Galil IOC

In some cases it is necessary for one IOC to talk to multiple galil motor controllers.

For example, this IOC is used for SANS2D, which have a jawset with opposing jaw blades on different galil controllers.

### Configuration macros

The `GALILMUL` iocs are configured with `ADDR` and `MTRCTRL` macros as for a normal galil. A blank `MTRCTRL` macro specifies that no controller exists.

### Motor configuration files

The `GALILMUL` iocs load `.cmd` files from `C:\instrument\settings\config\<machine>\configurations\galilmul`, similar to the existing (single) galil controller IOC. The `.cmd` file it looks for depends on the controller `GALILMUL` IOC has loaded. If controller `01` and `02` is selected in galilmul configuration then it will look for `galilmul01.cmd` and `galilmul02.cmd` files. The same files can be loaded as the usual, single, galil controller (for example `jaws.cmd` or `motorExtensions.cmd`). 

If multiple `GALILMUL` iocs are present on a beamline, use a macro guard like `$(IFIOC_GALILMUL_01=#)` to select the appropriate IOC

### Example configuration for split jaws

IOC macros:
- `GALILADDR1`: `192.168.x.x`
- `GALILADDR2`: `192.168.x.y`
- `MTRCTRL1`: `1`
- `MTRCTRL2`: `2`

In file `C:\Instrument\Settings\config\NDWxxxx\configurations\galilmul\jaws.cmd`:

```
$(IFIOC_GALILMUL_01=#) dbLoadRecords("$(JAWS)/db/jaws.db","P=$(MYPVPREFIX)MOT:,JAWS=JAWS1:,mXN=MTR0101,mXS=MTR0102,mXW=MTR0103,mXE=MTR0201")
```