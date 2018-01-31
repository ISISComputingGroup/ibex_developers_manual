> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Jaws and Slits](Jaws-and-Slits)

The GEM "Beamscraper" jaw set is unique to GEM. The four blades move independently and are all driven by a LinMot. Some calibration is required between the demanded position and the steps sent to the controller. For North/South this calibration is linear, for East/West it is quadratic.

## Control under SECI

LinMot calibration: 0.01953125 mm/steps (Mistakenly labelled as steps/mm in the VI)

Jaw | Offset | Read Calibration Curve | Write Calibration Curve
---- | -------| ------ | ----------
North | 2710 | `x + 0.025*x` | `x - 0.025*x`
South | 1530 | `x + 0.025*x` | `x - 0.025*x`
East  | 2200 | 	`(-0.12038 + 0.06452 * x  + 0.02998 * x**2)/0.9` | `(x - 0.1*x)` , `((-0.06452 + sqrt(0.06452**2 + 4*0.02998*(0.12038 + x))) / (2*0.02998))` 
West  | 2200 | 	`(-0.12038 + 0.06452 * x  + 0.02998 * x**2)/0.9` | `(x - 0.1*x)` , `((-0.06452 + sqrt(0.06452**2 + 4*0.02998*(0.12038 + x))) / (2*0.02998))` 

Where there are two equations the first equation calculates the x used in the second equation where there are two.

The calibration/offset values are used as below:

Read/Write | Axis | Equation
---------- | ---- | --------
Write | South | `OFF + (x / calibration)`
Write | N/E/W | `OFF - (x / calibration)`
Read | South | `(x - OFF) * calibration)`
Read | South | `(OFF - x) * calibration)`

Where x has been calculated from the calibration curves above.

The setpoints are all set to 5 when home is pressed. There is some tolerance checking, tolerance is set to 1.00, and is based on the presented value.

The limits for the values that the user can set are:

Axis | Min | Max
--- | --- | ---
H Gap | 0.2 | 25
V Gap | 0.2 | 40
North | 0.1 | 20
South | 0.1 | 20
West | 0.1 | 12.5
East | 0.1 | 12.5

## Control under IBEX