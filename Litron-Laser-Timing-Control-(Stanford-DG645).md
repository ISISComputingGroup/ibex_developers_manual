Litron Laser Timing Control is an extension of the DG645 IOC made for HIFI to use. It replaces the LabView functionality as described [here](https://github.com/ISISComputingGroup/IBEX/issues/6089#issuecomment-2102423879).

![image](https://github.com/user-attachments/assets/54ddca66-99a6-4e71-94cc-713110807a5f)

## Delay & Offset

By setting a delay and offset the following calculation is done. 

`dC_0 = Delay + Offset` in `us`

Under the following constraints:

```
If mode is 1:
    if dC_0 + Delay + Offset > 39900 us
        or Delay + Offset < 0 us
    then:
        Error State
  
If mode is 2:
    if Delay + Offset > 39900 us
        or dC_0 + Delay + Offset <= 0 us
    then:
        Error State
```

## Mode

When the user tries to set the mode then the following is applied:

```
If IOC mode is 1 or 2 then:
    Set device mode to be 1 or 2 respectively

else: # IOC mode is auto

    if Delay > Offset then:
        Set device mode to 1

    else:
        Set device mode to 2
```
Note that IOC mode is not the same as device mode. IOC mode refers to a value of `auto` or `1` or `2`, the device mode refers to which configuration/setting slot the DG645 is in (0-9). IOC mode 1 and 2 refers to device setting slots 1 and 2.
