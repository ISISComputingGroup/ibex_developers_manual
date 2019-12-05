This is a guide to set up googleTest with EPICS at ISIS. This allows you to write C++ unit tests for your C/C++ code in an IOC.

## Contents
* [googleTest](#googletest)
* [Release file](#Release-file)
* [Building the test runner](#building-the-test-runner)
* [Running your tests](#running-your-tests)
* [Adding a target to run tests](#Adding-a-target-to-run-tests)
* [Adding tests to Jenkins](#adding-tests-to-Jenkins)
* [Sample Test](#sample-test)
* [Notes](#Notes)


## googleTest

You will need to have the `googleTest` support submodule and built the master branch. This will create a `gtest.lib` which you can link against.

More information on googleTest can be found at https://github.com/abseil/googletest. We are using version 1.8.x currently at ISIS.

Good places to start on how to write tests using googleTest is [here](https://github.com/abseil/googletest/blob/master/googletest/docs/primer.md). 

More advanced usage (including `ASSERT_THROWS`, `ASSERT_NO_THROW` and `ASSERT_DOUBLE_EQ`) can be found [here](https://github.com/abseil/googletest/blob/master/googletest/docs/advanced.md). 

Examples can be found [here](https://github.com/abseil/googletest/blob/master/googletest/docs/samples.md).

## Release file

Remember to add the path to the Google Test support module in your support module Release file.

```
GTEST=$(SUPPORT)/googletest/master
```

## Building the test runner

Make sure you include the following lines in your Makefile alongside the source code to create a test runner executable.

```Makefile
# googleTest Runner

TESTPROD_HOST += runner
USR_CPPFLAGS += -I$(GTEST)/googletest/include 
runner_SRCS += run_all_tests.cc
runner_LIBS += gtest
```

Where `run_all_tests.cc` is a file containing the following lines. Make sure to also add all libs needed for the files being tested.

```C++
#include "gtest/gtest.h"

int main(int argc, char **argv) {
    ::testing::InitGoogleTest( &argc, argv );
    return RUN_ALL_TESTS();
    }

```

This file will run all your test. It will need to be in the same directory as your tests/code.

You then need to include all the files you need for your tests using 
```Makefile
runner_SRCS += #names of test files and source files
```

If your tests are in a different directory to your source files, you can add that directory to your SRCs path using 

```Makefile
SRC_DIRS += #path to your tests directory
```

## Running your tests

Include a copy of the following batch file in your top directory to run all your tests. It will create XML reports on your tests in `test-reports` directory at the top level. Replace `IOCNAME` by the name of your IOC.

```batch
:: Run all tests
@echo off
SET TOP="."

SET Tests_failed=%errorlevel%

:: Change the directory depending on if you have a src sub directory
call IOCNameSup\src\O.windows-x64\runner.exe --gtest_output=xml:%TOP%\test-reports\TEST-IOCName.xml

exit /B %Tests_failed%
```

## Adding a target to run tests

To run the tests by `make test` add the following to the top level Makefile of the support module

```Makefile
.PHONY: test
test:
	run_tests.bat
```

## Adding tests to Jenkins

To have these tests run on Jenkins, add the following to the bottom of the `jenkins_build.bat` file replacing IOCNAME with the name of your IOC.

```batch
:: Run googleTest C++ unit tests for IOCNAME
cd /d %FINAL_DIR%\support\IOCNAME\master\
make test
if %errorlevel% neq 0 (
    @echo ERROR: Tests failed in IOCNAME\master
    goto ERROR
)
```

Make sure that Jenkins has been configured to look for xUnit test reports and that you have the `xunit` Jenkins plugin installed.

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

## Notes
We are currently using an outdated version of google tests, so some features shown in tutorials and documentation will not work as they have since been renamed.
For example, we need to use `INSTANTIATE_TEST_CASE_P` instead of `INSTANTIATE_TEST_SUITE_P`, `SetUpTestCase()` instead of `SetUpTestSuite()` and `TearDownTestCase()` instead of `TearDownTestSuite()`.