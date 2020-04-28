> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) >

## Introduction

A PLC (programmable logic controller) is a device that is capable of doing near real-time control of a number of inputs and outputs. They're used throughout ISIS to do control that needs to happen very quickly or very reliably/safely e.g. if a vessel is under vacuum make sure it cannot move. In general IBEX doesn't need to worry about what logic the PLC is performing but just needs to read and write to various memory addresses on the device to make sure it performs the correct logic.

## Models

There are a number of different PLCs in use at ISIS:

* [Beckhoff](Beckhoff) - Mostly used for motion but are in fact generic PLCs
* Omron FINS

## Omron FINS


