> [Wiki](Home) > [Project tools](Project-tools) > [Remote Debugging from Visual Studio](Remote-Debugging-from-Visual-Studio)

Remote debugging allows you to debug in visual studio c and c# applications running on another machine. To do this:

1. On the remote machine run the visual studio remote debugging (x64) tool for your version of visual studio. It can be downloaded from [microsoft](https://docs.microsoft.com/en-gb/visualstudio/debugger/remote-debugging) but may be there already. You can also run the one at `ISIS_Experiment_Controls_Public\VS_Remote_Debuggers\VS2017\x64`
1. Set the tool to allow no authentication (Tools->Options No Authentication)
1. Set the environment variable on your local machine 
    `_NT_SYMBOL_PATH=srv*\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\Releases\Symbols;srv*\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\EPICS\Symbols;srv*\\isis.cclrc.ac.uk\inst$\Kits$\CompGroup\ICP\ISISICP\Symbols;srv*c:\MyServerSymbols*https://msdl.microsoft.com/download/symbols`
1. Run VS on your local machine
1. Select Debug -> Attach to Process
1. Set Connection Type Remote(no authentication) and use the server name in connection target
1. Select the process from the list
    1. If you need to catch an error in ioc startup, start the ioc with `runIOC.bat aaa` this will cause it to start up with running st.cmd. 
    1. Once you are connected and have break points setup then type `< st.cmd` to boot the ioc
1. Open the Modules windows (Debug -> Windows -> Modules), find a module you are interested in right click and do load symbols. I am a bit hazy on how this works Freddie knows more. If it works for you please put how you did it here.
1. You should now be a able to open code and put breakpoints in as usual.

