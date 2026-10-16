# Purchasing new equipment

```{toctree}
:hidden:
:glob:
:titlesonly:
:maxdepth: 1

purchasing_new_equipment/*
```

```{note}
This page relates to "slow" control; if looking at items like cameras, DAQ, or items at a higher frequency than 10Hz, please {external+ibex_user_manual:ref}`contact Experiment Controls <report_a_problem>`.
```

## Off the shelf devices
If purchasing "simple" off the shelf devices (e.g. power supplies, temperature controllers, gaussmeters, etc.) please bear the following in mind: 
- The device itself needs to allow an external computer to control it. 
- Only certain transport layers will interact with our architecture readily. If it is not in this list, we are unlikely to be able to integrate it easily, so please engage with the group as soon as possible. This list is in order of preference. 
  * **Serial** (RS232 is preferred, but RS422 and RS485 can be accommodated with advanced warning). Ideally DB9 or DB25 connectors.
  * **Ethernet** - but please make sure there is provision for updates to the device system. Ideally this would be DHCP capable, but should also allow for configuration of a static IP.
  * **GPIB**
- If the only connection option available is **USB**, then you **MUST** get in touch with us early, as the options for integrating these devices are limited, and it may need a dedicated computer purchasing. 
- With regards to the control protocol, the following can all be integrated easily, other protocols would need to be discussed: 
  * {external+secop:doc}`SECoP <index>` 
  * [SCPI](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments)
  * [OPCUA](https://en.wikipedia.org/wiki/OPC_Unified_Architecture)
  * ASCII based command sets (please see the {doc}`purchasing_new_equipment/Designing-Protocols` guide for more details of preferences of how these would look)
  * [Modbus](https://en.wikipedia.org/wiki/Modbus)

If a protocol needs to be designed, please consider {external+secop:doc}`SECoP <index>` first, or read the {doc}`purchasing_new_equipment/Designing-Protocols` guide.

As much warning as possible is needed to ensure availability of new devices within IBEX; please {external+ibex_user_manual:ref}`contact Experiment Controls <report_a_problem>` as soon as possible when considering the purchase of a new device.

## Systems which integrate a Computer 

It is not unusual for moderately complex systems to require a computer to provide suitable control. This raises greater concerns for ISIS generally, as well as the Experiment Controls team. 

Agreement needs to be ensured during tender and selection in relation to: 
- Who supplies the computer 
- Who maintains it 
- Who ensures it is kept up to date 
- Who deals with changes when the hardware must be updated or the operating system updates cause something to function in an unanticipated manner 
- Recovery procedures for failure conditions 
- Who is responsible for the cybersecurity level and maintenance of this computer 

Service level agreements for any of these issues should also be agreed. These should match the expected lifetime of the item being purchased. If this is not possible, then an agreement as to the risk needs to be made, and considerations for ways to mitigate it which do not put undue stress on the resources in question. 

Conversations with the Experiment Controls team from the outset would be beneficial for such items. 

Updates for security aspects are especially important for any item which is placed on a network, there is greater grace available should the communication between IBEX and the device be via a transport layer other than ethernet as the computer can be kept off a network. 