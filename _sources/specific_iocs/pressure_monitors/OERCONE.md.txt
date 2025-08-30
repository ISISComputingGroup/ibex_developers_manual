# OERCONE

The Oerlikon Centre-One pressure gauge is used to monitor pressure for NIMROD.

COM settings are a single port, 9600,8,None,1, Line Feed as termination character, No flow control.

Pressures are read by sending "PR1<CR><LF>", waiting 100ms, then sending "05" in Hex and reading back the response in the format %d,%f into a status and Gauge value respectively. The gauge value is then displayed and plotted on a graph.

Units can be either mbar (Default), Torr, Pascal or Micron. These are read using by sending "UNI<CR><LF>", waiting 100ms, then sending "05" in Hex and reading back the response which will contain 0 for mbar, 1 for Torr, 2 for Pascal and 3 for Micron.

Units can also be set. To do this the IOC sends "UNI,{0|1|2|3}<CR><LF>", (with the numbers corresponding to mbar, Torr, Pascal and Micron as above), waiting 100ms, then sending "05" in Hex and reading back the response which will contain 0 for mbar, 1 for Torr, 2 for Pascal and 3 for Micron.