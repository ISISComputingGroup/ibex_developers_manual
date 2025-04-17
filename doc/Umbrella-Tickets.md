Umbrella tickets (or Epics in agile speak) are over arching tickets which contain multiple stages. Sometime you may feel it is beneficial for you or the reviewer to split a ticket which has been agreed in backlog prep into multiple smaller tickets; in this case you create an umbrella ticket. These can exist as actual tickets, but can also be raft tickets on the Program Increment (PI) board.

## On the PI Board

* These will have a classification of `Project/Feature`, and will have a whole number for the `PI Priority`.
* The smaller tickets will have a classification of `To do for a Project/Feature`, and will have a decimal value for the `PI Priority`. The number for the decimal point is the priority for the umbrella ticket, and the number after is the priority in relation to the other tickets underneath that umbrella.

## Case 1 Before working on an original ticket it is clear it should be split

* Create a smaller ticket it should be named `<TICKET NUMBER>-1`: `<Ticket purpose>`
* Estimate the ticket
* Assign the ticket to yourself
* Reference the ticket in the original ticket and reduce its estimate by the estimate of this ticket. If this makes the ticket negative by more than 1 then talk about it with a member of the team.
* Work on the ticket as if it were a normal ticket

## Case 2 After working on a ticket for a while you want to spin out a new ticket

* Create the umbrella ticket with the original estimate of the ticket minus the estimate of the present ticket. If this makes the ticket negative by more than 1 then talk about it with a member of the team.
* Name this ticket the same as the original
* Rename the original tickets as `<TICKET NUMBER>-1`: `<Ticket purpose>`
* Set the estimate on the original ticket
* Spin out any new tickets as in case 1

