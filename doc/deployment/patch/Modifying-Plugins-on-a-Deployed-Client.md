# Patching a deployed client

If you need to modify a plugin on an IBEX client running on an instrument, such as OPIs, you need to go to 

```<installed client dir>/plugins/<whichever plugin you're interested in>```.

## Live editing opis / non-compiled code

These can be edited on the fly. If you edit a `.opi` file, the change will be seen the next time the opi is opened in IBEX. However, if you edit `opi_info.xml` (for example, to add an entirely new opi) you will need to relaunch the client as this file is only read once at startup.

## Live editing "compiled" code

Plugins can be built as either folders containing `.class` files, or `.jar` files. If you need to edit the contents of a `.jar`:
- Rename the plugin from `_.jar` to `_.zip`
- You can now extract the files and make any necessary changes
- When done, put it all back into a `.zip` archive, ensuring that the directory structure is the same as before
- Rename the `.zip` back to a `.jar`
- Relaunch the client and test your changes