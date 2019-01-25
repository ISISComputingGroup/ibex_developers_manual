> [Wiki](Home) > [Project overview](Project-Overview) > Design documents

The aim of the reflectometer project is to allow users of the reflectometers to have a common and easy experience to set the position of items on the beam line. The setup is fairly complex because of there are multiple items that need to be coordinated to make a measurement. This page should give an overview of what is going on and the user cases that are needed.

[Diagram created in visio](reflectometers/Reflectometry1.vsdx).

## Experiment to perform

The reflectometry experiment is described in part in the [mantid documentation](http://docs.mantidproject.org/v3.12.0/techniques/ISIS_Reflectometry.html) and in [more detail for POLREF](https://github.com/ISISComputingGroup/IBEX/wiki/Reflectometry-at-Isis). The important things to know from this and other are:

1. The data needed to be retrieved is neutron count vs Q.
1. The [momentum transfer](https://en.wikipedia.org/wiki/Momentum_transfer) is characterised from `Q = 4π / λ sin θ` 
1. The wavelength is proportional to the time of flight. So to get a large range of q the scientists stitch together spectra from multiple angles.
1. There are other experiments that can be performed where off-specular alignments are used. Also where the sample is rocked.
1. When thinking about alignments, there is a path through the experiment set by the super mirror, sample point, analyser angle and detector position. Everything else can be aligned to this path but does not control that path. 

## Setup

Generally, the idea is to position the detector at **theta** around the **sample point** (= the coordinates of the beam at a fixed distance x from the detector). We make a distinction between two types of reflectometry instruments based on beamline equipment and the way their detector is positioned.

![TS1 and TS2 nr mode](reflectometers/TS1_and_TS2_nr_mode.png)

In the first case (for INTER, CRISP, SURF), the detector slides up and down on a height stage and can be angled to be perpendicular to the incident beam. This means the distance between sample and detector actually varies slightly, however the beam path on these instruments is relatively short so the resultant error is tolerable.

In the second case (for POLREF, OFFSPEC), the detector sits on a bench, that can be angled, driven up/down, and slide closer/further from the sample, which allows the detector to actually move along a radius around the sample.

![Polarisation mode](reflectometers/polarised_mode.png)

Devices on the beamline are classed as active or passive: **active** devices affect the direction of the beam; **passive** devices do not.  A slit which blocks the beam is passive because it does change the beam direction. Equipment will usually track the beam path; it might not during initial alignment or for some unusual experiments. This means that an offset needs to be added to the position and angle of each piece of equipment after a path change so that it remains centred and perpendicular/parallel to the beam. 

Beamline equipment can be in the beam or not depending on the mode; e.g. some experiments use a super mirror others don't. Once the beamline equipment has been moved to its tracking position the variables that are used to set the values need to be read back to account for engineering errors. For instance:

1. The angle theta is set
1. This sets the detector height
1. The detector will move to this position
1. The readback should then be read
1. The theta for the readback (not the setpoint) is then used to calculate the theta of the device

### Equipment on the beam

#### Polariser/Super Mirror

An active component before the sample which changes the angle of the incoming beam

#### Slit

Slits are passive components that can sit anywhere along the beam line. The centre of a slit is measured from the beam's path.

#### Analyser

An active component placed after the sample which will split the beam. Some forms of analysers change the beam path horizontally, some vertically. In the vertical case they should be treated like mirrors with an angle.

#### Detector

A detector is a passive component that sits at the end of the beam line. There are at least two common types point and 1 D detectors.

## Experimental Modes

### Modes

- Neutron Reflection (NR) mode: just a straight reflection from the ideal sample point. Used for solids and liquids with solids, i.e. things that can be rotated and are not affected by gravity
- Liquids NR: Since liquids cannot be angled, the super mirror is instead used to angle the incoming beam at the sample and make the specular condition correct for different theta.
- Polarised NR: Like NR, but with a polarising supermirror in the beam path set to a given angle, which changes the angle of the incoming beam at the sample point.
- Polarisation Analysis (PA) mode: Like NR but now after the sample point, the beam is split into two by an analyser and the detector moves to see either beam. 2* Theta is still the angle between the incoming and outgoing beam at the sample point.
- Disabled: All beamline components are unlinked from one another's geometry constraints and can be moved independently.

Note: When adding theta into a mode it is expected that you will add the items that define theta to the mode too. This way when you change theta the beamline parameter that sets the component to for theta will move automatically. If you do not do this your readback for theta will be different to you theta value. However we have not put an automatic check on this because it may be desired behaviour (We can add a check in the future).

### Off Specular vs Specular

In Specular mode the point detector is used whereas in off specular the 1D detector is used.

### Components in a mode

Table of our understanding for each mode what is in the beam and what is tracking the beam. States are:

- O: Out of the beam
- I: In the beam but not tracking it
- T: In the beam and tracking it

Mode      | S1 | Polariser | S2 | sample stack | ideal sample point | S3 | analyser | S4 | Detector
---       | --- | -----    |  --- | ----       | ----               | --- | ---     | --- | ----
NR        | T  | O         | T  | I            | T                  | T  | O        | T  | T  
polarised | T  | T         | T  | I            | T                  | T  | O        | T  | T  


In sim language

Mode | S1 Height above beam |  Polariser angle and height above 

## Calculating Height of an Item Above Straight Through Beam

The height of an item along the beam can be calculated based of the incoming angle. This diagram shows how this works.

![Image](reflectometers/Non-small_angle_approx.png)

## Items to Document

### Theta beam path calculation

The theta beam line parameter and its associated component is special because it depends on other item(s) in the beamline. All other components are independent. For read-back, the "angle" of the component is set based on the incoming beam and the angle from the point where the incoming beam hits the sample axis to where a specified component is. For example, on CRISP it is the angle to the detector. This means if the detectors moves it must signal back to the Theta component that it has moved. *TODO* Write done what happens when the given component is not on the beam path.
In disabled mode, the incoming beam is no longer altered and this means changing theta would have no effect on the component it is pointing at, e.g. changing Theta would not alter the position of the detector. To fix this (and a question will be asked about this) there is a special route to force an incoming beam path to be set. This should allow the component defining theta to move when theta is changed.

## Questions

### Answered

1. Is the ideal sample point x position fixes?
    - Yes. The beam coming in will hit any pre-sample active components and the height of the sample point is the point at which the beam reaches this x coordinate.
1. I think each mode of operation sets up fixed rules and relations and this is what we need to capture.
1. We need to calculate both the positions based on composite parameters and composite parameters based on the positions of the components, is this right?
    - Yes, it would be strange not to have this readback
    1. What happens if the beam having hit the super mirror does not hit the sample axis?
        - apart from pathological cases, beam going straight up or backwards, there is always a point that the sample axis is hit
    1. What happens if the detector is not looking at the sample point?
        - Nothing, but a warning in this case would be useful.
1. Does the beam always go forwards?
    - Yes, on reflectometers the beam always goes forward. 
1. Are there any corrections to the idealised model, at that level?
    - No
1. What does an analyser do to the beam? Is it an active component? How does it affect the measurement of theta?
    - Yes it is an active component on some beam lines (depends on type). It doesn't effect the measurement of theta; although if you are calculating the readback the outgoing beam goes to the analyser not the detector.
1. How are slits measured (along the arc or along there length)?
    - In the end it doesn't really matter but they are measured along their length.
1. Room coordinates are these ok as we defined them?
    - Maybe, they should be the same as Mantid default.

### Unanswered

1. Currently, the theta readback displays the angle to the detector but if the detector is set to be above the beam the readback is still to the detector and so the theta sp and readback do not agree. What should we do:
    1. Don't allow displacement relative to the beam to be set on components which interface with Theta
    1. Use the difference between the beam intercept and the position for the setpoint and add this to the read back position
    1. Do nothing this is the correct behaviour and is telling the instrument scientist they are not measuring what they think they are
1. Will you want to do individual moves while another move is going on?
1. Do we need to reflect SP of motors into Reflectometry server
1. Can we have the dance script.
1. Does it matter whether you can change parameters on components parked out of the beam? (e.g. SM Angle in NR Mode)
1. CRISP: What is the position for S4? (found it in mantid IDF, but values differ from those in VI - assumption is VI is correct)
1. Coordinates: according to IDFs, ZYX on `INTER`, `SURF`, `OFFSPEC` is XZY on `CRISP`, `POLREF`. We use the former. Is this a problem?