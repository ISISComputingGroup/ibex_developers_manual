> [Wiki](Home) > [The Backend System](The-Backend-System) > [Specific Device IOC](Specific-Device-IOC) > [Miscellaneous motion control](Miscellaneous-Motion-Control) > [Reflectometry IOC](Reflectometry-IOC) > [POLREF](Reflectomtery-IOC-POLREF)

Specific information about POLREF.

### Slit 3/Beam blocker

Slit 3 is a tall set of normal jaws sitting on the bench. In horizontal sample mode the centre of the jaws is set using the `S3OFFSET` parameter which sets the distance from beam to the jaws, (usually set to 0). The bench movement means that the centre of the jaws rarely needs to change except during a slit scan.
Slit 3 can also be set into beam blocker mode; south jaw in horizontal mode, east or west jaws in vertical sample mode. In this state the beam blocked jaws will move independently of the slit centre using `S3S` and `S3N` or `S3W` and `S3W`. They retain the natural jaw directions so that positive is away from the centre of the jaw.