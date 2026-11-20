# Archive Engine Troubleshooting

## CSS components won't start (IDE, Block Archiver, Inst Archiver, Alarm server)

Ensure Java 8 is **NOT** installed on the system. If java 8 is installed, uninstall it and reboot. A java 8 installation will prevent CSS components from starting correctly, as they will detect this and attempt to use it, but they are incompatible with java 8 and require java 11+.

For the IDE:
- Symptom is either a hang at IDE startup (on splash screen, loading bar will never display) or an immediate pop-up saying java 8 is being used and is incompatible.
- Make sure java 8 (or any earlier java) is not installed on system and you have the current recommended IBEX java version installed.
- restart your machine
- run `git clean -fqdx` in the css directory
- run `create_icp_binaries.bat`
- run `setup_css.bat`
