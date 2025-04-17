## Register SELOGCOM in COM+
The steps here are only required on a SECI instrument that needs an updated ISISICP, or an IBEX instrument that may revert back to SECI at some stage
 
Open GENIE is a 32bit program, the ISISICP is 64 bit, and a DCOM component called SELOGCOM is used by SECI and Open GENIE to log values. This component is no longer built in 32bit format, SECI already uses the 64bit version (built as part of isisicp) but a workaround is needed for Open GENIE.

Many DCOM components are run in-process and need to be of the correct architecture, however if a DLL component is registered with COM+ it will automatically be run out of process using `dllhost.exe` and so be callable by any architecture.

## Registering SELOGCOM with COM+
   
* create a CMD windows with admin privileges
* type `dcomcnfg`
* select `component service` -> `computers` -> `my computer`
* open COMP+ Applications and confirm SELOGCOM is not already there
* right click on `com+ applications`, select `new application` and  `create empty application`
* when prompted, chose `server application`, name it  `SELOGCOM` and accept the remaining default answers.
* right click on `selogcom` in COM+ applications, in `properties`, `security tab` uncheck/disable "enforce access checks for this application"
* open up the `selogcom` tree in explorer, right click on `components` and select  `new component` then  `install new component`, browse to `C:\labview modules\DAE\service\x64\Release\selogcom.tlb`
