Asyn provides an echo driver that will return on a read what was last provided by a write. This can
be used for some very basic stream device testing / simulation e.g. if the real function is

```
getFrequency {
    out "FREQ?"; in "%f";
}
```

Then by connecting the device to the echo driver you could write

```
Terminator = ETX;

getFrequency {
    out "10.0"; in "%f";
}
```

Note, you must have a terminator otherwise the echo driver gets confused and won't work.

Potentially you could have both a real  `getFrequency()`  and a dummy `getFrequencyTest()` function in the protocol file and then control with one was used by writing   `getFrequency$(TEST=)`   in the DB file and setting  `TEST=Test`   with `dbLoadRecords() `

To enable support for the echo driver in a Makefile:
* Add  **`asynEcho`** to $(APPNAME)_LIBS
* Add  **`drvAsynEcho.dbd`**  to $(APPNAME)_DBD

And then in st.cmd use e.g.:

```
echoDriverInit(“L0”, 0.1, 0, 0)
```

Where L0 is the asyn port name and 0.1 is, in this case, how long to take to return a reply (**this must be greater than zero**). The other options allow selecting `noautoconnect` or multi-device if required.

