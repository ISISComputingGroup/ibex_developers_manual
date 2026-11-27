# Delft Furnace

## Usually used on LARMOR, but has been seen on ZOOM

This is a bespoke 19" crate containing a Eurotherm, which is the only part of the equipment IBEX talks to.  The Eurotherm communicates via **MODBUS**, otherwise the settings/macros are the same as any other unit.  In this particular case: 9600 baud, 8 data bits, No parity, 1 stop bit (AKA 9600-8-N-1).

There are other scaling factor macros that must be set in `globals.txt` as they're not present in the GUI.  These are: `P_scaling_X`, `I_scaling_X`, `D_scaling_X` and `Output_scaling_X`, where `X` is the sensor number.  Typical values are 0.0001, 0.1, 1, 0.1 respectively.

The crate has a rear-mounted flying-lead with male 9-pin 'D-type' serial connector, rather than a conventional panel-mounted socket.  This needs a female MOXA lead (_without_ null modem) to connect to a MOXA NPort.
 
### Troubleshooting (besides general advice)

- Check Eurotherm macro values in client and in `globals.txt` file
- Check communications settings in physical Eurotherm unit are as expected. i.e. protocol: **MODBUS**; serial: **9600-8-N-1**
- More information on Eurotherm macros and communications settings [here](/specific_iocs/temp_controllers/Eurotherm).
