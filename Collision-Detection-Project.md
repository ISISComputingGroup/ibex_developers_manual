 This project aims to develop a system for detecting collisions within the LARMOR instrument at STFC's ISIS facility, using the IBEX control system.

## Current Behaviour

Presently, experiments are executed using Genie Python scripts, which command the various axes of motion, as well as the DAE system. Care must be taken to ensure that the motion axes are not allowed to collide with each other, or other parts of the instrument. This means that "soft" limits must be placed on each axis of motion, as determined by the instrument scientist and the equipment present on the instrument.
 
There are certain instrument configurations and situations where setting these "soft" limits does not allow the full range of motion required, or where the limits on multiple axes become interdependent. In this case, it would be useful to re-calculate the "soft" limits dynamically, in order to improve equipment safety whilst also giving the scientists greater freedom.
 
## Proposed System

This project aims to produce a system capable of:
 
 1. Developing a method for describing the geometry & motion of an instrument
 2. Detecting collisions which have occurred, and stopping motion
 3. Dynamically calculating the range of motion for each axis of motion
 4. Dynamically updating the "soft" limits for each axis
 
The system must appear transparent to the instrument users, and to this end, should require minimal changes to experiment scripts. 
 
The system will be prototyped using python, which is already used extensively as part of IBEX.  
 
## Prerequisites
 
This project assumes a development environment with a configured IBEX installation.

The system has been developed using PyCharm.
 
The system interfaces with the IBEX server using EPICS via the Channel Access protocol. Genie python is used for simple setting and getting of PVs, and the python `ca` module is used to monitor changes in PVs. The environment variable `EPICS_CA_ADDR_LIST` needs to be set according to your system. You can find the correct data from an EPICS terminal, by typing `set EPICS`.
 
For collision detection, the system uses the Open Dynamics Engine, through the python module `pyode`.
 
The system also produces a visual rendering of the system, for diagnostic and development purposes. This uses the `pyopengl` bindings, which need `glut.dll` and `glut32.dll`, which are included in the repository. 
***I need to work out  where these came from and what license they need.***
 
## System Overview

The system comprises four main parts:
1. Collision detector
2. Limit calculator
3. PV server
4. Graphic visualiser

Additionally the instrument geometry configuration is loaded in from `config.py`.

### Collision Detector

The collision detector is responsible for stopping motion if a collision occurs. The collision detector must be executed frequently, to stop collisions as promptly as possible. The collision detector runs in a separate thread, to allow it to operate independent to the main program, and provides a `CollisionDetector.collisions` list for interfacing with the rest of the program.

The system uses the Open Dynamics Engine (ODE) to calculate whether any bodies have collided, using the function `collide`. A list of `GeomBox` objects are created, one for each body, each containing an `ode.GeomBox` object. The `ode.Collide` function is used to determine whether each pair of geometries has collided. The `config.ignore` list ensures that only the geometries of interest are analysed, reducing the computational load. 
*Maybe a "collisions of interest" list would be more useful??*

When a collision is detected, the system sends a `.STOP` message to each motor that is currently moving, using genie python.


### Limit Calculator

The system dynamically calculates limits by stepping each motor through its range of motion, and checking for collisions, using the `auto_seek_limits` function. This can be approached as a sequential search, where `collide` is evaluated at each step along the motion. Each direction is searched first with a coarse step, then with a fine step. 

This works on the assumption that most collisions behave like a [rectangular function](https://en.wikipedia.org/wiki/Rectangular_function), and remain collided for a significant portion of movement. Typically this is true for linear motion, but when objects are inclined or in rotary cases the duration of the rectangle function is short. This means that for any step size, the search is not guaranteed to find collision.

If the geometries of the computer model are sufficiently larger than the real-world system, the search step can be optimised.

For a given increase in size `S` applied to each face of the box:
```
modeled size = actual size + 2S
```
Assuming a head on collision and considering only linear movement of the seeking axis, a collision of the real world system occurs once the model has collided by at least `2S`. Furthermore, taking two objects with an actual size of zero, and a modeled size of `2S`, a "head-on" collision is maintained for `4S`. 
In the case of an inclined collision, the collision will persist for longer as the collision path through the centre of the object increases with angle. 
In the case of a glancing collision, whereby the collision of the model does not infer a collision of the real world system, a collision of the model may or may not be detected, but the real-world system will never be at risk.
Therefore any search step of `4S` or less will detect a real-world collision. 

For movements which involve rotation however, the search step must be chosen to ensure that no point on the body moves by more than `4S` in any direction. To achieve this, the system calculates the positions of each vertex of the body at each step. The magnitude of the move is calculated, and if greater than `4S`, the search step can be reduced. The magnitude of the move is re-calculated and the step reduced until the step is less than or equal to `4S`. 

Once an appropriate step size has been found, the magnitude of the move need not be calculated further, reducing the computational load. This assumes that the movement of any body can be expressed as a linear function of the seeking axis - each subsequent step in the seeking process produces a movement of magnitude equal to the first step.

## A title...

### Op modes

### A note on dial *vs* user coords

### Describing Instrument Geometry

The geometry of the instrument is described in `config.py`. Generally the content of this file is a set of parameter lists, where index `i` of each list refers to body `i` of the mechanical system. The various parameters are:

Parameter List  | Description
:---            | :---
`color`         | A list of RGB values of the colour of the body, where `(1, 1, 1)` is white. The colours will be re-used if there are more bodies than colours.
`geometries`    | A `dict` containing the `size` and `position` parameters of the body. For moving bodies, the `position` is not required, as it will be overridden whenever the system moves.
`moves`         | A list of functions which take a list of `Monitor` objects, and return a `Transformation` to describe the new position of each mechanical body.
`ignore`        | A list of collision pairs which are not of interest. This is useful for bodies which are mechanically connected - we don't care if the carriage collides with it's slide.
`pvs`           | A list of motor PVs for each motor axis. The order of these PVs is the order of the `Monitor` objects given to the the `moves` functions.
`hardlimits`    | The end limits of each axis of motion. Nominally the end of travel, though tighter limits can be imposed. The dynamically calculated limits are always within these values. 



















