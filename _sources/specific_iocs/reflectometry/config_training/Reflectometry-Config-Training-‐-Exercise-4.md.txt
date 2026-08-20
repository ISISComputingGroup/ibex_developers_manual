# Exercise 4 - Theta

Other than the properties of the sample itself, the reflectivity of surfaces and interfaces between media is dependant on a primary parameter. This parameter is the incident angle of the beam at the sample, also known as Theta. For any given sample, the scientists usually take measurements at 3 or 4 different Theta angles, then stitch the data together to get the complete reflectivity profile. 

> Side note: taking more measurements at finer Theta steps would produce better data. Theoretically, scientists could take measurements at many more discrete angles, stopping and starting data collection in between, however this is impractical due to the added overhead in time and effort required for setting up each measurement. The current approach of measuring a handful of Theta is considered a "good enough" solution. 
>
> In an ideal world, we could sweep scan over the whole Theta range, taking one snapshot of data for the current Theta RBV for every ISIS pulse. Currently this is not possible as our move synchronization is not sophisticated enough to ensure a consistent alignment throughout the sweep. Solving this problem is what we mean when we talk about "Continuous Scanning". 

Setting a Theta angle is similar to setting a super mirror angle in that every component downstream from the `ThetaComponent` in the reflectometry config will be subject to the new beam path. There is an important difference however in that Theta is NOT linked to the physical angle of the sample stack. This is because the scientists do not want this angle to ever be set implicitly as it could have severe consequences if the sample is e.g. a large tank of liquid which could accidentally be angled and spill all over the blockhouse. Instead, Theta only sets the positions of downstream components for a theoretical incident angle. To ensure the actual beam follows this beam path, the sample Phi angle needs to be set to match this theoretical beam path, the Theta parameter and component are however entirely separate entities from the Sample component and angle.

Similarly, the Theta RBV is not derived from the sample Phi axis, but from a axis representing the position of the detector. At ISIS, we have two different types of detectors from a motion point of view:
1. Detectors moving on a linear height stage that can tilt towards the beam (SURF, CRISP)
1. Detectors mounted on another component that moves on an arc around the sample (POLREF, INTER, OFFSPEC)

For the former, Theta is calculated via trigonometry, where the Detector Height is the Adjacent, and the distance between Sample and Detector is the Opposite side of the right angle triangle. For the latter, the component the detector is mounted on (= a bench or vacuum tank) will have a rotation axis that we can use as readback.

From a config point of view, we can provide the `ThetaComponent` with a list of downstream components from which Theta's RBV can be derived. This is a list as some beamlines may use one of several detectors. Theta will look for the next component in the list that is currently active in the beam and derive it's angle from it. 

As an example, let's say SURF has a structure of `Beam Source - Sample - Point Detector - Linear Detector` where both detectors are driven by linear height stages. If both detectors are in the beam, Theta will derive its value from the Point Detector Height axis. If the point detector is parked out of the beam, Theta will derive its value from the Linear Detector Height axis.

> Side note: The arc detector solution is technically superior as it maintains a constant distance between sample and detector, meaning e.g. Time of Flight is not dependant on Theta. This produces a slight inaccuracy for SURF and CRISP, however due to the optical lever on those beamlines being fairly short the effect is small enough to be ignored.

## Exercise 4

In this exercise, let's add Theta and a detector component from which we can derive its value to our beamline model. For this exercise, we will assume we are using the setup that is found on SURF and CRISP, i.e. a detector that can move up and down on a linear height axis, and tilt towards the beam via a separate rotation axis. (we will look at a bench setup in a later exercise). Add the following to your config:
1. Theta Component and Parameter
1. Detector Component and Detector Height & Angle parameters linked to appropriate motor axes (referred to in the motor axis descriptions as `Sgl detector` = single detector)
1. At this point you can restart the IOC and you should be able to move detector height and angle parameters as with everything we have added previously. Theta should also be there and read `NaN` as we have not yet told it what axis it should derive its value from.
1. Add the detector to Theta's list of components define its angle. The ThetaComponent provides the methods `add_angle_to(component)` to do this for a linear height axis, or `.add_angle_of(component)` for an arc component. 
1. You should now be able to set `Theta` and see it move the detector height & angle. This works the same as the `sm_angle` - you can try setting Theta to 22.5 which should move the detector height axis to the distance between the Theta and detector components, and the angle to 45 deg.

Some tips:
- Theta has it's own component type, `ThetaComponent`. This component has the added functionality of being able to listen to a different component from which to derive it's values.
- The (virtual) Theta component's coordinates need to match the (real) Sample Components coordinates.
- The `Theta` parameter itself is just a simple Axis Parameter that should look basically the same as e.g. `sm_angle`
- All parameters should be in all modes - we always need Theta as well as the detector.
