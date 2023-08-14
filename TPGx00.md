> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Pressure Monitors](Pressure-Monitors) > [TPGx00](TPGx00)


## TPGx00
A type of device which controls a series of four pressure sensors (A1, A2, A3, A4). 

TPGx00 is shorthand for the TPG 300 and 500 Pfeiffer Vacuum Gauges which use the same `TPG300` IOC. The two models also share the same `TPG300.opi` file, which updates its appearance based on TPG model number.

**To configure the IOC for the 500, define the MODEL macro: it defaults to TPG300**

The TPG300/500 are similar to the [TPG26x](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TPG26x) and [TPG36x](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/TPG36x), but have 4 pressure sensors to read from, and have a slightly more complicated IOC. All TPG manuals can be found in `<share>\ISIS_Experiment_Controls\Manuals\Pfeiffer TPG<xxx>`.


## Communication


**The IOC has the macros `IPADDR` and `PORT` to configure communication with the TPG. `IPADDR` can only be used for 500 models, as the 300 does not have an ethernet interface.**

### TPG300
The TPG300 communicates over a serial interface via RS232 with the use of an IF 300C plugin interface card.

### TPG500
The TPG500 communicates over a serial interface via Ethernet, USB and RS485 (virtual com-port), and RS232 with the use of an IF 300C plugin interface card.

Pfeiffer has their own 'Ethernet Configuration Tool' software which can be used to configure a virtual com-port (see page 32 of the 'Operating Instructions' manual), although this software has yet to be used to connect to a TPG500 successfully.


## Communication Protocol

First send a command (e.g. ask for the pressure) then the device will return ACK.
Then send ENQ to get the actual value.

An example: (S: Send, R: Receive)
1. S: `<Command><CR><LF>`
2. R: `<ACK><CR><LF>`
3. S: `<ENQ>`                  
4. R: `<Data><CR><LF>`

> !!! Important that the `<ENQ>` is not terminated with `<CR><LF>` which would cause the device to report syntax error.


## Talking to a real device or the emulator


### Talking to a real device

TPG300

1. Connect it to the moxa and identify the COM port it is linked to through `NPort Administrator`.
2. Start HTerm and connect to the right COM port with the following settings: \
Baud: 9600, Data: 8, Stop: 1, Parity: None
3. When sending the first command use ASC and CR-LF as `Send on enter`
4. You should receive an ACK (acknowledgement).
5. Now send the HEX code 05 ENQ command ! Make sure you change the type to HEX and the"Send on enter" to None.
6. The data returned should be what you requested in the first command.

TPG500

You can use "TCP Terminal" to connect to the IP address of the TPG500 with the port being 8000. Then follow the instructions above but use TCP Terminal instead of HTerm. There won't be COM port settings as the communication is done through TCP now.


### Talking to an emulator

See [this wiki page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Emulating-Devices) on how to start an emulator. Or alternatively start the tests with the `-a` flag to run the emulator and IOC.

Once it's running you can read off the IP address and PORT from the lewis start command. Use those in the TCP Term to send instructions directly to the emulator.


## Differences between the 300 and 500
The TPG500 is the slightly newer version of the TPG300; the main differences between these two devices is in their communication protocols. See the manuals for what these properties are used for. 

|  | 300                   | 500                                                  | Affected commands |
| ---- | --------------------- | ---------------------------------------------------- | ---- |
| Switching Functions | `1, 2, 3, 4, A, B` | `1, 2, 3, 4` | `SPx` |
| Switching Function assignments | `No Assignment, A1, A2, B1, B1, A1 self-monitoring, A2 self-monitoring, B1 self-monitoring, B1 self-monitoring` | `Off, A1, A2, B1, B2, On` | `SPx` |
| Units    | `mbar, Torr, Pa` | `hPascal, mbar, Torr, Pa, Micron, Volt, Ampere` | `UNI`/`UNIx` |

Some less explicit differences are as follows:
* Communication terminators
   * The TPG300 manual has a mismatch of `<ACK><CR><LF>` and `<ACK><CR>` for intermediate acknowledgement terminators. Hardware testing with the 300 has confirmed that **this is a typo** and all commands use `<ACK><CR><LF>`. This is the same as the 500, so we can universally use `<CR><LF>` terminator in the protocol file.
