# Lumacam

The Lumacam is an imaging camera, which has been used on INES. It is comparable to the {doc}`../other/nGEM-detector`.

## Lumacam control PC

This camera has a dedicated Ubuntu Linux control PC, which travels with the camera. We do not manage (and do not
have credentials for) this PC. 

The Lumacam PC runs several IOCs and an EPICS gateway, under `docker-compose`.

## Networking

The Lumacam control PC should be connected to the instrument private network, and manually assigned an IP address
in the `192.168.1.x` range. INES have previously used `192.168.1.15` for this PC.

The EPICS gateway configuration on the Lumacam PC may need adjusting to reflect this private static IP if it is
changed in future.

## `EPICS_CA_ADDR_LIST`

In order to allow scripts and GUIs on an NDX machine to connect to the Lumacam PC, the static IP of the Lumacam PC
needs to be added to `EPICS_CA_ADDR_LIST`.

To do this for the GUI (including both cs-studio components and the PyDEV scripting console), edit:
```
\Instrument\Apps\Client_E4\plugins\uk.ac.stfc.isis.ibex.e4.client_<VERSION>\plugin_customization.ini
```

Note that the address list appears in two places in this configuration file; both places need to be updated.

## Scripting

Basic scripts to begin and end a Lumacam data acquisition are stored in:
```
\Instrument\Settings\config\NDXINES\Python\inst\lumacam.py
```

## File copying and data output

No file copying or data transfer of any type has been provided. Data will be manually copied by users from the
Lumacam PC to appropriate locations.

## Remote access to the Lumacam PC

The Lumacam PC can be reached by SSH from the NDX machine, using its configured static IP address.

If the users wish to use a graphical client (such as NoMachine), they need a client laptop which also connects to
the private network and is set to use a *different* static IP address (on INES, `192.168.1.16` has previously been
used for this purpose).

The NoMachine client is configured on a user Linux machine, not on an ISIS machine.
