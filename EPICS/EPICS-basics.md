> [Wiki](Home) > [The Backend System](The-Backend-System) > [EPICs](EPICs) > EPICS basics

If you are setting up a development environment for the first time, it is recommended that you first look at the [Getting started guide](First-time-installing-and-building-(Windows)).

The following instructions have been migrated from Trac to GitHub and some steps may no longer be appropriate for the IBEX project.


# Building EPICS with VS2012 Express on a 64-bit Windows #

This section is an old way of installing EPICS brand new. Not relevant to ISIS anymore since EPICS comes already installed if you follow [Building the backend](First-time-installing-and-building-(Windows))

1. Download and install Visual Studio Express 2012 for Windows Desktop
1. Download and install Strawberry Perl (64 bit version) to `C:\strawberry\`
1. Download, unzip and copy GNU Make for Windows to `C:\gnuwin32`
1. Download LibIntl for Windows, LibIconv for Windows as they contain dlls we need for gnumake.
1. Extract the files and copy `libintl3.dll`, `libiconv2.dll` and copy to `C:\gnuwin32\bin\` (i.e. the same directory as make)
1. Create a directory such as C:\EPICS. Download and unzip EPICS base (3.14.12.3). Move and rename base to `C:\EPICS\base`. Note: you may need to install 7-Zip to unzip EPICS base
1. Open `C:\EPICS\base\startup\win32.bat` and check/change the following settings:
    - check the perl path is correct; for example it might be set `PATH=C:\strawberry\perl\bin;%PATH%`
    - check the gnuwin32 path is correct
    - comment out the `call C:\Program files\Microsoft Visual Studio 10.0\VC\vcvarsall.bat" x86` line
    - below that add the following line: `call C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x86_amd64`. **NOTE:** we are using the cross-compiler to build 64bit EPICS, hence "x86_amd64" rather than "x64"
    - uncomment the `set EPICS_HOST_ARCH=windows-x64` line and comment out the `set EPICS_HOST_ARCH=win32-x86` line
    - comment out the `set PATH=%PATH%;C:\Program files\Bazaar` line
    - Save the file.
1. Open a standard command line prompt and type the following:
    - `cd C:\EPICS\base\startup`
    - `win32.bat`
    - `cd ..`
    - `make`
    
It should build now, taking about 5-10 minutes.

## Preparing to use EPICS ##

