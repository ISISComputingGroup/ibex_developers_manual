This is a guide to set up googleTest with EPICS at ISIS. This allows you to write C++ unit tests for your C/C++ code in an IOC.

# Google Test Module

You will need to have the `googleTest` support submodule and built the master branch. This will create a `gtest.lib` file which you can link against.

# Release file addition

Remember to add the path to the google test support module in your release file. E.g.

```
GTEST=$(SUPPORT)/googletest/master
```

# Src Makefile

Make sure you include the following lines in your make file to create a test runner executable.

```
# googleTest Runner

TESTPROD_HOST += runner
USR_CPPFLAGS += -I$(GTEST)/googletest/include 
runner_SRCS += run_all_tests.cc
runner_LIBS += gtest
```

where `run_all_tests.cc` is a file containing the following lines

```C++
#include "gtest/gtest.h"

int main(int argc, char **argv) {
    ::testing::InitGoogleTest( &argc, argv );
    return RUN_ALL_TESTS();
    }

```

This file will run all your test. It will need to be in the same directory as your tests/code.

You then need to include all the files you need for your tests using 
```
runner_SRCS += #test-files
```

If you tests are in a different directory, you can add that directory to your SRCs path using 
```
SRC_DIRS += #Test-Directory
```

## Running your tests

Include a copy of the following batch file in your top directory to run all you tests. It will create xml reports on your tests in `test-reports` directory at the top level.

```batch
:: Run all tests
@echo off


SET TOP="."

set {IOCNameSuppApp}_tests_failed=%errorlevel%

:: run tests
call {IOCNameSupApp}\src\O.windows-x64\runner.exe --gtest_output=xml:%TOP%\test-reports\TEST-{IOCName}.xml

exit /B %keithley_2001_tests_failed%

```