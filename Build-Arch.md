> [Wiki](Home) > [Project tools](Project-tools) > [Build Arch](Build-Arch)

Build a directory under a given architecture instead of the default. This will switch the archtiecture temporarily to a given state for building. You can build multiple architectures within the same tree of EPICS (it will be built into `bin/<architecture>`). Run:
 
    build_arch <architctrue>

e.g. build_arch windows-x64-static

Architectures allowed are given my the files in .... TODO
