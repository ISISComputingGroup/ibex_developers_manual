# Arduino RKNDIO PLC Control

## Purpose

RKNDIO IOC is the IOC for logic control for RIKEN FE PLC interactions.

Created as part of Ticket [#3267](https://github.com/ISISComputingGroup/IBEX/issues/3267).

## Setup

To interact with the device (an Arduino Uno) you need to follow the following steps:

1. Download the Arduino IDE from https://www.arduino.cc/en/Main/Software. Select the windows zip file to download.

2. Next, update the drivers for the device. 
    - To do this connect the device via USB.
    - Then open device manager as administrator.
    - Select `Ports (COM & LPT)`.
    - Select the port the device is plugged into.
    - Right-click on the device port and select `update driver`. 
    - Select `Browse my computer for driver software`.
    - Navigate to the Arduino folder you just downloaded and select `drivers` folder within it.
    - Click `Next` and agree to install the Arduino driver.

3. Now download the specific Arduino sketch and libraries from https://github.com/KathrynBaker/se-arduino-devices (as of 29/06/2018) and copy the content into your Arduino folder which contains the `arduino.exe` file

4. Finally, start the `arduino.exe` file to start the Arduino IDE and load the `RikenFEDIO.ino` sketch onto the device. Now you should now be able to communicate with the device. 

For more information on setting up an Arduino Uno see [Getting Started with Arduino and Genuino UNO](https://www.arduino.cc/en/Guide/ArduinoUno#toc8).

## List of Commands

| *Send* | *Receive* | *Notes* |
| --- | --- | --- |
|*IDN?|`RIKENFE Prototype v2.0`|There are changes planned to the protocol which may change the version number|
|STATUS|The error string|The error string is `No error` or a string detailing the error|
|ERR|The error string|The error string is `No error` or a string detailing the error|
|READ n|`TRUE` or `FALSE`|n is a digit for the hardcoded list of digital inputs|
|WRITE n state|`OK` or `ERROR`|n is a digit for the hardcoded list of digital outputs, state is `TRUE` or `FALSE`|

You can read from pins 2 to 7 and write to pins 8 to 13.
   
