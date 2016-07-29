## Ibex-Gui build failure

### Lack of randomness?

Build stops with:
    
    Failed to execute goal org.eclipse.tycho:tycho-surefire-plugin:0.20.0:test (default-test) on project uk.ac.stfc.isis.ibex.targets.tests: An unexpected error occured (return code 13). See log for details. -> [Help 1]

In log file 

    java.lang.InternalError: Unexpected CryptoAPI failure generating seed

This might be caused by not enough randomness in the system (not sure). It went away once I logged into the server (which appeared to be new) and re-ran the build.