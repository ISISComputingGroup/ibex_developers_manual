> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [TPGx00](TPGx00)

## TPGx00
TPGx00 is shorthand for the TPG300 and the TPG500 Pfeiffer Vaccuum Gauges which use the same `TPG300` IOC, which controls a series of four pressure sensors (A1, A2, A3, A4). 

**To configure the IOC for the 500, define the MODEL macro: it defaults to TPG300**

These devices are similar to the [TPG26x](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TPG26x) and [TPG36x](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TPG36x), but have 4 pressure sensors to read from, and a slightly more complicated IOC. All their manuals can be found in `<share>\ISIS_Experiment_Controls\Manuals\Pfeiffer TPG<xxx>`.

## Differences between the 300 and 500
The TPG500 is the slightly newer version of the TPG300; the main differences between these two devices is in their communication protocols. See the manuals for what these properties are used for. 

|  | 300                   | 500                                                  | Affected commands |
| ---- | --------------------- | ---------------------------------------------------- | ---- |
| Switching Functions | `1, 2, 3, 4, A, B` | `1, 2, 3, 4` | SPx |
| Switching Function assignments | `No Assignment, A1, A2, B1, B1, A1 self-monitoring, A2 self-monitoring, B1 self-monitoring, B1 self-monitoring` | `Off, A1, A2, B1, B2, On` | SPx |
| Units    | `mbar, Torr, Pa` | `hPascal, mbar, Torr, Pa, Micron, Volt, Ampere` | UNI/UNIx |

## Commands
The IOC currently supports the use following commands with the TPGx00 devices:
| Command | Description                   |
| ------- | ----------------------------- |
| **`Pxx`**, where xx is `A1\|A2\|A3\|A4` | Gets the pressure measurement from the specified channel |
| **`ERR`** | Get the error status of the device |
| **`SPS`** | Get the statuses of all the switching functions |
| **`SPx`**, where x is `1\|2\|3\|4` (+ `A\|B` for 300) | Get/set the threshold settings for a specified switching function |
| **`UNI`** | Get the unit of measurement |
| **`UNIx`**, where x is `1\|2\|3` (+ `0\|4\|5\|6` for 500) | Set the current unit of measurement |
