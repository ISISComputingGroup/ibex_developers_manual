> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Neocera LTC 21

Neocera is a temperature controller. It has two outputs (i.e. set points with output current) one connected to a heater (output 1) and one connected to an analogue circuit (output 2). It also has two temperature sensors which can be connected to either of the outputs. 
The system has four control modes; only two of which are accessible from the IOC. The modes are:

1. Monitor: temperature is monitored but the heater is never switched on
1. Control: Temperature is controlled using the heater for outputs/setpoints which exist
1. Off: Display is off not really sure how to access this mode
1. Autotune: unit is auto tuning the PID settings.

## Commands currently Supported

All commands are terminated by a ';' replies are separated by ';'. It ignores all spaces, new lines and carriage returns.

command | meaning
 ---    | --------
QISTATE? | What is the operating mode; reply is numeric monitor (0)/control (1)/auto tune (2)/off (3)
SCONT | set into control mode
SMON | set into monitor mode
QHEAT? | heater power; numeric return is percentage of full scale
QOUT?\<channel\> | Output config (note different returns for analogue and heater)
QPID?\<channel\> | Query PID settings (note different returns for analogue and heater)
QSETP?\<channel\> | Query setpoint; return temperature with units
QSAMP?\<channel\> | Query Temperature; returns temperature with unit
SHCONT\<control enum\> | Set heater output control; AUTO P (0)/AUTO PI(1)/AUTO PID (2)/PID (3)/TABLE(4)/DEFAULT (5)
SACONT\<control enum\> | Set analogue control; PID (3)/TABLE(4)/DEFAULT (5)/MONITOR (6)
SPID\<channel\>,\<P\>,\<I\>,\<D\>,\<Manual percent term\>,(\<Power limit\> or \<Gain\>.\<Offset\>) | Set PID and other setting for heater set power limit for analog set gain ad offset
SETP\<channel\>,\<temp\> | Set the setpoint for the given channel


where \<channel\> is 1 - Heater and 2 - Analog
