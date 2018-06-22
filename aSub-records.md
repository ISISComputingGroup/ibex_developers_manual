# Introduction
aSub records are useful when the output of a device is too complicated to be reasonably parsed in .protocol files.


# DB records



# Build files
Declare a `.dbd` file with the names of all the functions declared in the `C` file which will be called by EPICS.

```
function(function_name)
function(another_function_name)
[...]
```

In the make file references need to be added for the `.dbd` file and the `C` code:

```
DBD += dbd_filename.dbd

$(APPNAME)_SRCS_DEFAULT += c_sources.c
```

# C code
Need to define a C function which will be called by the aSub record:

```
static long function_name(aSubRecord *prec)
{
    return 0;
}
```

Need to tie in this function to the epics database with a call to `epicsRegisterFunction`:
```
epicsRegisterFunction(function_name);
```

# Escaping to C++

# C++ code