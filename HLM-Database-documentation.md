Temporary root for documentation for HLM database documentation.

# Helium Level Monitoring Database

1. [Introduction](#introduction)
2. [Overview](#overview)
3. [List of functions](#list-of-functions)

## Introduction

The Helium Level Monitoring project is concerned with developing software for the management of helium for a large scale scientific facility. It is a collaboration of the HZB, ILL and ISIS, under the umbrella of the International Society for Sample Environment.

Helium is becoming increasingly rare and expensive. Therefore, smart management is needed in order to minimise losses, track expenses, and localise and fix leaks. 

The HLM software developed at HZB is responsible for tracking the all inputs and outputs in to the helium supply system, helium usage at individual experiments, helium levels in all types vessels, and the flow of helium gas in recovery lines. Moreover, it allows for detecting overpressure in vessels and detecting warm/forgotten vessels.

The data is collected from the scales used for weighing incoming and outgoing Helium vessels, the wireless base stations, and the gas counters from the gas recovery lines.

The wireless base stations are wireless devices developed by HZB that use the XBEE protocol to communicated. They gather data from various level meters, cryostats, gas counters, etc., that are in the facility. These devices can be moved, and therefore the HLM software is also used for locating them.

The database stores the information to all of the measurements taken from devices, as well as information about every device, their model, type and display properties. It was developed by the team at HZB and currently runs on MySQL.

## Overview

The main table in the database is the GAM_OBJECT table. This table represents an object, which is an individual piece of equipment used for helium management: an individual level meter, an individual cryostat, and so on.

Objects are classified into object types, which are themselves classified into object classes, which are classified into functions.

In addition, the database stores relationships between individual devices, as well as various measurements associated with one object.

Finally, the database has the GAM_COORDINATE, GAN_DISPLAY, GAM_IMAGE and GAM_NETWORK tables, which provide information used for the graphical UI representation of the helium management system.

![Schema for the database of the HLM program](D:\Documente\Munca\HLM\software\update GAM ERD)

## List of devices grouped by their function

[Coordinators](Coordinators)

[Balance devices](Balance-devices)

[Storage devices](Storage-devices)

[Gas flow meters](Gas-flow-meters)

[Positions](Positions)

[Measurement devices](Measurement-Devices)

[Indicators](Indicators)

[Valves](Valves)