## Overview
This page details how to write soft `motor` records that control two hard `motor` records with a `transform` record converting between the two coordinate systems in between. This is based on experiences writing the Larmor beamstop controller which has two Galil motor axes representing the angle of the arm (`theta`) and a horizontal (`w`) position which is controlled by two soft motors in a Cartesian coordinate system (`x`, `y`). This system is complicated by the fact that the `y` axis in Cartesian space is related to both the `w` and `theta` axes of the motors.

## Key Components
There are several parts that need to be considered. The most important fields in the soft `motor` records are the `OUT`, `RDBL`, `STOO`, and `DINP` fields.
 - The `RDBL` field reads the current position of the transformed motor positions from the `transform` record
 - The `OUT` field writes out the soft motor position to the `transform` record
 - The `STOO` field writes out a bit indicating if the user has requested the motors stop, this needs to be transformed to both the underlying motors.
 - The `DINP` field reads in a bit indicating if the underlying motors have stopped moving, this needs to read from both the underlying motors.

## Known issues



