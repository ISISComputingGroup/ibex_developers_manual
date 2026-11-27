# `raw_data_1/runlog/icp_event`

The `icp_event` dataset describes DAE state transitions. A new entry is written on each state transition.

The entries are written as strings, in the following formats:

### `CHANGE_PERIOD %d`

This is written on a transition from one period to another (including one just before run start, resetting period to 1).

### `START_COLLECTION PERIOD %d GF %d RF %d GUAH %f`

This is written whenever the acquisition transitions from a not-collecting state (e.g. SETUP, PAUSED, WAITING) to a
collecting state (e.g. RUNNING).

The GF (good frames), RF (raw frames) and GUAH (good uAh-hour) counters reflect the total in the run so far.

### `STOP_COLLECTION PERIOD %d GF %d RF %d GUAH %f DUR %d`

This is written whenever the acquisition transitions from a not-collecting state (e.g. SETUP, PAUSED, WAITING) to a
collecting state (e.g. RUNNING).

The GF (good frames), RF (raw frames) and GUAH (good uAh-hour) counters reflect the total in the run so far.

The DUR (duration) parameter describes the duration, in seconds, of the acquisition period since the `START_ACQUISITION` message

### `BEGIN`

This is written at the beginning of a run.

### `FAILED_BEGIN`

This is written when a run attempted to start, but failed.

### `END`

This is written at the end of a run.

### `PAUSE`

This is written when a run pauses.

### `RESUME`

This is written when a run resumes from a pause.

### `WAIT_START`

This is written when run control transitions to out-of-range.

### `WAIT_FINISH`

This is written when run control transitions to in-range.

### `ABORT`

This is written when a run is aborted (ended without saving data).
