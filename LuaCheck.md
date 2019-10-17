## Installing LuaCheck

Either install via the hererocks python script or luacheck by itself. The hererocks way is longer but will integrate with your environment and favourite text editor nicely as it sets up parts such as luacheck.path and luarocks 

Via the hererocks python script:
- Download hererocks:
    - Open powershell and navigate to somewhere you would like hererocks to download to
    - Run `wget https://raw.githubusercontent.com/mpeterv/hererocks/latest/hererocks.py -OutFile hererocks.py`
- Install and activate lua and luarocks:
    - In an EPICS terminal navigate to where you downloaded hererocks.py and run `python hererocks.py lua53 -l5.3 -rlatest` which installs lua 5.3 into `$current directory$\lua53`
    - Add `$current directory$\lua53\bin` to your PATH where current directory is the directory you installed lua 5.3 in
    - Close and reopen your EPICS terminal to allow your PATH to update
- Install luacheck:
    - In your new EPICS terminal run `luarocks install luacheck`
- Luacheck is now installed

OR install luacheck by itself:
- Go to the [luacheck GitHub page](https://github.com/mpeterv/luacheck/tree/76bb56736702e8651537b2a9c10ae55ab7dc1d5d) and under Windows binary download click the download link which will download the file luacheck.exe
- Place the luacheck.exe file in a useful place e.g. Program Files and add that location to your PATH.
- Restart any command lines you have open.
- Luacheck is now installed

## Using luacheck:

Post-install step:
- Set luacheck config:
    - Create a new file `.luacheckrc` in `%LOCALAPPDATA%\Luacheck` as this is where luacheck looks for config files
    - Add the below information to the file to set the config
    - Note: This ignores setting, mutating and accessing undefined global variables. We are doing this because epics Lua uses an interactive Lua shell which requires us to use global variables in a different way to regular Lua.

```
ignore = {"111", "112", "113"}
```

Basic usage: `luacheck file.lua`

For more detailed instructions on the use of luacheck see the [luacheck documentation](https://luacheck.readthedocs.io/en/stable/).

The [luacheck GitHub page](https://github.com/mpeterv/luacheck/tree/76bb56736702e8651537b2a9c10ae55ab7dc1d5d) also has information about how to use luacheck in your favourite editor.