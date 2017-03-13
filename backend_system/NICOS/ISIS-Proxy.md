> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > ISIS Proxy

# ISIS Proxy

## Motivation

NICOS uses a low level socket protocol based on specific bytes having special meaning and on the python pickling library for sending and receiving objects. For more information see the protocol section of the documentation that come with the NICOS source code.

It was decided that a proxy client should be written to sit between IBEX and NICOS for the following reasons:
* To allow some separation of the GUI and NICOS specific protocols (allowing for a potential swap of script servers in the future)
* Libraries to handle pickled objects in JAVA exist but are underdeveloped
* Low level socket communication is not something that the GUI currently does

Instead it was decided that the technology to communicate between the GUI and NICOS (via the proxy) would be JSON being transferred over ActiveMQ queues. Both of these technologies are already used extensively elsewhere in IBEX. The log messages use an ActiveMQ queue to send messages back to the client and JSON is used to communicate between the blockserver and GUI (using the well established GSON library)

## Implementation

The Proxy is written in python (so as to be able to use pickled objects and JSON) and currently resides in a folder within the NICOS source code. 

The first version of the proxy purely converted the pickled protocol into JSON and but used a similar low level socket protocol to communicate with any clients. This still exists in the client_connection/HTTP folder within the proxy, along with a simple command line client that can be used for testing.

The second version uses ActiveMQ queues for communication with clients the structure of the connections is as follows, where red lines are ActiveMQ connections and Blue are low level socket connections:

![NICOS Proxy Design](backend_system/NICOS/ProxyDesign.png)

1. When a client starts up it will create a new temporary queue that will last the lifetime of the client.
2. The client will then send a message down the known, fixed ss_admin queue (the contents of which is irrelevant) which contains in the reply-to section of the header a link to the temporary queue.
3. The proxy will then establish a new connection with NICOS (unique to each client)
4. The client will then be expected to send the information for logging into NICOS

Subsequently all data sent from the client to the proxy will be through the ss_admin queue (with a reply-to link to the temp queue) and all information sent back from the proxy will be in this temp queue. For an example of this working see the example Java client (which can be easily run in eclipse) located in the STOMP client folder. 

## Security

To ensure that an unauthorised user cannot run scripts on your machine there is a credentials system on ActiveMQ. Only users with the correct credentials can send/receive messages on the ss_admin queue and thus run scripts. As default the proxy in version control will not work due to this. To fix make sure all of the following passwords are the same:
* The _CHANGEME_ password in `...EPICS\ISIS\ActiveMQ\master\conf\activemq.xml`
* The _ACTIVEMQ\_PASS_ in `...EPICSISIS/ScriptServer/nicos-core/master/ISIS\_script\_server/client\_connection/Stomp/client\_listener.py`
* The _PASSWORD_ in `Stomp/test\_client/src/Client.java`
* The _PASSWORD_ in `...ibex_gui\base\uk.ac.stfc.isis.ibex.nicos\src\uk\Nicos.java`

## Future developments

* ActiveMQ allows messages to have a correlationID, which gives some idea of which messages from NICOS correspond to those sent from the client. This may or may not be useful for future depending on how fast messages take to process
