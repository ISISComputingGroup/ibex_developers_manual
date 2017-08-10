# Introduction

The SDTEST IOCs allow us to set up communications with an arbitrary device on-the-fly. This often happens if an instrument acquires a bit of equipment to achieve a short term goal. We should try and ensure that if a device is to be used long-term that we find out about it early enough to provide a dedicated IOC, or deliver it as soon as practical.

# Macros

Each SDTest IOC supports communication with 8 separate devices on 8 ports. Macros should be suffixed by the device number in the range `1` to `8` inclusive (e.g. `PORT1`):

- `PORT`: Communications port (e.g. COM1)
- `BAUD`: Baud rate (default: 9600)
- `BITS`: Message bits (default: 8)
- `PARITY`: Message parity (default: none)
- `STOP`: Number of stop bits (default: 1)
- `CLOCAL`: Output flow control using DSR signal (Y/N, default: Y)
- `CRTSCTS`: Hardware flow control (Y/N, default: N)
- `IXON`: Software flow control for output (Y/N, default: N)
- `IXOFF`: Software flow control for input (Y/N, default: N)
- `OEOS`: Output terminator (default: \r\n)
- `IEOS`: Input terminator (default: \r\n)
- `NAME`: Name of the device
- `SCAN`: Scan rate
- `GETOUT`: Command for getting the readback
- `GETIN`: Format of the readback
- `SETOUTA`: Command for setpoint
- `SETOUTB`: Secondary setpoint value
- `SETOUTC`: Tertiary setpoint value
- `SETIN`: Format of the setpoint
- `INITOUT`: Initialisation command
- `INITIN`: Format of init response
- `INITP`: Send an initialisation command (default: NO)
- `PROTO`: Path to custom protocol file, (default: SDTEST-default.proto)

Note that typically 

# Example

This is an example of `globals.txt` for using SDTest for talking to a Lakeshore 625:

```
SDTEST_01__NAME1=LakeShore625_1
SDTEST_01__PORT1=COM41
SDTEST_01__BAUD1=9600
SDTEST_01__BITS1=7
SDTEST_01__PARITY1=odd
SDTEST_01__IEOS1=\\r\\n
SDTEST_01__OEOS1=\\r\\n
SDTEST_01__SCAN1=.5 second
SDTEST_01__SCAN1=Passive
SDTEST_01__GETOUT1="RDGI?"
SDTEST_01__GETIN1="%f"
SDTEST_01__SETOUTA1="SETI"
SDTEST_01__SETOUTB1=0x20
SDTEST_01__SETOUTC1=%f
SDTEST_01__SETIN1=
```