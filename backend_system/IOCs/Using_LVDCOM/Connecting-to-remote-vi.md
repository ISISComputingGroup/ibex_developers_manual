> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Using LVDCOM](Using-LVDCOM) > Connecting to remote VI

# Connecting an IOC to a VI on a different PC

To connect to a lvDCOM IOC to a VI on a different PC is very straightforward.

Edit the st.cmd of the IOC to change the lvDCOMConfigure line from something like this:

```
lvDCOMConfigure("ex1", "example", "$(TOP)/lvDCOMApp/src/examples/example_lvinput.xml", "", 6)
```

To something like this:

```
lvDCOMConfigure("ex1", "example", "$(TOP)/lvDCOMApp/src/examples/example_lvinput.xml", "ndxtestmjc", 6, "", "account_name", "password")
```

Of course, the account_name and password should be changed to match your system.