# Serve file contents over EPICS

## FileContentsServer

You can serve the raw contents of files in a directory over EPICS by using the "FileContentsServer" component of https://github.com/ISISComputingGroup/EPICS-FileServer

This is done by calling `FileContentsServerConfigure()`, with an asyn port name as well as a directory path in an `st.cmd` alongside loading `FileContentsServer.db` with the same asyn port name. 

## Device screen

There is an accompanying device screen("File Editor" in the list) for viewing and editing the file served by this mechanism. 