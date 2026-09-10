# Muon Front end slits

The Muon front end feeds three instruments (MUSR,EMU and HIFI). It controls the moment and number of neutrons to the experiments.  Momentum is controlled by a single momentum slit device connected to a Galil motor controller.  The exposure for each of the three instruments is controlled separately by 3 barndoor-type slits, also each connected to a Galil.

## Momentum Slits

The momentum slits are controlled by giving a distance between the slits to a PV. This then converts this to a distance to feed into the motor record. The distance sent to the motor is exactly half the distance from the PV. The setting for the motor are created from the lab view settings (created during commissioning). This is converted using Gareth's utility. 

| PV  | Description |
| --- | ------------|
| \<Instrument>MSLITS | Momentum slit motor record, set to gap wanted, for block readback use .RBV field |
| \<Instrument>$(MTR) | Underlying motor record, set as a macro in the st.cmd file |

## Barndoors

Barndoors can be opened to different distances. The distance is no linearly connected to the voltage of the feedback from the motor. The aim is to provide 3 pvs which can be set the distance the barn doors should be opened by. The conversion is given in the conversion file. The file contains three columns Voltage EMU, MUSR and HIFI. A similar conversion is done in Eurotherm and Danfysik. We also need a readback PV. There is currently some Galil code to control the value but using a straight motor record might be better, if it can be made to work.

| PV  | Description |
| --- | ------------|
| `\<Instrument>$(INST)BARNDOORS` | Barndoors motor record for the instrument $INST. Set to gap wanted |
| `\<Instrument>$(INST)$(MTR)` | Underlying motor record for instrument $INST, set as a macro in the st.cmd file |

## Setup

The barndoors and momentum slits are part of the galil motor set up and are per instrument. There is an example at `...\EPICS\support\motorExtensions\master\settings\barndoors\*.cmd` copy this to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`

Remember to add an address to the IOC in the IBEX GUI for the Galil IOC. If you're testing locally you still need to set it but it can just be `127.0.0.1`

## Alternative move command

This was done particularly for the muon barndoors. They do not move the "motor" by sending pulses from the
galil, rather there is a program running in the galil that changes the bias voltage and then readback is done
via a galil analogue output line. To allow control of this via the galil, it is now possible to change the command
used by the galil for setting the motor - this is done using a PV like  $(P)MOTMTR0101_MOVE_CMD   and a %f within this
string will be replaced with the requested position. A real galil would have this internally doing something like "PRA=%f" for "position relative axis A" - this can bet set to any valid galil command sequence.  

This means that the motors on MUONFE are disabled by design - a raw galil command is sent to the galil controller by LabVIEW VIs on each of EMU, MUSR, HIFI. For IBEX instruments this means they use an LVDCOM wrapper, which is the `MUONJAWS` ioc.
  