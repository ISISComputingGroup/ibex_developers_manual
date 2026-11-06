# `raw_data_1/isis_vms_compat`

This has an `NX_class` of `IXvms`; this is not a class specified by upstream NeXus definitions.

Data under these groups are provided to aid backwards-compatibility with older analysis programs.

:::{seealso}
See also {download}`libget.txt`
:::

### `raw_data_1/isis_vms_compat/HDR`

This is the "header block". Is is a fixed-size 80 character string.

```
   P    1       HDR(1:8)        c*8     RUN identifier (eg. LAD12345 )
                                         -  3 characters for INSTRUMENT,
                                         -  5 characters for RUN NUMBER.)
   U            HDR(9:28)       c*20    User name                      
   U            HDR(29:52)      c*24    Experiment short title         
   P            HDR(53:64)      c*12    start date                     
   P            HDR(65:72)      c*8     start time                     
                HDR(73:80)      c*8     run duration (µA.Hr)    
```

### `raw_data_1/isis_vms_compat/VER1`

```
   F    2       VER1            I*4     format version number (ver=2)   ***B   
```

### `raw_data_1/isis_vms_compat/ADD`

```
   P    3       ADD(1)          I*4     start address of RUN  section
   P            ADD(2)          I*4     start address of INST section
   P            ADD(3)          I*4     start address of SE   section
   P            ADD(4)          I*4     start address of DAE  section
   P            ADD(5)          I*4     start address of TCB  section
   P            ADD(6)          I*4     start address of USER section   ***B
   P            ADD(7)          I*4     start address of DATA section   ***B
   P            ADD(8)          I*4     start address of LOG  section   ***B
		ADD(9)          I*4  	spare
```

### `raw_data_1/isis_vms_compat/FORM`

```
		FORM		I*4	data format flag (0 or 1)       ***C
					0 - all TC for each spectrum
					1 - the same TC from every spectrum 
```

### `raw_data_1/isis_vms_compat/VER2`

```
   F    1       VER2            I*4     RUN section version number
```

### `raw_data_1/isis_vms_compat/RUN`

```
   P    2       RUN             I*4     run number (starting from 1)
```

### `raw_data_1/isis_vms_compat/TITL`

```
   U    3       TITL            C*80    run title
```

### `raw_data_1/isis_vms_compat/USER`

```
   U    2       USER(1)         C*20    user name
   U            USER(2)         C*20    user telephone no. 1(day)
   U            USER(3)         C*20    user telephone no. 2(day)       
   U            USER(4)         C*20    user telephone no. (night)
   U            USER(5)         C*20    user institution
                                C*20(3) spare
```

### `raw_data_1/isis_vms_compat/IRBP` / `RRBP` / `CRBP`

`IRBP` and `RRBP` represent the `RBP` table, represented as integer and float types respectively.

- `IRPB` is an integer representation of this data
- `RRBP` is a float representation
- `CRBP` is a string representation. Non-printable characters, `\0`, and any character outside the ASCII range are replaced with the `?` character. The string is then null-terminated.

```
   P    4       RPB(1)          I*4     actual run duration 
   U            RPB(2)          I*4     scaler for RPB(1),(22) (1=sec,..)
   U            RPB(3)          I*4     test interval of RPB(2) (sec)
   U            RPB(4)          I*4     dump interval
   U            RPB(5)          I*4     scaler for RPB(4)
   U            RPB(6)          I*4     test interval of RPB(5)(sec)
   U            RPB(7)          I*4     2**k (SNS frequency(Hz)=50/2**k) 
   P            RPB(8)          R*4     good proton charge (uA.hr)
   P            RPB(9)          R*4     total proton charge (uA.hr)
   P            RPB(10)         I*4     number of 'good' frames         
   P            RPB(11)         I*4     total number of frames
   U            RPB(12)         I*4     required run duration(units=RPB(1))***B
   P            RPB(13)         I*4     actual run duration (seconds)      ***B
   P            RPB(14)         I*4     monitor sum 1
   P            RPB(15)         I*4     monitor sum 2
                RPB(16)         I*4     monitor sum 3
   P            RPB(17-19)      C*12    finish date (dd-mmm-yyyy_)      
   P            RPB(20-21)      C*8     finish time (hh-mm-ss)          
		        RPB(22)		    I*4	    RAL Proposal Number
                RPB(- 32)       spare
```

