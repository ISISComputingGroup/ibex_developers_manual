**Configuration:** Configuration in reflectometry defines the beamline and the components in the beamline. Reflectometry configuration is written in python.

**Component:** An item on the beamline that interacts with the beam in some way (tracking or modifying its path)

**Super mirror:** Some samples, such as liquids, cannot be angled. Therefore non-polarising “supermirrors” can be used to change the incident angle of the beam to enable multiple angles to be measured from the surface.

**Reflecting component:** An item on the beamline that can change the direction of the incoming beam for e.g. Super mirror

**Passive component:** An item on the beamline which interacts with the beam but does not change the direction of the incoming beam for e.g. slits

**Incoming Beam:** The beam as described by position and angle at the point where its path last changed before a given component.

**Parameter:** A top-level user parameter, describing some value relative to the incoming beam.

**Straight Through Beam:** The beam as described by its position and angle when it enters the blockhouse. The coordinate system used by the reflectometry IOC is relative to the straight through beam, i.e. a component at height 0 would sit in the centre of the straight through beam.

**Engineering correction:** It is a human correction applied to components by users in users' configuration. Engineering correction is applied in the driver layer

**0D or point detectors:** A simple tube is used to integrate intensity, the detector itself has no position sensitivity, just the angle it is positioned at

**1D detector:** Also referred to as linear, area or multidetector’s, where a stack of tubes/pixels is used to integrate intensity with either vertical or horizontal position sensitivity equal to the pixel size

**2D detector:** Also referred to as area detector. Similar to the 1D but with both vertical and horizontal position sensitivity. Note pixels may not be uniform in horizontal/vertical size.




