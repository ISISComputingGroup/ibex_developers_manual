# Muon Active Compensation

```{note}
This is a design document; the functionality is not currently implemented.
```

A [new opportunity for a small project](https://stfc365.sharepoint.com/sites/ISISProjects-Hub/Lists/Project%20List/All%20ISIS%20Projects%20%20Open.aspx?FilterFields1=ListID&FilterValues1=672%2E000000000000%3B%23816%2E000000000000&FilterTypes1=Number&viewid=2180a052%2D20c1%2D4f00%2D9018%2D48e893ad2986) was added by the Muon scientists in 2018 to provide active compensation to the Muon beam-steering magnets on the south side (EMU, MUSR and HIFI). This page contains the notes from a meeting trying to scope the requirements shortly after and was updated in September 2025 following a meeting to confirm requirements. This should capture the basics of the requirements, whoever takes the project on should verify that the requirements are complete.

As muons have a magnetic moment and as the instruments are in close proximity the use of the magnet on one instrument can have an impact on the behaviour of the muons and the flux seen on the other two.

Typically this is EMU diverting the paths of the other two beams due to location and shielding differences.

Each instrument needs to be aware of the magnitude and direction (positive/negative and transverse/longitudinal) of their own magnet, and of the other two instruments.

Each steering magnet will be set to the desired value by the scientist/user, and the system should correct the actual value sent, based on the power of the main magnets of the other instruments. The time to react should be less than two seconds, though ideally faster. 

A set of linear coefficients (to be provided by the scientists, and ideally alterable by them as well) should be enough to provide this information. It should be possible to run the system without the corrections being used (i.e. the coefficients are not actioned), as this will be required for calibration and refining these cooeffecients. 

Both the corrected and set values should be exposed through the GUI.

The data flow would be as follows:
1. Value requested of A for the steering magnet
1. Value A is passed through the coefficients and altered based on the status of the magnets on the other instruments (this is a continuous loop with a timescale of a couple of seconds), giving value B
1. Value B is sent to the device
1. The value read back from the device should be considered and kept within a tolerance of Value B

The coefficients should be of a similar layout to the following:

| Steering Magnet | Set | EMU | MUSR | HIFI | Offset to Apply |
| --- | --- | --- | ---| --- | --- |
| Horizontal | Desired value | Coefficient 1 | 1 (This instrument) | Coefficient 2 | The result of the equation for the offset to apply to the setpoint based on the appropriate input values |
