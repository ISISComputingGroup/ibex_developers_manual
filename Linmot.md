# Getting initial values for a migration

There are no config files, values are hardcoded in labview VIs. On a block diagram you will find a number referred to as `linmotcalibration` - this will be `MRES` in ibex. So normally `MRES = linmotcalibration`

Also look at the offset values in the VI, these are in motor steps and in ibex need to be in EGU. Also note that they are usually applied in a way that requires a sign change, but check VI logic. So normally `OFST = -(offset_in_vi *  linmotcalibration)

Velocity - this is hardcoded in VI, but often `50`. It is in steps per second in both cases. So `VELO = value_in_vi` 
 
COM port - due to an indirect logic lookup, the real COM port to use is 1 more than the number in the VI. `ibex_com_port = labview port + 1`

Check order axes are indexed A,B,C,D = MTR01,02,03,04 in ibex 

If all is correct, values should agree onscreen when swapping between ibex and labview

# Setting limits

To set limits use PV values in the configuration. For examples of this see ENGINX and/or MAPS jaw sets e.g. setting `IN:ENGINX:MOT:MTR0102.HLM` and `IN:ENGINX:MOT:MTR0102.LLM`. You can get the limits required from the labview front panel, right click on a control and look at "data entry properties" of blades and gaps. You should also set DRVH and DRVL on VGAP:SP and HGAP:SP if limits are set in labview. Taking SXD as an example, individual blades have a range of -4.5 to 41 and gaps 0.2 to 82


  