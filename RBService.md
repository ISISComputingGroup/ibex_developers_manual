## Introduction

RBService is a C# program that runs as a service and pulls IBEX `experiment details` information from [BUS apps API](https://api.facilities.rl.ac.uk/ws/ScheduleWebService?wsdl) and saves it in an XML file. The generated XML file is then stored in `C:\Data\RBNUM`, and is read by SECI to fill up the experiment details perspective in SECI. This service ideally should only be running on the SECI instrument as it is now been replaced by [Experiment Database Populator](https://github.com/ISISComputingGroup/ExperimentDatabasePopulator) in an IBEX instrument.

## Code

The code is available from http://svn.isis.rl.ac.uk/InstrumentControl/RBNumberFinder/. It is a simple service app, which is built using .NET Framework 4.8 however, it can be run on an instrument which has .NET Framework between 4.5 and 4.8. The element `<supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.8"/></startup>` has been removed from the `.config` file so that it can run on machine which does not have .NET Framework 4.8. It does not use any features which are only exclusively available at 4.8 and it should work fine on the instrument which has .NET Framework above 4.5.

## Troubleshooting

### Fault occurred while processing
* Check that the password is correct

### Could not establish secure channel for SSL/TLS with authority
* Check that you are using the TLS protocol supported by the API. Anything below 1.2 is not supported



