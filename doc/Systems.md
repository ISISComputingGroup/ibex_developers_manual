# Systems Administration & Hardware

```{toctree}
:glob:
:titlesonly:
:maxdepth: 1

systems/*
```

## Looking up Dell service-tag numbers

You can check specifications of Dell machines by getting their service tag, using the following command in `powershell`:

```powershell
get-ciminstance win32_bios | select SerialNumber
```

This will return a short string which can be looked up on the [Dell support site](https://www.dell.com/support/home/en-uk).
