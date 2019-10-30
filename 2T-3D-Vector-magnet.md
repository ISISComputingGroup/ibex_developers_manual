> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [2T 3D Vector Magnet](2T-3D-Vector-magnet)

# Scientific Magnetics 2T 3D Vector Magnet

The system comprises: 
* temperature controllers (including a Lakeshore 336)
* 3 power supplies (one for each axis)
* helium level gauge
* a rotation stage (controlled separately by a Galil axis)
* needle valve (controlled by Galil analogue output, or Thurlby-Thandar EX355P PSU)

## VI

There is a manufacturer supplied VI and an LVDCOM IOC. A copy of the manufacturer's VI is located on the C: drive on LARMOR, in `C:\LabVIEW Modules\Drivers\Scientific Instruments\3D Magnet\Source Code\Vector-control-v16isis.vi`.  This VI has been used on LARMOR and ZOOM and it uses the TTi PSU for needle valve control.  When the magnet was originally used on POLREF, an analogue output from the Galil was used.

## MOXA NPort

The magnet control rack has its own dedicated MOXA NPort 5616 due to the number of devices it uses.  When the system is moved between instruments, this MOXA is added to the NPort configuration on the local control machine and the NDX IP address is added to the "accessible IPs list" via the administration webpage (and subsequently removed when the magnet is finished with).  Currently, the settings of the dedicated MOXA are:

* IP address : 130.246.37.108 (Need to check DHCP reserved)
* Port 1 : SMC X PSU
* Port 2 : SMC Y PSU
* Port 3 : SMC Z PSU
* Port 4 : Cryocon 32 temperature controller
* Port 5 : Helium level meter
* Port 6 : TTi EX355P PSU (for needle valve)
