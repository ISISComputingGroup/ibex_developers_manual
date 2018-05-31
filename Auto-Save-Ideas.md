After a quick chat with Freddie have had thoughts about auto save and PV sets.

The problem to be solved is how to use autosave as part of a configuration which can be changed. The thought here are we want to be able to quick and easily use the autosave mechanism within configurations. Use cases are usually for motors:

1. Multiple motor settings need to be stored and are set for all time
1. It is possible different configuration should use different settings
    - an example of this is when LARMOR uses different sample stacks the limtis are different
1. If the Galil power cycles (it is on UPS) then the last known position should be restored so scientists do not have to rehome

Idea is to save things into an autosave file but only autosave manually for settings. Different config would use different autosave files.
Things like the galil position that are continuously saved are saved to a different file and loaded in a normal fashion.