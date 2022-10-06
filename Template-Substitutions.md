> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > Template Substitution

Template substitution allows you to take a database template file and substitute the macros in it for a list of chosen values, the documentation for this can be found [here](https://epics.anl.gov/base/R7-0/1-docs/msi.html). This is used for example to create the same set of records for `North`, `East`, `South`, and `West` jaw blades. This helps to avoid writing a lot of duplicate PVs. 

This requires two files: a `.template` and a `.substitutions` file
- The `.substitutions` file loads the `.template` (or several) and runs a list of macro substitutions on it. This lives inside the IOC under `\<iocDir>\<ioc>App\Db\<something>.substitutions`.
- The `.template` file looks the same as a `.db`. It can live anywhere, you just need to specify the right path in the `.substitutions` file.

To build a `.db` from this, you need to include a reference to the `.substitutions` file in the `makefile` in the same folder, e.g.: `DB += <something>.db` (this instruction will look, in order, for a .db, then a .template, then a .substitutions file named `<something>`)

The general format of a substitutions file is as follows:
```
file <FILEPATH_1> { 
  pattern 
    {MACRO_1, MACRO_2, (...) MACRO_N}
    
    {"MACRO_1_SUB_1", "MACRO_2_SUB_1", (...) "MACRO_N_SUB_1"}
    {"MACRO_1_SUB_2", "MACRO_2_SUB_2", (...) "MACRO_N_SUB_2"}
    (...)
    {"MACRO_1_SUB_M", "MACRO_2_SUB_M", (...) "MACRO_N_SUB_M"}
}

file <FILEPATH_2> { 
    ...
}
```

This will create M sets of records, with each of the N macros replaced with what is specified in each row. Note that you need to substitute every macro that occurs in the `.template` file, otherwise the substitution procedure will fail. If it's something you don't want to replace (e.g. the PV Prefix) you can just replace it with itself.

See [IOC Utilities](IOC-Utilities#db-templates) for some practical examples.
