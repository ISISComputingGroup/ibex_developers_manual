> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Motor IOCs](Motor-IOCs) > [EnginX Sample Positioner](EnginX-Sample-Positioner)

The sample positioner on EnginX allows the sample to be moved into position. It is not controlled by IBEX through the motor record but instead via lvdcom this is to allow them to use the EnginX jog box. when plugged in the jog box allows the operator (once SECI mode is selected) to jog the positions of various axes at various speeds; the controller has a speed control and an enable jog button. There is user information for the sample poistioner in the [user manual](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Engin-X-Sample-Stack).

Under the hood the IBEX `SamPos` IOC uses lvdcom to talk with the labview vi. The labview vi then talks through the table of motors to the galil controller. The controller runs a special program which allows the jog box to work as well as normal positioning. The controller is then connected to a BLuAC which converts the motor signals from the galil into signals that the motor can use (I think this is stepper to servo). The BLuAC has its own encoder which it uses to position the motor. The galil uses a different encoder for its positions.

### Galil Program

The program should be burnt in to the controller see the readme text in the labview modules `LabVIEW Modules\Instruments\Enginx\Galil Programs`. The program is also in there and is called `jogboxwithpos.gal` this is the one to upload it is a compressed version of a more commented program. Recently we were going to replace the controller but uploading the program did not seem enough, we ended up reverting to the original controller. The new program didn't allow jogging but we think this was because certain variable were not defined, we are not yet sure where they are defined. We were trying to move Z axis the variables not defined were `JOGS`, `MultD` and `TwkD`. The variables in the current controller are as follow (as on 2020/09/02):

```
ADI= 1.0000
AIM= 0.0000
BDI= 1.0000
BIM= 0.0000
CDI= 1.0000
CIM= 0.0000
DDI= 1.0000
DIM= 0.0000
EDI= 1.0000
EIM= 0.0000
EmStop= 0.0000
ITERB= 1.0000
JGVAL= 19354.9988
JIM= 0.0000
JOGS= 0.0000
JVAL= 9.9951
JVALA= 19980.4749
JVALB= -6605.7648
JVALC= -13021.2616
JVALD= 4278.5767
JVALE= 7.6294
JogM= 0.0000
LightC= 0.0000
LimAct= 0.0000
LimFA= 0.0000
LimFB= 0.0000
LimFC= 0.0000
LimFD= 0.0000
LimFE= 0.0000
LimRA= 0.0000
LimRB= 0.0000
LimRC= 0.0000
LimRD= 0.0000
LimRE= 0.0000
LocM= 0.0000
MULTA= 3000.0000
MULTB= 3000.0000
MULTC= 3000.0000
MULTD= 3000.0000
MULTE= 3000.0000
MultA= 200.0000
MultB= 200.0000
MultC= 200.0000
MultD= 200.0000
MultE= 200.0000
ODCA= 1024.0000
ODCB= 998400.0000
ODCC= 1024.0000
ODCD= 1024.0000
ODCE= 19456.0000
PosA= 0.0000
PosB= 0.0000
PosC= 0.0000
PosD= 0.0000
PosE= 0.0000
PvPosA= 0.0000
PvPosB= 0.0000
PvPosC= 0.0000
PvPosD= 0.0000
PvPosE= 0.0000
TESTWT= 1000.0000
TPosA= 1006864.0000
TPosB= -2286.0000
TPosC= 4540.0000
TPosD= -152439.0000
TPosE= -443800.0000
TwkA= 1.0000
TwkB= 1.0000
TwkC= 1.0000
TwkD= 1.0000
TwkE= 1.0000
VA= 1024.0000
VB= 998400.0000
VC= 16384.0000
VD= 16384.0000
VE= 9216.0000
```

The program is described in the directory but in `Jog Box.dmc`.
