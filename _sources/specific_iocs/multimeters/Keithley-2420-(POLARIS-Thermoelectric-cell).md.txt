# Keithley 2420 (Polaris Thermoelectric cell)

Polaris occasionally use a Keithley to do a thermoelectric cell measurement. Originally this was from https://github.com/ISISComputingGroup/IBEX/issues/2801

Currently, doing this measurement requires a few hacks to get it going. These are documented below:

## Keithley setup

- Keithley needs to have it's current source range set high enough.
  * Source -> I -> Right arrow -> range up (until desired range is displayed)
- It is helpful to connect a test resistor to the Keithley to get sensible values back

## IOC setup

- Currently the Keithley IOC sends some commands at initialization that cause problems for this measurement, so need to remove/comment out `PINI` and `SCAN` fields in the DB
- The `MEAS` command in the protocol is a generic measure command - to force it to use a particular mode, the `get_V` and `get_R` commands will need to be changed to match the following:
   - The Keithley 2400 IOC has implemented this protocol
```
# /// Read the voltage from the data string. Format is %g (V), %g (I), %g (R), %g (Timestamp), %g (Status)
get_V {
   ExtraInput = Ignore;
   out ":MEAS:VOLT?";
   in "%f,%*f,%*f";
}

# /// Read the current from the data string. Format is %g (V), %g (I), %g (R), %g (Timestamp), %g (Status)
get_I {
   ExtraInput = Ignore;
   out ":MEAS:CURR?";
   in "%*f,%f,%*f";
}

# /// Read the resistance from the data string. Format is %g (V), %g (I), %g (R), %g (Timestamp), %g (Status)
get_R {
   ExtraInput = Ignore;
   out ":MEAS:RES?";
   in "%*g,%*g,%g";
}
```


## Blocks

The following blocks need to be set up:

`keithley2420_resistance_2` -> `TE:NDWxxxx:PARS:USER:R2`

`keithley2420_resistance_1` -> `TE:NDWxxxx:PARS:USER:R1`

`keithley2420_voltage` -> `TE:NDWxxxx:PARS:USER:R0`

Set up precisions and units:
```
caput %MYPVPREFIX%PARS:USER:R2.PREC 5
caput %MYPVPREFIX%PARS:USER:R1.PREC 5
caput %MYPVPREFIX%PARS:USER:R0.PREC 5

caput %MYPVPREFIX%PARS:USER:R2.EGU ohm
caput %MYPVPREFIX%PARS:USER:R1.EGU ohm
caput %MYPVPREFIX%PARS:USER:R0.EGU volt
```

## Script

The following script was run to push values from the IOC into blocks. Save into instrument scripts directory.

For the next experiment, they would like the thermoelectric cell to run intermittently. It should be left in voltage mode when not in use. The following modifications need to be made to the script below to allow this measurement to run:
- In `__exit__`, set the measurement mode back to voltage.
- Show the instrument scientists how to wrap certain parts of their script using this context manager.

