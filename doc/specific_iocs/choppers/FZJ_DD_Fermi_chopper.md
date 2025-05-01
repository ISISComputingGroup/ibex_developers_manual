# FZJ Digital Drive Fermi Chopper

IOC name: `FZJDDFCH`.

Prototype digital drive Fermi chopper controller made by Forschungszentrum Jülich (FZJ).  A single "one-off" device unlikely to be used anywhere other than on MAPS.

## Gotchas
- Only one TCP connection allowed at a time. Other TCP connections will appear to connect but not give any responses (this can cause the IOC to read "zero" for everything).
- Message length limit at 19 chars. For some commands (e.g. setting phase setpoint) this means the device cannot handle more than 1 d.p. If the message is too long the device will respond with an error message and not accept the setpoint at all. This length limit *includes* the `\r\n` terminator so really the message length limit is 17 characters.
- The manual does not match the command set. For example, the order of responses in the long response packet is incorrect and several of the commands simply don't exist. The best (most up-to-date) place to get the command syntax from is the Jülich VIs which are running on the chopper control machine (David has a copy of these).
- Be careful about renaming/removing PVs, this IOC is used by a CaLAB wrapper and that will need to be updated if the PV names change.
- Errors on all PVs are propagated from a single source so may not accurately reflect which command(s) have gone wrong

## Connection

Connected to a computer on the network which is looked after by the chopper group. If this computer is not pingable, contact the chopper group to restart it (the chopper needs to be stopped before restarting the control PC).