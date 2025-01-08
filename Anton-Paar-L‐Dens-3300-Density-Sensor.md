- This device has no commands and asynchronously sends readings.
- Which readings it sends depends on which application is loaded onto the device, at ISIS we use the `Live Raw Data` application at the moment with room to expand, meaning it is safe to assume the device will send data in the following format `T= 24.74 <°C> D= 0.8 <kg/m³><\r><\n>`; a temperature of the fluid and the density of the fluid in degrees Celsius and kilograms per metre cubed respectively.
- If a different application is loaded then the temperature and density PVs sit in `INVALID` alarm. 
- To account for the device's asynchronous behaviour we use I/O interrupt AI records which trigger when the input it is pointing to changes.
- If 10 seconds pass and no messages are received in the expected format then the temperature and density PVs go into `INVALID` alarm. 

The IOC to facilitate use of this was implemented under https://github.com/ISISComputingGroup/IBEX/issues/8413.

Baud = 9600

Data = 8

Parity = None

Stop = 1

The manual can be found at `\\ISIS\Shares\ISIS_Experiment_Controls\Manuals\AntonParr_L-Dens3300`. (With the operator and admin pass codes on page 16)