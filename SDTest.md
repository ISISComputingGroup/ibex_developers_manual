# Introduction

The SDTEST IOCs allow us to set up communications with an arbitrary device on-the-fly. This often happens if an instrument acquires a bit of equipment to achieve a short term goal. We should try and ensure that if a device is to be used long-term that we find out about it early enough to provide a dedicated IOC, or deliver it as soon as practical.

# Macros

Each SDTest IOC supports communication with 8 separate devices on 8 ports. Macros should be suffixed by the device number in the range `1` to `8` inclusive (e.g. `PORT1`):

`PORT`: 
`BAUD`:
`BITS`:
`PARITY`:
`STOP`:
`CLOCAL`:
`CRTSCTS`:
`IXON`:
`IXOFF`:
`OEOS`:
`IEOS`:
`NAME`:
`SCAN`:
`GETOUT`:
`GETIN`:
`SETOUTA`:
`SETOUTB`:
`SETOUTC`:
`SETIN`:
`INITOUT`:
`INITIN`:
`INITP`:
`PROTO`:


# Simple setup

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