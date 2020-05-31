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

The database stores the infomration to all of the measurements taken from devices, as well as infomration about every device, their model, type and siplay properties. It was developed by the team at HZB and currently runs on MySQL.

## Overview

## List of devices categorised by their function

[Coordinators](Coordinators)

[Balance devices](Balance-devices)

[Storage devices](Storage-devices)

[Gas flow meters](Gas-flow-meters)

[Position](Position)

[Measurement devices](Measurement-Devices)

[Indicators](Indicators)

[Valves](Valves)