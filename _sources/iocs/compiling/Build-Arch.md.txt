# Build Arch

```{note}
This page documents an advanced compilation workflow.

These instructions are unnecessary for a "standard" build
```

Build a directory under a given architecture instead of the default. This will switch the architecture temporarily to a given state for building. You can build multiple architectures within the same tree of EPICS (it will be built into `bin/<architecture>`). Run:

``` 
    build_arch <architecture>
```

e.g. build_arch windows-x64-static

Architectures allowed are given my the files in `EPICS/base/master/configure/os/CONFIG.<architecture>.Common`

NB You must build `EPICS/base` in the given architecture first.
