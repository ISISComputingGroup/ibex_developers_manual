**Configuration:** Configuration in reflectometry defines the beamline and the components in the beamline. Reflectometry configuration is written in python.

**Component:** An item on the beamline that interacts with the beam in some way (tracking or modifying its path)

**Reflecting component:** An item on the beamline that can change the direction of the incoming beam for e.g. Super mirror

**Passive component:** An item on the beamline which interacts with the beam but does not change the direction of the incoming beam for e.g. slits

**Incoming Beam:** The beam as described by position and angle at the point where its path last changed before a given component.

**Parameter:** A top-level user parameter, describing some value relative to the incoming beam.

**Straight Through Beam:** The beam as described by its position and angle when it enters the blockhouse. The coordinate system used by the reflectometry IOC is relative to the straight through beam, i.e. a component at height 0 would sit in the centre of the straight through beam.

**Engineering correction:** It is a human correction applied to components by users in users' configuration. Engineering correction is applied in the driver layer



