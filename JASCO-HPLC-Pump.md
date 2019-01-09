> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Gas and liquid handling systems](Gas-And-Liquid-Handling-Systems) > [JASCO HPLC Pump](JASCO-HPLC-Pump)

## Initial thoughts on the pump

Equipment talked continuously for just under 2 days without any problems using our standard MOXA 5610.
The serial baud rate is 4800.
Setting Flow rate appeared fine.
Concentration setting appeared to need a program loaded into the device and run. Did not find a solution to this (unless a program is used). The developer should be aware of this. Using the program option all the time might be a solution.
LabVIEW test vi can be found in C:\LabVIEW Modules\Drivers\Jasco PU-4180 HPLC Pump\Jasco Test.vi. This vi is not fit for beam line usage and has not been developed for user operation. It only proves the operation of the device which was demonstrated to people in the soft matter lab.
There is an example of a program that can be downloaded to the device in the Jasco Pump manual (page 10) that is useful.
I noted that when operated remotely, the settings were not shown on the device display. This was irritating but may need to be accepted by users.

## Connection Details

Baud rate: 4800


