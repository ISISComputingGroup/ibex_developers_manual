{#updating_instrument_email_template}
# Updating an instrument machine (email templates)

It is important to remember when making any changes to instruments (e.g. installing new IBEX versions, cleaning disk space etc) that they are in (potentially) constant use by the instrument scientists and so they must be properly informed. Below is a template of what to send to scientists, this should be sent from the Experiment Controls email account.

If most instruments are going to be modified then email the `ISIS Instrument Scientists + Others` outlook address, if only a subset of instruments are being modified you can use the `instrument-` contact email address from https://sparrowhawk.nd.rl.ac.uk/footprints/contacts.html#instemail 

{#updating_instrument_new_release_email_template}
## New Release

For a new release of IBEX the following should be sent as soon as possible, at least a week (ideally 2 weeks) before the deployment date:

```
Dear All,

We have recently created version **X.x.x** of IBEX and will be looking to install it to the (summer | winter) group, between **date** and **date** which includes the following instruments:

The list of new features and bug fixes in this release can be found at **links to release notes since last deply to group**.

To perform the release we will have to stop the instrument from taking data for a couple of hours. If there is a specific day you would like us to perform the release, you would rather not have this release for your instrument or you have any other concerns please get in contact with us ASAP. If we do not hear back from you we will assume that you are happy for us to do this any day in the above range.

Please note that this is a separate task to any operating system updates that may be going on, we will co-ordinate between those two tasks as appropriate.

Thanks,
ISIS Experiment Controls
```

{#updating_instrument_hotfix_email_template}
## Hot-fix

In this context a hot fix refers to any modification of an instrument machine that needs to be done at somewhat short notice e.g.:
* Patching a critical bug in some code
* Clearing up disk space

Hot-fixes may cause disruption to experiments (but less than the issue you are trying to fix) and so to minimise this you should do as much of the following as possible:
* Try to organise for maintenance days
* Give as much notice to scientists as you can
* Minimise the number of instruments to modify

The following is a template and will require some modification based on what the issue is you are trying to resolve:

```
Dear All,

Unfortunately we have recently seen an issue on your instruments where **describe issue here**.

To resolve this issue we will need to **detail fix here**. To do this we will require **stopping taking data? use of remote desktop?** for **time it will take to fix**.

If we do not do this then **how will it affect the user's experiments**.

Ideally we would like to do this **on maintenance day? ASAP**. Please let us know when would be a suitable time to make this change.

Apologies for any inconvenience,
ISIS Experiment Controls 
```
