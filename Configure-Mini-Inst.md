> [Wiki](Home) > [Deployment](Deployment) > [Deployment on an Instrument Control PC](Deployment-on-an-Instrument-Control-PC) > Configure Mini Inst

As well as installing the EPICS aspects of the instrument, the directory `C:\Instrument\Settings\config\NDXxxxxx\configurations\`.

Inside that directory create
- startup.txt which contains a list of the IOCs to start (use the IOC name as in the IOCs list)
- globals.txt with the macro values relating to the IOCs in startup.txt
