> [Wiki](Home) > [The Backend System](The-Backend-System) > [Useful tools](Useful-tools) > Add sim records script

The add_sim_records script (located in EPICS/ISIS/DbChecker/master) will automatically add simulation and disable records to a db file. Usage:

```
python.exe c:\Instrument\Apps\EPICS\ISIS\DbChecker\master\add_sim_records.py db_file.db 

optional arguments:
   -o --output = name of output file
```

By default, the new db file's name will match the input file prefixed by `sim_.`
