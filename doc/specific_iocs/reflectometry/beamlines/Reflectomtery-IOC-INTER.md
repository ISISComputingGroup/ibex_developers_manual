# Reflectometry IOC - INTER

Specific information about INTER.

### Mirrors

Inter is equipped with 2 supermirrors, which may be used in any combination (just `SM1`, just `SM2`, both in, neither in) depending on the experiment. `SM2` also presents a special case for the reflectometry IOC - when it is not used to bounce the beam, it is used as a beam guide. In this configuration the mirror is physically moved out of the beam, but still has to track the beam as reflected by `SM1` at an offset. `SM2` is never in a fixed parked position.

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

{#refl_inter_beam_blocker}
### Slit 3/Beam blocker

The [beam blocker](../Reflectometry-Beam-Blocker) on INTER is not setup yet.

### Sample height correction

INTER has a correction function on sample height which is a fudge factor to account for engineering imperfections in the mirror alignment. [See here](https://github.com/ISISComputingGroup/IBEX/issues/6357#issuecomment-844244014) for more detail


## Initial Testing
Initial testing on `INTER` was performed from 19 Aug 20 to 21 Aug 20. Tests performed:
- Correctness of SECI <-> IBEX swap scripts
- Motor setup has been transferred correctly
    - Compared current positions/limits after swap
    - Compared direction of movement/backlash
- Testing tracking for different combinations of SM1 angle, SM2 Angle and Theta.
    - Using Laser: checking the dot reaches the centre of the detector
    - Using motor positions: Recorded positions and compared them to motor positions under SECI

### Notes

We noticed some discrepancies between the motor positions in SECI and IBEX for the mirror/theta tests. Investigation revealed that parts of the SECI calculations are incorrect. The theoretical IBEX approach is correct - correctness of the IBEX implementation still needs to be confirmed by the scientists. SECI implementation may need to be fixed as INTER will likely still be running on SECI in the near future.

#### Issues found with conversion script:
- "Home position" offset applied to `MTRXXXX.OFF` 
    - In our case we wanted to ignore this value as homing is only done in SECI for now, but in other cases this is the correct behaviour
- Offset sign was incorrect
- De-energise set incorrectly
- Encoders were not set 
    - This is due to running the conversion on simulated motors. Information added [to the motor migration wiki page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Migrating-Galil-motors-from-SECI-to-IBEX).

--> [Ticket 5654](https://github.com/ISISComputingGroup/IBEX/issues/5654)

#### Issues found with reflectometry server:
- InBeam status incorrect at component level 
    - [Ticket 5655](https://github.com/ISISComputingGroup/IBEX/issues/5655)
- Noticed a slight delay before move starts 
    - [Ticket 5658](https://github.com/ISISComputingGroup/IBEX/issues/5658)
- Some axes sounded unhappy when moving synchronously at a slow speed (e.g. detector height, optimised for certain speeds)
    - Marked SM1/2 height driver as not synchronised as super mirror height axes are slow and are likely the main cause for this issue


#### Issues found with IBEX in general
- If a motor drives past its limits due to backlash it can stall and not complete the move 
    - This is an edge case but we should have a discussion whether this is the right behaviour
- Noticed IBEX IOC list to be blank after running SECI to IBEX swap script
    - [Ticket 5659](https://github.com/ISISComputingGroup/IBEX/issues/5659)
- Boy console popping up hides scripting window
    - [Ticket 5302](https://github.com/ISISComputingGroup/IBEX/issues/5302)
- Slit 3 West value was slightly off after a switch from SECI to IBEX.
    -  When switching back to SECI later it was the same as in IBEX, suggesting it is not an issue with the readback value between the two systems, but rather the axis had actually moved. The axis was not moved explicitly during this whole time, so not sure what exactly happened. We should keep an eye out to see whether this happens again.
