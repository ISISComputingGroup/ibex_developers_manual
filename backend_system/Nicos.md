> [Wiki](Home) > [The Backend System](The-Backend-System) > Nicos

NICOS is a Python based control system developed at FRM-II. The general software documentation can be found [here](http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-master/dirhtml/). Although NICOS is a fully fledged control system ISIS are currently only using it as a script server.

# [Getting Started](Installing-Nicos-on-Windows)

How to install Nicos on Windows.

# [Running Nicos](Running-Nicos)

How to run Nicos.

# [Instrument Configuration](Configuring-a-New-Nicos-Instrument)

How to set up and configure a new Nicos instrument.

# [Initial evaluation](Nicos-evaluation)

An evaluation of Nicos and its suitability for integration into the IBEX project.

# [Script server design](Script-server-design)

The design of the Nicos script server.

# Developer notes
- [Testing Nicos](testing-nicos)
- [Nicos commands](NICOS-commands)


# Repository

- Git repo is at `git://trac.frm2.tum.de/home/repos/git/frm2/nicos/nicos-core.git`
- [Documentation](http://cdn.frm2.tum.de/fileadmin/stuff/services/ITServices/nicos-2.0/dirhtml/)

Don't try to merge their repository with ours - they have mangled email addresses in their history which github won't accept. Instead, copy-paste the entire codebase into the `vendor` branch of our repository, and then merge the vendor branch with our master branch.