### `raw_data_1/isis_vms_compat/VER3`

```
   F    1       VER3            I*4     INSTRUMENT section version no.(=2) ***B
```

### `raw_data_1/isis_vms_compat/NAME`

```
   F    2       NAME            C*8     instrument name
```

### `raw_data_1/isis_vms_compat/IVBP` and `raw_data_1/isis_vms_compat/RVBP`

`IVPB` and `RVBP` represent the `IVPB` table, represented as integer and float types respectively.

```
        3               INSTRUMENT VARIABLE PARAMETER BLOCK
   U            IVPB(1)         R*4     frequency chopper 1     (Hz)
   U            IVPB(2)         R*4     frequency chopper 2     (Hz)
   U            IVPB(3)         R*4     frequency chopper 3     (Hz)
   U            IVPB(4)         I*4     delay c1                (µs)
   U            IVPB(5)         I*4     delay c2                (µs)
   U            IVPB(6)         I*4     delay c3                (µs)
   U            IVPB(7)         I*4     max error on delay c1   (µs)
   U            IVPB(8)         I*4     max error on delay c2   (µs)
   U            IVPB(9)         I*4     max error on delay c3   (µs)
   U            IVPB(10)        I*4     apperture c1            
   U            IVPB(11)        I*4     apperture c2            
   U            IVPB(12)        I*4     apperture c3           
   U            IVPB(13)        I*4     status c1  (run,stopped,stop open)
   U            IVPB(14)        I*4     status c2  (run,stopped,stop open)
   U            IVPB(15)        I*4     status c3  (run,stopped,stop open)
   U            IVPB(16)        I*4     main shutter (open=1)
   U            IVPB(17)        I*4     thermal shutter( " )
   U            IVPB(18)        R*4     beam apperture horizontal(mm)   
   U            IVPB(19)        R*4     beam apperture vertical(mm)     
   U            IVPB(20)        I*4     scattering posn.(eg 1or2 HRPD)
   U            IVPB(21)        I*4     moderator type no. (e.g HET=3)
   U            IVPB(22)        I*4     detector tank vacuum (1=vacuum on) 
   U            IVPB(23)        R*4     L1                              
        	    IVPB(24)	I*4	Rotor Frequency			HET
                IVPB(25)	R*4	Rotor Energy			HET
                IVPB(26)	R*4	Rotor Phase			HET
                IVPB(27)	I*4	Rotor Slit Package (0="unknown",1="L",2="Med", 3="Hi") 		HET
                IVPB(28)	I*4	Slow Chopper (1=on,0=off)	HET
                IVPB(29)	R*4	LOQ X centre			LOQ
                IVPB(30)	R*4	LOQ Y centre			LOQ
                IVPB(31)	I*4	Beam stop			LOQ
                IVPB(32)	R*4	Radius Beam Stop		LOQ
                IVPB(33)	R*4	Source to detector distance	LOQ
                IVPB(34)	R*4	FOE angle			LOQ
                IVPB(35)	R*4	Angle of Incidence		CRISP
	            IVPB( - 64)             spare
```

### `raw_data_1/isis_vms_compat/NDET`

```
   U    4       NDET    I*4             no.  of detectors
```

### `raw_data_1/isis_vms_compat/NMON`

```
   U    5       NMON    I*4             no.  of monitors 
```

### `raw_data_1/isis_vms_compat/NUSE`

```
   U    6       NUSE    I*4             no. of UTn  tables                 ***B
```

### `raw_data_1/isis_vms_compat/MDET`

```
   U    7       MDET    I*4(nmon)       detector nos. of the monitors  
```

### `raw_data_1/isis_vms_compat/MONP`

```
   U    8       MONP    I*4(nmon)       prescale values for the monitors 
```

### `raw_data_1/isis_vms_compat/VER4`

```
   F    1       VER4    I*4             SE section version #    (=2)
```

