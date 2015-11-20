=============================================================
Refactoring for Observables, Observers, Writables and Writers
=============================================================

This document describes before and after of refactoring performed on various classes that relate to reading and writing to PVs.

Observers
---------
Before.

.. image:: images/refactoring_for_observables_and_writers/observers_before.png
   :height: 606 
   :width: 449
   :scale: 100 %
   :align: center

After.

.. image:: images/refactoring_for_observables_and_writers/observers_after.png
   :height: 525 
   :width: 438
   :scale: 100 %
   :align: center

After refactoring the two existing interfaces were combined into a single Observer interface, and ObservableAdapter was renamed.
