# Clearing the "motors moving" state

If a motor controller is disconnected during a move, then the moving flag is left in a moving state. This can cause scripts to fail to run. Each motor controller can supply the moving state information for the global `CS:MOT:MOVING` flag, so while you can caput to the specific record to reset this a server restart can be the quickest way to remedy this issue.