> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > [Background Script IOC](Background-Script-IOC)

The background script IOC will run a script in the background. The script must be in python3 and be called `background_script.py` and be in the python configuration directory. For the second background ioc the script must be called `background_script2.py`.

If you want the IOC to register as started the user must include the lines:

```
sys.path.insert(0, 'C:\\Instrument\\Apps\\EPICS\\ISIS\\inst_servers\\master\\')

from server_common.ioc_data_source import IocDataSource
from server_common.mysql_abstraction_layer import SQLAbstraction

ioc_data_source = IocDataSource(SQLAbstraction("iocdb", "iocdb", "$iocdb"))
ioc_data_source.insert_ioc_start(ioc_name, os.getpid(), exepath, STATIC_PV_DATABASE, ioc_name_with_pv_prefix)
```
