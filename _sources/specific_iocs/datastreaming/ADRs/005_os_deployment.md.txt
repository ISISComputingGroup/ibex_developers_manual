# 5 - Base OS and deployment strategy for data streaming technology

## Status

Accepted

## Context

For the data streaming project for HRPD-X, we need to be able to host containers and deploy them easily, for prototyping and hotfixing. 

To be able to do this we need to set the host up, as decided in {ref}`dslinuxadr`, with a base operating system and then decide on the deployment method to push containers and system updates out to the machine. 

There are several ways to set up the base machine, including manually, but this is not repeatable. If the machine went down, we wouldn't easily be able to recreate it. 

### Base Operating system options
These are some of the options we could consider for a base operating system for the data streaming machine(s):

#### Debian
Pros: Debian is widely used and a very stable OS. It uses the aptitude package manager, which is user-friendly. Debian is also relatively lightweight. 
Cons: Debian can be slow to update, so we might miss out on nice features that other distributions offer. It also doesn't come "shipped" with as many tools out of the box. 

#### Ubuntu server
Pros: Ubuntu server is very easy to set up and supports lots of hardware. It is one of the most popular server distributions. It is based on Debian (see above as it shares the benefits) but uses different repositories so generally gets updates quicker. 
Cons: It is less lightweight than Debian, but comes with more tooling out of the box. 

#### Fedora CoreOS
Pros: This is a container infrastructure based OS which provides Docker and Kubernetes from the start. It uses its own "ignition" files for an automated install and provides rolling releases. Immutable filesystem.
Cons: Fedora is not as widely used as Debian or CentOS based distributions. Configuration is bespoke to Fedora. It is slightly harder to set up than the others.  

#### Rocky Linux
Pros: This is essentially the free version of CentOS and Red hat so shares the package management mechanisms with those distributions. It is the most widely used server OS in the world.
Cons: It is slightly harder to use than Debian-based distributions. 

Note: we have discounted RHEL and CentOS from this decision due to (ongoing) costs, but if we go with Rocky and decide to switch to the enterprise version we could so very easily. 

### Unattended upgrades
Most of the distributions listed above offer unattended upgrades (ie. rolling updates) however this could be risky mid-cycle if it caused data acquisition to stop - for this reason we won't be using it.

### gitops/continuous deployment

We may consider using a Github repository to describe the machine. This needs to be foolproof and pin version numbers rather than using the latest image of a container image as that could differ if a machine needed to be recreated.

### Maintenance and deployment for base OS

There are a few ways to automate steps on the base OS, for example using [Ansible](https://docs.ansible.com/). We have some experience with it already as it's been used for other things in IBEX including part of the main deployment. 

Alternatives include `Puppet`, `Chef` and `Saltstack`.

### Container infrastructure

#### Kubernetes (k8s) or similar distributions ie. `k3s`, `microk8s`
- Has a steep learning curve - may not be best for our team to learn as we don't use it currently
- works well for horizontal scaling and HA
- well used in community
- tools available ie. helm and Argo CD for CI/CD

#### Docker compose - manual `pull` and `up`
- Easy to do, but manual and therefore not suitable for a multi-node system

#### `portainer`
See https://docs.portainer.io/start/install-ce
- More automated than docker compose manual step, but still manual when creating stacks/environments to add new machines
- container monitoring useful. 
- lose some benefits of this if not using CI/CD and/or gitops 

#### `komodo`
See https://komo.do/
- As above but open source

#### Ansible with docker
see [this module](https://docs.ansible.com/projects/ansible/latest/collections/community/docker/docker_compose_v2_module.html)
- Automated, declarative
- we will possibly use Ansible for base os maintenance and provisioning, could use this for containers

#### Ansible with docker-compose
See [this module](https://docs.ansible.com/projects/ansible/latest/collections/community/docker/docker_container_module.html#ansible-collections-community-docker-docker-container-module)
- As above but with a compose file instead of inline

## Decision

We will use the latest version of Rocky Linux for the base operating system, and update/re-provision when new versions come out. This is because it's widely used on site - SCD and Accelerator Controls both use it. We use it for our main Jenkins node and so on. Ansible collections/roles available all seem to support RHEL-based distributions as well as Debian. 

We will use Ansible for both the base OS configuration, as well as container deployment. A playbook will serve as a single source of truth for a machine in a Github repository, and this will be idempotent so can be run multiple times on an existing machine. No manual steps besides installing the operating system should be performed, this is so they aren't lost when the machine is re-provisioned. 

These decisions are initial and can be changed later - if the base OS changes for example, it doesn't matter too much as its main role is to host containers.

## Consequences

- We need to manually run playbooks on machines - there isn't really an alternative to this as we don't have a cluster to be able to roll out updates with no downtime/HA so can't continuously deploy our software. This also depends on being out of cycle and so on.
- if a machine dies or becomes obsolete, it should be very straightforward to replace it as our configuration is stored as code rather than a set of manual steps
- setup is marginally more difficult as it needs to be done in a repeatable way, versus just running commands manually on a machine to install docker etc.  
- we need to keep inline with the latest version of RockyOS, though this is no different to doing the same for any operating system.
- Ansible knowledge is required - though it is now part of the main IBEX deployment anyway. 
