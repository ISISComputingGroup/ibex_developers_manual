> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [PLCs](PLCs) > [Omron FINS](Omron-FINS) > [He Recovery PLC](Helium-Recovery-PLC)

# Introduction

The Helium Recovery PLC is a FINS PLC used for monitoring various parameters related to the helium gas recovery system. It contains data that will need to be stored in the database of the Helium Level Monitoring project. Therefore, we wrote an IOC for this PLC so that the data will then be read by a python server via Channel Access.

# Connection

The Helium Recovery PLC communicates by using FINS over UDP, and is connected over Ethernet. However, you should use TCPNOHEAD when running tests in devsim. The FINS cmd should be similar to the example given [here](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Omron-FINS#configuration).

The IP address and node for this PLC are noted on the memory map spreadsheet in the shares drive, in Manuals > OMRON_FINS_PLCs > Helium recovery PLC.

## Commands

The memory map of this PLC can be found in a spreadsheet in the shares drive, as mentioned above. Not all of the memory locations in the memory map can be read by the IOC, as not all are needed for the HLM project. The red cells indicate elements that are not needed, yellow cells indicate elements that might need to be added in the future when Cryogenics has more information, and clear cells are needed and have all been implemented.

The memory map details the name, memory address, data type, description and units for every thing of interest to the HLM project that it stores.

The command used by the IOC to read from the PLC is `0x0101` for Memory Area Read, and it reads from the DM Memory area, with code `0x82`. The PLC uses word designted memeory addresses, so the third byte of the start address in the FINS command should always be 0.

This PLC uses big endian notation. The word size is 16 bit, so on the memory map the INT and UINT data types take up 16 bits, and the DWORD data type uses 32 bits. The REAL data type also takes up two words, so 32 bits.