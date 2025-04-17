> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Motor IOCs](Motor-IOCs) > [Galil](Galil) > [Galil userdef records](Galil-Userdef-Records)

the `galil_userdef_records.template` file in support/galil provides a mechanism to associate EPICS ai/ao records with a variable in the galil, the epics PV name and galil variable name can be specified as macros when the template is loaded.

The `galil_userdef_records8.template` file in support/galil is created from this via a substitutions file from this, it define 8 records each setting the variable name specified as per `galil_userdef_records.template` but additionally adding A-H to the end of the variable name. This allows the mechanism to be used for setting some of the galil ceramic parameters, as the syntax is the same as setting a general galil variable.

For an example see `galil_userdef_records8.substitutions` in the `ioc/GALIL-IOC-01App/Db`. Here you will see a line defining a `K1` parameter, this will then use `galil_userdef_records8.template` to create 8 records accessing `K1A` to `K1H`. Add any new parameters to the end of this file. The SCAN (for monitor) and PINI (for sets) are also specified here.

This mechanism is useful for values that need to be set at startup and not sent again unless changed. It is more flexible than the PREM field in that is is very easy to change individual values via channel access, autosave them, and archive/monitor them if necessary. If you need a value sent every move though them PREM is the place to do it.
  
   

   