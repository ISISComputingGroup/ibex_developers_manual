> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [CRISP](Reflectomtery-IOC-INTER)

Specific information about INTER.

### Axes

The following were unused axes on August 2020:

- `SM Trans Y`
- `FOMS - Z2`
- `SM Angle2`
- `SM2 AngleEnc`
- `Long travel`
- `PD Distance`
- `PD2 Angle`

The `SM2 AngleEnc` is the axis which has the SM2 angle encoder connected to enable us to record the encoder and motor position separately.

They don't currently use the detector z axis so we don't need to have this in the reflectometry server


### Blocks

Blocks that may be confusing:

- `Height`: Distance from the sample centre of rotation to the sample. This is used to align the sample with the beam.
- `Height2`: Distance between the beam and the centre of rotation; usually set a 0. This moves the course z stage tracking the beam.
