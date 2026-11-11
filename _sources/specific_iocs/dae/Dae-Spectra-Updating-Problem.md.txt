# Dae Spectra Updating Problem

There has been a long running problem with spectra stopping updating after a certain amount of time 
[issue 2750](https://github.com/ISISComputingGroup/IBEX/issues/2750) this has not been reproducible on developer test machines, the only clue came recently when the related detector diagnostics display stopped and reported a message that looked a bit like thread termination. The proposed solution has been to add additional exception handling on the assumption that a windows structured exception rather than a C++ std::exception is the cause. To handle these non-C++ exceptions, the following has been done:

1. Compiling with `/EHa` which allows catch(...) to handle Structured Exceptions 
2. Registering a structured exception handler to convert Structured Exceptions into C++ exceptions

In theory (2) is all that is needed, but the handler needs to be installed on a per thread basis so just to be extra safe (1) has been implemented too  