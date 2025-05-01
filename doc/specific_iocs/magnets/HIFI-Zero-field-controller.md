# Zero field controller (HIFI)

The zero field controller on HIFI follows a similar design to [the zero field controller used on other instruments such as EMU and MuSR](Zero-field-controller), but is implemented as a separate IOC, `ZFHIFI`, due to a number of differences.

The main differences are:
- There are 6 field probes, across 2 magnetometer devices (each an instance of a Group3 hall probe, `G3HALLPR`). 
  * There is HIFI-specific field correction logic used to get a corrected field from these 6 probes
- The zero field system on HIFI uses the shim coils from the HIFI cryomag as it's outputs. These are `CRYOSMS_02`..`CRYOSMS_04`, hosted on `hifi-cryomag`


## Expected setup

The expected setup for this system is:
- `CRYOSMS` IOCs on `HIFI-CRYOMAG` for the shim coils, configured with:
  * `"CRYOMAGNET": "No"` (The shim coils should *not* be set up as a cryomagnet)
  * `"NON_PERSISTENT_SETTLETIME": 0` (To avoid excessive settle times on ZF writes)
  * `"HOLD_TIME": 0` (To avoid excessive settle times on ZF writes)
  * `"HOLD_TIME_ZERO": 0` (To avoid excessive settle times on ZF writes)
- `G3HALLPR` IOCs on `NDXHIFI` configured with:
  * `"FIELD_SCAN_RATE": "Passive"` (the zero-field system will scan these when relevant)
  * `"FLNK0": "IN:HIFI:ZFHIFI_01:MAGNETOMETER:X1:READINGS_UPDATED.PROC CA"` (and similar for `flnk1/2`)
- `ZFHIFI_01` configured with:
  * `"PSU_X": f"IN:HIFI-C11:CRYOSMS_02"` (and similar for `PSU_Y`/`PSU_Z`)
  * `"MAGNETOMETER_X1": f"IN:HIFI:G3HALLPR_01:0"`
  * `"PSU_X_MIN": -15` (and similar for `Y`&`Z`, and `MIN`/`MAX`)

The flow of control is:
- The `ZFHIFI` ioc will request the magnetometers to take readings by processing `G3HALLPR:...:TRIGGER`
- The `G3HALLPR` ioc will take a reading
- The `G3HALLPR` ioc will process the `READINGS_UPDATED` pv on the `ZFHIFI` ioc
- When all probes are ready, the zero-field ioc will calculate corrected fields
- The zero-field controller will write a new setpoint to the cryosms IOCs
- The cryosms IOCs will ramp the fields on the shim coils using it's internal state-machine
- The zero-field controller will wait for the cryosms to be "within tolerance" of the setpoint and reporting `READY` status.
