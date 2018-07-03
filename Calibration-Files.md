> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [Configurations](Configurations) > Calibration files

The calibration files are anything that are equipment specific but not how to drive it, they are settings which are common to all instruments. The test for whether a file belongs in this repository is as follows. Imagine changing a file on an instrument; the change should be reflected to the other instruments thus improving their results. There will be some grey areas for instance the barn doors on Muon Front end. It is unlikely these calibration setting will be used elsewhere but they could be, and if they were changed it wouldn't effect anything else so this is a good place to put them.

A prime example of this are the temperature sensors which have a calibration of current to temperature. If a mistake is found in the calibration it should be corrected and pushed to other instruments.

These files live in a separate repository at:

    http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git

This repo should be cloned with:

    git clone http://control-svcs.isis.cclrc.ac.uk/gitroot/instconfigs/common.git C:\Instrument\Settings\config\common

The reason these files are in a separate repository is that they have a different release cycle to the ibex backend (they can be updated mid experiment where we wouldn't want to release a whole new experiment backend). It might be possible to place them in the configuration branch for instruments but merging them across instruments would be tricky. They need to be shared because equipment is shared between experiments.

## Calibration Data within the Repo

1. `temp_sensors` - temperature sensor calibration files
1. `magnets` - calibration for magnets (mostly Danfysik)
1. `barndoors` - calibration for motors on barndoors
1. `ramps` - shared ramp files (mostly for a eurotherm)

Items **NOT** within the repository

1. `motion set points` - calibration for motion set points e.g. sample changers. These probably do not belong in the repository (after debate) because they will be changed on an instrument but if this is pushed to another instrument the offsets do not make any sense. Some motion set points might be applicable we shall wait and see.

## Updating Calibration File on Instruments

If the common calibration file change and they need updating on all instruments then you can run the [calibration update script which can be found in ibex utils](https://github.com/ISISComputingGroup/ibex_utils/blob/master/installation_and_upgrade/calibration_files_updater.py)

## Calibration file format

1. First lines starts with `# ISIS calibration`
1. Header block which is a JSON dictionary with `#` before each line. Dictionary entries are:
    - `sensor_type`: string of the sensor type
    - `format_version`: string of the format number, can be float. For this version must be 1.
    - `conversion_date`: date for conversion as string in `YYYY/MM/DD`
    - `column1_name`: (String) name of the first column
    - `column1_units`: (String) units of the first column [should match epics units conventions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/PV-Units-&-Standards#unit-standards)
    - `column2_name`: (String) name of the second column
    - `column2_units`: (String) name of the second column [should match epics units conventions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/PV-Units-&-Standards#unit-standards)
1. Tables of data in two columns separated by a comma
    - First column is floats representing temperature
    - Second column is floats representing reading from sensor

### Examples

To set units to `C`:
```
# ISIS calibration
# {
#    "sensor_type": "K-type",
#    "format_version": "1",
#    "conversion_date": "2018/06/07",
#    "column1_name": "Temperature",
#    "column1_units": "C",
#    "column2_name": "Voltage",
#    "column2_units": "mV"
# }
1.20927230303971000000,1.50736314598516000000
1.29965829974167000000,1.52132663750615000000
1.40140216241767000000,1.53731669735489000000
1.59677148943797000000,1.56816244669350000000
```

To set units to `K`:
```
# ISIS calibration
# {
#    "sensor_type": "K-type",
#    "format_version": "1",
#    "conversion_date": "2018/06/07",
#    "column1_name": "Temperature",
#    "column1_units": "K",
#    "column2_name": "Voltage",
#    "column2_units": "mV"
# }
1.20927230303971000000,1.50736314598516000000
1.29965829974167000000,1.52132663750615000000
1.40140216241767000000,1.53731669735489000000
1.59677148943797000000,1.56816244669350000000
```

There is a set of DB records in DB area of ReadAscii that will push any metadata from the file into an epics record. This script has a configurable property name (so you can extract any metadata property from the file) and a configurable default (if the metadata didn't exist or wasn't valid).

Call it using lines similar to the following in the `st.cmd`

```
dbLoadRecords("$(ReadASCII)/db/get_metadata.db","DIR=$(P)TEMP,CAL=$(P)CAL:RBV,OUT=$(P)TEMP,OUTF=EGU,NAME=column1_units,DEFAULT=K")
dbLoadRecords("$(ReadASCII)/db/get_metadata.db","DIR=$(P)TEMP,CAL=$(P)CAL:RBV,OUT=$(P)TEMP:SP,OUTF=EGU,NAME=column1_units,DEFAULT=K")
dbLoadRecords("$(ReadASCII)/db/get_metadata.db","DIR=$(P)TEMP,CAL=$(P)CAL:RBV,OUT=$(P)TEMP:SP:RBV,OUTF=EGU,NAME=column1_units,DEFAULT=K")
```

### Justification for ISIS format

Freddie, Kathryn, John, Kevin and Tom had a meeting to discuss calibration formats. The meeting decided the following:
- Files will be a two-column format to facilitate using the existing epics `cvt` record
- Any metadata will be stored in a commented block at the top of the file (the comment delimiter is `#`)
- The files will start with some identifiable magic bytes. I have chosen `# ISIS calibration`
- Metadata will be stored as a JSON structure
- The metadata will allow the following core information to be stored
  * Sensor type so that we know what the sensor plugged in should be
  * Conversion date so that conversion errors can be traced
  * File format version so that we can change the format later
  * Name and units of each column so that we know what the data represents
  * Any arbitrary metadata should be able to be added later

As part of implementation, it was decided in a discussion between John and Tom that the JSON namespace should be a flat dictionary. The advantage of using this approach is that the same script can extract any arbitrary metadata from the file, by providing the key to the dictionary.

### Lakeshore

Examples of the lakeshore format can be found on the [lakeshore site](https://www.lakeshore.com/Documents/ZipReadme.pdf).

