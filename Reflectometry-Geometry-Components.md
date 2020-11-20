> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [Geometry Components](Reflectometry-Geometry-Components)

A component represents a point of interaction with the beam on the beamline; for example, a slit set or mirror. They form the relationship between:

- the incoming beam: the position in space and angle of the beam which will intersect the components movement
- outgoing beam: the beam path after the beam has interacted with the component (which may or may not be altered)
- user set value relative to the beam: where the user would like an object relative to the beam (e.g. for something on the beam 0mm above the beam) on a given axis (e.g. linear / rotational offset)
- Mantid coordinates: the values for position in the room or of underlying PVs value, often a motor. Theses value don't change based on moving the beam.

In effect, the component layer is responsible for translating motor values/mantid coordinates (relative to straight-through beam) to high-level parameter values (relative to current beam path) and vice versa.

Each component captures the relationships for both set points (where the user wants the beamline to be) and readbacks (where the beamline actually is) separately i.e. the system maintains two separate models of the beam path. 

**For more information on implementation specifics see the [Beamline Configuration page](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Reflectometry-Configuration#components)**

## Architecture

This section is *Work in progress*

### Major Classes

![Architecture of the component](reflectometers/ComponentArchitecture.png)

The components contains two major elements the beam path setpoint and beam path readback. The setpoint allows positions to be set from user parameters and these setpoints are translated to setpoints on the motor level. The readback takes motor positions and calculates the user parameters from them. Both use the beam path (also either setpoint or readback) to perform the calculations. The beam path calc object that perform the calculation try to be generic for both cases, to differentiate between the motor and user level we use the terms relative to beam, for user parameters, and displacement, for motor parameters. This makes complete sense for the tracking parameters but less so for the direct parameters, which are relative to the fixed beam so also absolute, e.g. for a TRANS axis the beam is always at 0 so relative and displacement will be the same.
The tracking beam path calc has a number of component axes representing a single quantity that can change, e.g. slit 2 height. These must have a variety of methods on them to allow the axis value to be read and written in various ways, e.g. relative to beam, and it has whether the axis is in various states, e.g. changing because the motor is moving. These states are:

- `is_changing`: an underlying motor is moving
- `is_changed`: a set point has been changed but the change has not been sent to the driving layer
- `alarm`: the alarm status of the axis, usually a reflection of the underlying motor axis
- `is_in_beam`: True if this axis in the beam, i.e. not at its parked position
- `has_out_of_beam_position`: True if the axis has an out of beam position, these are usually set on the driving layer
- `can_define_axis_position_as`: True if the axis can have its position defined as something else
- `autosaved_value`: The value last read from autosave for this axis

There are two sorts of axes, `DirectAxis` and the `BeamPathCalcAxis`. The `DirectAxis` overrides the methods above to set there is no transform between relative and displacement values. The `BeamPathCalcAxis` uses the methods from the `TrackingBeamPathCalc` to calculate the various values. The axis pointing to the methods is not as clean as it should be; but it is unclear exactly how it should change.

In general a component is made from multiple axes and can respond to changes in those axes, the bench component does this for instance. The bench component has 3 user parameters height, angle and seesaw and these drives three drivers front jack, rear jack and slide. All of these changable values are axes. To make this work the component monitors the  monitors for changes in the values and transforms the user parameters to the motor axes for set points and vice versa for read backs.

The `InBeamManager` is used to coordinate whether a component is in the beam based on all of its axes. This can either be set from a user parameter in which case user axes get set or it can read from the motor axes for the readbacks.

The most complicated component is the `ThetaComponent` this has two beam calcs one for the readback `BeamPathCalcThetaRBV` and one for the setpoint `BeamPathCalcThetaSP`. The setpoint simply reflects the beam when it reaches the virtual sample point whereas the read back needs to calulcate the angle of the component that it is pointed at. 

The final complication is that components that define where theta do not use the readback beam path to calulcate there position because this would always be zero, since it defines theta, instead they use the setpoint beam path.

### Events

The whole system of readbacks, and to lesser extend setpoints, work on events being passed between the various classes. We have tried very hard not to bind the components to any of part of the system directly so that the component layer can act independently. To so this events are monitored with observers. This has mostly be successful but it does get slightly complicated what the events are and where the go so we will present what events we have and where they go for a typical beamline.

#### Defining, Triggering and Observing an Event

The event is captured using a single class, this can be whatever you need but the trend at the moment is to use a dataclass (there are still quite a few named tuples about). For example:

```
@dataclass()
class MyEvent:
    """
    doc
    """
    param1: <type name>
    param2: <type name>
```

To make a class observable simply add `@observable(<event>)`:

```
@observable(MyEvent, OtherEvent, ThirdEvent)
class IWantToObserveThis()
...
```

When you want to trigger the event in the class use:

```
self.trigger_listeners(MyEvent(value1, value2))
```

To observe the event you need a call back function which takes the event as an argument to the instance of the class and this will be called when the event is triggered, e.g.

```
def my_callback(event: MyEvent):
   ....

i_want_to_observe_this = IWantToObserveThis()
i_want_to_observe_this.add_listener(my_callback)
```

We use this pattern every where, so lets look at how a setpoint which is not in the mode gets to the motor:



