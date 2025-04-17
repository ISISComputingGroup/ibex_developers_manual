Issues that arise when running a mini-inst.

### IOC will not start and console is not available for IOC I have put in startup.txt

If you want to start an IOC but it doesn't appear to have a console even though it is in `startup.txt`. It is likely that the `proc serve` has not been created to make the list of proc server running small. To fix this run `make iocstartups` in the base epics folder. If you can not restart IBEX then start the IOC manually.

