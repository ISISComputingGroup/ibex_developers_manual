=============================================================
Refactoring for Observables, Observers, Writables and Writers
=============================================================

This document describes before and after of refactoring performed on various classes that relate to reading and writing to PVs.

Observers
---------

Before.

.. image:: images/refacotring_for_observables_and_writesrs/observers_before.png
   :scale: 50 %
   :align: center

After.

 .. image:: images/refacotring_for_observables_and_writesrs/observers_after.png
    :scale: 25 %
    :align: center

After refactoring the two existing interfaces were combined into a single Observer interface, and ObservableAdapter was renamed.
