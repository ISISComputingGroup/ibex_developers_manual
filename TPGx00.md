> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [TPGx00](TPGx00)

## TPGx00
TPGx00 is shorthand for the TPG300 and the TPG500 Pfeiffer Vaccuum Gauges which use the same `TPG300` IOC; an IOC which controls a series of four pressure sensors (A1, A2, A3, A4). 

**To configure the IOC for the 500, define the MODEL macro: it defaults to TPG300**

These devices are similar to the [TPG26x](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TPG26x) and [TPG36x](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TPG36x), but have 4 pressure sensors to read from, and have a slightly more complicated IOC. All their manuals can be found in `<share>\ISIS_Experiment_Controls\Manuals\Pfeiffer TPG<xxx>`.

## Differences between the 300 and 500
The TPG500 is the slightly newer version of the TPG300; the main differences between these two devices is in their communication protocols. See the manuals for what these properties are used for. 

|  | 300                   | 500                                                  | Affected commands |
| ---- | --------------------- | ---------------------------------------------------- | ---- |
| Switching Functions | `1, 2, 3, 4, A, B` | `1, 2, 3, 4` | SPx |
| Switching Function assignments | `No Assignment, A1, A2, B1, B1, A1 self-monitoring, A2 self-monitoring, B1 self-monitoring, B1 self-monitoring` | `Off, A1, A2, B1, B2, On` | SPx |
| Units    | `mbar, Torr, Pa` | `hPascal, mbar, Torr, Pa, Micron, Volt, Ampere` | UNI/UNIx |

Some less explicit differences are as follows:
* Communication terminators
   * in the TPG300 manual, there is a mismatch of `<CR><LF>` and `<CR>` receive acknowledgement terminators. The TPG500 consistently uses `<CR><LF>`. This may be a typo in the TPG300 manual, but luckily as all the commands we use for the TPG300 are listed as using `<CR><LF>`, this shouldn't cause any headaches.
* `SPS` command
   * Although the 300 and 500 have a mismatch of switching functions, `SPS` returns status values for all switching functions (e.g. `1|2|3|4|A|B`) for _both_ models. However, we don't actually care about the return values for SFs `A` and `B` for either model, so these last two values are skipped in the protocol file. Regardless, it's worth noting that for the 500 the values returned for A and B are:  
      * 1 if an automatic function is active for sensor A1 (for SF `A`) or B1 (for SF `B`) and the sensor is ON 
      * 0 otherwise
* `SPx` command
   * This command returns a couple of parameters, one of which is the 'switching function assignment'. As noted above, these differ between the 300 and 500, but most importantly, `B1` being repeated twice isn't a typo - this is specified in the manual. By contrary, the 500 does have a `B2`.
   * For the 500, this command returns an extra parameter which is the 'ON-Timer', but we don't care about this so is skipped in the protocol file.

## Commands
The IOC currently supports the use following commands with the TPGx00 devices:
| Command | Description                   |
| ------- | ----------------------------- |
| **`Pxx`**, where xx is `A1\|A2\|A3\|A4` | Gets the pressure measurement from the specified channel |
| **`ERR`** | Get the error status of the device |
| **`SPS`** | Get the statuses of all switching functions `1\|2\|3\|4\|A\|B` |
| **`SPx`**, where x is `1\|2\|3\|4` (+ `A\|B` for 300) | Get/set the threshold settings for a specified switching function |
| **`UNI`** | Get the unit of measurement |
| **`UNIx`**, where x is `1\|2\|3` (+ `0\|4\|5\|6` for 500) | Set the current unit of measurement |

At the moment, there is some level of protection for using invalid commands between devices (e.g. sending a `UNI6` to a TPG300):
* `$(P)UNITS:SP` (note: **_not_** `$(P)UNITS`) goes into alarm if set outside the states defined for the current model
* `$(P)FUNCTION` has protective PV `$(P)FUNCTION:VALID` which only allows switching function SP/RB PVs to interact with the protocol file IFF `$(P)FUNCTION` is in a 'valid' state. 
   * For example, if you try to query the switching function `B` on a TPG500, `SPB` cannot be sent to the TPG. However, as of [#7458](https://github.com/ISISComputingGroup/IBEX/issues/7458), no alarm is raised if `$(P)FUNCTION` is set to `B`, as is with `:UNITS:SP`.