* `SPS` command
   * Although the 300 and 500 have a mismatch of switching functions, `SPS` returns status values for all switching functions (e.g. `1|2|3|4|A|B`) for _both_ models. However, we don't actually care about the return values for switching functions `A` and `B` for either model, so these last two values are skipped in the protocol file. Regardless, it's worth noting that for the 500 the values returned for A and B are:  
      * 1 if an automatic function is active for sensor A1 (for SF `A`) or B1 (for SF `B`) and the sensor is ON 
      * 0 otherwise
* `SPx` command
   * This command returns a couple of parameters, one of which is the 'switching function assignment'. As noted above, these differ between the 300 and 500, but most importantly, `B1` being repeated twice isn't a typo - this is specified in the manual (but this is not certain, so will be checked in [#7860](https://github.com/ISISComputingGroup/IBEX/issues/7860)). By contrary, the 500 does have a `B2`.
   * For the 500, this command returns an extra parameter which is the 'ON-Timer', but we don't care about this so is skipped in the protocol file.

## Commands
The `TPG300` IOC currently supports the use following commands with the TPGx00 devices:
| Command | Model available |  Description                   |
| ------- | ------- | ----------------------------- |
| **`Pxx`**, where xx is `A1\|A2\|A3\|A4` | Both | Gets the pressure measurement from the specified channel |
| **`ERR`** | 300 only | Get the error status of the device |
| **`SPS`** | 300 only | Get the statuses of all switching functions `1\|2\|3\|4\|A\|B` |
| **`SPx`**, where x is `1\|2\|3\|4` (+ `A\|B` for 300) | Both | Get/set the threshold settings for a specified switching function |
| **`UNI`** | Both | Get the unit of measurement |
| **`UNIx`**, where x is `1\|2\|3` (+ `0\|4\|5\|6` for 500) | Both | Set the current unit of measurement |

At the moment, there is some level of protection for using invalid commands between devices (e.g. sending a `UNI6` to a TPG300):
* `$(P)UNITS:SP` (note: **_not_** `$(P)UNITS`) goes into alarm if set outside the states defined for the current model - but only on a TPG300 (this may be due to the fact for an 300, the `mbbi` does not have a defined zero-state, and so cannot default to zero as a 500 can).
* `$(P)FUNCTION` has protective PV `$(P)FUNCTION:VALID` which only allows switching function SP/RB PVs to interact with the protocol file IFF `$(P)FUNCTION` is in a 'valid' state. 
   * For example, if you try to query the switching function `B` on a TPG500, `SPB` cannot be sent to the TPG. However, as of [#7458](https://github.com/ISISComputingGroup/IBEX/issues/7458), no alarm is raised if `$(P)FUNCTION` is set to `B`, as is with `:UNITS:SP`.

## Known issues

> These issues seem to have been resolved by correcting the communication protocol.
> During transmission when sending the `<ENQ>` ASCII code (hex `05`) it should not be appended by
> the terminators `<CR><LF>` in contrast to the first command. (See [Communication Protocol](#communication-protocol))

### TPG500

~~The TPG500 has some slightly odd behaviour that is worth noting.~~

* Error state
   * The `ERR` command was added to the `TPG300` IOC as of [#7458](https://github.com/ISISComputingGroup/IBEX/issues/7458). Upon start-up, the TPG500 enters the default `No error` (`0000`) state. However, after the first command is sent to the device, regardless of validity, the device is pushed into a `Syntax error` (`0001`) state, and this persists for the rest of this power cycle. Thus, the `ERR` command is currently only implemented for the 300, as it doesn't report anything of use. 
* `SPS` command
   * The `SPS` command currently is not accepted by the TPG500 (inconsistently with the manual): `SPS` will receive `NAK><CR><LF>`, i.e. negative acknowledgement, which is the same response for syntactically incorrect commands. Oddly, when sent as the _very first_ command after start-up, this command will be accepted as per the manual, but for every attempt after, it will be rejected. Thus, this command is also only implemented for the 300 - for the 500 we can infer this information from the 'Circuit Assignment' readback box in the OPI, so it is not necessarily essential. 
* Firmware
   * TPG500s will most likely have software version `010100`. Upgrading the firmware to `010300`, to be inline with minimum version specified by the manual, creates some weird handshake behaviour. Whilst in a persisting `Syntax error` state as detailed above, the TPG (inconsistently with the manual) will append `NAK><CR><LF>` (`15 0D 0A` in hex) to every healthy command. These, however, don't seem to upset the protocol file, so are relatively harmless.