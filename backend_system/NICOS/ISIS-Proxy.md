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

The second version used ActiveMQ queues for communication with client and so the structure looked something like this:

![NICOS Proxy Design](backend_system/NICOS/ProxyDesign.png)

## Future developments

* STOMP/ActiveMQ allows messages to have a correlationID, which gives some idea of which messages from NICOS correspond to those sent from the client. This may or may not be useful for future depending on how fast messages take to process
