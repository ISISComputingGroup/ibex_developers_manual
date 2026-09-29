# Technix

## Description 

Technix PSU is a High Voltage Power Supply for the separators on the RIKEN front-end. The analog board executes the instructions and confirms to the user the instruction has been executed by forwarding back to the user the same instruction wave form which was sent. 

Eg. Instruction --> `P7,1` Answer --> `P7,1`.

## Command Set


| Title | Command | Description |
| ---  | ---  | --- |
| OUTPUT VOLTAGE PROGRAMMING     | `d1,X` ( X E [0 ;4095]) | Sets the voltage. |
| OUTPUT CURRENT PROGRAMMING     | `d2,X` ( X E [0 ;4095])  | Sets the current. |
| OUTPUT VOLTAGE MONITOR     | `a1`  | Gets the voltage. |
| OUTPUT CURRENT MONITOR     | `a2`  | Gets the current. |
| HV ON     | `P5,1` --> (delay 100 ms) `P5,0`  | Sets HV ON. |
| HV OF     | `P6,1` --> (delay 100 ms) `P6,0`  | Sets HV OFF. |
| LOCAL/REMOTE MODE     | LOCAL:`P7,1` REMOTE:`P7,0`  | Sets local/remote mode. |
| INHIBIT     | ACTIVE:`P8,1` IDLE:`P8,0`  | Sets inhibit mode. |
| MAINS INFORMATION     | `F`  | Gets mains information. (F001 mains correct/ F000 mains defective) |
| IMAGE OF THE POWER SUPPLY LOGICAL STATUS     | `E`  | Gets the status of the device. |

## Image of the power supply logical reading 

The answer is 8 bit coded.

Status bits information:

* PL1 = 1 voltage regulation 
* PL1 = 0 current regulation 
* PL2 = 1 fault 
* PL2 = 0 No fault 
* PL3 = 1 open interlock 
* PL3 = 0 closed interlock 
* PL4 = 1 Hv-On status 
* PL4 = 0 Hv-Off status 

PL5, PL6, PL7, PL8 are input bits corresponding to P5, P6, P7 and P8 instructions ( image of output logical instructions) 

## Use and safety

As some of internal parameters are configured by the H.V. generator, we advise: 
1. Firstly you have to switch on the High Voltage Power Supply by using the front panel. 
1. Secondly you have to send an « HV off » RS 232 instruction (P6,1 followed by P6,0). 
So supplied and programmed, it becomes possible to initialize communication to the computer following 
the different instructions listed previously. 

**WARNING**:
_According to safety rules, a 5 seconds watchdog device is initialized after each instruction. Therefore, if the generator does not receive any instruction at least every five seconds, it will be automatically stopped and switched in local mode._

## Device Manual

 \\\isis\shares\ISIS_Experiment_Controls\Manuals\Technix power supply

## Troubleshooting

### Cannot turn on Power supply despite interlocks being clear

Try switching to local mode, waiting a bit, then remote mode, wait a bit, and finally re-attempt to turn on the HV.

Note: attempting to do this automatically via the protocol file did not work during hardware testing. Testing on the hardware is required if this is re-attempted.