1. Add some environment variables:
    - `EPICS_HOST_ARCH=windows-x64`
    - `EPICS=C:\EPICS\`
1. Add the following directory to the PATH environment variable: `%EPICS%\base\bin\%EPICS_HOST_ARCH%`

## To build a debug version ##

Edit `startup\win32.bat`:
- Change `set EPICS_HOST_ARCH=windows-x64 line` to `set EPICS_HOST_ARCH=windows-x64-debug`

Then rebuild using make.

# Creating a simple IOC #
Run Win32.bat from `$EPICS_BASE\startup`

Create a directory in the directory below EPICS base called `my_iocs` or whatever. Inside that create a directory called `simpleioc`.

From inside `simpleioc`, type the following:

```
makeBaseApp.pl -t ioc simple
makeBaseApp.pl -i -t ioc simple
```

Accept the default name (i.e. press Return)

Move to the Db directory:

```
cd simpleApp\Db
```

Create a file called simple.db:

```
echo. 2>simple.db
```

Open it in notepad (or similar) and add the following records and save the file:

```
record(ai, "simple:value1")
{
    field(VAL, 1)
}
record(ai, "simple:value2")
{
    field(VAL, 2)
}
record(calc,"simple:diff")
{
    field(SCAN,"1 second")
    field(INPA, "simple:value1")
    field(INPB, "simple:value2")
    field("CALC", "A - B")
}
```

Open the Makefile in the Db directory and add the following near where it says #DB += xxx.db:

```
DB += simple.db
```

Save it!

Move back up to the simpleioc directory and type make. After it completes successfully move to the `iocBoot\iocsimple` directory Edit the st.cmd file:

Change 

```
#dbLoadRecords("db/xxx.db","user=blahblah")
```

to 

```
dbLoadRecords("db/simple.db","user=blahblah")
```

Save it!

Now to start the IOC by typing the following from the `iocBootiocsimpledirectory`:

```
..\..\bin\windows-x64\simple.exe st.cmd
```

The IOC should start. Type dbl to print a list of PVs. If the PVs are not there then read the the IOC start up messages to see if there is an error.

If you start a new command line and set the paths as above if it will be possible to use caput, caget etc. If you edit the records, you may need to run make again - just stop the IOC, type make and then restart the IOC.

# Creating a random number generator IOC #

Run Win32.bat from `$EPICS_BASE\startup`.

Create a directory called `random` and move to it. Run the following commands (accept the defaults):

```
makeBaseApp.pl -t ioc rand
makeBaseApp.pl -i -t ioc rand
```

Move to the `randApp\src directory`. Create the dbd file:

```
echo. 2>randdev.dbd
```

Open and add the following:

```
device(ai,CONSTANT,devAiRand,"Random")
```

Create the C file:

```
echo. 2>devrand.c
```

Open and add the following:

```
#include <stdlib.h>
#include <epicsExport.h>
#include <dbAccess.h>
#include <devSup.h>
#include <recGbl.h>
#include <aiRecord.h>
static long init_record(aiRecord *pao);
static long read_ai(aiRecord *pao);
struct randState {
  unsigned int seed;
};
struct {
  long num;
  DEVSUPFUN  report;
  DEVSUPFUN  init;
  DEVSUPFUN  init_record;
  DEVSUPFUN  get_ioint_info;
  DEVSUPFUN  read_ai;
  DEVSUPFUN  special_linconv;
} devAiRand = {
  6, /* space for 6 functions */
  NULL,
  NULL,
  init_record,
  NULL,
  read_ai,
  NULL
};
epicsExportAddress(dset,devAiRand);
static long init_record(aiRecord *pao)
{
  struct randState* priv;
  unsigned long start;
  priv=malloc(sizeof(struct randState));
  if(!priv){
    recGblRecordError(S_db_noMemory, (void*)pao, "devAoTimebase failed to allocate private struct");
    return S_db_noMemory;
  }
  recGblInitConstantLink(&pao->inp,DBF_ULONG,&start);
  priv->seed=start;
  pao->dpvt=priv;
  srand(&priv->seed);
  return 0;
}
static long read_ai(aiRecord *pao)
{
  struct randState* priv=pao->dpvt;
  pao->rval=rand() % 100;
  return 0;
}
```

Edit `randApp\src\MakeFile` and add the following in the appropriate places:

```
rand_DBD += randdev.dbd
rand_SRCS += devRand.c
```

Move to the `randApp\Db` directory. Create the db file:

```
echo. 2>rand.db
```

Open and edit it to read:

```
record(ai,"test:rand"){
    field(DTYP,"Random")
    field(DESC,"Random numbers")
    field(SCAN,"1 second")
    field(INP,"$(S)")
}
```

Edit `randApp\Db\Makefile` and add:

```
DB += rand.db
```

Move to `<top>` and run `make`

Move to `iocBoot\iocrand\`

Edit the appropriate parts of st.cmd to look like this:

```
# Register all support components
dbLoadDatabase "dbd/rand.dbd"
rand_registerRecordDeviceDriver pdbbase
# Load record instances
dbLoadRecords("db/rand.db", S=324235")
```

Now run the IOC:

```
..\..\bin\windows-x64\rand.exe st.cmd
```

# ProcServer #

## Installation ##

Download the Windows executable from [http://sourceforge.net/projects/procserv/](http://sourceforge.net/projects/procserv/) and install somewhere in your EPICS installation. For example: `C:\EPICS_PILOT\support\procserver`. Obtain `CygWin1.dll` and put it into the ProcServer directory (installing CygWin and copying and pasting the file is one way).

Add the ProcServer directory to your EPICS path; for example: edit the .bat file that is used to configure your EPICS environment.

## Running a simple example ##

From the command line, move to the iocBoot directory of an IOC (e.g. `C:\EPICS_PILOT\ISIS\simpleioc\iocBoot\iocsimple`).

Run ProcServer like so:

```
procserv -e ..\..\bin\windows-x64\simple.exe -n "Simple IOC" -L log.txt 20000 ./st.cmd
```

This will spawn a blank command window for the IOC. The parameters explained:

- -e: points to the IOC executable
- -n: the IOC name for the logging
- -L: the name of the log file
- 20000: the port that ProcServer will run on

From another command line it should be possible to use caget to get values from the newly spawned IOC. **Note:** ProcServer can be started without the IOC being loaded using `-w`, the IOC can then be started later remotely.

## Connecting remotely ##

By default, ProcServer access is restricted to the local host. To enable read-only remote access the `-l` (small L) parameter needs to be specified with a port number. For example:

```
procserv -e ..\..\bin\windows-x64\simple.exe -n "Simple IOC" -L log.txt -l 20001 20000 ./st.cmd
```

Note: the remote access port needs to be opened in the firewall.

Using telnet via PuTTY or similar connect to the appropriate IP address and port, this will lead to something like the following:

```
@@@ procServ server PID: 7424
@@@ Server startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
@@@ Child startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
@@@ Child "Simple IOC" started as: ./st.cmd
@@@ Child "Simple IOC" PID: 2152
@@@ procServ server started at: Thu Apr  4 11:34:24 2013
@@@ Child "Simple IOC" started at: Thu Apr  4 11:34:24 2013
```

The `@@@` indicates that the message is generated by ProcServer.

To enable remote read/write the `--allow` parameter must be passed in to the !ProcServer startup. For example:

```
procserv -e ..\..\bin\windows-x64\simple.exe --allow -n "Simple IOC" -L log.txt 20000 ./st.cmd
```

Note: the port (in this case 20000) needs access through the firewall.

Connecting now will show slightly more information:

```
@@@ Welcome to procServ (procServ Process Server 2.6.0)
@@@ Use ^X to kill the child, auto restart is ON, use ^T to toggle auto restart
@@@ procServ server PID: 4748
@@@ Server startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
@@@ Child startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
@@@ Child "Simple IOC" started as: ./st.cmd
@@@ Child "Simple IOC" PID: 6252
@@@ procServ server started at: Thu Apr  4 10:52:40 2013
@@@ Child "Simple IOC" started at: Thu Apr  4 10:52:40 2013
@@@ 0 user(s) and 0 logger(s) connected (plus you)
```

This connection is read/write so sending IOC commands like `dbl` and `dbtpf` will work.

By default, typing exit and pressing return will quit and restart the IOC, and a mixture of ProcServer and IOC messages will be seen. The IOC can be set to not automatically restart by specifying the `--noautorestart` parameter when starting ProcServer. It is still possible to restart the IOC remotely once exited by using `CTRL+X` followed by pressing return.

# PV Gateway #

## Building ##

NOTE: this has already been done for the EPICS PILOT, so it can be downloaded and built from there.

Download `gnuregex` from EPICS site. Place in `extensions\src` directory (assuming extensions_top has already been installed).

Download gateway source source from EPICS site. Place in `extensions\src` directory.

Edit `gateway.cc` by adding the following near the top:

```
#ifdef WIN32
  #define strcasecmp _stricmp
#endif
```

Edit gateResources.cc and edit line 55 to read:

```
time_t now;
```

Edit line 117 in the Makefile in srcgateway to read:

```
PROD_LIBS = regex
```

Move to the extensions directory and type "make" to build it.

## A simple example ##

Three machines:

1. INST = PC running IOCs
1. GATE = PC running gateway
1. VIEW = Viewing PC (only needs caget)

![Gateway schematic](EPICS/gateway.png "Gateway schematic")

The gateway uses a file called gateway.pvlist that defines the PVs available via the gateway; using your PV names, edit it so it contains something along the lines of:

```
PCA:KITNAME:PV1 ALLOW
PCA:KITNAME:PV2 ALLOW

```

IMPORTANT: there must be a blank line after the final definition or it will not work!

There is a second file called gateway.access that defines the access rights. The access is defined using the EPICS Access Security syntax. For read-only access for everyone it should contain:

```
ASG(DEFAULT) {
   RULE(1,READ)
}
```

For more information, see [Access Security](#epics-access-security).

Start the gateway with the following command (replacing `IP_OF_INST` and `IP_OF_GATE` with the correct IP addresses):

```
gateway -pvlist gateway.pvlist -access gateway.access -cip IP_OF_INST -sip IP_OF_GATE
```

NOTE: to send multiple client addresses, use a quoted space separated list, e.g. `192.168.0.1 192.168.0.2`. NOTE: if `-cip` is not defined then the gateway will use `EPICS_CA_ADDR_LIST` by default. \

On `VIEW`, run the following commands:

```
set EPICS_CA_ADDR_LIST= IP_OF_GATE
caget PCA:KITNAME:PV1
```

Hopefully, that should work. If you now stop the gateway process on GATE and retry the caget on VIEW, it should fail.

To use an aliases, simply change the gateway.pvlist, so it contains something like:

```
MY_ALIASNAME ALIAS PCA:KITNAME:PV1
```

IMPORTANT: there must be a blank line after the final definition or it will not be defined!

From VIEW, it should now be possible to use caget with the alias:

```
caget MY_ALIASNAME
```

To access statistics about the gateway via Channel Access the gateway.pvlist needs to be edited to allow access to the
gateway PVs:

```
PCA:KITNAME:PV1 ALLOW
PCA:KITNAME:PV2 ALLOW
YOURMACHINE.* ALLOW
```

The PVs should now be accessible like so:

```
caget YOURMACHINE:pvtotal
```

## Running on one machine (Block Server) ##

## IOC ##

set `EPICS_CA_ADDR_LIST=127.0.0.1 YOUR_IP_ADDRESS`

Run the SimpleIoc!

## Gateway ##

Create a file called `blocks.pvlist` and add the following:

```
BLOCK1 ALIAS NDWxxx:username:SIMPLE:VALUE1
<BLANK LINE>
```

Create a file called `gateway.access` and add the following:

```
ASG(DEFAULT) {
   RULE(1,READ)
}
```

```
gateway -pvlist blocks.pvlist -access gateway.access -cip 127.0.0.1 -sip YOUR_IP_ADDRESS
```

## CAGET ##

```
set EPICS_CA_ADDR_LIST=127.0.0.1 YOUR_IP_ADDRESS
caget BLOCK1  #This works via the gateway
caget NDWxxx:username:SIMPLE:VALUE1  #This works via standard CA
caput NDWxxx:username:SIMPLE:VALUE1 5  #This works via standard CA
caput BLOCK1 10  #This is not allowed by the gateway
```

## Creating an Alias Gateway ##

An alias gateway offers three advantages:

It allows access to multiple IOCs running on a single host, regardless of which starts first.
Firewall rules are required only for a single process using known ports
It offers a single place to impose security
In order to prevent the gateway from blocking itself, it needs to be run on a different interface or port from the IOCs it is serving.

To use a different port, start gateway with the options `-sport 5066 -cport 5064` and on the client use set `EPICS_CA_ADDR_LIST=130.246.37.143:5066`

We however are planning to restrict the IOCs to running on the loopback interface by setting:

```
set EPICS_CA_ADDR_LIST=127.255.255.255
set EPICS_CAS_BEACON_ADDR_LIST=127.255.255.255
set EPICS_CAS_INTF_ADDR_LIST=127.0.0.1
```

Note that for multiple IOCs to work, the broadcast address must be used.

Because the clients only use the loopback interface they have no interaction with windows firewall.

The gateway can then be started with:

```
gateway.exe -pvlist pvlist.txt -access access.txt -prefix HOST:gateway -cip 127.255.255.255 -sip 130.246.37.143
```

Since it listens only on the external address and looks for PVs only on the loopback address, there is no need for aliasing for non-standard ports to prevent ambiguity.

Assuming the PVs all start HOST:user, the following pvlist.txt will allow full access to any PV, along with the gateway's internal PVs:

```
EVALUATION    ORDER ALLOW, DENY
HOST:gateway:.*    ALLOW
HOST:user:.*    ALLOW    DEFAULT 0
HOST:user:.*    ALLOW    DEFAULT 1
```

The following `access.txt` allows full access to everything that does not have a group set:

```
ASG(DEFAULT) {
    RULE(0,WRITE)
    RULE(1,WRITE)
}
```

The HOST firewall needs either to allow network access for the gateway program, or rules like:

```
netsh advfirewall firewall add rule name="EPICS" dir=in localport=5064 action=allow protocol=udp
netsh advfirewall firewall add rule name="EPICS" dir=in localport=5064 action=allow protocol=tcp
netsh advfirewall firewall add rule name="EPICS" dir=in localport=5065 action=allow protocol=udp
```
if you want to turn firewall off for some tests you can use
```
netsh advfirewall set allprofiles state off
```



Clients need to point at the correct host:

```
set EPICS_CA_ADDR_LIST=130.246.37.143
```

Any request for a PV starting HOST:user will then be received by the gateway and it will access the IOC.

# EPICS Access Security #

See the [EPICS Application Developer's Guide](http://www.aps.anl.gov/epics/base/R3-15/0-docs/AppDevGuide/node9.html#SECTION00910000000000000000) for more information.

All examples assume you are using the [Simple IOC](#creating-a-simple-ioc) or something similar.

## Simple Example ##

```
UAG(uag) {user1, user2}
HAG(hag) {officePC, instPC}
ASG(DEFAULT) {
  RULE(1,READ)
  RULE(1,WRITE) {
    UAG(uag)
    HAG(hag)
  }
}
```

These rules provide read access to anyone located anywhere and write access to user1 and user2 if they are located at officePC or instPC.

The 1 in `RULE(1,READ)` represents the access level for a field and must be set to 0 or 1. By default, the standard records types are all defined as 1 except for `VAL`, `CMD` and `RES`. For example: it could be configured that everybody can read record fields with 0 access level, and advanced users can read everything:

```
RULE(0,READ)
RULE(1,READ) {
  UAG(uag)
}
```

Having level 1 access automatically includes access to level 0.

To enable security on an IOC, the following needs to be added before iocInit:

```
asSetFilename("C:\absolute_path_to_ioc\iocBoot\iocsimple\security.acf")
```

An absolute file path for the security file should be used.

## Advanced Example ##

```
UAG(local) {user1}
HAG(cabin) {instPC}
UAG(remote) {user2}
HAG(office) {officePC}
ASG(DEFAULT) {
  INPA(simple:value2)
  RULE(1,READ)
  RULE(1,WRITE) {
    UAG(local)
    HAG(cabin)
  }
  RULE(1,WRITE) {
    UAG(remote)
    HAG(office)
    CALC("A=1")
  }
}
```

This rule states that:

- everyone can read the PVs
- user1 can write to PVs from instPC only
- user2 can write to PVs from his office PC, but only if simple:value2 equals 1

## Access Security Groups ##

A record can be added to a specific access security group using the ASG field, otherwise it will be automatically placed in the `DEFAULT ASG`. For example, the following adds the simple:value2 record to the `ACCESS ASG`:

```
record(ai, "simple:value2")
{
    field(ASG, "ACCESS")
    field(VAL, 2)
}
```

The `ACCESS` group can then have different security settings to the `DEFAULT` group. For example, modifying the security file like so:

```
UAG(local) {user1}
HAG(cabin) {instPC}
UAG(remote) {user2}
HAG(office) {officePC}
ASG(DEFAULT) {
  INPA(simple:value2)
  RULE(1,READ)
  RULE(1,WRITE) {
    UAG(local)
    HAG(cabin)
  }
  RULE(1,WRITE) {
    UAG(remote)
    HAG(office)
    CALC("A=1")
  }
}
ASG(ACCESS) {
  RULE(1,WRITE) {
    UAG(local)
    HAG(cabin)
  }
}
```

Now only user1 (on instPC) can read or write to `simple:value2`.

## Changing Permissions Example ##

There are two subroutines (`asSubInit`, `asSubProcess`) that can be used to force the IOC to reload the security settings file. In the .db file add a record like this:

```
record(sub,"reset") {
   field(INAM,"asSubInit")
   field(SNAM, "asSubProcess")
}
```

Set the security file to look something like (change the UAG and HAG details to match your system):

```
UAG(user) {user1}
HAG(office) {officePC}
ASG(DEFAULT) {
  RULE(0,READ)
  RULE(1,WRITE) {
     UAG(user)
     HAG(office)
  }
}
```

Test that it is possible to write to one of the PVs using caget. Next manually remove the write rule from the security file and save it. Type the following:

```
caget reset 1
```

The security settings should now have been reloaded, and it should no longer be possible to write to any of the PVs (including resetting the permissions!).

# Using the Array Subroutine (aSub) #

An `aSub` record is a record that can call a C routine. This record is not used for device communication.

## Creating an IOC that uses aSub ##

A simple example that creates an aSub record that doubles the input value.

Create an IOC in the usual method:

```
makeBaseApp.pl -t ioc asubtest
makeBaseApp.pl -i -t ioc asubtest
```

Move to the `asubtestApp\sr`c directory and create a file called `my_asub_routine.c`. In the new file put (warning: bad C code alert):

```
#include <registryFunction.h>
#include <epicsExport.h>
#include "aSubRecord.h"
#include "stdlib.h"
static long my_asub_routine(aSubRecord *prec) {
    long i;
    double *a, *vala;
    prec->pact = 1;
    //Note: may be an array
    a = (double *)prec->a;
    for(i=0; i < prec->noa; ++i)
    {
        ((double *)prec->vala)[i] = a[i] * 2.0f;
    }
    prec->pact = 0;
    //Debug message - prints to IOC
    //printf("my_asub_routine called");
    return 0;
}
epicsRegisterFunction(my_asub_routine);
```

Create a file called `asubroutine.dbd` and put the following in it:

```
function(my_asub_routine)
```

Open the Makefile, and add the following in the appropriate places:

```
asubtest_DBD += asubroutine.dbd
asubtest_SRCS += my_asub_routine.c
```

Move to the `asubtestApp\Db` directory and create a file called `asubtest.db`. Add the following to it:

```
record(ai, "testasub:value_in")
{
    field(VAL, 1)
    field(FLNK,"testasub:my_asub")
}
record(aSub,"testasub:my_asub")
{
    field(SNAM,"my_asub_routine")
    field(FTA, "DOUBLE")
    field(INPA, "testasub:value_in")
    field (OUTA, "testasub:value_out")
    field (FTVA, "DOUBLE")
}
record(ai, "testasub:value_out")
{
    field(INP, "testasub:my_asub.VALA")
}
```

Return to the IOC's top directory and run make. Assuming it builds successfully, run the IOC and from another command-line try:

```
caput testasub:value_in 5
```

Followed by:

```
caget testasub:value_out
```

The caget should return a value of 10.

NOTE: The aSub record automatically allocates space for input and output values based on NOA and NOVA.

# Adding devIocStats to an IOC #

Assuming `devIocStats` exists in your system and the IOC to be modified is complete (i.e. it builds and runs correctly), follow the following steps to add `devIocStats` to it:

Open `configure\RELEASE` and add `DEVIOCSTATS=YOUR_PATH/devIocStats/3-1-11` with `YOUR_PATH` replaced appropriately.

_Here `DEVIOCSTATS`'s value can only be set to maximum of 256 characters if anything more than 256 characters is used then it will be truncated down to 256 characters. It is due to EPICS environment variables only being able to store up to 256 characters._

Open the `st.cmd` for the IOC and change it to look something like this
```
#!../../bin/windows-x64/MY_IOC
# You may have to change MY_IOC to something else
# everywhere it appears in this file
< envPaths
epicsEnvSet "IOCNAME" "$(P=$(MYPVPREFIX))MY_IOC"               # (1) The IOC name used in PVs
epicsEnvSet "IOCSTATS_DB" "$(DEVIOCSTATS)/db/iocAdminSoft.db"  # (2) The path to devIocStats db to use
cd ${TOP}
# Register all support components
dbLoadDatabase "dbd/MY_IOC.dbd"
MY_IOC_registerRecordDeviceDriver pdbbase
dbLoadRecords("db/my_ioc.db","P=$(IOCNAME)")                   # (3) Pass the IOCNAME to the IOC's db
dbLoadRecords("$(IOCSTATS_DB)","IOC=$(IOCNAME)")               # (4) Load the devIocStats db
cd ${TOP}/iocBoot/${IOC}
iocInit
```

The key changes are highlighted by the numbered comments.

Open `MY_IOCApp\src\Makefile` and add:

```
MY_IOC_DBD += devIocStats.dbd
MY_IOC_LIBS += devIocStats
```

**Additional step:** if there is a dbd file in `MY_IOCApp\src`, then you might need to add include "devIocStats.dbd" to it.

Finally rebuild the IOC (make clean uninstall followed by make)

# Creating a Sequencer #

## Create an IOC ##

```
mkdir seqex
cd seqex
makebaseapp.pl -t ioc seqex
makebaseapp.pl -i -t ioc seqex
```

## Create additional files ##

```
cd seqexApp/db
echo. 2> seqex.db
cd ..
cd src
echo. 2> sncProgram.st
echo. 2> sncExample.stt
echo. 2> sncExample.dbd
```

## Modify the files ##

## seqexApp/db/seqex.db ##

```
record(ai, "$(user):aiExample")
{
        field(DESC, "Analog input")
        field(INP, "$(user):calcExample.VAL  NPP NMS")
        field(EGUF, "10")
        field(EGU, "Counts")
        field(HOPR, "10")
        field(LOPR, "0")
        field(HIHI, "8")
        field(HIGH, "6")
        field(LOW, "4")
        field(LOLO, "2")
        field(HHSV, "MAJOR")
        field(HSV, "MINOR")
        field(LSV, "MINOR")
        field(LLSV, "MAJOR")
}
record(calc, "$(user):calcExample")
{
        field(DESC, "Counter")
        field(SCAN,"1 second")
        field(FLNK, "$(user):aiExample")
        field(CALC, "(A<B)?(A+C):D")
        field(INPA, "$(user):calcExample.VAL  NPP NMS")
        field(INPB, "9")
        field(INPC, "1")
        field(INPD, "0")
        field(EGU, "Counts")
        field(HOPR, "10")
        field(HIHI, "8")
        field(HIGH, "6")
        field(LOW, "4")
        field(LOLO, "2")
        field(HHSV, "MAJOR")
        field(HSV, "MINOR")
        field(LSV, "MINOR")
        field(LLSV, "MAJOR")
}
```

## seqexApp/db/Makefile ##

Add:

```
DB += seqex.db
```

## seqexApp/src/sncProgram.st ##

```
#include "../sncExample.stt"
```

## seqexApp/src/sncExample.stt ##

```
program sncExample
double v;
assign v to "{user}:aiExample";
monitor v;
ss ss1 {
        state init {
        when (delay(10)) {
                printf("sncExample: Startup delay over\n");
        } state low
        }
        state low {
        when (v > 5.0) {
                printf("sncExample: Changing to high\n");
        } state high
        }
        state high {
        when (v <= 5.0) {
                printf("sncExample: Changing to low\n");
        } state low
        }
}
```

## seqexApp/src/sncExample.dbd ##

```
registrar(sncExampleRegistrar)
```

## build.mak (if using ISIS build) or Makefile (if not) ##

Add:

```
ifneq ($(SNCSEQ),)
        # Build sncExample
        sncExample_SNCFLAGS += +r
        $(APPNAME)_DBD += sncExample.dbd
        $(APPNAME)_SRCS += sncExample.stt
        $(APPNAME)_LIBS += seq pv
endif
```

## configure/RELEASE ##

Make sure there is a uncommented line like below but with the correct path for your system:

```
SNCSEQ=PATH_TO_YOUR_SEQ_INSTALLATION
```

## iocBoot/iocseqex/st.cmd ## 

Uncomment and adjust the dbLoadrecords line, e.g:

# Load our record instances

```
dbLoadRecords("db/seqex.db","user=yournameHost")
```

Uncomment and adjust the seq line, e.g.:

```
## Start any sequence programs
seq sncExample,"user=yourname3Host"
```

## Build the IOC ##

Build and run the IOC as normal.