=============================================================
Refactoring for Observables, Observers, Writables and Writers
=============================================================

This document describes before and after of refactoring performed on various classes that relate to reading and writing to PVs.

Observables
===========
Original
--------

.. image:: images/refactoring_for_observables_and_writers/observables_before.png
   :height: 606 
   :width: 449
   :scale: 100 %
   :align: center

November 2015
-------------

.. image:: images/refactoring_for_observables_and_writers/observables_after.png
   :height: 525 
   :width: 438
   :scale: 100 %
   :align: center

Observers
=========
Original
--------

.. image:: images/refactoring_for_observables_and_writers/observers_before.png
   :height: 606 
   :width: 449
   :scale: 100 %
   :align: center

November 2015
-------------

.. image:: images/refactoring_for_observables_and_writers/observers_after.png
   :height: 525 
   :width: 438
   :scale: 100 %
   :align: center

After refactoring the two existing interfaces were combined into a single Observer interface, and ObservableAdapter was renamed.

Writables
=========
Original
--------

.. image:: images/refactoring_for_observables_and_writers/writables_before.png
   :height: 606 
   :width: 449
   :scale: 100 %
   :align: center

November 2015
-------------

.. image:: images/refactoring_for_observables_and_writers/writables_after.png
   :height: 525 
   :width: 438
   :scale: 100 %
   :align: center

Writers
=======
Original
--------

.. image:: images/refactoring_for_observables_and_writers/writers_before.png
   :height: 606 
   :width: 449
   :scale: 100 %
   :align: center

November 2015
-------------

.. image:: images/refactoring_for_observables_and_writers/writers_after.png
   :height: 525 
   :width: 438
   :scale: 100 %
   :align: center

