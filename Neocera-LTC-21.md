> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Neocera LTC 21

## Commands currently Supported

command | meaning
 ---    | --------
QISTATE?; | Operating mode, monitor/control/suto tune/off
SCONT | set into control mode
SMON | set into monitor mode
QHEAT?; | heater percentage
QOUT?<channel>; | Output config (note different returns for analogue and heater)
QPID?<channel>; | Queres PID (note different returns for analogue and heater)
QSETP?<channel>; | Setpoint and units
QSAMP?<channel>; | Temperature and unit
SHCONT%.0f; | Heater output control
SACONT%.0f; | Analogue control
SPID<channel>,%.2f,%.2f,%.2f,%.2f,%.2f; | Set PID etc
SETP%.0f,%.2f; | Setpoint set
