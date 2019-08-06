## Communications

Serial settings (baud rate, parity) can be changed on the front panel of the device. Ensure the IOC matches the physical device. Device communicates using a straightforward ASCII protocol with carriage-return terminators (`\r`).

## Channels

Each PR4000B unit can talk to two sensors independently. The controller can acquire a large amount of diagnostic data alongside the "primary" readings for each channel. This diagnostic data polls more slowly than the main readings, as they probably change less frequently.

## IOC

The IOC is forked from a Diamond repository, however it has been heavily modified to fit ISIS standards and working practices. In reality it should be treated as "our own" driver rather than as a "vendor" driver.