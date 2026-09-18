# Removing or renaming an IOC module

If you rename or remove a support module, you will need to edit the Makefile in e.g. support/Makefile or ISIS/Makefile
The Makefile contains a default list of modules for all architectures, then additional modules based on build architecture can be added e.g. modules only for Windows

If you rename or remove an IOC, you will need to edit the Makefile in ioc/master/Makefile  This Makefile contains a variable IOCDIRS that lists all potentially valid IOC directories, then other _NOTBUILD variables are used to remove certain builds on certain architectures.   