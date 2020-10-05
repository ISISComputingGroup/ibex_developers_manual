> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Other](Other) > [Background Script IOC](Background-Script-IOC)

The background script IOC will run a script in the background. The script must be in python3 and be called `background_script.py` and be in the python configuration directory. For the second background ioc the script must be called `background_script2.py`.

If you want the IOC to register as started the user must include the lines:

```python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.environ["KIT_ROOT"], "ISIS", "inst_servers", "master")))

from server_common.helpers import register_ioc_start

register_ioc_start("BGRSCRPT_01")
```

### Background Plot

A popular use of this is to generate a [background plot](https://github.com/ISISNeutronMuon/InstrumentScripts/wiki/Muon). This can be using the script:

```python
import sys
import os
from time import sleep

sys.path.insert(0, os.path.abspath(os.path.join(r"C:\\", "Instrument", "scripts")))
sys.path.insert(1, os.path.abspath(os.path.join(os.environ["KIT_ROOT"], "ISIS", "inst_servers", "master")))

from technique.muon.background_plot import BackgroundBlockPlot
from genie_python import genie as g
from server_common.helpers import register_ioc_start


register_ioc_start("BGRSCRPT_01")

g.set_instrument(None)

plot=BackgroundBlockPlot((("Temp_Sample", "value"), ("Temp_SP", "set point")), "Temperature").start()

while True:
    sleep(10)
```

In addition to this to show the plot add the following to the instrument init:

```python
def init(inst):
    g.adv.open_plot_window(is_primary=False)
```

#### Background restart of an IOC if it crashes and doesn't recover

A script has been put on EMU for if an IOC goes into a severe alarm state (`INVALID`) and fails to reconnect to the hardware. The script is responsible for restarting the IOC if this happens and checking that the IOC has come back online and is no longer in an alarm state. 
This script is also now available in the instrument scripts repository. 