# Creating a Motor IOC

Here we wll create a motor IOC from an exisiting IOC. Specifically create an ESP300 IOC using anotehr Newport IOC.

The motor is supported by teh newport module as per https://github.com/epics-motor/motorNewport and there are examples of usage in https://github.com/epics-motor/motorNewport/tree/master/iocs/newportIOC/iocBoot/iocNewport and https://github.com/epics-motor/motorNewport/tree/master/newportApp/iocsh that need to be compared. Driver support is built into the Newport module 


A search of `Newport` in our IOCS shows `CONEXAGP`  or `SMC100` as potential templates to follow. Unfortunately both of these are 
model 3 motor drivers (they use asyn motor class and `asyn_motor.db`) whereas ESP300 is the older model 1 style (like MCLENNAN or LINMOT) so the Db files and syntax to call the driver will be more like mclennan/linmot (`motor.db`)

We will do a very basic implementation to start with as a proof of principle that it works

* make a copy of SMC100 ioc tree and rename to ESP300
* analyse the examples above to see what commadns are neded to connect to the motor e.g. serial or etehrnet
* change Db include from `asyn_motor.db` to `motor.db`








