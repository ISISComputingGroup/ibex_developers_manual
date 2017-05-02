> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Barndoors and momentum slits on MUON Front End

Muon front end is feeding three instruments. It controls the moment and number of neutrons to the experiments. Momentum is controller by a single momentum slit device connected to a Galil. The exposure for each of the three instruments are controlled separately by 3 barndoors. 

## Momentum Slits

The momentum slits are controlled by giving a distance between the slits to a PV. This then converts this to a distance to feed into the motor record. The distance sent to the motor is exactly half the distance from the PV. The setting for the motor are created from the lab view settings (created during commissioning). This is converted using Gareth's utility. 

| PV  | Description |
| --- | ------------|
| \<Instrument>MSLITS | Momentum slit motor record, set to gap wanted, for block readback use .RBV field |
| \<Instrument>$(MTR) | Underlying motor record, set as a macro in the st.cmd file |

## Barndoors

Barndoors can be opened different distances. The distance is no linearly connected to the voltage of the feedback from the motor. The aim is to provide 3 pvs which can be set the distance the barn doors should be opened by. The conversion is given in the conversion file. The file contains three columns Voltage EMU, MUSR and HIFI. A similar conversion is done in Eurotherm and Danfysik. We also need a readback PV. There is currently some Galil code to control the value but using a straight motor record might be better, if it can be made to work.

| PV  | Description |
| --- | ------------|
| \<Instrument>$(INST)BARNDOORS | Barndoors motor record for the instrument $INST. Set to gap wanted |
| \<Instrument>$(INST)$(MTR) | Underlying motor record for instrument $INST, set as a macro in the st.cmd file |

## Setup

The barndoors and momentum slits are part of the galil motor set up and are per instrument. There is an example at `...\EPICS\support\motorExtensions\master\settings\barndoors\*.cmd` copt this to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`
