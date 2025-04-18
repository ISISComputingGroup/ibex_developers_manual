# ALF Goniometer

The ALF Goniometer is a 6-axis goniometer. There is no specific logic required in controlling it, all that is required is the standard movement across the whole range with appropriate encoder/motor counts, and an ability to home all axes to a known position.

## Axes Conventions
The numbering of the axes below corresponds to the number of the axes on the [annotated diagram](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/ALF/ALF_Gonio_annotated.png) of the ALF goniometer.

1. `Z-axis`
1. `theta` (a.k.a. `Rrot`)
1. `Cy` (according to `galil.ini` for LabVIEW control)
1. `Cx` (according to `galil.ini` for LabVIEW control)
1. `Rlower`
1. `Rupper` 

## Axes & Motors
The table below defines how the goniometer axes are connected to motors, and the motor setup data needed: 

Axis Name | `Rupper` | `Rlower` | `Cx` | `Cy` | `theta` | `Z`
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
Axis letter (crate) | F | E | D | C | B | A
Units | deg | deg | mm | mm | deg | mm
Acceleration | 4000 | 4000 | 4000 | 4000 | 8192 | 2048
Deceleration | 4000 | 4000 | 4000 | 4000 | 8192 | 2048
Speed | 700 | 2000 | 2000 | 2000 | 2048 | 4096
LabVIEW Motor Steps per Unit | 1358 | 1719 | 640 | 640 | 756 | 641
Motor Type | Reverse<br>Active<br>High | Reverse<br>Active<br>High | Reverse<br>Active<br>High | Forward<br>Active<br>High | Forward<br>Active<br>High | Forward<br>Active<br>High
Encoder Present | Yes | Yes | Yes | Yes | Yes | Yes
LabVIEW Encoder Steps per Unit | 842 | 1074 | 400 | 400 | 472 | 400
Encoder Type | Normal Quadrature | Normal Quadrature | Normal Quadrature | Reverse Quadrature | Normal Quadrature | Reverse Quadrature
Home Method | Forward<br>Limit | Forward<br>Limit | Forward<br>Limit | Forward<br>Limit | None<br>Available | Reverse<br>Limit
Home Value | 25.4 | 27.6 | 55.6 | 57.922 | N/A | 0
Max from Home | 25.4 | 27.6 | 55.6 | 57.5 | N/A | 200
Min from Home | -25.4 | -27.6 | -55.6 | -57.5 | N/A | 0
Max Travel | 40 | 80 | 100 | 100 | 360 | 200 