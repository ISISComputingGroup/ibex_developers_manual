> [Wiki](Home) > [Processes](Processes) > [Sprint Burndown Chart](Sprint-Burndown Chart)

Sprint Burndown Chart

The [sprint burndown chart](http://shadow.isis.cclrc.ac.uk/ibex/burndown-points.html) is intended to show the team's progress towards the sprint goal (expressed as a target number of points for the sprint).  It is reviewed daily, during the daily stand-up meeting, so that everyone in the team can see the team's progress.

The chart is deliberately arranged to show progress as a count down.  At the start of the sprint there are <N> points in the sprint backlog.  As work progresses, individual backlog items are completed and the item's number of points is deducted from the target.  Thus, the lines on the chart show the cumulative progress of the team towards completing all items in the sprint backlog.

The target is the total number of points in completed tickets the team expects to achieve in the sprint.

#### What do the lines on the Chart mean?  
The chart shows 3 lines:
   1. Completed - shows the target minus the number of points in completed tickets as a function of time.
   1. Completed (Ideal) - shows the "ideal" progress, assuming points are earned at a steady rate.  The purpose of this line is to act as a comparison to the Completed line.
   1. Review + Completed - shows the target minus the number of points of tickets in the Review & Completed columns.

In an ideal world, the Completed line will coincide with the Ideal line.  However, it is not realistic to expect backlog items to be completed at a steady rate - backlog items are discrete items, of differing size, taking varying times to complete.  In reality, the Completed line will always diverge from Ideal line.  

#### So what is the purpose of the Ideal line?  
If the team completes backlog items in a metronomic fashion, the Completed line will closely track the Ideal line.  If the Completed line diverges from the ideal line, it provides an immediate visual indication of the team's progress relative to the ideal.
   * if the Completed line is above the Ideal line, the team is not achieving sufficient points to meet the target
   * if the Completed line is below the ideal line, the team is on track to exceed the target.
Small divergences are usually just a reflection of the discrete size of backlog items - they usually correct after a few days.  Larger divergences are an indication of a problem.

#### So what do divergences mean?:
Divergences above the Ideal line can mean:
   * The team is consistently underestimating the size/complexity of backlog items.  It is taking longer than expected to complete backlog items.
   * The team is setting its target too high.  It is over-filling the sprint backlog and setting an unrealistically high target.  It cannot, therefore, complete tickets fast enough to keep up with the Ideal line.
   * There is a bottleneck in the process; something is preventing backlog items making it through to completion.
   * Something else is diverting the attention of the team.

Divergences below the Ideal line can mean:
   * The team is consistently overestimating the size/complexity of backlog items.  They are completing backlog items faster than expected.
   * The team is setting its target too low.  It is under-filling the sprint backlog and choosing an overly pessimistic target.

When the team sees the Completed line diverging significantly from the Ideal line, it needs to take action, to correct its course.

The Review + Completed line helps diagnose potential problems.  It shows the number of points in the Review and Completed columns.  It is a measure of the what the team could potentially achieve if all the items in the review column were completed.  If there are a large number of items in the review column, it will diverge from the Completed line.  It is an indicator of a build-up of items in the Review column.  The greater the divergence between the Completed  and the Review + Completed lines, the greater the build-up.
