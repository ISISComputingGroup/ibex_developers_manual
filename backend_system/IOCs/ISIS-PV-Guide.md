> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > ISIS PV Guide

**This does not cover the PV naming convention, rather it covers the PVs you need to implement.**

The PV naming conventions are described on the [PV naming](PV-Naming) page.

1. For a slow changing value (e.g. a temperature), there needs to be a current value readback, a setpoint and a setpoint readback:

    ```
    record(ai, "$(P)TEMP") 
    {
        field(SCAN, "1 second")
        field(DTYP, "stream")
        field(INP,  "@devEuro.proto getCurrentTemp $(PORT)")
        field(PREC, "3")
        field(EGU,  "K")
    }
    
    record(ao, "$(P)TEMP:SP") 
    {
        field(DTYP, "stream")
        field(OUT,  "@devEuro.proto setTempSetpoint $(PORT)")
        field(PREC, "3")
        field(EGU, "K") 
    }
    
    record(ai, "$(P)TEMP:SP:RBV") 
    {
        field(SCAN, "1 second")
        field(DTYP, "stream")
        field(INP,  "@devEuro.proto getTempSetpoint $(PORT)")
        field(PREC, "3")
        field(EGU,  "K")
    }
    ```

1. For a value that changes instantly (e.g. a trigger level), there needs to be a current value readback, a setpoint and a setpoint readback. However the setpoint readback should be an alias for the readback:

    ```
    record(ai, "$(P)TRIG_LVL") 
    {
        field(SCAN, "1 second")
        field(DTYP, "stream")
        field(INP,  "@devHameg_8123.proto getTriggerLevel $(PORT)")
        field(PREC, "3")
        field(EGU,  "V")
    }
    
    record(ao, "$(P:)TRIG_LVL:SP") 
    {
        field(DTYP, "stream")
        field(OUT,  "@devHameg_8123.proto setTriggerLevel $(PORT)")
        field(PREC, "3")
        field(EGU, "V") 
    }
        
    alias("$(P)TRIG_LVL", "$(P)TRIG_LVL:SP:RBV")
    ```

1. For a toggle-style button (e.g. voltage on/off) where the current setting can be read, use the same format as 2) but with binary records:
    ```
    record(bi, "$(P)VOLTAGE_ON") 
    {
        field(SCAN, "1 second")
        field(DTYP, "stream")
        field(INP,  "@devPSU.proto getVoltageOn $(PORT)")
        field(ZNAM, "OFF")
        field(ONAM, "ON")
    }
    
    record(bo, "$(P)VOLTAGE_ON:SP") 
    {
        field(DTYP, "stream")
        field(OUT,  "@devPSU.proto setVoltageOn $(PORT)")
        field(ZNAM, "OFF")
        field(ONAM, "ON")
    }
    
    alias("$(P)VOLTAGE_ON", "$(P)VOLTAGE_ON:SP:RBV")
    ```

1. For a toggle-style button where the current setting ```cannot``` be read or a push-style button (e.g. a reset button), there needs to be a setpoint and, for convenience, an alias for the current value. This allows the value to be set using either PV.
    ```
    record(bo, "$(P)RESET:SP") 
    {
        field(DTYP, "stream")
        field(OUT,  "@devMyDevice.proto reset $(PORT)")
        field(ZNAM, "YES")
        field(ONAM, "TRUE")
    }
        
    alias("$(P)RESET:SP", "$(P)RESET") 
    ```

1. A read-only value (e.g. a status string).
    ```
    record(stringin, "$(P)STATUS") 
    {
        field(DTYP, "stream")
        field(INP,  "@devMyDevice.proto getStatus $(PORT)")
        field(SCAN, "1 second")
    }
    ```

1. For a value(s) which the user wants to review before changing then press a set button (for motor records this can be done via [SPMG](https://epics.anl.gov/bcda/synApps/motor/R6-5/motorRecord.html#Fields_command)):
    - `XXX` - read back
    - `XXX:SP` - set the value immediately
    - `XXX:SP:RBV` - the value that the device has as a setpoint
    - `XXX:SP_NO_ACTION` - don't set the value but wait (this is a temporary value if you restart the IOC it is lost, consider putting autosave on it)
    - `XXX:ACTION` - when written to with any value take the SP_NO_MOVE and send it to the device
    - `XXX:ACTION:SP` - when written to with any value take the SP_NO_MOVE and send it to the device
    - `XXX:CHANGED` - are the setpoint on device and current setpoint different? It is an enum:
        - `NO` there is no change to apply
        - `YES` there is a change to apply
