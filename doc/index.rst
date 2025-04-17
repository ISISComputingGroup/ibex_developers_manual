

Welcome to ibex_bluesky_core's documentation!
=============================================

``ibex_bluesky_core`` is a library of common ``bluesky`` functionality and ``ophyd-async``
devices for use on the ISIS neutron & muon source's beamlines.

`Bluesky <https://blueskyproject.io/bluesky/main/index.html>`_ is a generic data acquisition
framework, which started at NSLS-ii but is developed as a multi-facility collaboration. Bluesky
provides concepts such as "scanning" in a generic way.

`ophyd-async <https://blueskyproject.io/ophyd-async/main/index.html>`_ is a python device
abstraction library, which allows bluesky to communicate with an underlying control system
(EPICS/IBEX, in our case).

``ibex_bluesky_core`` provides:

- Central configuration for core bluesky classes, such as the ``RunEngine``.
- ``RunEngine`` Callbacks customized for use at ISIS: file writing, plotting, fitting, ...
- Central implementations of ISIS device classes using ``ophyd-async``: Blocks, DAE, ...
- Bluesky or scanning-related utilities which are useful across multiple beamlines.


Getting started
===============

.. toctree::
   :maxdepth: 2
   :caption: Tutorial
   :glob:

   tutorial/overview.md

Reference documentation
=======================

.. toctree::
   :maxdepth: 2
   :caption: Devices
   :glob:
   
   devices/*

.. toctree::
   :maxdepth: 2
   :caption: Callbacks
   :glob:

   callbacks/*

.. toctree::
   :maxdepth: 2
   :caption: Fitting
   :glob:

   fitting/*

.. toctree::
   :maxdepth: 2
   :caption: Plan stubs
   :glob:

   plan_stubs/*

.. toctree::
   :maxdepth: 2
   :caption: Plans
   :glob:

   plans/*

.. toctree::
   :maxdepth: 2
   :caption: Plans (Reflectometry)
   :glob:

   plans/reflectometry/*

.. toctree::
   :maxdepth: 2
   :caption: Preprocessors
   :glob:

   preprocessors/*

.. toctree::
   :maxdepth: 2
   :caption: Developer information
   :glob:

   dev/*
   
.. toctree::
   :titlesonly:
   :caption: Architectural decisions
   :glob:
   :maxdepth: 1

   architectural_decisions/*

.. toctree::
   :titlesonly:
   :caption: API reference

   _api
