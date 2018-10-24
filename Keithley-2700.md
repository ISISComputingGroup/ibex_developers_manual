This is a multimeter used on HIFI to measure the temperature (via measured resistance values) at diffrerent points on the cryomagnets. It also calculates the temperature drift between measurements, in part to check the stability of the magnet. 

### Drift

The calculation used to calculate the drift uses information from the previous scan (inclulding the previous calculated drift) and the information from the new scan. 

![drift-calculation]

Where 

![delta-temp]

![delta-time]

![dn]

![dp]


[//]: # (URLs for latex images)

[drift-calculation]: http://mathurl.com/y77q3ex2.png

[dn]: http://mathurl.com/ydykpgb5.png

[dp]: http://mathurl.com/ycpzu8wu.png

[delta-temp]: http://mathurl.com/ybcns6ud.png

[delta-time]: http://mathurl.com/y8lccdz7.png