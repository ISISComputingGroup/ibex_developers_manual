# Blind script output

```
C:\Windows\system32>call C:\Instrument\Apps\EPICS\..\Python\genie_python.bat
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
No instrument specified - loading local instrument

genie_python version 5.2.0
pv prefix NDXCRISP
THIS IS CRISP!
PV prefix is IN:CRISP:

In [1]: g.change_script_dir("c:\\scripts")

In [2]: g.load_script("do_experiment.py")
Loaded the following script(s): runscript
From: c:\scripts\do_experiment.py
File last modified: 2019-03-28 17:30:32

In [3]: runscript()
** Run angle Si_D2O **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.005, Psi=-0.94
Theta set to: 0.3
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 0.609, 0.206, 0.6, 0.9
Wait for 50 uA
** Beginning Run 00103644 at 17:31:47 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 50 uamps
** Ending Run 00103644 at 17:48:50 28/03/19
** Run angle Si_D2O **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.305, Psi=-0.94
Theta set to: 0.6
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 1.218, 0.412, 1.2, 1.8
Wait for 120 uA
** Beginning Run 00103645 at 17:49:12 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 120 uamps
** Ending Run 00103645 at 18:29:39 28/03/19
** Run angle Si_D2O **
Translation to -18.5
Change to mode: NR
Sample: Phi=1.205, Psi=-0.94
Theta set to: 1.5
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 3.045, 1.03, 3.0, 4.5
Wait for 200 uA
** Beginning Run 00103646 at 18:30:18 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 200 uamps
** Ending Run 00103646 at 19:37:38 28/03/19
** Contrast change for valve1 **
Concentration: Valve 1, concentrations [38, 0, 62, 0], flow 1.5,  volume 30, time None, and NOT waiting for completion
Waiting for 1.0 seconds
Waiting for IN:CRISP:CS:SB:Pump_is_on=1
** Transmission Si_Trans **
Translation to -18.5
Change to mode: NR
Theta set to: 0.0
Sample: height offset from beam=-42.067
Setting hgaps to [None, None, None, None] (None's are not changed)
Slit gaps 1-4 set to: 0.25, 0.25, 10, 5
Wait for 180 uA
** Beginning Run 00103647 at 19:38:52 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 180 uamps
** Ending Run 00103647 at 20:41:14 28/03/19
Sample: height offset from beam=-37.067
Reset horizontal gaps to [('S1HG', 39.9985), ('S2HG', 29.9995), ('S3HG', 30.0019), ('S4HG', 40.0)]
** Run angle Si_SMW **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.005, Psi=-0.94
Theta set to: 0.3
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 0.609, 0.206, 0.6, 0.9
Wait for 100 uA
** Beginning Run 00103648 at 21:38:19 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 100 uamps
** Ending Run 00103648 at 22:12:00 28/03/19
** Run angle Si_SMW **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.305, Psi=-0.94
Theta set to: 0.6
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 1.218, 0.412, 1.2, 1.8
Wait for 180 uA
** Beginning Run 00103649 at 22:12:21 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 180 uamps
** Ending Run 00103649 at 23:14:07 28/03/19
** Run angle Si_SMW **
Translation to -18.5
Change to mode: NR
Sample: Phi=1.205, Psi=-0.94
Theta set to: 1.5
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 3.045, 1.03, 3.0, 4.5
Wait for 300 uA
** Beginning Run 00103650 at 23:14:46 28/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 300 uamps
** Ending Run 00103650 at 00:55:45 29/03/19
** Contrast change for valve1 **
Concentration: Valve 1, concentrations [0, 0, 100, 0], flow 1.5,  volume 30, time None, and waiting for completion
Waiting for 1.0 seconds
Waiting for IN:CRISP:CS:SB:Pump_is_on=1
Waiting for IN:CRISP:CS:SB:Pump_is_on=0
** Run angle Si_H20 **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.005, Psi=-0.94
Theta set to: 0.3
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 0.609, 0.206, 0.6, 0.9
Wait for 80 uA
** Beginning Run 00103651 at 01:16:40 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 80 uamps
** Ending Run 00103651 at 01:43:39 29/03/19
** Run angle Si_H20 **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.305, Psi=-0.94
Theta set to: 0.6
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 1.218, 0.412, 1.2, 1.8
Wait for 150 uA
** Beginning Run 00103652 at 01:44:07 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 150 uamps
** Ending Run 00103652 at 02:34:39 29/03/19
** Run angle Si_H20 **
Translation to -18.5
Change to mode: NR
Sample: Phi=1.205, Psi=-0.94
Theta set to: 1.5
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 3.045, 1.03, 3.0, 4.5
Wait for 250 uA
** Beginning Run 00103653 at 02:35:33 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 250 uamps
** Ending Run 00103653 at 03:59:38 29/03/19
** Contrast change for valve1 **
Concentration: Valve 1, concentrations [100, 0, 0, 0], flow 1.5,  volume 30, time None, and NOT waiting for completion
Waiting for 1.0 seconds
Waiting for IN:CRISP:CS:SB:Pump_is_on=1
** Transmission Si_Trans **
Translation to -18.5
Change to mode: NR
Theta set to: 0.0
Sample: height offset from beam=-42.067
Setting hgaps to [None, None, None, None] (None's are not changed)
Slit gaps 1-4 set to: 0.25, 0.25, 10, 5
Wait for 180 uA
** Beginning Run 00103654 at 04:00:59 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 180 uamps
** Ending Run 00103654 at 05:01:41 29/03/19
Sample: height offset from beam=-37.067
Reset horizontal gaps to [('S1HG', 39.9985), ('S2HG', 30.000500000000002), ('S3HG', 30.000700000000002), ('S4HG', 40.0)]
** Run angle Si_D2O **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.005, Psi=-0.94
Theta set to: 0.3
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 0.609, 0.206, 0.6, 0.9
Wait for 50 uA
** Beginning Run 00103655 at 05:02:23 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 50 uamps
** Ending Run 00103655 at 05:21:42 29/03/19
** Run angle Si_D2O **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.305, Psi=-0.94
Theta set to: 0.6
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 1.218, 0.412, 1.2, 1.8
Wait for 120 uA
** Beginning Run 00103656 at 05:22:13 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 120 uamps
** Ending Run 00103656 at 06:02:46 29/03/19
** Run angle Si_D2O **
Translation to -18.5
Change to mode: NR
Sample: Phi=1.205, Psi=-0.94
Theta set to: 1.5
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 3.045, 1.03, 3.0, 4.5
Wait for 200 uA
** Beginning Run 00103657 at 06:03:26 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 200 uamps
** Ending Run 00103657 at 07:10:56 29/03/19
** Contrast change for valve1 **
Concentration: Valve 1, concentrations [38, 0, 62, 0], flow 1.5,  volume 30, time None, and NOT waiting for completion
Waiting for 1.0 seconds
Waiting for IN:CRISP:CS:SB:Pump_is_on=1
** Transmission Si_Trans **
Translation to -18.5
Change to mode: NR
Theta set to: 0.0
Sample: height offset from beam=-42.067
Setting hgaps to [None, None, None, None] (None's are not changed)
Slit gaps 1-4 set to: 0.25, 0.25, 10, 5
Wait for 180 uA
** Beginning Run 00103658 at 07:12:07 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 180 uamps
** Ending Run 00103658 at 08:12:50 29/03/19
Sample: height offset from beam=-37.067
Reset horizontal gaps to [('S1HG', 39.9975), ('S2HG', 30.0), ('S3HG', 30.0015), ('S4HG', 40.0)]
** Run angle Si_SMW **
Translation to -18.5
Change to mode: NR
Sample: Phi=0.005, Psi=-0.94
Theta set to: 0.3
Sample: height offset from beam=-37.067
Slit gaps 1-4 set to: 0.609, 0.206, 0.6, 0.9
Wait for 100 uA
** Beginning Run 00103659 at 08:13:26 29/03/19
*  Proposal Number: 0
*  Experiment Team:
Waiting for 100 uamps
```