> [Wiki](Home) > [Processes](Processes) > [Estimating Sprint Capacity](Estimating-Sprint-Capacity)

Sprint capacity is not used by this group to limit points in a sprint, but to track work throughput via a burndown chart.

The values applied to tickets can be found in the announce channel on our teams instance. The points for a ticket should include time for reviews and any rework and reviews that may be needed. At the last update of this page these are:
```
1 point < 1 hour 
2 points < 0.5 day 
3 points < 1 day 
5 points < 2 days 
8 points < 3 days 
13 points < 5 days 
20 points < 8 days 
40 points < 16 days 

Timeboxes - pointing allows for reviews 
0.5 day - 3 points 
1 to 1.5 days - 5 points 
2 to 2.5 days - 8 points 
3 to 4.5 days - 13 points 
5 to 7 days - 20 points 
```

The value assigned to a sprint is `the_number_of_days_in_this_sprint * the_average_from_the_previous_three_sprints_of_(points_completed_in_sprint/the_number_of_days_in_the_sprint)`

The number of days in a sprint is the sum of the days that the team members are available between the start and end date, with a multiplier to allow for the time spent not doing work on tickets which varies based on the responsibilities of different team members.