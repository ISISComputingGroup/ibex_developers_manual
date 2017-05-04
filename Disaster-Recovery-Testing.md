> [Wiki](Home) > [Deployment](Deployment) > [Disaster Recovery Testing](Disaster-Recovery-Testing)

We currently don't do disaster recovery testing on deploy or as part of manual system testing; maybe we should.  Here is a list of things that we should consider testing:

1. Restart PC does IBEX/SECI recover
    1. Do IOCs recover i.e. are they restarted if they need to be
    1. Do motor positions recover (should they)
1. Restart the moxa
    1. Check IOCs reconnect
1. Disconnect and reconnect the network
    1. Check IOCs reconnect
