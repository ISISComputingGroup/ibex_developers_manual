=============================================
Overview of Observables and Observers in IBEX
=============================================

This documentation is intended for anyone using or changing the code in uk.ac.stfc.isis.ibex.epics.observing. Here there is a high level description of what each class provides.

The tests in uk.ac.stfc.isis.ibex.tests.observing should also be used to understand the behaviour of these classes.

Abstract Observables
====================

Observable Interface and BaseObservable
----------------------------------------

The observable specifies a :code:`addObserver()` method, and is implemented by all observables. BaseObservable implements this, along with protected :code:`setValue()`, :code:`setError()` and :code:`setConnectionStatus()` methods intended to be used by subclasses.

ClosableObservable Interface
----------------------------

This is an observable that can be closed, normally to close a connection to a PV. Inherits the Observable and interfaces but also specifies a :code:`close()` method.

CachingObservable Interface and BaseCahingObservable
----------------------------------------------------

This specifies the methods :code:`getValue()`, :code:`isConnected` and :code:`lastError()`. The values returned by these are all 'cached' as fields on the BaseCahingObservable object.

ClosableCachingObservable Interface
-----------------------------------

Implements both ClosableObservable and CahingObservable interfaces.

ForwardingObservable Abstract Class
-----------------------------------

An observable that takes a CachingObservable as an argument, and observes it, updating itself when the other observable changes.

TransformingObservable Abstract Class
-------------------------------------

Converts the value it is observing from one type to another, via a method implemented in a sub class.

Concrete Observables
====================

* InitialiseOnSubscribeObservable - Takes a CahingObservable and immediately calls the update value on the observer, which calls :code:`onValue()`, :code:`onError()` and :code:`onConnectionStatus()`

* SwitchableObservable - Takes a CachingObservable, but can be switched to another CachingObservable

* ClosingSwitchableObservable - Similar to SwitchableObservable, but will also close the connection to the old observable on switching

* ConvertingObservable - Will convert an observable between types, taking a Converted object as its argument

* ObservablePair - Takes two observables, of any type, and observes them both, updating when either changes (returns a Pair object with the fields :code:`first` and :code:`second`)

Abstract Observers
==================

Observer Interface
------------------

Implements an interface with methods :code:`onValue()`, :code:`onError()` and :code:`onConnectionStatus()`

InitialisableObserver Interface
-------------------------------

Adds the update method to the Observer, which calls the three methods in the Observer interface

Concrete Observers
==================

* Logging Observer - An observer that writes a log message whenever it receives changes

Subscription
============

Subscription Interface
----------------------

This has a :code:`removeObserver()` method. An object conforming to this interface is returned when :code:`addObserver()` is called on an observable, providing a way to remove the observer.

Concrete Subscriptions
----------------------

* Unsubscriber - the only implementation of Subscription, holds references to the observerables list of observers, and the observer, and implements the :code:`removeObserver()` method

Class Overview
==============

The image below shows an overview of the class hierarchy for the observables as it has evolved over time. Note that PairObservable is left off to keep the diagrams easy to read.

Original
--------

.. image:: images/overview_of_observables_and_observers_in_ibex/observables_pre_nov_2015.png
    :scale: 100 %
    :align: center
    
November 2015
-------------

.. image:: images/overview_of_observables_and_observers_in_ibex/observables_nov_2015.png
    :scale: 100 %
    :align: center
