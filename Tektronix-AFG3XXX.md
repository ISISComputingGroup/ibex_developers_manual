> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Signal Generators](Signal-Generators) > Tektronix AFG3XXX](Tektronix-AFG3XXX)

The Tektronix AFG3XXX is a signal generator.

It has an OPI for very basic controls, such as a trigger button and readbacks/setters for frequency, voltage and voltage offset. 

The trigger PV is a `bo` type but calls `*TRG` on the device which generates a trigger event. 