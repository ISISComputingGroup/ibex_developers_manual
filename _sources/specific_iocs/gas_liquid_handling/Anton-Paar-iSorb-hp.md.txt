# Anton-Paar iSorb HP

This is a gas adsorption system, used on WISH and also used in the Hydrogen lab.

The principle of operation is to 'dose' gas into a porous material, and measure the rate at which that gas gets adsorbed onto that material. When used on a beamline, we also want to perform neutron measurements between doses.

The iSorb has no native communication interface (despite the manufacturer having been asked for this). Our EPICS support module is implemented in an unusual way:
- There is a program running on the manufacturer PC, alongside the manufacturer software
- This program uses a combination of GUI automation and log-scraping to extract information of interest from the manufacturer software
- This information is then exposed over standard HTTP endpoints
- A usual StreamDevice IOC communicates with these HTTP endpoints

## PC and manufacturer software

The manufacturer software is called `iSorb HPwin` and runs on the equipment-specific PC associated with this system.

:::{important}
The experiment controls team does not maintain the Windows or manufacturer software installation on this PC; that is done by the equipment owners.
:::

## Local control script (`isorb.py`)

This script is software which the experiment controls group has written, and runs on the PC alongside the manufacturer software.

To run it, check out [the support module](https://github.com/isisComputingGroup/epics-isorbhp) locally on the manufacturer PC into `C:\Users\User\isorb-hp`, ensure `uv` is available, and then run:

```
cd C:\Users\User\isorb-hp
uv run isorb.py
```

This will ensure a suitable Python version is used and that dependencies are automatically downloaded.

This script is implemented using FastAPI and exposes standard HTTP endpoints on port `8000`.

## IOC & support module

The IOC and support module run on the NDX in the typical way. The IOC uses streamdevice to poll the HTTP endpoints exposed by the `isorb.py` script.

## Troubleshooting

### GUI actions (pause/resume) do not work

This relies on UI automation, via `pywinauto`. This means that it is sensitive to the state of
the manufacturer software UI. Ensure that:
- The manufacturer software is open, maximised, and in focus
- There are no additional windows 'in front' of the main UI (which shows a diagram including the manifold and various valves)

You can see stack traces by logging on to the equipment-specific PC and checking the logs emitted by the `isorb.py` script; these may give further hints about why the UI automation is failing.
