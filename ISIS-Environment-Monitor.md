## Background
The Environment Monitor is a simple, read-only device with two sensors, A and B, that can be attached. Each sensor records a temperature value and a humidity value. In the IOC macros, each sensor can be set as connected or disconnected, defaulting to disconnected.

| PV Name      | Meaning      |
| ------------- | ------------- |
| TEMPA | Temperature reading from sensor A |
| RHUMIDA | Relative humidity reading from sensor A |
| TEMPB | Temperature reading from sensor B |
| RHUMIDB | Relative humidity reading from sensor B |
| SENSORA:PRESENT | Whether Sensor A is connected (yes / no) |
| SENSORB:PRESENT | Whether Sensor B is connected (yes / no) |

## IOC Setup
The IOC has two macros for sensor A present and sensor B present which need to be set in the IOC configurations.
When connecting to the real device it must be connected via serial, and the IOC requires the device's COM Port in its macros.

## Implementation
The device only takes one command with no argument ```?STS``` which will return data in the following format e.g "A21.31,B43.01,C22.12,D31.67", whereby the floats after each letter represent the following in this order, 
- A : Temperature A (°C)
- B : Relative Humidity A (%)
- C : Temperature B (°C)
- D : Relative Humidity B (%)

Anything other than ```?STS``` sent return ```NAK```.