# Moxa configurator

Note: this page relates to the python service which allows users to configure allowed IPs on MOXA NPORT devices by hostname, not the built-in moxa configuration web pages.

### Setup

- Clone the moxa configuration repository from [here](https://github.com/ISISComputingGroup/moxa-configurator).
- Install python (genie_python may be used, but is not required)
- `python -m pip install -r requirements.txt` from the repository above to install dependencies
- Set up necessary environment variables:
  * `MOXA_IP` - the IP address of the moxa this webserver will manage (displayed on front of moxa)
  * `MOXA_PW` - the password for the moxa this webserver will manage (same password as for the moxa web interface)
  * `ISIS_DEFAULT_NETMASK` - the netmask for the ISIS network (to find this out, type `ipconfig` on any computer connected to the ISIS network)
- cd into `moxa_configurator/web` and then run `python manage.py runserver` to start the webserver

The server will then be available at `localhost:8000`.