# Linmot

## Getting initial values for a migration

There are no config files, values are hardcoded in LabVIEW VIs. On a block diagram you will find a number referred to as `linmotcalibration` - this will be `MRES` in ibex. So `MRES = linmotcalibration`

Also look at the offset values in the VI, these are in motor steps but in ibex need to be in EGU. Also note that they are usually applied in LabVIEW that requires a sign change when going to ibex, but check VI logic. So normally `OFST = -(offset_in_vi *  linmotcalibration)`

Velocity - this is hardcoded in VI and in `internal_units_per_second`, but often `50`. Just set `VELO = value_in_vi_used_in_a_!SV_command` 
 
COM port - due to an indirect logic lookup in LabVIEW, the real COM port to use in ibex is 1 more than the number in the VI. `ibex_com_port = labview linmot port + 1`

Check order axes are indexed in,  A,B,C,D = MTR01,02,03,04 in ibex 

If all is correct, motor position values should agree onscreen when swapping between ibex and LabVIEW

## Setting limits

To set limits use PV values in the configuration. For examples of this see ENGINX and/or MAPS jaw sets e.g. setting `IN:ENGINX:MOT:MTR0102.HLM` and `IN:ENGINX:MOT:MTR0102.LLM`. You can get the limits required from the LabVIEW front panel, right click on a control and look at "data entry properties" of blades and gaps. You should also set DRVH and DRVL on VGAP:SP and HGAP:SP if limits are set in LabVIEW. Taking SXD as an example, individual blades have a range of -4.5 to 41 and gaps 0.2 to 82


  