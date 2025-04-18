# Stanford DG645

For the Litron Laser Timing Control see [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Litron-Laser-Timing-Control-(Stanford-DG645)).

## About
Stanford DG645 is a digital delay generator. There is an IOC, emulator and tests for it. The OPI is constructed in a modular fashion
out of smaller OPIs, to be reused if needed. The IOC is using a ['fork'](https://github.com/ISISComputingGroup/EPICS-delaygen) version of [Delaygen (original here)](https://github.com/epics-modules/delaygen).

Currently does not support RECSIM mode.

## Connection
The device supports varying BAUD rates but other communication parameters are fixed, hence we do not have macros for them. Default BAUD rate is 9600.

The device also supports an ethernet connection using Telnet. In order to connect via ethernet, follow these steps on the device:
1. In the NET menu (SHIFT -> STO) set:
    1. TCPIP = Enabled

    2. DHCP = Enabled

    3. Telnet = Enabled

    4. Reset = Yes

    5. Press the Enter Button
2. Then access the status menu (SHIFT -> 6) and use the arrows to navigate to TCPIP Status.
2. Press 6 until you get to IP
3. Make a note of this IP address

Then in IBEX:

5. Set the `INTERFACE` macro to `ETHERNET`
6. Set the `ADDR` macro to the IP you wrote down earlier
7. Start the IOC

This IP will be reassigned if the device is down for a while. So steps 2-7 will need to be repeated.

## Usage
The IOC currently covers setting and reading of delays of channels T0, T1, A, B, C, D, E and F. T0 is the base channel that is not changeable from the IOC. Channels A-F can be configured to have their own delay value, offset by reference to another channel. For example:
- Channel T0 is currently 0ms
- Channel A is currently 5ms + T0
- Channel D is currently 10ms + A
## 
Then final delay for channel D is 15ms which in the GUI is called a 'channel width'.It is possible to chain references across all of the channels. Channel T1 serves as max function of all the other channels.

### Widths

Channel widths are calculated by the IOC for the sake of drawing graphs. For example, channel width AB would be delay of channel A + delay of channel B.

### Graphs
Graphs are controlled using a script. The script's only purpose is to **read** data from the IOC and does not influence it's behaviour. Graphs are a visual representation of length, starting point and polarity of delay between two channels. All of this functionality was based on behaviour of the VI (C:\LabVIEW Modules\Drivers\Stanford DG645).

### Polarity logic
Negative or positive polarity logic will influence if the graph's max value is -1 or 1. NIM/TTL/NR logic works as follows:
- NIM, if OutputAmpAO is set to 0.8 and OutputOffsetAO is set to -0.8
- TTL, if OutputAmpAO is set to 4 and OutputOffsetAO is set to 0
- NR if neither of above is true

This is based on VI's behaviour.

### Error queue
The device supports an error queue of up to 20 errors. The VI, and subsequently the IOC currently displays a queue of 10 translated error messages.