> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [MERLIN and LET Oscillating Radial Collimators](MERLIN-and-LET-Oscillating-radial-collimators)

The oscillating radial collimator on MERLIN is similar but not quite the same as the one on LET.

# Starting it

Occasionally the oscillating collimator stops oscillating, you can tell because the `current angle` on the OPI will not be changing.

To restart this is sometimes tricky try the following:

1. On the OPI
1. Click Stop
1. Alter the `swept angle` and `operating frequency` to a **valid** and **different** values so it will resend the setting
   1. The valid values for the swept angle as currently 0-2 (you can see by right click on the input text box and `Show pv info`)
   1. The valid values of operating frequency are 0-0.5
1. Set the swept angle and operating frequency back to the required settings
1. Click start
1. The `Mode` should now read `Homing` then `Oscillating` and the current angle should start changing. 
    - this was fairly quick (less than 1 minute)

# Hardware quirks:
- The thread will die if zero is sent for distance and velocity. The driver must ensure that distance and velocity are not sent at IOC start.
- The oscillation will stop if the galil is power cycled. To restart the oscillation, the galil driver will need to be restarted to re-upload the oscillation code, and then the collimator restarted as usual via it's OPI. Once the collimator is started via to OPI it will home and then switch to oscillating. 

# Galil Code

The oscialltions are managed by the galil code different on [LET](https://github.com/ISISComputingGroup/EPICS-galil/blob/master/GalilSup/Db/galil_Oscillating_Collimator.gmc) and [MERLIN](https://github.com/ISISComputingGroup/EPICS-galil/blob/master/GalilSup/Db/galil_Oscillating_Collimator_Merlin.gmc). This section is an rough explanation of the code.

```
'************MERLIN Collimator*********
'***********************************
'DETERMINE INITIAL POSITION
'***********************************
```
Comments

```
#HOMER
'*******STEP 1 - Retract Motor******
mode=0
count=0
MT~a=2
DC~a=1024;AC~a=1024;SH~a
```

For homing set up some variables:

- mode (what galil is doing) 
- count (how many oscialltions it has performed)

Then set the acceleration and deacceleration and switch motor on.

```
JP #HOME, @IN[6]=1
SP~a=250;PR~a=2600
mode=1
BG~a
#INI
JP #INI, @IN[6]<>1
WT 100
ST~a
AM~a
```

If at home switch then move off it otherwise go directly to `HOME` step.

```
#HOME
'*******STEP 2 - Find Gigital Home*******
mode=1
AC~a=67107840;DC~a=1024;SP~a=250;PR~a=-2600
SH~a;BG~a
#HEO
JP #HEO, @IN[6]=1
ST~a
AM~a
WT100
```
Move in negative direction and stop as soon as we hit the home switch.

```
AC~a=1024;DC~a= 67107840;SP~a= 20;PR~a=2600
SH~a;BG~a
#HR
JP #HR, @IN[6]<>1
ST~a
AM~a
WT1000
```
Move off the home switch and stop as soon as it disengages.

```
DP~a=-200
PA~a=0
SH~a
SP~a=1024
BG~a
AM~a
WT1000
```
Set the position of the home switch as -200 and move to 1024.

```
#OSCILSU
'****Step 3 - Oscillation Setup*******
mode=2
count=0
AC~a=accel;DC~a=accel;SP~a=vel
SH~a
PA~a=-dist/2
MC~a
```
Move to half the oscialltion distance in the negative direction.

```
#OSCIL
'****Step 4 - Oscillations************
time1=TIME
SP~a=vel
SH~a;PA~a=dist/2;BG~a;
#CHECK1
JP #CHECK1, @IN[6]=0
check=_RP~a
AM~a
SH~a;PA~a=-dist/2;BG~a;AM~a
count=count+1
time=TIME-time1
'JP #HOMER, check>125
JP#OSCIL
EN
```
Move to positive and then negative positions of osciallition, recording time for total movement. There is a disabled check that we clear the limit switch. Repeat this motion forever.

The code on LET is the same except that:

1. It uses a different input for the home switch, 
1. It performs jogs instead of limited moves
1. The home switch is defined to be at 0 (not -200)
1. It does not switch on the motor before each move
1. After the home and before the setup oscialltion it does not move the motor away from the home switch position

