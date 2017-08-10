# Introduction

# Macros

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