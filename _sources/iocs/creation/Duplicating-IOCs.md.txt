# Duplicating IOCs
## IOC Duplication script
There is a script in ibex utils to duplicate IOCs, more information can be found [here.](#ioc_copier_script)

The manual instructions below can also be used.
<summary>Manual instructions</summary><details>## Creating IOC 2
If you need more than 1 IOC (i.e. you are making the second IOC) there is only a process to follow, rather than a script, as various IOCs can have their own nuances: so take this with a grain of salt. Let us refer to the IOC you are duplicating as `newIOC`, for clarity.

Navigate to an IOC folder which has two or more IOCs: here we have two folders to focus on, `<ioc>/iocBoot/` and `<ioc>/<ioc>-IOC-0<n>App` (where `n` is the number of IOCs). Make sure this IOC has a `st-common.cmd` file (to make your life easier!). Let us refer to this as `refIOC`. 

Now, let's get cracking!


### Making IOC 2: `iocBoot/ioc<newIOC>-IOC-02>`
1. Create a new **`ioc<newIOC>-IOC-02`** folder in `/iocBoot/`.
2. Navigate to the **`config.xml`** file of `refIOC`. In `01` you will see macros being defined, in `02` you will see the `01` config file being referenced. Create a `config.xml` file in `ioc<newIOC>-IOC-02` and do the same.
3. Check that there is a **`st-common.cmd`** file in `ioc<newIOC>-IOC-01`
      - if there **is**, note how `st.cmd` references this. Copy this file into `ioc<newIOC>-IOC-02` and refactor all instances of `01` to `02`. Then, where the file calls `st-common.cmd`, you will need to add a line that navigates to the `ioc<newIOC>-IOC-01` directory above it (there will be an example of this in `ioc<refIOC>-IOC-02`).
      - if there **is no**t, note how the `st.cmd` and `st-common.cmd` are set up in `refIOC`. In `ioc<newIOC>-IOC-01`, transition the `st.cmd` contents to a 
`st-common.cmd` file and refactor the `st.cmd` to reference this in a similar way. Now follow the step above!
4. Copy across the **`Makefile`** - this stays unchanged.
5. Copy across **`envPaths`**, changing `ioc<newIOC>-IOC-01` to `ioc<newIOC>-IOC-02` if it appears.
6. Copy across **`dllPath<...>`** and **`relPaths`** files. These also stay unchanged.


### Making IOC 2:  `<newIOC>-IOC-02App`
This one may be slightly less straightforward. There may be nuances and additional things in this folder to deal with that aren't mentioned below - either try find another IOC with similar oddities or ask someone!

1. Create a new **`<newIOC>-IOC-02App`** folder in `/<newIOC>/`
2. Navigate to `<newIOC>-IOC-01App` and copy across **`Db`** to the `02App` folder. 
      - Empty the `O.` folders of all `.db` files.
      - Delete all `.substitutions` files from top level.
      - In `Db\O.windows-x64\Makefile`, refactor the line `DB += something.db ...` with `#DB += xxx.db` (e.g just comment it out)
4. Navigate to `<newIOC>-IOC-01App` and copy across **`src`** to the `02App` folder. 
      - Empty the contents of both `O.` folders. 
      - Delete the `build.mak` file 
      - Rename the `<...>Main.cpp` file with the correct IOC number, and rename the header in the file itself.
      - In the `Makefile`, update `APPNAME` with the correct IOC number - but the `include ...` line needs to stay the same. 
5. Check whether `<newIOC>-IOC-01App` has a **`protocol`** file
      - If it does, just copy this across. As far as I can see, the Makefiles and folder contents seem to be the same.
</details> 

### After duplication
After either using the script or creating duplicates manually be sure to make and test to IOC.

### Making the IOC
1. **`make`** the `<newIOC>` folder
2. **`make iocstartups`** in EPICS top
3. Try to run your new IOC!

### Testing the IOC
Navigate to `IOCTestframework` or the `ioc/<newIOC>` folder (wherever the IOC tests live). 
Refactor `DEVICE_PREFIX` to `<newIOC>_02` and you will need to refactor any calls to `get_default_ioc_dir()` with additional parameter `iocnum` (or whatever the equivalent is in your test module, this should be pretty intuitive).

****WARNING:**** If you will also be making more IOCs via the method below, you should be _very_ confident that your new `<newIOC>_02` behaves the same as `<newIOC>_01` before duplicating: any issues with `<newIOC_02` will be propagated in _every_ other new IOC you make as well.
>