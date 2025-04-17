> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Stream Device Tips and Tricks

# Waveforms

With any waveform record protocol, you need to specify a separator to split the input or output string. For example, to split on commas use `separator = ",";` within the protocol function for the record. See https://paulscherrerinstitute.github.io/StreamDevice/tipsandtricks.html

## Reading in a string into a waveform of strings

If you have a waveform record of `FTVL` `STRING`, then you have to be careful about which formatter you use to read in that string.

Instead of using `%s` as your formatter, you need to use a character set, e.g. `%[A-Z0-9a-z.+-]`, which does not include the separator you are splitting on. If you use `%s`, then the whole string will be read into the zeroth element of the array, and won't be split on the separator.

## Dealing with enums

The record type for enums in EPICS is mbbo/mbbi. However, StreamDevice also provides [support for enums within the protocol file](https://paulscherrerinstitute.github.io/StreamDevice/formats.html#enum).

The way that the `mbbo` works is that it takes a user set value into the `VAL` field and uses it to lookup a value to output based on `ZRVL`, `ONVL` etc. this is outputted to the `RVAL` field. The value in `RVAL` is then passed to the protocol file, which could also have an enum specified. This effectively means that you have two enums stacked on top of each other and is BAD. Not only does it reduce readability it has historically caused issues when StreamDevice was modified to take into account `RVAL`, see [here](https://github.com/ISISComputingGroup/IBEX/issues/5263). It is up to the developer whether the enum should be defined in the protocol or the record but you should only use one.

On the record side the `mbbi` works in the same way as the `mbbo` but in reverse. However, the behaviour for an `mbbi` in StreamDevice is not symmetrical with `mbbo`, which you can see by comparing [here](https://paulscherrerinstitute.github.io/StreamDevice/mbbi.html) and [here](https://paulscherrerinstitute.github.io/StreamDevice/mbbo.html) under the ENUM behaviour. This effectively means the enum defined in `mbbi` is ignored in StreamDevice so you are forced to use the protocol for defining this.  

# Multi-value Protocols

## Dealing with multi-value stream device protocols

It often happens that a single read query to a device returns multiple values, which we ultimately need to store in separate PVs. Similarly, sometimes a single write command requires multiple values. Below are some tips on how to deal with multi-value read protocols, but the same kind of tricks can be applied to write protocols too.

If all the values are the same format, you could read them into a `waveform` or `aai` record using the `separator` as described above, and then split them or manipulate after than e.g. `acalcout`, `calcout` or `scalcout`

### Passing the PV names as protocol parameters

Here is an example of record redirection, where a single status read query returns three different values, which correspond to three different PVs. The first PV triggers the protocol, and in doing so passes the name of the second and third PVs as arguments to the protocol:

```
## Read the status value 1. This also populates the status value 2 and 3.

record(ai, "$(P)VALUE1") {
  field(DESC, "Status value 1")
  field(DTYP, "stream")
  field(INP, "@ls336.proto getValues($(P)VALUE2,$(P)VALUE3) $(PORT)")
  field(SCAN, "$(SCAN) second")
}

## Read the status value 2.
record(bi, "$(P)VALUE2") {
  field(DESC, "Status value 2")
  field(ZNAM, "Off")
  field(ONAM, "On")
}

## Read the status value 3.
record(bi, "$(P)VALUE3") {
  field(DESC, "Status value 3")
  field(ZNAM, "OK")
  field(ONAM, "Error")
}
```

The corresponding protocol would be:

```
getValues {
   out "VALUES?";
   in "%f,%(\$1)d,%(\$2)d";
}
```

where `\$1` and `\$2` indicate the first and second argument, respectively. The protocol will redirect the second and third value to the PVs specified.

As our PV prefix `$(P)` tends to be quite long, often the `INP` field calling the protocol ends up being longer than the max number of allowed characters. We can shorten the `INP` field by passing the prefix as a separate argument (and remove blank spaces between arguments!):

```
...
field(INP, "@ls336.proto getValues($(P),VALUE2,VALUE3) $(PORT)")
```

and the prefix can be pre-pended to the PV names inside the protocol:

```
...
in "%f,%(\$1\$2)d,%(\$1\$3)d";}
```

You need to keep in mind that PVs that are using this method can not be tested in RecSim. This is because with this method only one PV has a SCAN and INP field, while the other updated records do not have these fields. Therefore, they can not be updated unless the protocol method is called. But in RecSim the protocol is not used at all, so these PVs can not be set in RecSim.

If the protocol returns many values, even this approach may result in too long `INP` fields. One solution would be to pass the prefix `$(P)` as an argument and hard-code the rest of the PV names inside the protocol, but we try to avoid this as much as possible as it introduces extra coupling between the protocol and the db file. Read on for other tricks!

### Reading into the inputs of a calc record

If you can't fit all the PV names in a single INP field, you can redirect them to the input fields of a `calc` record instead. We need a trigger PV which calls the protocol, and a buffer `calc` record to temporarily store the parsed values. The final PVs can then fetch their values from the `calc` record:

```
## Trigger the read protocol. Parsed values are stored in a buffer calc PV.
record(bi, "$(P)READ_DO") {
  field(DTYP, "stream")
  field(INP, "@ls336.proto getValues($(P)BUFFER) $(PORT)")
  field(SCAN, "$(SCAN) second")
}

## Store the parsed values
record(calc, "$(P)BUFFER") {
  field(CALC, "0")
}

## 
## Read the status value 1. 
##
record(ai, "$(P)VALUE1") {
  field(INP, "$(P)BUFFER.A CP")
  ...
}

## 
## Read the status value 2.
##
record(bi, "$(P)VALUE2") {
  field(INP, "$(P)BUFFER.B CP")
  ...
}

## 
## Read the status value 3.
##
record(bi, "$(P)VALUE3") {
  field(INP, "$(P)BUFFER.C CP")
  ...
}
```

and the protocol becomes:

```
...
in "%(\$1.A)f,%(\$1.B)d,%(\$1.C)d";
```

If you have to read strings as well as numbers, you can always use a `scalcout` record instead of a `calc`.

### ... and if everything fails

Another way is to read the entire input as a string into a `string` record, and then use various `scalcout` or `asub` records to parse the individual bits and pieces. An example of this usage can be found in the Linkam95 IOC. 

### Other considerations

The error on disconnection is not passed through from stream and so you may consider doing this via the error setter; see [IOC Utilities](IOC-Utilities#error-setting) for details.

Useful links:

https://paulscherrerinstitute.github.io/StreamDevice/index.html