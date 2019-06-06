> [Wiki](Home) > [Galils Under SECI](galils-under-seci)

The move is undertaken as a state machine, and as such the text below attempts to explain the behaviours


State Name | Actions in State | Condition for next state | Next State
---        | ---              | ---                      | ---
Init       |                  | First Call               | Idle
|          |                  | New Setpoint             | Send Setup
|          |                  | Stop triggered           | Stop
|          |                  |                          |
Idle       |                  |                          | Send Setup
|          |                  |                          |





