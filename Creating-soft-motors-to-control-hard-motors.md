## Overview
This page details how to write soft `motor` records that control two hard `motor` records with a `transform` record converting between the two coordinate systems in between. This is based on experiences writing the Larmor beamstop controller which has two Galil motor axes representing the angle of the arm (`theta`) and a horizontal (`w`) position which is controlled by two soft motors in a Cartesian coordinate system (`x`, `y`). This system is complicated by the fact that the `y` axis in Cartesian space is related to both the `w` and `theta` axes of the motors.

## Implementation
And example of two soft motors with a non-trivial coordinate transform in between taken from the Larmor beamstop is given below:

```
record(motor, "$(P)ARM:X") 
{ 
    field(LOCK, "YES")
    field(DESC, "X axis position")
    field(SCAN, "Passive")
    field(DTYP, "Soft Channel") 
    field(OUT, "$(P)CONVERTXY.C PP MS") 
    field(RDBL, "$(P)CONVERTXY.F CP MS") 
    field(STOO, "$(P)ARM:MOTORS:STOP.A  PP MS") 
    field(DINP, "$(P)ARM:MOTORS:DMOV CP MS") 
    field(URIP, "Yes") 
    field(MRES,"0.001") 
    field(RRES,"1.000") 
    field(PREC,"3") 
    field(TWV,"5") 
    field(RTRY,"0") 
    field(EGU,"mm") 
}

record(motor,"$(P)ARM:Y") 
{ 
    field(LOCK, "YES")
    field(DESC, "Y axis position")
    field(SCAN, "Passive")
    field(DTYP,"Soft Channel") 
    field(OUT, "$(P)CONVERTXY.D PP MS") 
    field(RDBL,"$(P)CONVERTXY.G CP MS") 
    field(STOO,"$(P)ARM:MOTORS:STOP.B  PP MS") 
    field(DINP,"$(P)ARM:MOTORS:DMOV CP MS") 
    field(URIP, "Yes") 
    field(MRES,"0.001") 
    field(RRES,"1.000") 
    field(PREC,"3") 
    field(TWV,"5") 
    field(RTRY,"0") 
    field(EGU,"mm") 
}

record(transform, "$(P)CONVERTXY") {
	field(DESC, "Transform X then Y") 
    field(ASG, "READONLY")

    field(INPA, "$(P)TOTHETA.B CP MS")
    field(INPB, "$(P)$(MTR2).DRBV CP MS")
    field(INPE, "$(ARMLEN)")

    field(CLCF, "COS(A)*E + B")
    field(CLCG, "SIN(A)*E")
    field(CLCH, "ASIN(D/E)")
    field(CLCI, "C - SQRT(E**2 - D**2)")

    field(OUTH, "$(P)FROMTHETA.A PP")
    field(OUTI, "$(P)$(MTR2).DVAL PP")
}
```
There are several fields that need to be considered. The most important fields in the soft `motor` records are the `OUT`, `RDBL`, `STOO`, and `DINP` fields.
 - The `RDBL` field reads the current position of the transformed motor positions from the `transform` record
 - The `OUT` field writes out the soft motor position to the `transform` record
 - The `STOO` field writes out a bit indicating if the user has requested the motors stop, this needs to be transformed to both the underlying motors.
 - The `DINP` field reads in a bit indicating if the underlying motors have stopped moving, this needs to read from both the underlying motors.

The former two fields can be linked directly to a single `transform` record. A `transform` record can handle both the conversion to and from the soft motor's coordinate system. For the latter two fields, two additional records are required if the axes of the soft motors are defined by a combination of the underlying motors. These should output a combination of the states from both underlying motors. For example:
```
record(transform, "$(P)ARM:MOTORS:STOP") {
    
    field(CLCC, "A || B")
    field(CLCD, "A || B")

    field(OUTC, "$(P)$(MTR1).STOP PP")
    field(OUTD, "$(P)$(MTR2).STOP PP")

    field(PINI, "YES")
}

record(calc, "$(P)ARM:MOTORS:DMOV") {
    field(SCAN, "Passive")
    field(INPA, "$(P)$(MTR1).DMOV CP")
    field(INPB, "$(P)$(MTR2).DMOV CP")

    field(CALC, "A && B")

    # Must include MDEL to avoid a race condition when setting
    # either of the soft motors to the position they're already at
    field(MDEL, "-1") 
    field(PINI, "YES")
}
```

## Known issues



