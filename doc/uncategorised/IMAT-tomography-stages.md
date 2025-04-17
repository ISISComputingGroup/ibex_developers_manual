# Switching motor resolutions

To switch between different resolutions on IMAT's tomography stages, you need to:
- Stop the galil_08 ioc
- Copy the contents of either `C:\instrument\var\autosave\galil_08_2_axis` or `C:\instrument\var\autosave\galil_08_3_axis` into `C:\instrument\var\autosave\galil_08`
- restart the galil ioc