## System Testing Proposals

It is proposed to use Eclipse RCPTT for the system testing. Some findings from a first try with it are available here - [System Testing with RCPTT](System-Testing-with-RCPTT).

The UI tests can be run automatically, see the example script on the above link. As RCPTT only requires the binaries for the client the building of the client can be kept separate.

To use Eclipse RCPTT for a full system test the steps would be:
* Copy built version of EPICS back end system
* Copy built version of client
* Clear out any existing configurations
* Run the scripted system tests

### Notes on RCPTT

This used to be called Q7, and was formely a closed source product. Now everything, including the test runner for automating running the tests is open source.

## Alternative UI Testing Tools

There are a number of other possible UI testing tools available:
* [SWTBot](http://www.eclipse.org/swtbot/) - this is widely used and maintained, and tests are written and run in a similar way to normal JUnit tests
* [Jubula](http://www.eclipse.org/jubula/) - similar to RCPTT, designed for recording test with minimal coding knowledge
* [Full List of UI Testing Tools](https://wiki.eclipse.org/Eclipse/Testing#UI_tests)