## Names

We need to settle on a good name for this. Current ideas are:
* Component Viewer
* Components
* Beam/SE Devices
* Beam/SE Components
* Target View
* Component Targets
* Target View
* OPIs (technical term, not really suitable)

## GUI Design

The figure below shows a layout for the GUI. This is designed as a first attempt layout, to be similar to the existing synoptic view and hence straightforward to implement. We need to consider how best to open up multiple OPIs on one screen, but this does not necessarily need to exist in the first iteration.

![OPI View](design_documents/images/Opening-an-OPI-Outside-of-a-Synoptic/IBEX_UI_New_OPI_View.png)

Note that the 'Edit List' dialogue will look different with the changes for automatically setting defaults and the new way of setting properties.

## BlockServer Storage

The BlockServer will be responsible for saving a list of 'Component Views'. It is proposed that each of these are stored as a separate XML file in the folder: `NDXXXXX/configurations/component_views`.

The component targets are currently stored in the synoptics, for example as:
```xml
<target>
    <name>Pinhole Selector</name>
    <type>OPI</type>
    <properties>
        <property>
            <key>PH</key>
            <value>PINHOLE</value>
        </property>
        <property>
            <key>MM</key>
            <value>MOT:MTR0601</value>
        </property>
    </properties>
</target>
```

We should be able to use this structure directly. A schema for the component views will be required, which can just be a subset of what is currently in the synoptics:

```xml
<complexType name="target">
    <sequence>
        <element name="name" type="string" maxOccurs="1"
            minOccurs="1">
        </element>
        <element name="type" type="tns:targettype" maxOccurs="1"
            minOccurs="1">
        </element>
        <element name="properties" type="tns:targetproperties" maxOccurs="1" minOccurs="0"></element>
    </sequence>
</complexType>

```

The component views will be served up in the same way as the synoptics, JSON over Channel Access. Note the way PVs are named needs to take [#1053](https://github.com/ISISComputingGroup/IBEX/issues/1053)
into account.

## Synoptic changes

Changes should be made once this is complete to use the component targets within the synoptics. This should not be done until the component targets editor and BlockServer changes are completed and well tested. When implementing the changes this should be taken into account though, to make sure synoptics can easily make use of a component target.
