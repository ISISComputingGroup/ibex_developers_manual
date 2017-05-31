> [Wiki](Home) > [Project tools](Project-tools) > [Config Upgrader](Config-Upgrader)

The config upgrader will upgrade a config to include all the latest changes. This will be run as part of the [deployment steps](Deployment-on-an-Instrument-Control-PC).

The script looks for a version number in the configuration directory and take the config from there to the latest config using upgrade steps. To run it in an EPICS terminal use:

    cd ...\EPICS
    python misc\upgrade\master\upgrade.py

Log files are written to `...\Var\logs\upgrade`. You will then need to use git to commit any changes. 

## Adding an upgrade Step

To add an upgrade step create an upgrade class in `...EPICS\misc\upgrade\master\src`. This class should derive from class `UpgradeStep` and have a single function `def perform(self, file_access, logger):` so it should be of the form:

```
class UpgradeStepFromXpxpx(UpgradeStep):
    """
    What it does
    """

    def perform(self, file_access, logger):
        """
        Perform the upgrade step

        Args:
            file_access (FileAccess): file access
            logger (LocalLogger): logger

        Returns: exit code 0 success; anything else fail

        """
        logger.info("Starting step ...")
        return -1
```

Next the step needs to be added to the upgrade list. This is found in `upgrade.py` and look like:

```
UPGRADE_STEPS = [
    ("3.2.1", UpgradeStepFrom3p2p1()),
    ("3.2.1.1", UpgradeStepFrom3p2p1p1()),
    ("3.2.1.2", UpgradeStepNoOp()),
    ("3.3.0", None)
]
```

Add the entry in replacing the `None` with your class, then add a new version label and None. The version label should be of the form "X.X.x.m" where `X.X.x` is from the last production build and `m` is the next number. The `("3.2.1.2", UpgradeStepNoOp)` line is a way of getting from a development configuration to a production build without doing anything. E.g.

```
UPGRADE_STEPS = [
    ("3.2.1", UpgradeStepFrom3p2p1()),
    ("3.2.1.1", UpgradeStepFrom3p2p1p1()),
    ("3.2.1.2", UpgradeStepNoOp()),
    ("3.3.0", MyNewUpgradeStep()),
    ("3.3.0.1", None
]
```

You are now ready to code the perform function to do the upgrade, please use tests. The file system is isolated from the code using file_access and logging should use logger. 

## Creating a Production upgrade script

To create a production config simply edit the `UPGRADE_STEPS` list in `upgrade.py`. Replace the None with `UpgradeStepNoOp()` and add a new tuple `("X.X.x", None)` to the list, don't forget the comma. E.g. from:

```
UPGRADE_STEPS = [
    ("3.2.1", UpgradeStepFrom3p2p1()),
    ("3.2.1.1", UpgradeStepFrom3p2p1p1()),
    ("3.2.1.2", None)
]
```

to 

```
UPGRADE_STEPS = [
    ("3.2.1", UpgradeStepFrom3p2p1()),
    ("3.2.1.1", UpgradeStepFrom3p2p1p1()),
    ("3.2.1.2", UpgradeStepNoOp()),
    ("3.3.0", None)
]
```

or

```
UPGRADE_STEPS = [
    ("3.2.1", UpgradeStepFrom3p2p1()),
    ("3.2.1.1", UpgradeStepNoOp()),
    ("3.3.0", None)
]
```

to

```
UPGRADE_STEPS = [
    ("3.2.1", UpgradeStepFrom3p2p1()),
    ("3.2.1.1", UpgradeStepNoOp()),
    ("3.3.0", UpgradeStepNoOp()),
    ("3.4.0", None)
]
```
