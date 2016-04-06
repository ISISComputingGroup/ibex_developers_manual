> [Wiki](Home) ▸ [[Design Documents]] ▸ **Hackathon - Opening an OPI Outside of a Synoptic**

## Vague Outline for the Hackathon for Ticket 1083

* [Link to ticket on GitHub](https://github.com/ISISComputingGroup/IBEX/issues/1083)
* [Link to original design document (superseded by this)](Opening-an-OPI-Outside-of-a-Synoptic)

### The aim in a nutshell
Add a tab to the IBEX GUI where OPIs for connected equipment can be viewed – similar to the LabVIEW tab in SECI.

![SECI](design_documents/images/Hackathon---Opening-an-OPI-Outside-of-a-Synoptic/SECI.png)

### Proposed implementation

This may change on the day as we get going but it is something to get started with.

#### 1. The interface
The BlockServer and GUI s communicate through two PVs; one for reading and one for writing:

* `%MYPVPREFIX%CS:BLOCKSERVER:GET_SCREENS` = returns the XML for the screens

* `%MYPVPREFIX%CS:BLOCKSERVER:SET_SCREENS` = sets the XML for the screens

The data sent over Channel Access will need to be zipped and hashed in the same way as the configurations and synoptics.

#### 2. The BlockServer

The BlockServer will be responsible for saving and loading a list of 'Device Screens'. It is proposed that these are stored in a separate XML file in the configuration or component: `NDXXXXX/configurations/my_config/device_screens.xml`.

The XML will be something like:

```xml
<devices>
    <device>
        <name>Eurotherm 1</name>             
        <key>Eurotherm</key>                 
        <type>OPI</type>
        <properties>
            <property>
                <key>EURO</key>
                <value>EUROTHERM1</value>
            </property>
        </properties>
    </device>
</devices>
```

A schema will also be required. It could look something like:

```xml

<complexType name="devices">
    <sequence>
        <element name="device" type="device" maxOccurs="unbounded" minOccurs="0"></element>
    </sequence>
</complexType>

<complexType name="device">
    <sequence>
        <element name="name" type="string" maxOccurs="1"
            minOccurs="1">
        </element>
        <element name="key" type="string" maxOccurs="1"
            minOccurs="1">
        </element>
        <element name="type" type="tns:type" maxOccurs="1"
            minOccurs="1">
        </element>
        <element name="properties" type="tns:properties" maxOccurs="1" minOccurs="0"></element>
    </sequence>
</complexType>

<simpleType name="type">
    <restriction base="string">
        <enumeration value="COMPONENT"></enumeration>
        <enumeration value="OPI"></enumeration>
    </restriction>
</simpleType>

<complexType name="property">
    <sequence>
        <element name="key" type="string"></element>
        <element name="value" type="string"></element>
    </sequence>
</complexType>

<complexType name="properties">
    <sequence>
        <element name="property" type="tns:property" maxOccurs="unbounded" minOccurs="0"></element>
    </sequence>
</complexType>

```

The PVs and logic should be implemented in such a way as to be optional, so if, say, the ESS didn’t want the functionality it would be easy to exclude. The way the synoptics are handled is an example of how to do this.

The XML for the synoptic may need to change to allow device screens to be specified – this will need to be coordinated with the GUI side (see Task 5 in Section 3).

**UNIT TESTS MUST BE WRITTEN!**

#### 3. The GUI

It is proposed that it will be via the device screens that macros etc. are configured for an OPI. The synoptic editor will be simplified to just allow the already configured device screens to be used for creating a synoptic. In other words, if the device screen is not configured for an item of kit, it will not be possible to add that kit to the synoptic. 

*Note: We may need a quick way to launch the "device screen configurator" from the synoptic editor*

Tasks:

1. Connect up to the new PVs and decode/encode the data
1. A new perspective/tab for showing the OPIs (see mockup in figure 1)
1. A dialog for configuring the device screens (see mockup in figure 1)
1. The synoptic editor will no longer need to allow editing of macros, but will need a way to pick the correct screen (and suggest defaults)
1. The synoptic XML may need to change to handle device screens (this will need to be done in collaboration with the people working on the BlockServer)
1. Unit tests
1. GUI tests (ask Ian for help)

![OPI View](design_documents/images/Hackathon---Opening-an-OPI-Outside-of-a-Synoptic/IBEX_UI_New_OPI_View.png)
*Figure 1 - Mockup of the Device Screen view with the configuration dialog*
