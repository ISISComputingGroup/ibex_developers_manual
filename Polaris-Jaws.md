> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > [Polaris Jaws](Polaris-Jaws)

Polaris jaws are a set of 5 jaws which work in concert to limit the beam of neutrons reaching the sample. Jaws 1-4 are instrument user controlled and work together in a pyrmid shape to reduce the beam size in stages. The gap in each jaw set is set based on its distance from the sample. 

Jaw set 5 is under on instrument scientist control. To change these settings the user must put the GUI into management mode. 

## Setup

The control files for the polaris jaws are part of the gallil motor set up and are per instrument. There is an example in `...\EPICS\support\motorExtensions\master\settings\polaris_jaws\*.cmd` which would need to be copied to `C:\Instrument\Settings\config\<instrument host name>\configurations\galil`