### `raw_data_1/isis_vms_compat/SPB` / `ISPB` / `RSPB` and `
CSPB`

- `SPB` and `ISPB` are identical integer representations of this data
- `RSPB` is a float representation
- `CSPB` is a string representation. Non-printable characters, `\0`, and any character outside the ASCII range are replaced with the `?` character. The string is then null-terminated.

```
        2                               SAMPLE PARAMETER BLOCK
   U            SPB(1)  I*4             position of sample changer
   U            SPB(2)  I*4             sample type     (1 = sample+can
                                                         2 = empty can
                                                         3 = vanadium
                                                         4 = absorber
                                                         5 = nothing
							 6 = sample, no can)
   U            SPB(3)  I*4             sample geometry (1 = cylinder 
                                                         2 = flat plate
                                                         3 = HRPD slab)
   U            SPB(4)  R*4             sample thickness normal to sampl.(mm)
   U            SPB(5)  R*4             sample height (mm)
   U            SPB(6)  R*4             sample width (mm)
   U            SPB(7)  R*4             omega sample angle (deg)
   U            SPB(8)  R*4             psi sample angle (deg)
   U            SPB(9)  R*4             phi sample angle (deg)      
   U            SPB(10) R*4             scat.geom.(1=trans.2=reflect.      ***B
   U            SPB(11) R*4             sample sCOH (barns)            ***B
   U            SPB(12) R*4             sample sINC (barns)            ***B
   U            SPB(13) R*4             sample sABS (barns)            ***B
   U            SPB(14) R*4             sample number density (atoms.A-3)
   U            SPB(15) R*4             can wall thickness (mm)            ***B
   U            SPB(16) R*4             can    sCOH (barns)             ***B
   U            SPB(17) R*4             can    sINC (barns)             ***B
   U            SPB(18) R*4             can    sABS (barns)             ***B
   U            SPB(19) R*4             can   number density (atoms.A-3)
   U            SPB(20) C*40            sample name or chemical formula
                SPB( -64)               spare
```

### `raw_data_1/isis_vms_compat/NSEP`

:::{note}
This is unconditionally written as zero.
:::

```
   F=0  3       NSEP    I*4             no. of SE parameters            
```

### `raw_data_1/isis_vms_compat/VER5`

```
   F    1       VER5    I*4             DAE section version #   (=2)          
```

### `raw_data_1/isis_vms_compat/DAEP`

```
        2               DAE PARAMETER BLOCK
   U            DAEP(1) I*4             Word length in bulk store memory  
   F            DAEP(2) I*4             Length of bulk store memory (bytes)**A
   U            DAEP(3) I*4             PPP minimum value                  ***B
   P            DAEP(4) I*4             good PPP total (high 32 bits)   ***B
   P            DAEP(5) I*4             good PPP total (low  32 bits)   ***B
   P            DAEP(6) I*4             raw  PPP total (high 32 bits)   ***B
   P            DAEP(7) I*4             raw  PPP total (low  32 bits)   ***B
   P            DAEP(8) I*4             good ext. neut tot (high 32bits)***B
   P            DAEP(9) I*4             good ext. neut tot (low  32 bits)***B
   P            DAEP(10) I*4            raw  ext. neut tot (high 32 bits)***B
   P            DAEP(11) I*4            raw  ext. neut tot (low  32 bits)***B
   P            DAEP(12) I*4            ext. neutron gate (t1) (µs)   ***B
   P            DAEP(13) I*4            ext. neutron gate (t2) (µs)   ***B
   U            DAEP(14) I*4            detector for MON 1  (12 bits)   ***B
   U            DAEP(15) I*4            module   for MON 1  ( 4 bits)   ***B
   U            DAEP(16) I*4            crate    for MON 1  ( 4 bits)   ***B
   U            DAEP(17) I*4            mask     for MON 1  (c4:m4:d12) ***B
   U            DAEP(18) I*4            detector for MON 2  (12 bits)   ***B
   U            DAEP(19) I*4            module   for MON 2  ( 4 bits)   ***B
   U            DAEP(20) I*4            crate    for MON 2  ( 4 bits)   ***B
   U            DAEP(21) I*4            mask     for MON 2  (c4:m4:d12) ***B
   P            DAEP(22) I*4            total GOOD EVENTS (high 32 bits)***B
   P            DAEP(23) I*4            total GOOD EVENTS (low  32 bits)***B
   P            DAEP(24) I*4            frame synch delay (4µs steps) ***B
   U            DAEP(25) I*4            frm snch origin(0:none/1:ext/2:int)***B
   U		DAEP(26) I*4		Secondary Master Pulse (0:en,1:dis)
   U		DAEP(27-29) I*4		External vetoes 0,1,2 (0 dis,1 en)
                DAEP( -64)              Spare        
```

### `raw_data_1/isis_vms_compat/VER6`

```
   F    1       VER6    I*4             TCB secton version #
```

### `raw_data_1/isis_vms_compat/NTRG`

```
   U/P  2       NTRG    I*4             # of time regimes (normally =1)
```

### `raw_data_1/isis_vms_compat/NFPP`

```
   F=1  3       NFPP    I*4             # of frames per period          
```

### `raw_data_1/isis_vms_compat/NPER`

```
   F=1  4       NPER    I*4             # of periods      
```

### `raw_data_1/isis_vms_compat/PMAP`

```
   F=1  5       PMAP    I*4(256)        period # for each basic period  
```

### `raw_data_1/isis_vms_compat/NSP1`

```
   U/P  3       NSP1    I*4             No. of spectra (+1 for zeroth)  
```

### `raw_data_1/isis_vms_compat/NTC1`

```
   U/P  4       NTC1    I*4             No. of time channels ( " )      
```

### `raw_data_1/isis_vms_compat/TCM1`

```
   U    5       TCM1    I*4(5)          time chan. mode (see footnote)
   
    TIME CHANNEL MODES:
        0       Boundaries set by a table held in file TCB.DAT

        1       TCB1(n) = (TCP1(1) + (n-1)*TCP1(2)-DAEP(24)*4)*32/PRE1
                        (ie. Dt = c )
                        (ie. less frm.synch delay)

        2       temp(1)  = TCP1(1)
                TCB1(1)  = (TCP1(1)-DAEP(24)*4)*32/PRE1 (ie. Dt = c.t
                temp(n+1)= temp(n)*(1 + TCP1(2))
                TCB1(n+1)= (temp(n+1) - DAEP(24)*4)*32/PRE1
```

### `raw_data_1/isis_vms_compat/TCP1`

```
   U    6       TCP1    R*4(4,5)                time chan. parameters (µs)
```

### `raw_data_1/isis_vms_compat/PRE1`

```
   P    7       PRE1    I*4             prescale value for 32MHz clock (<=15)
```

### `raw_data_1/isis_vms_compat/VER7`

```
        1       VER7    I*4             DATA version #
```

### `raw_data_1/isis_vms_compat/ULEN`

:::{note}
This is unconditionally written as zero.
:::

```
        2       ULEN    I*4             USER_LEN
```

### `raw_data_1/isis_vms_compat/VER9`

Undocumented. Written as `2` (int32).

### `raw_data_1/isis_vms_compat/NTNL`

Undocumented. Written as `0` (int32).

### `raw_data_1/isis_vms_compat/NTLL`

Undocumented. Written as `0` (int32).

### `raw_data_1/isis_vms_compat/NOTE`

Unconditionally written as the string `"No notes were made"`.

### `raw_data_1/isis_vms_compat/TTHE`

```
   U    13      TTHE    R*4(ndet)       2Theta table (scattering angle)
```

### `raw_data_1/isis_vms_compat/SPEC`

```
   U    9       SPEC    I*4(ndet)       spectrum # table
```

### `raw_data_1/isis_vms_compat/DELT`

```
   U    10      DELT    R*4(ndet)       'HOLD OFF' in (µs)           ***B
```

### `raw_data_1/isis_vms_compat/LEN2`

```
   U    11      LEN2    R*4(ndet)       L2  table (m) (upstrem monitors -ve.
```

### `raw_data_1/isis_vms_compat/CODE`

```
   U    12      CODE    I*4(ndet)       code to define use of UT values    ***B
```

### `raw_data_1/isis_vms_compat/CRAT`

```
   U    3       CRAT    I*4(ndet)       crate no.for each detector
```

### `raw_data_1/isis_vms_compat/MODN`

```
   U    4       MODN    I*4(ndet)       module no. for each detector
```

### `raw_data_1/isis_vms_compat/MPOS`

```
   U    5       MPOS    I*4(ndet)       posn. in module for each detector
```

### `raw_data_1/isis_vms_compat/UDET`

```
   U    7       UDET    I*4(ndet)       'USER DETECTOR #' for each det ***B
```

### `raw_data_1/isis_vms_compat/TIMR`

```
   U    6       TIMR    I*4(ndet)       TIME REGIME # table
```

### `raw_data_1/isis_vms_compat/UT01` - `UT99`

There are `NUSE` user-tables defined.

```
   3       15   UT01    R*4(ndet)       USER defined table 1              ***B
    ..cont. to  UTn
```
