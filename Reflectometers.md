> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers)

The aim of the reflectometer project is to allow users of the reflectometers to have a common and easy experience to set the position of items on the beam line. The setup is fairly complex because of there are multiple items that need to be coordinated to make a measurement. This page should give an overview of what is going on and the user cases that are needed.

The image below shows a schematic of the inside of the block house for a typical reflectometer.

![Reflectometer Schematic](reflectometers/refl_beamline_setup.PNG)

- The beam travels from the neutron target on the left to the detector on the right, bouncing off a sample along the way.
- Theta is the main parameter we care about in reflectometry experiments.
- Different experiments may require different beamline setups which may affect the beam path. (e.g. adding a mirror in this instance)
- Whenever the beam path is modified, we want equipment to automatically track the beam as appropriate for the currently active configuration. Coordinating motion at the beamline level in this way is the primary purpose of our reflectometry system.


Related pages for more detail:

- [Setup and science behind the experiment](Reflectometers-Science)
- [Reflectometers Beam Height Calculation](Reflectometers-Beam-Height-Calc)
- [Reflectometry IOC](Reflectometry-IOC)
- [Reflectometry Testing](Reflectometry-Testing)

### Components in a mode

Table of our understanding for each mode what is in the beam and what is tracking the beam. States are:

- O: Out of the beam
- I: In the beam but not tracking it
- T: In the beam and tracking it

Mode      | S1 | Polariser | S2 | sample stack | ideal sample point | S3 | analyser | S4 | Detector
---       | --- | -----    |  --- | ----       | ----               | --- | ---     | --- | ----
NR (Neutron reflecting)        | T  | O         | T  | I            | T                  | T  | O        | T  | T  
polarised | T  | T         | T  | I            | T                  | T  | O        | T  | T  


In sim language

Mode | S1 Height above beam |  Polariser angle and height above 


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
1. Coordinates: according to IDFs, ZYX on `INTER`, `SURF`, `OFFSPEC` is XZY on `CRISP`, `POLREF`. We use the former. Is this a problem?
    - Convention from `INTER` etc. is correct.
1. Currently, the theta readback displays the angle to the detector but if the detector is set to be above the beam the readback is still to the detector and so the theta sp and readback do not agree. What should we do:
    1. Don't allow displacement relative to the beam to be set on components which interface with Theta
    2. Use the difference between the beam intercept and the position for the setpoint and add this to the read back position
    3. Do nothing this is the correct behaviour and is telling the instrument scientist they are not measuring what they think they are
    - *Answer* 2
1. Will you want to do individual moves while another move is going on?
    - Yes

### Unanswered Questions

1. Beam block, turn on beam block mode what do you expect to happen? What can we control - yes I know this is th 3rd iteration of this
1. Change engineering correction based on mode how does this work 
1. CRISP: What is the position for S4? (found it in mantid IDF, but values differ from those in VI - assumption is VI is correct)
1. Do we need to reflect SP of motors into Reflectometry server
     - Alarm on sp not same as RBV is good. OK?
1. #5456: Are there lots of configs and scripts to convert, which ones?
1. Can we have the dance script for POLREF?
1. Ask about vertical CHI for FOM/SAMPLE again
1. Ask about where horizontal/vertical gaps should be and what labels on vertical config
   - More generally how does this apply to all components
1. Are there different park position dependent on the mode
1. How to get pixel 28 out is it a numbered spectra
1. Clash conditions on POLREFR
    - sample table height is the the only one
    - Homing how does that work
1. Homing of motors what can and what can't
1. Bump strips what does it do
1. Bender offspec analyser: Which motor drives chi? Do you need to change motor settings?