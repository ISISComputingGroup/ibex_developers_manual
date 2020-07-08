> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) >

## Introduction

A PLC (programmable logic controller) is a device that is capable of doing near real-time control of a number of inputs and outputs. They're used throughout ISIS to do control that needs to happen very quickly or very reliably/safely e.g. if a vessel is under vacuum make sure it cannot move. In general IBEX doesn't need to worry about what logic the PLC is performing but just needs to read and write to various memory addresses on the device to make sure it performs the correct logic.

## What is a PLC?

PLCs, or programmable logic controllers, are specialised, ruggedized computers used in the control f manufacturing processes. They replaced previous electrical relays, which were large, heavy, unreliable and had to be physically rewired if there needed to be a change in the logic of the control process. Since PLCs are a type of computers, they can be reprogrammed by writing new software, which is much easier than physically changing an electrical circuit. 
PLCs are composed of a CPU, Input modules, output modules, communication equipment, and a power supply. Input modules are responsible for taking input from devices (such as sensors, etc), translating that signal to a digital signal that the CPU can understand , as well as removing electrical noise, conditioning and isolating the signal from the PLC, and debounces switched input. The output modules do a similar job, but instead they handle the output signal coming from the PLC towards devices such as solenoid valves, on/off buttons, and others. They translate the binary output of the CPU to a digital or analogue signal that the output device can understand. Each input/output port or module enable the PLC to take input and give output to a wide array of specific devices that may use different communication protocols. The communication equipment is an interface that allows the computer to be controlled and reprogrammed by users. It can be as simple as a USB port that allows a regular laptop to connect to it. Through this communication equipment the PLC can also have remote input or output, that comes from a different place that at the point of use.
All of these components are installed in a chassis or rack. There are two main types of PLCs in this regard: fixed and modular. Fixed PLCs are all-in-one machines that come with a fixed set of inputs and outputs. They are fairly small, can be installed easily, cheap and also include a small screen that can be used for manually programming the PLC. Modular PLCs are formed out of a series of connected modules that are bought separately. They are installed on a rack or clipped on a rail attached to a wall. A modular PLC has at least a CPU module and a power supply. The input and output modules can be added sideways and removed when not needed. Therefore, modular PLCs can be very flexible as you can configure their I/O to be exactly what you need.
The computer software used to program PLCs is often proprietary and supplied by the manufacturer. The same is for the removable I/O modules. This is a disadvantage for PLCs compared to PCs, as users are locked into the PLC manufacturers proprietary ecosystem. On the other hand, they have easy access to good technical support, and they can be sure I/O modules from the PLC manufacturer work with the PLC with little set-up.
Although the programming software is often proprietary, the programming language used usually follows one of five IEEE standards: ladder diagram, sequential function charts, function block diagram, instruction list, or structured text. Ladder diagrams are the most popular, as it is a graphical programming language based on ladder logic. This type of logic was used when designing electrical relays, and thus ladder diagrams are easy to use for electrical engineers. Structured text is a text based programming language, with syntax similar to C. Instruction list is a text based language that is similar to assembly programming languages. 
As mentioned above, a PLC is a type of computer that is specialised for controlling industrial processes. A PC can also be used for this. However, a PLC is specially designed for this type of job, has specialised modules from manufacturers with experience in this area, it does not have normal peripherals of a PC that are unnecessary for its job such as mice, keyborads, monitors, and is more rugged so that it can operate in environments with electrical noise, vibrations, etc. It is designed with more reliability on both a hardware and software level. PLCs have a minimal Operating System whose only job is to run the PLC code sequentially. This is in contrast with a full OS of a PC, which has a lot more functionality and is more flexible, but may be too bloated for the task and not reliable enough for processes where lost time is very expensive. PLC programming languages are more suited for applications in controls engineering, and more accessible for engineers in this area. A PC on the other hand, can support a wider range of applications, can use any general purpose programming language, and do not depend on a particular manufacturer’s ecosystem. They are also more expensive than most PLCs. Thus, PCs are only used instead of PLCs for rare cases when the controls process is more complex and needs to be more flexible.


## Models

There are a number of different PLCs in use at ISIS:

* [Beckhoff](Beckhoff) - Mostly used for motion but are in fact generic PLCs
* [Omron FINS](PLCs#omron-fins)

## Omron FINS

The Omron FINS is a PLC controlled via a driver first written at Diamond, see [here](https://github.com/ISISComputingGroup/EPICS-FINS). The IOC works by loading an instrument specific `FINS_01.cmd` in `configurations/fins`, which will load an instrument specific `db` from `ioc/master/FINS/db`. The dbs in here are usually created from a number of templates matching specific memory addresses to PVs. Currently the following specific FINS PLC installations are supported in IBEX:

* IMAT FINS PLC
* LARMOR air PLC
* SANS2D vacuum PLC
* WISH vacuum PLC
* ZOOM vacuum PLC

### PLC init

The fins PLC communication is set up with the following:

```
finsUDPInit(<port Name>, <address>, <protocol>, <simulate>)
```
where:

- port name: ASYN port name (usually PLC)
- address: ip address of the PLC
- protocol: which protocol to use
    - "TCP": use TCP communication
    - "TCPNOHEAD": use TCP comms, but without TCP header. This is required (and should only be used for) the devsim emulator 
    - anything else: use UDP protocol
- simulate: whether to simulate calls
    - 0: Do not simulate (real device or devsim)
    - 1: Simulate (don't send commands), this is required for recsim as it lets device initialisation complete successfully with no device

### Testing the FINS IOC in DevSim

If you want to test the IOC for a FINS PLC in devsim mode, you need to add to the FINS_01.cmd file used by that specific FINS IOC the line:
```
$(IFDEVSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 0, "$(PLCNODE=)")
```  

At the same time, the file should either not have any other finsUDPInit call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.

### Testing the FINS IOC in RecSim

If you want to test the IOC for a FINS PLC in recsim mode, you need to add to the FINS_01.cmd file used by that specific FINS IOC the line:
```
$(IFRECSIM) finsUDPInit("PLC", "$(PLCIP):$(EMULATOR_PORT=)", "TCPNOHEAD", 1, "$(PLCNODE=)")
```  

At the same time, the file should either not have any other finsUDPInit call for talking with the real PLC, or have ```$(IFNOTDEVSIM) $(IFNOTRECSIM)``` before that call.
