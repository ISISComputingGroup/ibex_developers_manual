# Temperature Jump Apparatus

The device has been designed and built in house.

There are two temperature blocks, which are set to a temperature using a standard controller. The cell is pressed against one, a length of time is allowed to pass to set the temperature, the block in contact with the cell is then swapped for the other block, which will be at a different temperature.

### Communication
- Device uses 9-way male moxa with null modem.
- Needs longer timeouts to correctly read the status command.

Note: the Temperature Jump apparatus IOC will be included in the release after `v12.0.1`. If anyone needs to use it before the next is deployed we can easily patch the fixed protocol file over for it. 