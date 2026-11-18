# Muon Active Compensation

As muons have a magnetic moment and as the instruments are in close proximity the use of the magnet on one instrument can have an impact on the behaviour of the muons and the flux seen on the other two.

Typically this is EMU diverting the paths of the other two beams due to location and shielding differences.

Each instrument needs to be aware of the magnitude and direction (positive/negative and transverse/longitudinal) of their own magnet, and of the other two instruments.

This has been achieved via an IOC that reads values from all interfering magnet IOCs across the 3 beam-lines (That is, the main and transverse field on HIFI and EMU, and the field and direction on MUSR.) These values are then multiplied with a coefficient set by the scientists per magnet and then summed to find the correction for a single steering magnet, this process is repeated with unique coefficients for each steering magnet.

<img width="743" height="362" alt="image" src="https://github.com/user-attachments/assets/79670ff7-2344-4a9b-8fdf-21b2d2600105" />

The offset calculated from the interfering magnets and coefficients can then be used to modify set-points to each steering magnet, or ignored if corrections are disabled.

<img width="604" height="414" alt="image" src="https://github.com/user-attachments/assets/b64891bf-3b4d-4731-8d6f-8ff09e6cf8b2" />

If the offset changes at all while corrections are enabled (whether by a change in the interfering magnets, or the coefficients being altered) then the value sent to the magnet will also immediately be updated, based on the most recent set-point and the new offset.


### Macros
While setting up the Beam Correction IOC, Macros must be set to define to PVs to interact with for each interfering and steering magnet, as well as an additional macro to set the number of steering magnets. (Currently should be 2 for EMU and MUSR, and 4 for HIFI, SUPERMUSR plans to move to 6). There is also a macro that allows the scientists to control whether or not corrections are enabled by default (Though this macro itself defaults to false).

The OPI allows for an additional 4 macros to be used to name steering magnets to increase clarity for users.

### Implementation Details
While corrections are enabled the calculation for a Steering magnet is  $`b = a + \sum_{i=1}^n c_im_i`$ where $`n`$ is the number of interfering magnets, $`c_i`$ is the coefficient for a specific interfering magnet and the steering magnet, $`m_i`$ is the current value of an interfering magnet, $`a`$ is the requested set-point, and $`b`$ is the output sent to the steering magnet.
When the correction is disabled the the requested set-point $`a`$ is instead sent directly to the magnet IOC.
