> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Muon Active Compensation](Muon-Active-Compensation)

A new opportunity for a small project with a deadline of the 1st of February 2019 was added by the Muon scientists to provide active compensation to the Muon beam-steering magnets on the south side (EMU, MUSR and HIFI).
This page contains the notes from a meeting trying to scope the requirements. This should capture the basics of the requirements, whoever takes the project on should verify that the requirements are complete.

As muons have a magnetic moment and as the instruments are in close proximity the use of the magnet on one instrument can have an impact on the behaviour of the muons and the flux seen on the other two.

Typically this is EMU diverting the paths of the other two beams due to location and shielding differences.

Each instrument needs to be aware of the magnitude and direction (positive/negative and transverse/longitudinal) of their own magnet, and of the other two instruments.

Each magnet will be considered from the desired value by the scientist/user, and the system should correct the actual value sent. This monitoring needs to occur and be acted upon within a few seconds of each other.

A set of linear coefficients (to be provided by the scientists, and ideally alterable by them as well) should be enough to provide this information. It should be possible to run the system without the corrections being used (i.e. the coefficients are not actioned). 

The data flow would be as follows:
1. Value requested of A for the steering magnet
1. Value A is passed through the coefficients and altered based on the status of the magnets on the other instruments (this is a continuous loop with a timescale of a couple of seconds), giving value B
1. Value B is sent to the device
1. The value read back from the device should be considered and kept within a tolerance of Value B

There is a need for an immediate solution, as well as a longer-term solution under IBEX. As such the following changes are needed to the existing LabVIEW system:
1. The control of the septum magnet on HIFI needs to be returned under SECI as well and will be required as part of this work
1. Need to provide an offset field for all steering magnets, this should then be added and subtracted from the set and readback values
1. The offset will be supplied by another piece of code, ideally an IOC ready for later migration to IBEX

The coefficients should be of a similar layout to the following:

| Steering Magnet | Set | EMU | MUSR | HIFI | Offset to Apply |
| --- | --- | --- | ---| --- | --- |
| Horizontal | Desired value | Coefficient 1 | 1 (This instrument) | Coefficient 2 | The result of the equation for the offset to apply to the setpoint based on the appropriate input values |