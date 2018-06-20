> [Wiki](Home) > [Project overview](Project-overview) > [Decision Log](Decision-Log)

A place to record decisions:

1. Decide format for calibration files. Decided to update labview and add a header with comments. This is because updating Seci is not a huge amount of work (1/2 day to do all instruments) and we don't make want to make a halfway house that has to be changed in the future. We don't want to go as far as allowing manufacturer file directly in EPICs because this is hard; this option can happen in the future.

2. We will not (in general) put `@init` handlers on records. This is because it is hard to do for any records which contain intermediate logic.
