# ENGIN-X Jaws

EnginX has 3 sets of jaws, all controlled by LinMot motors. The first two sets are conventional 4 axis jaws, each axis controlling a single blade. The 3rd jawset has 2 axis, one controlling horizontal gap, the other controlling the vertical. The 3rd jawset is also non-linear, i.e. due to complicated linkages a movement in the motor does not linearly correspond to the change in gap. The exact correlation is not known and changes over time as they often crash samples into the jaws. As such, scientists will periodically measure the relationship between set points and actual gaps, fit a quadratic to this data and modify the software accordingly. (They are hopefully getting new jaws soon)

The limits of the Jaws (taken from the limits on the controls in the labview) are:

<table>
  <tr>
    <td></td>
    <td colspan="2">Jaws 1 and 2</td>
    <td colspan="2">Jaws 3</td>
  </tr>
  <tr>
    <td></td>
    <td>Low</td><td>High</td>
    <td>Low</td><td>High</td>
  </tr>
  <tr>
    <td>H Gap</td>
    <td>0.2</td><td>82</td>
    <td>0.5</td><td>10</td>
  </tr>
  <tr>
    <td>V Gap</td>
    <td>0.2</td><td>82</td>
    <td>0.5</td><td>25</td>
  </tr>
  <tr>
    <td>For each blade</td>
    <td>-4.5</td><td>41</td>
    <td>N/A</td><td>N/A</td>
  </tr>
</table>

The calibration for Jaws 3 are currently:

Gap| SP -> Motor | Motor -> SP
--- | --------- | -----
Horizontal | -0.0776*x*x + 1.9001*x + 8.9105 | 0.0434*x*x - 0.4519*x + 0.8232
Vertical | 0.0138*x*x + 0.4146*x + 1.1885 | -0.0358*x*x + 2.0167*x - 2.0091