Galil behavior:

1. Set high limit (HLM) to 100
2. Begin move to 100
3. Whilst moving, set HLM to 50
4. When motor reaches 50, motor will begin to decelerate to a stop (some overshoot)
5. If motor has already reached 50, motor will begin to decelerate to a stop (some overshoot)

Simulated behavior:

1. Set high limit (HLM) to 100
2. Begin move to 100
3. Whilst moving, set HLM to 50
4. Motor will continue past the limit, to the commanded position of 100