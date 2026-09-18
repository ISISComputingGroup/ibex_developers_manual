# Static Builds

```{note}
This page documents an advanced compilation workflow.

These instructions are unnecessary for a "standard" build
```

Static builds are where all the code is built into the executable and not sometimes loaded at runtime from a shared DLL. Thus statically linked executables will be much bigger than ones using DLLs, but will have less dependencies.

Though we don't use them directly in IBEX, it is a future option and it is useful to keep the ability to use them. It also makes our dependencies much clearer in the following way. If IOC A depends on library B and library B depends on library C then creating a DLL for library B will hide the library C dependency from IOC A, you only need to link against B as C will be activated at runtime automatically. For a static build as everything must be put into A you must add library C to the IOC Makefile.

In IBEX we will often see this when adding the "calc" module - this has a dependency on the "sscan" module, so you need to add both "calc" and "sscan" to _LIBS for windows-x64-static builds to work, the windows-x64 builds will work fine with just "calc" added to _LIBS
