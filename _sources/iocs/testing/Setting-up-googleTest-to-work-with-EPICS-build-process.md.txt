# Google Test

This is a guide to set up googleTest with EPICS at ISIS. This allows you to write C++ unit tests for your C/C++ code in an IOC. Examples of IOCs that run tests like this are the [Keithley 2001](https://github.com/ISISComputingGroup/EPICS-Keithley_2001) and the [cryosms](https://github.com/ISISComputingGroup/EPICS-Cryosms).

## Contents
* [Introduction](#googletest_intro)
* [Release file](#googletest_release_file)
* [Building the test runner](#googletest_building_test_runner)
* [Running your tests](#googletest_running_tests)
* [Sample Test](#googletest_sample)
* [Adding a target to run tests](#googletest_external_dependencies)
* [Troubleshooting](#googletest_troubleshooting)


{#googletest_intro}
## Introduction

You will need to have the `googleTest` support submodule and built the master branch. This will create a `gtest.lib` which you can link against.

More information on googleTest can be found at https://github.com/abseil/googletest. We are using version 1.8.x currently at ISIS.

Good places to start on how to write tests using googleTest is [here](https://github.com/abseil/googletest/blob/master/googletest/docs/primer.md). 

More advanced usage (including `ASSERT_THROWS`, `ASSERT_NO_THROW` and `ASSERT_DOUBLE_EQ`) can be found [here](https://github.com/abseil/googletest/blob/master/googletest/docs/advanced.md). 

Examples can be found [here](https://github.com/abseil/googletest/blob/master/googletest/docs/samples.md).

{#googletest_release_file}
## Release file

Remember to add the path to the Google Test support module in your support module Release file (in `configure/Release`).

```
GTEST=$(SUPPORT)/googletest/master
```

{#googletest_building_test_runner}
## Building the test runner

Make sure you include the following lines in your Makefile alongside the source code to create a test runner executable.

```Makefile
ifeq ($(findstring 10.0,$(VCVERSION)),)
# googleTest Runner

GTESTPROD_HOST+= runner
GTESTS += runner
endif
```

Note: you should exclude the line `GTESTS += runner` if you are using `run_tests.bat` as described below (i.e. if your tests need external dependencies). This is the line that tells the default `runtests` makefile target to include this test.

You then need to include all the files you need for your tests using 
```Makefile
runner_SRCS += #names of test files and source files
```

If your tests are in a different directory to your source files, you can add that directory to your SRCs path using 

```Makefile
SRC_DIRS += #path to your tests directory
```

{#googletest_running_tests}
## Running your tests

Once built you can run the tests by doing `make runtests` in your submodule. This will print the test results and also save them to an xml file in `src/O.$(EPICS_HOST_ARCH)`. This file will be picked up by Jenkins.

{#googletest_sample}
## Sample Test

The following below is a sample test file

```C++
#include "gtest/gtest.h"

namespace {
    TEST(Sample, this_is_a_sample_test){
        ASSERT_EQ(1+1, 2);
    }
} // namespace

```

{#googletest_external_dependencies}
## Tests with external dependencies

In some cases you may want to write unit tests that depend on other EPICS modules e.g. `asyn`. To do this you will need to create the required dlls and run the tests manually. First in your makefile in `src` add the following lines at the bottom:
```Makefile
ifdef T_A
install: dllPath.bat

dllPath.bat:
	$(CONVERTRELEASE) -a $(T_A) -T $(IOCS_APPL_TOP) $@
endif
```

Then in the top of your submodule create `run_tests.bat` that looks like:
```bat
@echo off
setlocal
set "ARCH=%1"
set "TESTPATH=%~dp0<IOC_NAME>App/src/O.%ARCH%"
if exist "%TESTPATH%\runner.exe" (
    call %TESTPATH%\dllPath.bat
    %TESTPATH%\runner.exe --gtest_output=xml:./test-reports/TEST-<IOC_NAME>.xml
) else (
    @echo No tests to run
)
```
Then in the top makefile you will need to override the `runtests` rule by adding in:
```Makefile
.PHONY: runtests

runtests:
	run_tests.bat $(EPICS_HOST_ARCH)
```
An example of an IOC that does this is the [cryosms](https://github.com/ISISComputingGroup/EPICS-Cryosms).

{#googletest_troubleshooting}
## Common issues

### Tests pass but error afterwards "Cannot detect source of runner.run"

You may need to include the line `-include $(GTEST)/cfg/compat.RULES_BUILD` at the end of your Makefile, note the leading `-` which is to make the include optional, this is to stop failures on a global `make clean` when `$(GTEST)/cfg` will get removed before the module is processed. 