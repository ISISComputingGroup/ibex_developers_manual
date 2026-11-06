# GEM Beamscraper Jaws

The GEM "Beamscraper" jaw set is unique to GEM. The four blades move independently and are all driven by a LinMot. Some calibration is required between the demanded position and the steps sent to the controller. For North/South this calibration is linear, for East/West it is quadratic.

## Control under IBEX

The calibration curves under IBEX have been simplified to:

Jaw | Offset | Read Calibration Curve | Write Calibration Curve
---- | -------| ------ | ----------
North | 2710 | `1.025*x` | `x / 1.025`
South | 1530 | `1.025*x` | `x / 1.025`
East  | 2200 | 	`-0.13376 + 0.07169 * x  + 0.03331 * x**2` | `(-0.07169 + sqrt(0.07169**2 + 4 * 0.03331 *(0.13376 + x))) / (2*0.03331)`
West  | 2200 | 	`-0.13376 + 0.07169 * x  + 0.03331 * x**2` | `(-0.07169 + sqrt(0.07169**2 + 4 * 0.03331 *(0.13376 + x))) / (2*0.03331)`

Note that the linear calibration curve is actually incorrect in the VI as `1 / 1.025 != 0.975`. Therefore in IBEX `1.025` and `1 / 1.025` are used for reading and writing respectively.

To do these calibrations an additional soft motor record has been placed between the conventional jaws db and the real motor, such as described [here](../Creating-soft-motors-to-control-real-motors).

The offset / motor resolution in IBEX uses `(MRES * x) + OFF` when reading, therefore the new offset motor resolution in IBEX are:

Jaw | New Offset | New Motor Resolution
---- | -------| ------ 
South | `-SECI_OFF * SECI_MRES` | `SECI_MRES`
N/E/W | `SECI_OFF * SECI_MRES` | `-SECI_MRES`

Tolerance and limits have been included in IBEX, the homing has not.
