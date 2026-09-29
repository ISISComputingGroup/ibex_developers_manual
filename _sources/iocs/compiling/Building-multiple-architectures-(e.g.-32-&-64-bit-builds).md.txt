# Building multiple architectures (e.g. 32/64-bit builds)

```{note}
This page documents an advanced compilation workflow.

These instructions are unnecessary for a "standard" build
```

The EPICS build system allows you to have multiple architectures present in the same source tree, architecture independent files are built in O.Common and architecture dependent ones built in O.windows-x64 and O.win32-x86 etc. 

Running `config_env` selects a default `EPICS_HOST_ARCH` for builds, and typing "make" or running "build.bat" will use this. Any IOCs and start_ibex_server will also use this.

The safe way to build another architecture in the same (or different) tree is to:
- Open a new command plain command windows (don't use an `epicsterm` link) and run `config_env` with the new architecture e.g. `config_env.bat win32-x86`
- This build tree will now default to your new architecture until you change it with `config_env` as above
- you can now `make` or `build.bat`

**Note:** it used to be possible to just pass a new architecture to `build.bat` e.g. `build.bat win32-x86` but it looks like recent software packages don't support this and it will need looking at if it is to work again. So use above instead.
 
If you need a 32 bit build in a hurry check out using a [Developer Server Build](Developer-Server-Build)
