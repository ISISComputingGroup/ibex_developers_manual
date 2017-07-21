## Overview
This page details how to write soft `motor` records that control two hard `motor` records with a `transform` record converting between the two coordinate systems in between. This is based on experiences writing the Larmor beamstop controller which has two Galil motor axes representing the angle of the arm (`theta`) and a horizontal (`w`) position which is controlled by two soft motors in a Cartesian coordinate system (`x`, `y`). This system is complicated by the fact that the `y` axis in Cartesian space is related to both the `w` and `theta` axes of the motors.

