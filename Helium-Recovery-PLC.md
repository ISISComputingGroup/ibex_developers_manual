> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) > [Omron FINS](Omron-FINS) > [He Recovery PLC](Helium-Recovery-PLC)

# Introduction

The Helium Recovery PLC is a FINS PLC used for monitoring various parameters related to the helium gas recovery system. It contains data that will need to be stored in the database of the Helium Level Monitoring project. Therefore, we wrote an IOC for this PLC so that the data will then be read by a python server via Channel Access.

The manuals folder on the shares drive has a note with a link to the web page used by Cryogenics to monitor the helium gas recovery system. This displays the vast majority of values that are read by the IOC and was used to make sure the IOC reads data correctly. The values not displayed on the web page are specified in the memory map.

This PLC is also currently being used for [HLM PV Import](https://github.com/ISISNeutronMuon/HLM_PV_Import).

# Connection

The Helium Recovery PLC communicates by using FINS over UDP, and is connected over Ethernet. However, you should use TCPNOHEAD when running tests in devsim. The FINS cmd should be similar to the example given [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Omron-FINS#configuration).

The IP address and node for this PLC are noted on the memory map spreadsheet in the shares drive, in Manuals > OMRON_FINS_PLCs > Helium recovery PLC.

## Commands

The memory map of this PLC can be found in a spreadsheet in the shares drive, as mentioned above. Not all of the memory locations in the memory map can be read by the IOC, as not all are needed for the HLM project. The red cells indicate elements that are not needed, yellow cells indicate elements that might need to be added in the future when Cryogenics has more information, and clear cells are needed and have all been implemented.

The memory map details the name, memory address, data type, description and units for every thing of interest to the HLM project that it stores.

The command used by the IOC to read from the PLC is `0x0101` for Memory Area Read, and it reads from the DM Memory area, with code `0x82`. The PLC uses word designated memory addresses, so the third byte of the start address in the FINS command should always be 0.

## Data representation

This PLC uses big endian notation. The word size is 16 bit, so on the memory map the INT and UINT data types take up 16 bits, and the DWORD data type uses 32 bits. The REAL data type also takes up two words, so 32 bits.

Because the IOC needs to read over 150 memory locations, and a lot of PVs would be identical, the IOC makes use of templates to achieve this. There are different templates for different types of record for different data types, and in the substitutions you assign a PV name, description, memory address and unit for each PV, based on the contents of the memory map. Some PVs are placed in the header template because they are unique or because a template for only 2 PVs is not worth it.

# Configuration

In order to run this IOC and talk to the Helium recovery PLC, you should have a `FINS_01.cmd` in the settings area with the contents:
```
#Init and connect
finsUDPInit("PLC", "$(PLC_IP)", "UDP", 0, "$(PLC_NODE=)")

## Load our record instances
dbLoadRecords("${TOP}/db/he-recovery.db","P=$(MYPVPREFIX),Q=HA:HLM:")

```
The PV domain name for this IOC is HA, with HLM as a sub domain. `$(MYPVPREFIX)` should be set to blank when this IOC runs on a production machine. This is to make it the same as central services which runs with a blank prefix because it runs IOCs in multiple domains. The decision for that is at point 17 [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Decision-Log). When running for IOC tests, `$(MYPVPREFIX)` will be `TE:MACHINE_NAME`.

You also need to set the PLC_IP and PLC_NODE macros in the IBEX GUI.

# Gotchas

- During testing when the IOC had all PVs implemented, it was discovered that it was very slow and each test took up to 40 seconds. This was because the emulator was slow due to 150+ requests each second. To fix this, for testing all PVs should be made passive by setting the `$(SCAN)` macro in the `dbLoadRecords` call, which will make the tests run quite fast. `$(SCAN)` is a global macro for the scan fields of every PV, except the heartbeat. For communicating with the real device, this macro should be set to 10 seconds. The heartbeat is an exception because in order to properly see it changing from 0 to 1 and back it needs to scan every 0.5 seconds.
- The vast majority of the PVs reading 16 bit integers from the PLC are private. They are read by an associated calc record which divides the value by 10 and is supposed to be user facing. The reason is that the these values need to be real numbers with decimal place, but they are represented as scaled integers in order to save memory space and be stored in 16 bits only rather than 32 bits. There three exceptions to this: the heartbeat and two turbine speeds. This is because the turbine speeds are not real numbers, and the heartbeat can only be 0 or 1.
- All of the PVs reading 16 bit integer values support negative values, except the heartbeat. Because negative integer support needs to be actively added as mentioned in [Omron FINS](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Omron-FINS#writing-iocs-for-fins-plcs), but the heartbeat can only be 0 or 1 and thus has no need. For the same reason, each 16 bit PV is tested with positive and negative values in the IOC Test Framework, to make sure the IOC can read properly whatever the PLC might store.
- Some mbbi records only have two possible values, and the reason they are not bi records is that the integers in the PLC for those values were 1 and 2, not 0 and 1.
- There are two liquefier alarms in the memory map. They are 16 bit integers, where each bit represents one alarm. In the first alarm liquefier integer, the first bit is a spare, and in the second one the last 7 bits are spares. These two integers are read by two longin records, from which the values are read into two mbbi direct records. The mbbiDirect records could not properly read from hardware directly. For each individual alarm, there is a bi record that reads from the correct bit in one of the two mbbiDirect records, and it is these records that are user facing. The meaning of each bit is commented in the IOC header template, in the shares drive and on the HLM project Sharepoint.


# NDAHEMON FINS setup notes (procServ, no IBEX)

Steps taken to run FINS static build on NDAHEMON with procServ without the rest of IBEX:

```
Copied:

\\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_STATIC_CLEAN_win7_x64\BUILD-1094\EPICS\ioc\master\FINS
\\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_STATIC_CLEAN_win7_x64\BUILD-1094\EPICS\iocstartup
\\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_STATIC_CLEAN_win7_x64\BUILD-1094\EPICS\tools
\\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_STATIC_CLEAN_win7_x64\BUILD-1094\EPICS\utils_win32
\\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_STATIC_CLEAN_win7_x64\BUILD-1094\EPICS\config_env.bat
\\isis\inst$\Kits$\CompGroup\ICP\EPICS\EPICS_STATIC_CLEAN_win7_x64\BUILD-1094\EPICS\config_env_base.bat
in C:\Instrument\Apps\EPICS

C:\Instrument\Settings\config\NDAHEMON\configurations\FINS
from NDW2123 (personal work desktop)

Copy libmysql.dll, mysqlcppconn.dll into C:\Instrument\Apps\EPICS\ioc\master\FINS\bin\windows-x64-static

Run config_env

Edit C:\Instrument\Apps\EPICS\iocstartup\preiocinit.cmd:
Comment out 
# asSetFilename("$(ACCESSSECURITY)/default.acf")
# asSetSubstitutions("P=$(MYPVPREFIX),ACF_IH1=$(ACF_IH1=localhost),ACF_IH2=$(ACF_IH2=localhost),ACF_IH3=$(ACF_IH3=localhost),ACF_IH4=$(ACF_IH4=localhost)")

Take C:\Instrument\Apps\EPICS\iocstartup\procserv.bat
Edit it by removing the other IOCs and 
commenting out 
REM --noautorestart --wait                    (from the %ICPTOOLS%\cygwin_bin\procServ.exe --logstamp... line)
REM set EPICS_CAS_INTF_ADDR_LIST=127.0.0.1


2021-01-06 10:50:37,936 35236:34060 caproto.bcast.search WARNING  PV TE:NDAHEMON:HA:HLM:IMPURE_HE_SUPPLY:PRESSURE with cid 15002 found on multiple servers. Accepted address is 130.246.49.117:5064. Also found on 127.0.0.1:5064
Remove the 127. address from EPICS CA ADDR LIST (duplicate PVs)
Don't run two IOCs talking at the same FINS PLC (Session IDs).
PLC replies back to the wrong IOC.
Solved by leaving only 130.246.51.255 as EPICS_CA_ADDR_LIST in the HLM Manager.


Scheduled task to start FINS IOC procServ on system Startup
HLM PV Import service startup type set to Automatic (Delayed)

To start the FINS IOC via procServ: C:\Instrument\Apps\EPICS\iocstartup\start_FINS_procserv.bat
```
#### start_FINS_procserv.bat
```
@echo OFF
setlocal
REM
REM generated by build_ioc_startups.py - DO NOT EDIT DIRECTLY
REM

REM launches procserv in delayed start mode for all known IOCs
REM The IOCs are started via channel access calls to ProcServCtrl (see procservctrl.bat)
set CYGWIN=nodosfilewarning
set MYDIRPROCSV=%~dp0
set IOCSH_SHOWWIN=H
set EPICS_CAS_BEACON_ADDR_LIST=127.255.255.255
call %MYDIRPROCSV%..\config_env_base.bat
set IOCLOGROOT=%ICPVARDIR%/logs/ioc
set LOGTIME=%%Y%%m%%d
for /F "usebackq" %%I in (`cygpath %IOCLOGROOT%`) do SET IOCCYGLOGROOT=%%I


REM IOC FINS_01 from C:\Instrument\Apps\EPICS\ioc\master\FINS\iocBoot\iocFINS-IOC-01
%ICPTOOLS%\cygwin_bin\procServ.exe --logstamp --logfile="%IOCCYGLOGROOT%/FINS_01-%LOGTIME%.log" --timefmt="%%Y-%%m-%%d %%H:%%M:%%S" --restrict --ignore="^D^C" --name=FINS_01 --pidfile="/cygdrive/c/windows/temp/EPICS_FINS_01.pid" --logport=20132 --chdir="/cygdrive/c/Instrument/Apps/EPICS/ioc/master/FINS/iocBoot/iocFINS-IOC-01" 20131 %ComSpec% /c runIOC.bat st.cmd

REM --noautorestart --wait
REM set EPICS_CAS_INTF_ADDR_LIST=127.0.0.1
```
