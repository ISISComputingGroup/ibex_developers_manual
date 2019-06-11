> [Wiki](Home) > [Galils Under SECI](galils-under-seci)

# Move for GPHI on CRISP

This is based on a theoretical move from 0 to 2.4, it is assumed that the encoder and motor are 'equal'.

This was based on the settings for GPHI  on CRISP, which are as follows:

| Setting | Value |
| --- | --- |
| Axis | G |
| Acceleration | 4096 |
| Deceleration | 4096 |
| Speed | 2048 |
| Motor steps per unit | 1600 |
| Used | True |
| Motor Type | 2 |
| De-energise | False |
| Encoder Present | True |
| Encoder Steps per Unit | 1000 |
| Forward Backlash | 0 |
| Backward Backlash | -0.2 |
| Correct Motion | True |
| Set-point Deadband | 0.000625 |
| Dual Position Stage | False |
| Move Call | |
| Positional Accuracy | 0.000625 |
| After Move | |
| Before Move | |


| State | Commands sent to Galil | Values |
| --- | --- | --- |
| Init | | Corrections = 0 <br><br> Setpoint = 2.4 <br><br> Position = 0 |
| Send Setup | <pre> g_spG = -3840 <br><br> PRG = 0 <br> DPG = 0 <br> MTG = -2 <br> ACG = 4096 <br> DCG = 4096 <br> SPG = 2048 <br> CEG = 0<\pre> | |
| Setpoint | PT = 1 <br><br> PAG = -3840 | |
| Begin Motion 3 | SHG <br><br> BGG | |
| Wait for Stop 3 | | Position = 2.4 |
| Setpoint + Correction | PRG = 0 <br><br> DPG = -3840 <br><br> PAG = -3840 <br><br> ACG = 409 <br><br> DCG = 409 <br><br> SPG = 204 | Corrections = 1 |
| Begin Motion 4 | SHG <br><br> BGG | |
| Wait for Stop 4 | | Position = 2.4 |
| Check for accuracy | | |
| Stop | STG | |
| Wait until Stop | | |
| Delay before Power Off `Wait 0.05s` | | |
| Power Off | SHG | |
| End | | |