> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [POLREF](Reflectomtery-IOC-POLREF)

Specific information about POLREF.

### Slit 3/Beam blocker

Slit 3 is a tall set of normal jaws sitting on the bench. In horizontal sample mode the centre of the jaws is set using the `S3OFFSET` parameter which sets the distance from beam to the jaws, (usually set to 0). The bench movement means that the centre of the jaws rarely needs to change except during a slit scan.
Slit 3 can also be set into beam blocker mode; south jaw in horizontal mode, east or west jaws in vertical sample mode. In this state the beam blocked jaws will move independently of the slit centre using `S3S` and `S3N` or `S3W` and `S3W`. They retain the natural jaw directions so that positive is away from the centre of the jaw.

### Components on the Bench

Components that are on the bench do not track the beam in the same way as normal components. They rely on the underlying bench to track the beam and then their positions are just relative to the bench. This will in effect look the same as if they were tracking the beam but they don't.

### Blocks

Blocks that may be confusing:

- `Height`: Distance from the sample centre of rotation to the sample. This is used to align the sample with the beam.
- `Height2`: Distance between the beam and the centre of rotation; usually set a 0. This moves the course z stage tracking the beam.

### Parameter Autosave

It is hard to know which parameters to autosave and which not to. Probably with use we will find out. I have gone with Theta and polariser angles are not autosaved all other heights and offsets are. So that when coming back from SECI the setpoints will mirror those in SECI quite closely. Other axis parameters, direct parameters and slits are not autosaved so they come back as they are, except for bench angle offset and seesaw which are autosaved.
