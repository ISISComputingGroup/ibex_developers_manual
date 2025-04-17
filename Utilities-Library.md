The `utilities` support module contains some C/C++ functions useful to IOC and support module developers

## putDbAndWait

This is based on `dbtpn` from the epics base `dbNotify.c`. It allows setting a PV from within C/C++ and waiting for a completion callback, if you do not need such a callback then using `dbNameToAddr` and `dbPutField` is sufficient.
```
putDbAndWait(const std::string& pvName, const void *value, double timeout)
```
`value` is interpreted as appropriate for the data type of `pvName`
  