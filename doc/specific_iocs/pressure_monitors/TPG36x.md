# TPG36x

The TPG36x IOC controls a series a pressure gauges. The TPG36x device is *very* similar to the [TPG26x](TPG26x) device: the main difference is that the TPG36x uses different communication terminators, and uses RS485 as opposed to RS232.

## Difference between 361 and 362

The 361 is single gauge whereas the 362 is dual gauge. This means the two devices have a different protocol in regards to pressure return values. The 362 returns 2 values whereas the 361 returns 1 value.

The drivers protocol defaults to the 362 protocol by having a default value of N for the macro IS361. If you have a 361 device this will cause a protocol mismatch and the **driver record will go into alarm**.

To change this for a 361 device set IS361 to Y in globals.txt or in an IBEX configuration.