# Building an MDT build server

This wiki page documents the process for setting up a new MDT (microsoft deployment toolkit) build server to create new windows 10 clones.

The central source of truth for MDT configuration files is `inst$\mdt$\`.

# Mental model

- `NDXINST` - this is the windows 10 virtual machine to be built. This is a usual NDX in the sense that it runs IBEX.
- `NDHINST` - this is the physical host on which the NDX virtual machine executes
- `NDHBUILD` - This is an MDT server which contains instructions which the NDX can execute to install standard operating systemsand/or software.

This wiki page descibes the process for setting up a new `NDHBUILD` machine (NOT an `NDHINST` or `NDXINST` machine).

---

1. Find a phyiscal NDH machine with space to host this VM (both in terms of memory and disk space). Standard instrument machines use 14GB of memory, so you will need at least this amount free. You will also need 256GB of free hard disk space.