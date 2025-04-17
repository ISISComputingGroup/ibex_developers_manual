> [Wiki](Home) > [The Backend System](The-Backend-System) > [System components](System-components) > [Settings and Configurations](Settings-and-Configurations) > Calibration files

The calibration files are anything that is equipment specific but not how to drive it; they are settings which are common to all instruments. The test for whether a file belongs in this repository is as follows. Imagine changing a file on an instrument; the change should be reflected on the other instruments thus improving their results. There will be some grey areas, for instance, the barn doors on Muon Front end. It is unlikely these calibration setting will be used elsewhere but they could be, and if they were changed it wouldn't effect anything else, so this is a good place to put them. The actual calibration is done by IEUSG, who going forwards are going to be responsible for handling these files and making sure they're in the correct format. 

A prime example of this are the temperature sensors which have a calibration of current to temperature. If a mistake is found in the calibration, it should be corrected and pushed to other instruments.

These files live in a separate upstream repository at:

    https://gitlab.stfc.ac.uk/isisexperimentcontrols/common.git

This repo should be cloned with:

    git clone https://gitlab.stfc.ac.uk/isisexperimentcontrols/common.git C:\Instrument\Settings\config\common

_Note that on an instrument PC these files are located in `C:\Instrument\Settings\config\common`_

The reason these files are in a separate repository is that they have a different release cycle to the ibex backend (they can be updated mid-experiment where we wouldn't want to release a whole new experiment backend). It might be possible to place them in the configuration branch for instruments but merging them across instruments would be tricky. They need to be shared because the equipment is shared between experiments.

### Local calibration files

There is the option to use a local calibration directory instead of the common one. This is intended for calibration files which will only ever be used on the local instrument, and usually only temporarily - all other files should be added to the common repository through the calibration file controller. This is set on a per-IOC basis via macro and is currently implemented for Eurotherm and Danfysik IOCs. The directory for local calibration files is `/config/<inst name>/calib/`

## Calibration Data within the Repo

1. `temp_sensors` - temperature sensor calibration files
1. `magnets` - calibration for magnets (mostly Danfysik. Note: magnetic field unit **needs to be Gauss**)
1. `barndoors` - calibration for motors on barndoors
1. `ramps` - shared ramp files (mostly for a eurotherm)

Items **NOT** within the repository

1. `motion set points` - calibration for motion set points, e.g. sample changers. These probably do not belong in the repository (after the debate) because they will be changed on an instrument, but if this is pushed to another instrument, the offsets do not make any sense. Some motion set points might be applicable we shall wait and see.

## RhFe temperature calibration conversion

### Convert from .dab files to .txt 
There is a script designed to convert RhFe temperature sensor calibration files in .dat format.

**Note: The script skips the first 3 lines of the files as they contain metadata.**

Call with `%PYTHON3% file_converter.py -i <input_folder> -o <output_folder>`.

`-hl allows you to specify the number of header lines a temp sensor file if needs be (default is 1)`

Produces a `.txt` file for every walk-able folder under `input_folder` that contains a `.dat` file. The first 3 lines of the `.dat` file are stripped (these are header lines we do not require), for each line we then split by whitespace and take the first two of elements of the produced array and separate them with a comma. These lines are then written to an output file with the name of the folder and the txt extension e.g. `F232.txt`.

### Convert from .curve files to .txt

There is a script designed to convert RhFe temperature sensor calibration files in .curve format.

**Note: The script skips the first 6 lines of the files as they contain metadata and creates a header in ISIS calibration file format (see below).**

Produces a `.txt` file for every walk-able folder under `input_folder` that contains a `.curve` file. The first 6 lines of the `.curve` file are stripped (these are header lines we do not require), a header block in ISIS calibration file format is generated and for each line we then split by whitespace and take the first two of elements of the produced array and separate them with a comma. These lines are then written to an output file with the name of the folder and the txt extension e.g. `F232.txt`.

Scripts are available at https://github.com/ISISComputingGroup/ibex_utils/tree/master/workflow_support_scripts.

**Note: Ensure that metadata of the new calibration files match with the format of the script you are using before running it. If not, the script may need adjusting to cope with different file formats.**

You will then need to push these files to the common config area and update the files on the instruments using the section below.

## Updating Calibration File on Instruments

If the common calibration file change and they need updating on all instruments, then you can run the [calibration update script which can be found in ibex utils](https://github.com/ISISComputingGroup/ibex_utils/blob/master/installation_and_upgrade/calibration_files_updater.py)

To update those instruments still on SECI use the folder `...\CompGroup\Calibration Files`:

1. Update files in `Calibration Files\Temperature Sensors\Files`
1. Run the deployment script in `Calibration Files\Temperature Sensors\Deployment Scripts`. 
    - There should be 1 error per instrument for deleting the network path

## Calibration file format

1. First lines start with `# ISIS calibration`.
1. Header block which is a JSON dictionary with `#` before each line. Dictionary entries are:
    - `sensor_type`: a string of the sensor type
    - `format_version`: a string of the format number, can be a float. For this version must be 1.
    - `conversion_date`: date for conversion as a string in `YYYY/MM/DD`.
    - `column1_name`: (String) name of the first column.
    - `column1_units`: (String) units of the first column [should match epics units conventions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/PV-Units-&-Standards#unit-standards)
    - `column2_name`: (String) name of the second column
    - `column2_units`: (String) name of the second column [should match epics units conventions](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/PV-Units-&-Standards#unit-standards)
1. Tables of data in two columns separated by a comma
    - The first column comprises floats representing temperature.
    - The second column comprises floats representing reading from the sensor.

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

As part of the implementation, it was decided in a discussion between John and Tom that the JSON namespace should be a flat dictionary. The advantage of using this approach is that the same script can extract any arbitrary metadata from the file, by providing the key to the dictionary.

### Lakeshore

Examples of the lakeshore format can be found on the [lakeshore site](https://www.lakeshore.com/resources/product-information).

### Out of range in the calibration file

If you above or below the maximum or minimum values in the calibration file, IBEX will interpolate beyond or below these values. Please be sure that you have selected the correct calibration file for your sensor and the sensor range. Readings beyond the calibration range may not be as accurate as those within.

The Eurotherm OPI alerts the user when you are above or below the maximum or minimum values in the calibration file. This is achieved using an IOC utility.
