> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [2T 3D Vector Magnet](2T-3D-Vector-magnet)

# Scientific Magnetics 2T 3D Vector Magnet

The system comprises: 
* temperature controllers (including a Lakeshore 336)
* 3 power supplies (one for each axis)
* helium level gauge
* a rotation stage (controlled separately by a Galil axis)
* needle valve (controlled by Galil analogue output, or Thurlby-Thandar EX355P PSU)

There is a manufacturer supplied VI. A copy of the manufacturer's VI is located on the C: drive on LARMOR, in C:\LabVIEW Modules\Drivers\Scientific Instruments\3D Magnet\Source Code\Vector-control-v16isis.vi.  This VI has been used on LARMOR and ZOOM and it uses the TTi PSU for needle valve control.  When the magnet was originally used on POLREF, an analogue output from the Galil was used.