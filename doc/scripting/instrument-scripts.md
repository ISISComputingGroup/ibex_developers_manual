# Shared Instrument Scripts

The general instrument scripts are in this [repository](https://github.com/ISISNeutronMuon/InstrumentScripts). These scripts include:
- The ['old' scans library](https://pygenie-scans.readthedocs.io/en/latest/index.html); as of October 2025, this is used by SANS instruments and reflectometers, but is being gradually replaced by {doc}`Bluesky-based scans <Bluesky-scanning>`
- A shared SANS scripting framework. Contains definitions of `do_sans` and `do_trans`
- Shared utilities for Muon beamlines, for example including:
  * Background plot configuration (using {doc}`/specific_iocs/other/Background-Script-IOC` and {doc}`Matplotlib`)
  * {doc}`Zero-field system </specific_iocs/magnets/Zero-field-controller>` calibration routines
  * {doc}`DAE pre & post commands </specific_iocs/dae/DAE-Pre-and-Post-commands>`
