# Rotating Stirrer Rack

## About
Rotating stirrer rack uses [TTI-PLP to control motors](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Thurlby-Thandar-TTI-PLP-Power-Supply). The TTI-PLP IOC controls the motor itself, while Stirring Stages IOC controls front-end of Rotating Stirrer Rack interface. For this reason both IOCs need to be configured and enabled, to interact with Rotating Stirrer Rack. The IOC behaviour was modelled on existing VI which can be found at C:\LabVIEW Modules\Drivers\TTi PL-P Stirring Stages

### Configuration
ROTSTIRR needs to be configured in config area to use same IOC number as TTIPLP. Additionally voltage trip point and RPM operating range need to be (for now) manually defined by the user. ROTSTIRR requires a text file that dictates RPM-to-Voltage translation that is read from following location:

C:\Instrument\Settings\config\common\rotating_stirrer_rack\Default.txt

The file is read using [convert record](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Convert-Record). Example translation file can be found in the IOC directory.

### Tests
Since ROTSTIRR currently does not directly control any hardware, there was no need to create a Lewis emulator, however file structure is there in case that changes in the future. This decision was taken since I wanted to leave TTI-PLP in it's original behaviour so we can use it for other purposes (not just Rotating Stirrer Rack) - in line with something like Galil. The tests are not located in IocTestFramework - but rather in the support directory itself.