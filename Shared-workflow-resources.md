A place to share resources for speeding up our workflow

## make_ioc batch script

Run in an EPICS terminal.
Makes an IOCs support module and IOC module or an IOCs ISIS module.

Usages: 
For an IOC with a support and IOC module: 
- `make_ioc support_folder_name ioc_folder_name`
- `make_ioc mk3chopper MK3CHOPR`
For an IOC in the EPICS directory (will give a warning): 
- `make_ioc isis_folder_name no_ioc`
- `make_ioc Chopper_sim no_ioc`
For an IOC with only an IOC module: 
- `make_ioc no_support ioc_folder_name`
- `make_ioc no_support mk3chopper`

Found in ibex_utils/workflow_support_scripts.
To make it easy to use add the ibex_utils/workflow_support_scripts folder to your PATH.

## make_ioc_test batch script

Run in an EPICS terminal.
Relies on the make_ioc script above.
Makes an IOC and then ask the user if they want to run tests.

Found in ibex_utils/workflow_support_scripts.
To make it easy to use add the ibex_utils/workflow_support_scripts folder to your PATH.