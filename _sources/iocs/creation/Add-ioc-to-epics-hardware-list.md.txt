# Add IOC to EPICS hardware support list

It would be nice to add all IOCs to the EPICS list so that other facilities do not have to rewrite a driver. Most of our IOCs are in public git hub repositories so there should be no problems doing this. We have discussed with the relevant team and we need to add licences before we can publish the link see but until then follow the procedure:


1. Visit epics page https://epics.anl.gov/modules/manufacturer.php
1. Click `To request a new entry in this table for your Hardware Support module, use this form.`
1. Add the following
    - Bus: the bus e.g. `RS-232 (Streams)`
    - Manufacturer: the manufacturer
    - Contact Name: `ISIS Computing Group`
    - Contact Email: `ISISEPICS@stfc.ac.uk`
    - Link URL: blank until licences are sorted out
    - Link Text: blank until licences are sorted out

NB Make sure that the support module [has a licence files](https://github.com/ISISComputingGroup/IBEX_device_generator/blob/master/templates/support/LICENCE)