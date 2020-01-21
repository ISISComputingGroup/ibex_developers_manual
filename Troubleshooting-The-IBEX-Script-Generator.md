## Warning: Could not load any configs from <FileSystemLocation>

This could be due to 4 things:

- The configs have not been loaded into the correct place in the filesystem
   - Indicated in the log by "Error loading from <FileSystemLocation>"
   - To fix simply move them into the location that is given in the warning message
- The IBEX preference is not pointing to the correct location in the file system
   - Indicated in the log by "Error loading from <FileSystemLocation>"
   - For a temporary fix you can move the configs into that location, but for a better fix ensure that the preference is pointing to the correct location (The preference can point to multiple locations by separating them with commas
- The configs all have errors on them and cannot be loaded
   - Indicated in the log by "Error loading <ConfigName>: <error>"
   - The configs are maintained by the instrument scientists, however, obviously provide support and guidance for this
- There is a chance that Python has crashed due to an error
   - This will likely be in the log

## Some of my configs have not loaded

- We can point a preference to where to load configs from. This can be a combination of different places separated by commas. One of these preferences may be slightly incorrect and the configs from that location not loaded.
   - Indicated in the log by "Error loading from <FileSystemLocation>"
   - Find out where the preference should point, adjust it and reload the GUI
- Some of the configs may have errors in them and so failed to load
   - Indicated in the log by "Error loading <ConfigName>: <error>"
   - The configs are maintained by the instrument scientists, however, obviously provide support and guidance for this