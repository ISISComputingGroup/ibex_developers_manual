To deploy a new IOC to an instrument, or patch an existing one, different levels of care need to be taken depending on what has changed

* OPI for new IOC

You do not usually need to deploy a new GUI, in fact it is best to avoid this as you may update other OPIs unintentionally, introducing changes that need IOC updates you are not deploying. So go for the minimal change approach if possible:
- keep existing GUI build
- copy across just the OPI changes you need and leave everything else as is
- if necessary (as in new rather than changed device), manually edit `opi_info.xml` to add new OPI to ibex list   

