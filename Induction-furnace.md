# Induction furnace

Device is being developed by Jakob Ahlburg at Aarhus university.

Internally it uses several pieces of hardware - a Julabo, a power supply etc but we only talk to an arduino controller (via serial). The arduino controller contains the PID controller and all logic that is needed to drive the device at the hardware level.

Serial command set is on manuals shared drive.

Some items cannot currently be read back from the device (e.g. PSU control mode, PSU fan status, PSU output relay status, HF oscillation active). I will contact Jakob to try to get these readbacks implemented.

