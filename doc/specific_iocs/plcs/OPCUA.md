# OPC UA 
## What is OPC UA
OPC UA is a cross-platform, open-source, IEC62541 standard for data exchange from sensors to cloud applications developed by the OPC Foundation. It is characterised by: 

* Standardized data models freely available for over 60 types of industrial equipment, published by the OPC Foundation via Companion Specifications
* Extensible security profiles, including authentication, authorization, encryption and checksums
* Extensible security key management, including X.509, token and password
* Support for both client-server and publish-subscribe communication patterns
* Communication protocol independent. Mappings to several communication protocols like TCP/IP, UDP/ 
IP, WebSockets, AMQP and MQTT are specified
* Initially successful in standardized data exchange with industrial equipment (discrete manufacturing, process manufacturing, energy) and systems for data collection and control, but now also leveraged in building automation, weighing and kitchen equipment and cloud applications
* [Open](https://en.wikipedia.org/wiki/Open_standard) – open-source reference implementations freely available to OPC Foundation members, non members under GPL 2.0 license[2]
* [Cross-platform](https://en.wikipedia.org/wiki/Cross-platform) – not tied to one operating system or programming language
* [Service-oriented architecture](https://en.wikipedia.org/wiki/Service-oriented_architecture) (SOA)
* The specification is freely available on the OPC Foundation website and is split into several parts 
to ease implementation, but only OPC UA stack vendors need to read them, end users simply leverage 
existing commercial and/or open-source stacks available in all popular programming languages

More info can be found [here on Wikipedia for a general overview](https://en.wikipedia.org/wiki/OPC_Unified_Architecture), or for a more detailed description from [OPC Foundation](https://opcfoundation.org/about/what-is-opc/).

## How is authentication handled?
Currently, the IOC does not seem to be able to support encrypted message security policy. It does, however, support “None” security mode, and connecting with a username and password, which also appears to require sending the password encrypted with Basic256 (username and password connection works with None security mode, but does not work if there is no certificate and private key provided via the `opcuaCLientCertificate` option in the `st-common.cmd` or `st.cmd` file, which loads the IOC with some other options.  

Currently, authentication configurations in Windows only seem to work with username and password. This is likely due to functionality missing from the `open62541` library, the open source library that we use in conjunction with `opcua` EPICS module. A username and password is set on the PLC itself, and those values can be read at IOC startup to authenticate, and sent via Basic256 encryption to the PLC to sign in. When implementing/installing onto a new instrument, the `client_private_key.pem`, `cert.txt` (which will need to be edited to reflect current username and password for the target PLC/server), and `OPCUA_01.cmd` should be moved from the Experiment Controls non-public share `OPCUA` folder, to the instrument's configurations area, in a new folder that should be named `opcua`. If done properly, the `opcua` EPICS module should be able to pick up the user name and password, log in to the OPC server properly, and begin a connection. 

## Do any settings in the PLC side need to be adjusted to get communicating properly?
On occasion, a client certificate needs to be trusted manually, from the PLC technician side. However, things *_should_* be set up on our PLCs currently deployed; this step is done in deployment/implementation. A security policy might be set that is not what the IOC is trying to use, if everything else seems fine but you are unable to connect. Lastly, another person might be connected to the server (perhaps testing an IOC or something), and they would need to be kicked off in order for the IOC to communicate properly. Speak with Tim Carter or a member of his team to see if this is the case.

## Where are instrument-specific configs loaded from 
We load instrument specific configs from the $(INSTRUMENT)/configurations/opcua/ folder. This `opcua` folder is created at implementation time, on the `NDX` machine. It should contain a `OPCUA_01.cmd` file, which contains any `DbLoadRecords` calls, and where paths are specified to the `db` files for that `NDX`'s specific `OPCUA` IOC. If an `NDX` is missing an `opcua` folder, create one; if you cannot find it's `OPCUA_01.cmd` file, it _should_ be placed in the Experiment Controls non-public network share, in the `OPCUA` folder, in a folder specific to that `NDX`. For example, `NDXMAPS`'s `OPCUA_01.cmd` file is in `<network share>/OPCUA/MAPS_OPCUA/`.

## Where are instrument-specific DBs defined
Instrument specific `db` files are currently defined in `ioc/master/OPCUA/OPCUA-IOC-01App/Db`. Hence, the `db` files should have somewhat specific names so as to avoid confusion.


## Any troubleshooting information (As a support/on call person, things to look out for)
As always, be sure to check the IOC log first, if something isn't working properly. If the IOC has connected properly to the server, the IOC log should print out something like the following: 
```
# namespace 4 urn:OMRON:SomeOpcUaServer:FactoryAutomation

Structure TPG_Gauge { # binaryEncodingId: ns=4;i=5002
  Float Pressure # mandatory opc:Float
  # memberSize=4 alignment=4 padding=0 memSize=4
  Float Lower_Threshold # mandatory opc:Float
  # memberSize=4 alignment=4 padding=0 memSize=8
  Float Upper_Threshold # mandatory opc:Float
  # memberSize=4 alignment=4 padding=0 memSize=12
  String Measured_Value_Status # mandatory opc:CharArray
  # memberSize=16 alignment=8 padding=4 memSize=32
  String Measuring_Circuit_Status # mandatory opc:CharArray
  # memberSize=16 alignment=8 padding=0 memSize=48
  String Switching_Function_Assignment # mandatory opc:CharArray
  # memberSize=16 alignment=8 padding=0 memSize=64
  String Switching_Function_Status # mandatory opc:CharArray
  # memberSize=16 alignment=8 padding=0 memSize=80
  String Filter_Time_Constant # mandatory opc:CharArray
  # memberSize=16 alignment=8 padding=0 memSize=96
}; # alignment=8 memSize=96 8 members
# adding type TPG_Gauge to known types
```
Which means that the IOC has read data properly from the server and has a good connection. 

You will then see output like this, near the bottom of the IOC log:

```
** Session OPC1: (readComplete) getting data for item ns=4;s=Opc_TPG2_Sensor_B2.Measuring_Circuit_Status = "No measuring channel" (String) Good
** Session OPC1: (readComplete) getting data for item ns=4;s=Opc_TPG2_Sensor_B1.Switching_Function_Assignment = "No assignment" (String) Good
** Session OPC1: (readComplete) getting data for item ns=4;s=Opc_TPG2_Sensor_B1.Switching_Function_Status = "Off" (String) Good
** Session OPC1: (readComplete) getting data for item ns=4;s=Opc_TPG2_Sensor_B1.Filter_Time_Constant = "Slow" (String) Good
```

If you don't see this sort of read out at the end of the IOC log, you'll know that something has gone wrong, and likely there is a repeated output that signifies attempts to connect to the server.

An example of BadInternalError IOC output, which can usually be caused by username and password not being read properly, or the paths not being set properly in the `OPCUA_01.cmd` file, looks like this: 

```
OPC UA: Autoconnecting sessions
Session OPC1: (initClientSecurity) loading client certificate C:/Instrument/Settings/config/<NDX###>/configurations/opcua/client_cert.der
Session OPC1: (initClientSecurity) loading client private key C:/Instrument/Settings/config/<NDX###>/configurations/opcua/client_private_key.pem
[2025-05-06 08:48:55.699 (UTC+0100)] warn/userland      AcceptAll Certificate Verification. Any remote certificate will be accepted.
[2025-05-06 08:48:55.705 (UTC+0100)] info/securitypolicy        The Basic128Rsa15 security policy with openssl is added.
[2025-05-06 08:48:55.711 (UTC+0100)] info/securitypolicy        The basic256 security policy with openssl is added.
[2025-05-06 08:48:55.716 (UTC+0100)] info/securitypolicy        The basic256sha256 security policy with openssl is added.
[2025-05-06 08:48:55.723 (UTC+0100)] info/securitypolicy        The Aes128Sha256RsaOaep security policy with openssl is added.
OPC UA session OPC1: cannot open credentials file C
OPC UA session OPC1: credentials file C does not contain settings for Username token (user + pass) or Certificate token (cert + key [+ pass])
Session OPC1: (setupSecurity) no security configured
[2025-05-06 08:48:55.736 (UTC+0100)] warn/client        The configured ApplicationURI does not match the URI specified in the certificate for the SecurityPolicy http://opcfoundation.org/UA/SecurityPolicy#None
[2025-05-06 08:48:55.743 (UTC+0100)] warn/client        The configured ApplicationURI does not match the URI specified in the certificate for the SecurityPolicy http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15
[2025-05-06 08:48:55.751 (UTC+0100)] warn/client        The configured ApplicationURI does not match the URI specified in the certificate for the SecurityPolicy http://opcfoundation.org/UA/SecurityPolicy#Basic256
[2025-05-06 08:48:55.759 (UTC+0100)] warn/client        The configured ApplicationURI does not match the URI specified in the certificate for the SecurityPolicy http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256
[2025-05-06 08:48:55.766 (UTC+0100)] warn/client        The configured ApplicationURI does not match the URI specified in the certificate for the SecurityPolicy http://opcfoundation.org/UA/SecurityPolicy#Aes128_Sha256_RsaOaep
Session OPC1: secure channel state changed from Closed to HelSent
Session OPC1: secure channel state changed from HelSent to AckReceived
Session OPC1: secure channel state changed from AckReceived to OPNSent
[2025-05-06 08:48:55.785 (UTC+0100)] info/channel       Connection 1704 | SecureChannel 140237378 | SecureChannel opened with SecurityPolicy http://opcfoundation.org/UA/SecurityPolicy#None and a revised lifetime of 600.00s
[2025-05-06 08:48:55.792 (UTC+0100)] info/client        Client Status: ChannelState: Open, SessionState: Closed, ConnectStatus: Good
Session OPC1: secure channel state changed from OPNSent to Open
[2025-05-06 08:48:55.801 (UTC+0100)] info/client        The initially defined EndpointURL opc.tcp://0.0.0.0:4080is valid for the server
[2025-05-06 08:48:55.810 (UTC+0100)] info/client        Rejecting UserTokenPolicy 0 (username) in endpoint 0: configuration doesn't match
[2025-05-06 08:48:55.813 (UTC+0100)] info/client        Rejecting endpoint 1: security mode doesn't match
[2025-05-06 08:48:55.818 (UTC+0100)] info/client        Rejecting endpoint 2: security mode doesn't match
[2025-05-06 08:48:55.822 (UTC+0100)] error/client       No suitable UserTokenPolicy found for the possible endpoints
[2025-05-06 08:48:55.825 (UTC+0100)] info/client        Client Status: ChannelState: Closed, SessionState: Closed, ConnectStatus: BadInternalError
Session OPC1 irrecoverably failed: BadInternalError
OPC UA session OPC1: connect service failed with status BadInternalError
```
This output will often repeat, as the client/IOC continually tries to connect to the server/PLC.

You'll see that the IOC gets quite close to connecting, as it goes from `Closed` to `HelSent`, or "hello sent", then from `HelSent` to `AckReceived`, meaning it receives an acknowledgement, and then moves to `OPNSent`, sending a message to open the connection, which then fails on configuration mismatch. More information about the [OPC UA Connection protocol can be found here](https://reference.opcfoundation.org/Core/Part6/v105/docs/7.1).