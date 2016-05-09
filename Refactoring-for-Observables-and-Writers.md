> [Wiki](Home) > [The GUI](The-GUI) > [Coding](GUI-Coding) > Refactoring for observables and writers

Class Diagrams for Observables, Observers, Writables and Writers
================================================================

This document contains the class diagrams for the various classes that relate to reading and writing to PVs.
It also shows how the design has been evolved and refactored over time.

Observables and Observers Overall Diagram
=========================================

NOTE: PairObservable is not depicted for clarity.

Original
--------

![Observables and observers pre nov 2015](GUI_development/images/refactoring_for_observables_and_writers/observables_and_observers_pre_nov_2015.png)
 
 
    
November 2015
-------------

![Observables and observers nov 2015](GUI_development/images/refactoring_for_observables_and_writers/observables_and_observers_nov_2015.png)
 
 
    
January 2016
-------------

![Observables and observers jan 2016](GUI_development/images/refactoring_for_observables_and_writers/observables_and_observers_jan_2016.png)
 
 


Observables
===========
Original
--------

![Observables before](GUI_development/images/refactoring_for_observables_and_writers/observables_before.png)




November 2015
-------------

![Observables after](GUI_development/images/refactoring_for_observables_and_writers/observables_after.png)




   
January 2016
-------------

![Observables Jan 2016](GUI_development/images/refactoring_for_observables_and_writers/observables_2016_01.png)





Observers
=========
Original
--------

![Observers before](GUI_development/images/refactoring_for_observables_and_writers/observers_before.png)




November 2015
-------------

![Observers after](GUI_development/images/refactoring_for_observables_and_writers/observers_after.png)





After refactoring the two existing interfaces were combined into a single Observer interface, and ObservableAdapter was renamed.

Writables
=========
Original
--------

![Writables before](GUI_development/images/refactoring_for_observables_and_writers/writables_before.png)




November 2015
-------------

![Writables after](GUI_development/images/refactoring_for_observables_and_writers/writables_after.png)




   
April 2016
-------------

![Writables Apr 2016](GUI_development/images/refactoring_for_observables_and_writers/writables_april2016.png)



   
After refactoring, the ForwardingWritable is passed a converter, which can either convert value or do nothing.

Writers
=======
Original
--------

![Writers before](GUI_development/images/refactoring_for_observables_and_writers/writers_before.png)




November 2015
-------------

![Writers after](GUI_development/images/refactoring_for_observables_and_writers/writers_after.png)





