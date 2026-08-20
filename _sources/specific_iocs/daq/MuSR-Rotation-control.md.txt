# MuSR Rotation control

MuSR can rotate it's detectors and magnets about the sample position. The two valid orientations are either longitudinal (aligned with the beam) or transverse (rotated 90 degrees relative to the beam).

Changing the orientation is a manual procedure, however the orientation state of MuSR is measured using an analog voltage. This analog voltage is fed into the same DAQMX box which is used for the zero field system, using a fourth (`SPARE`) channel. This channel is exposed via the `ZFMAGFLD` ioc.

The logic and DB records for MuSR's rotation are in `custom_records.db` in MUSR's settings area (these are loaded by the `INSTETC` ioc). The ComponentSwitcher blockserver component monitors the rotation state of MuSR and may change the blockserver configurations if the state changes.

Condition <br>(Channel 4 voltage)          | Action                                                                                  |
---------------------------------------|------------------------------------------------------------------------------|
voltage >= +4V                         | If orientation is not transverse,  set orientation  to transverse, and update the config files accordingly. <br> If orientation  is already transverse,  keep orientation  set to transverse          |
-4V < voltage < +4V                  | Do not change the current orientation                                                         |
voltage <= -4V                         |  If orientation is not longitudinal  set orientation to longitudinal and update the config files accordingly. <br> If orientation is already longitudinal, keep orientation set to longitudinal  |