## A

**Alignment:** The process of finding the position of an axis where it is centered/perpendicular to the neutron beam by scanning over a range of positions. This position is then usually defined as 0.

**[Diagram of axis conventions available here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectomtery-IOC-POLREF#axes)**

**Axis, X:** Translation across the `Natural Beam`.

**Axis, Y:** Height relative to the `Natural Beam`.

**Axis, Z:** Displacement along the `Natural Beam`.

**Axis, Chi:** Yaw angle of a component relative to the `Natural Beam`. (Rotation in XZ Plane)

**Axis, Phi:** Pitch angle of a component relative to `Natural Beam`. (Rotation in YZ Plane)

**Axis, Psi:** Roll angle of a component relative to `Natural Beam`. (Rotation in XY Plane)

**Axis, Long:** Z Translation axis of disused INTER detector (pre tank upgrade)

**Axis, Seesaw:** Rotation of a bench around its centre, achieved by applying an equal but inverse height offset to its front and back height jacks. Used for bench `Alignment`. Different to Bench Angle which rotates around the virtual sample point

## B

**Beam, Incoming:** The source of the beam segment before interacting with a given a component as described by Y, Z and Angle coordinates. This is the `Outgoing Beam` of the last reflecting component the beam has interacted with, or the `Natural Beam` if no reflections apply.

**Beam, Outgoing:** The origin of the beam path segment after interacting with a given component as described by Y, Z and Angle coordinates. This becomes the `Incoming Beam` for the following component. If this component is non-reflecting, repeat the outgoing beam of the last reflecting component.

**Beam, Natural**: The neutron beam as it enters an instrument blockhouse without any additional reflections. This is a downward 1.5° for TS1 beamlines and a downward 2.3° for TS2 beamlines. The `Natural Beam` defines the Z axis of the Y/Z tracking plane in which the coordinate system used by the reflectometry server exists.

**Beam, Straight Through:** See `Natural Beam`

**Beam, Reflected:** The current beam path including any reflections from mirrors & sample (often contrasted with the theoretical `Natural Beam`)

**Beamline Object:** The top level object holding & coordinating the whole geometry model inside the reflectometry server.

**Bench:** A large movable bench that pivots on an arc around a point of reflection i.e. a mirror or sample. Benches can be found on OFFSPEC and POLREF. They are all identical in dimensions and are each driven by 3 physical axes: Front height jack, back height jack and slide (which is a linear translation towards/away from the pivot). From these, we derive the bench angle and height offset from the beam. Benches usually have other components statically mounted on top of them e.g. Slits, Detectors

## C

**Characteristic Value:** The low level motor value which a given `Beamline Parameter` is derived from. Can be added as a readback to a `Beamline Parameter` for diagnostics purposes.

**Component:** An item on the beamline that interacts with the beam in some way (tracking or modifying its path)

**Component, Passive:** An item on the beamline which interacts with the beam but does not change the direction of the incoming beam e.g. slits

**Component, Reflecting:** An item on the beamline that can change the direction of the incoming beam for e.g. a super mirror

**Configuration:** Configuration in reflectometry defines the beamline and the components in the beamline. Reflectometry configuration is written in python.

**Coordinates, Mantid:** Coordinate system where everything moves perpendicular to the `Natural Beam`. The beamline geometry model in the IOC is described in this coordinate system. So named as this convention originated in the Mantid project.

**Coordinates, Room:** Coordinate system where everything moves perpendicular to the floor. Axis positions at the motor level are reported in this coordinate system, as are distances measured between components as part of beamline surveys i.e. these constants usually need to be transformed into their equivalent distances along the `Natural Beam` for the reflectometry config.

## D

**Detector, Point (0D):** A simple tube is used to integrate intensity, the detector itself has no position sensitivity, just the angle it is positioned at

**Detector, Linear (1D):** Also referred to as linear, area or multi-detector, where a stack of tubes/pixels is used to integrate intensity with either vertical or horizontal position sensitivity equal to the pixel size

**Detector, Area (2D):** Also referred to as area detector. Similar to the 1D but with both vertical and horizontal position sensitivity. Note pixels may not be uniform in horizontal/vertical size.

**Downstream**: Further from the source of the neutron beam relative to a given point

## E

**Engineering Correction:** A correction that is added to setpoints / removed for readback values for a given axis at the Composite Driver level. These corrections can be of fixed value, or calculated by a user function or an interpolation matrix. These exist to account for slight inaccuracies in engineering, e.g. a mirror that is not perfectly flat.

## I

**Incident Angle:** See `Theta`

## M

**Mirror:** Some samples, such as liquids, cannot be angled. Mirrors can be used to change the incident angle of the beam to enable multiple angles to be measured from the surface, essentially angling the whole beamline around the sample instead rather than the other way around.

**Mirror, Polarising**: A mirror that additionally polarises the neutrons that it reflects.

**Mirror, Super:** Non-polarising mirror designed specifically for reflecting neutrons. 

**Mode:** A set of defaults which can be used to easily configure the behaviour of the reflectometry server's beamline model at runtime. Modes can define which parameters track i.e. automatically move to stay aligned to the reflected beam, which components should be moved in/out of the beam, which corrections get applied, and they can define a set of parameter default values to apply when you enter the mode (and optionally, to re-apply on every beamline move).
  - Neutron Reflection mode (NR) : The simplest case - no mirrors or polarisers, just reflecting the beam off the sample.
  - Liquid mode: Reflect the beam off a mirror (or multiple) to change the incident angle while keeping the sample level
  - Polarised Neutron Reflection mode (PNR): Basically the same as liquid mode from a motion perspective, but with an added polariser system. 
  - Neutron Reflection mode with Analyser (NA): NR but with an analyser component in the beam between sample and detector
  - Polarised Neutron Reflection mode with Analyser (PA): PNR & NA modes combined
  - Disabled Mode: Disables all tracking and stops the beam path from being able to change while in this mode. Can be used e.g. for aligning a super mirror which would otherwise move the detector while scanning.

## P

**Parameter:** A top-level user parameter, describing some value relative to the incoming beam.
(aka. Beamline Parameter)

## R

**Redefine:** `Beamline Parameters` can be redefined via the reflectometry server, which abstracts the process of setting a motor axes from `USE` to `SET` mode, redefining the user offset and going back to `USE` mode into a single PV write. Redefining via a `Beamline Parameter` also takes any engineering corrections into account.

## T

**Tank:** Refers to the INTER detector tank. This is a large component that pivots on an arc around the virtual sample point, like the benches found on POLREF and OFFSPEC. It is however different, in that instead of two jacks it is driven by a linear height and rotation axis, and that its slide axis moves parallel to the floor rather than parallel to the current bench angle.

**Tracking:** Automatically moving in order to stay centred on the reflected beam as and when it changes.

**Trans:** Can mean one of two things
  - *Translation:* See `Axis, X`
  - *Transmission:* A data collection run with the sample out of beam, used for normalising neutron data.

## U

**Upstream**: Closer to the source of the neutron beam relative to a given point


## V

**Virtual Sample Point:** The theoretical intersection between the incoming beam at the sample and its movement axes.

