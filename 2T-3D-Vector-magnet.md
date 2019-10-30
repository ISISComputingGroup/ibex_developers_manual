> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [2T 3D Vector Magnet](2T-3D-Vector-magnet)

# Scientific Magnetics 2T 3D Vector Magnet

The system comprises: 
* temperature controllers (including a Lakeshore 336)
* 3 power supplies (one for each axis)
* helium level gauge
* a rotation stage (controlled separately by a Galil axis)
* needle valve (controlled by Galil analogue output, or Thurlby-Thandar EX355P PSU)

### VI

There is a manufacturer supplied VI and an LVDCOM IOC. A copy of the manufacturer's VI is located in SourceSafe here: `\LabVIEW Modules\Drivers\Scientific Instruments\3D Magnet\Source Code\Vector-control-v16isis.vi`.  This VI has been used on LARMOR and ZOOM and uses the TTi PSU for needle valve control.  When the magnet was originally used on POLREF, an analogue output from the Galil was used.

### Ethernet Switch

The magnet control rack has a small Ethernet switch inside to provide network access to the Lakeshore 336 and MOXA (see below).  This will need to be connected to the ISIS network to enable remote control of the magnet.

### MOXA NPort

The rack has its own dedicated MOXA NPort 5616 due to the number of devices it uses.  When the system is moved between instruments, this MOXA is added to the NPort configuration on the local control machine and its ports assigned to COM101-COM116 (so as not to interfere with common equipment).  The control machine IP address should be added to the "accessible IPs list" of the MOXA via the administration webpage (and subsequently removed when the magnet is finished with).  Currently, the settings of the dedicated MOXA are:

* IP address : 130.246.37.108
* Port 1 : SMC X PSU
* Port 2 : SMC Y PSU
* Port 3 : SMC Z PSU
* Port 4 : Cryocon 32 temperature controller
* Port 5 : Helium level meter
* Port 6 : TTi EX355P PSU (for needle valve)

### Rotation Stage

Standard unit controlled by a Galil axis on both SECI and IBEX instruments.  Details:

* +- 370 degrees
* Motor with encoder
* **_No_** limit switches - Do **not** rotate more than 360 degrees too many times or cables will be damaged.
* Home position defined by an index pulse on the encoder

When this magnet was last installed on ZOOM, one of the slit axes was used for the rotation stage as there are no spare cables in the sample area.  A batch file exists in the `configurations\galil` directory of the `settings` area to set the required PV values for the axis (edit if different axis is used), and a corresponding batch file in the `user\users\ZOOM` directory of the 'U-drive' will reinstate the settings for the slit axis when the magnet rotation stage is removed.

**NB** There are plans to install additional cabling into the ZOOM sample area to connect extra motion stages, so this _borrowing_ of an axis may not be needed any longer.  Check before altering PV values.

### Miscellaneous Information

* The system takes approximately 3 days to reach base temperature