```
from time import sleep
from threading import Thread

from genie_python import genie as g


IOC = "KHLY2400_01"

SCANNING_PVS = [
    "_READ_OUTPUT",
    "_READ_MODES",
]


def _get_voltage():
    """
    Gets the voltage for a record that has had it's scanning disabled.
    :param wait: How long to wait between processing the record and getting the value.
    :return: The voltage (volts)
    """

    g.set_pv("{}:V:RAW.PROC".format(IOC), 1, is_local=True)
    sleep(1)

    result = g.get_pv("{}:V:RAW".format(IOC), is_local=True)

    if result is None:
        raise IOError("Couldn't get voltage. Check the IOC is running ({})".format(IOC))

    return float(result)


def _get_resistance():
    """
    Gets the resistance for a record that has had it's scanning disabled.
    :return: The resistance (ohms)
    """

    g.set_pv("{}:R:RAW.PROC".format(IOC), 1, is_local=True)
    sleep(1)

    result = g.get_pv("{}:R:RAW".format(IOC), is_local=True)

    if result is None:
        raise IOError("Couldn't get resistance. Check the IOC is running ({})".format(IOC))

    return float(result)


class ScanRates(object):
    """
    Enum representing scan rates. Values should match index defined in
    http://www.aps.anl.gov/epics/base/R3-14/12-docs/AppDevGuide/node18.html
    """
    PASSIVE = 0
    EVENT = 1
    IO_INTERRUPT = 2
    TEN_SECONDS = 3
    FIVE_SECONDS = 4
    TWO_SECONDS = 5
    ONE_SECOND = 6
    POINT_FIVE_SECONDS = 7
    POINT_TWO_SECONDS = 8
    POINT_ONE_SECONDS = 9


def _set_scan_rate(scan_rate):
    """
    Switches scan rate on all PVs listed in {SCANNING_PVS}

    :param scan_rate: the new scan rate to set, should be one of {ScanRates}
    """
    for pv in SCANNING_PVS:
        # 0 = Passive. Don't set by name as that change may not be on instruments yet.
        g.set_pv("{}:{}.SCAN".format(IOC, pv), scan_rate, is_local=True)


class KeithleySourceModes(object):
    """
    Measurement modes that can be set on the keithley.

    Values should match up with what is in the DB (see C:\Instrument\Apps\EPICS\ioc\master\KHLY2400\db\KHLY2400.db)
    """
    CURRENT = 0
    VOLTAGE = 1


def _set_mode(mode):
    """
    Set the measurement mode of the keithley.
    :param mode: measurement mode to set, should be one of {KeithleySourceModes}.
    """
    g.set_pv("{}:SOURCE:MODE:SP".format(IOC), mode, is_local=True)


def _set_current(current):
    """
    Set a current (A) on the keithley
    :param current:
    """
    g.set_pv("{}:WRITE:SP".format(IOC), ":SOUR:CURR:LEV {:.9f}".format(current), is_local=True)


def experiment(loop_condition, currents, measurement_delay):
    """
    Main measurement loop
    :param loop_condition: A function that should return True when this method should keep looping,
                           and False to stop looping.
    :param currents: Tuple of currents (in Amps) at which to take measurements. For each element in the tuple a block
                     is expected with name "keithley2420_resistance_<index>", where <index> is the 1-based index of the
                     element in the tuple.
    :param measurement_delay: A time delay in seconds between setting the current and taking a measurement
    """

    g.set_pv("{}:RES:MODE:SP".format(IOC), 0, is_local=True)

    while loop_condition():
        print("looping")
        _set_mode(KeithleySourceModes.CURRENT)
        g.set_pv("{}:OUTPUT:MODE:SP".format(IOC), 1, is_local=True)
        sleep(0.1)
        _set_current(0)
        sleep(measurement_delay)
        voltage = _get_voltage()
        g.cset("keithley2420_voltage", voltage)

        for index, current in enumerate(currents, 1):
            _set_current(current)
            sleep(measurement_delay)
            resistance = _get_resistance()
            g.cset("keithley2420_resistance_{}".format(index), resistance)

    g.set_pv("{}:OUTPUT:MODE:SP".format(IOC), 0, is_local=True)
    _set_current(0)
    _set_mode(KeithleySourceModes.VOLTAGE)


class ThermoElectricCell(object):
    """
    Context manager for the thermo electric cell.

    Starts a background thread running the thermoelectric cell measurement loop.
    On exiting the context, terminates the thread.
    """
    def __init__(self, current1=30/1000., current2=-30/1000., measurement_delay=1):
        """
        Constructor
        :param current1: The first current to measure (in Amps)
        :param current2: The second current to measure (in Amps)
        :param measurement_delay: A time delay in seconds between setting the current and taking a measurement
        """
        self.keep_looping = True
        self.thread = Thread(target=experiment,
                             args=(lambda: self.keep_looping, (current1, current2), measurement_delay))

    def __enter__(self):
        """
        Run when entering the context manager. Disables scanning and starts the background thread.
        """
        print("Starting thermoelectric cell measurement loop...")
        _set_scan_rate(ScanRates.PASSIVE)  # Disable scanning.
        self.thread.start()
        print("... Done")

    def __exit__(self, *args, **kwargs):
        """
        Run when exiting the context manager. Re-enables scanninng and stops the background thread.
        :return: False (don't swallow exceptions)
        """
        print("Stopping thermoelectric cell measurement loop...")
        self.keep_looping = False
        self.thread.join()
        print("... Done")
        return False

```

It is run either as a context manager around an existing script:

```
with inst.ThermoElectricCell(current1=0.01, current2=-0.01):
    do_existing_script
```

Or, alternatively, in the background using a context manager around an infinite statement:

```
with ThermoElectricCell(current1=0.01, current2=-0.01):
    raw_input("Press return to stop thermo electric cell")
```