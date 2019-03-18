Meeting to discuss this happened. Summary of the main points that were discussed is below:

# High level design

A high level design to use **Eclipse RCP** was agreed. We will build this in two configurations:
- As a perspective in the IBEX GUI, similar to other existing perspectives
- As a standalone application
Note that these two configurations will be using the same code (except for build-specific files).

The following general design points were agreed:
- The GUI will be written in Java (eclipse rcp). It should have minimal logic in it other than pure display logic
- It will talk to a python process embedded in the GUI, whose responsibility it is to generate a python script based on the input that a user has provided
  * Py4j is already included in our GUI build and allows for Java-Python communication
  * We need this process to be implemented in Python because it needs to be able to run arbitrary user-supplied python parameter validators (see also "The `Action` class", below).

# The `Action` class

An `Action` is the base building block that the script generator will use to build up scripts. It is essentially a wrapper around a python function that can tell us:
- Whether a given set of inputs is valid
- The types of the parameters
- Possibly other metadata in future

As an example, consider a class that looks something like:

```
class DoRun(Action):
    def run(temperature, field, uamps):
        g.cset("temperature", temperature)
        g.cset("field", field)
        g.begin()
        g.waitfor_uamps(uamps)
        g.end()

    def parameters_valid(temperature, field, uamps):
        return 0.1 <= temperature <= 300 and -5 <= field 5

    def parameter_types():
        return [float, float, float]
```
(this is not necessarily the final API)

We would probably define some default "Actions", but instrument scientists would be responsible for writing and maintaining their own instrument-specific actions (in a similar way to the current instrument scripts).

# User interface

There are two main types of user interfaces that support slightly different workflows. We have decided that we will eventually need to support both, but as part of the MVP we should only implement the table-based view.

### Table based (part of MVP)

This interface is a simple table. It is configured for one (and only one) type of `Action`. It configures it's columns to match the parameters of the action.

For example, for the `Action` defined above, the table in the script generator would look like this:

| temperature | field | uamps |
| --- | --- | --- |
| 50.0 | -1 | 100 |
| 80.0 | 2 | 100 |

Each row in the table corresponds to exactly one `Action`. The type of action must be the same for all rows (otherwise, the columns would no longer make sense).

### List/tree view (not part of MVP, but likely to be requested in future)

This interface is a list of Actions and their parameters. In this UI, each action can be of a different type. The actions are executed sequentially. This is a more flexible approach, however it looks closer to the final python script, so is slightly more complex to use (as a user) than the table-based approach. The UI would look more like a set of bullet points:
- `doRun - temperature=50, field=5, uamps=100`
- `changeSomething - value=1000`
- `doRun - temperature=100, field=5, uamps=100`

In this sense, it is quite a thin wrapper over a python script. The main advantage it gives you is parameter type/value checking (and arguably. In future we may be able to extend this approach to allow for loops or other types of more complex statements.

# Configuration

The script generator will be configured by loading in a configuration file. This configuration file can initially be written in Python - though we have not necessarily ruled out moving to another format in future if the need arises.

This configuration file will define the available `Action`s, and will be editable by the instrument scientists. Each instrument that uses the script generator will need at least one configuration file (maybe more if they have different experimental setups which require very different scripts).