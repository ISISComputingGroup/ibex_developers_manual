> [Wiki](Home) > [Project tools](Project-tools) > Building on linux

# Building on Linux

## Creating a linux box on your desktop

1. Install virtual box
1. Install vagrant (https://www.vagrantup.com/downloads.html)
1. Clone repo (https://github.com/ISISComputingGroup/ibex_utils.git)
1. cd .../ibexutils/linux_env
1. vagrant up (this may not work from the Windows command line, but it should work from the Git Bash)

Should start a fresh vagrant machine (will take a while but is quicker second time round). With a gui you can log into. Login details are: `vagrant` (for username) and `vagrant` (for password).

If you get the following error:
```
VT-x is disabled in the BIOS for all CPU modes (VERR_VMX_MSR_ALL_VMX_DISABLED).

Result Code: 
E_FAIL (0x80004005)
Component: 
ConsoleWrap
Interface: 
IConsole {872da645-4a9b-1727-bee2-5585105b9eed}
```
you should try entering your BIOS (power off your machine; restart and immediately press the `F2` key) and verify that virtualisation options are enabled. See also [this related post] (https://forums.virtualbox.org/viewtopic.php?f=6&t=77139).

If you get the following error:
```
==> default: Errors were encountered while processing:
==> default:  dictionaries-common
==> default:  aspell
==> default:  aspell-en
==> default:  hunspell-en-us
==> default:  libenchant1c2a:amd64
==> default:  libwebkitgtk-3.0-0:amd64
==> default:  empathy
==> default:  mcp-account-manager-uoa
==> default:  account-plugin-aim
==> default:  account-plugin-jabber
==> default:  account-plugin-salut
==> default:  account-plugin-yahoo
==> default:  gir1.2-webkit-3.0
==> default:  apturl
==> default:  enchant
==> default:  gedit
==> default:  librhythmbox-core8
==> default:  gir1.2-rb-3.0
==> default:  libyelp0
==> default:  yelp
==> default:  gnome-user-guide
==> default:  zenity
==> default:  nautilus-sendto-empathy
==> default:  nautilus-share
==> default:  rhythmbox
==> default:  rhythmbox-mozilla
==> default:  rhythmbox-plugin-cdrecorder
==> default:  rhythmbox-plugin-magnatune
==> default:  rhythmbox-plugin-zeitgeist
==> default:  rhythmbox-plugins
==> default:  software-center
==> default:  ubuntu-release-upgrader-gtk
==> default:  unity-control-center
==> default:  ubuntu-desktop
==> default:  ubuntu-docs
==> default:  unity-control-center-signon
==> default:  webaccounts-extension-common
==> default:  xul-ext-webaccounts
==> default:  shotwell
==> default:  update-notifier
==> default:  update-manager
==> default:  indicator-bluetooth
==> default: E: Sub-process /usr/bin/dpkg returned an error code (1)
The SSH command responded with a non-zero exit status. Vagrant
assumes that this means the command failed. The output for this command
should be in the log above. Please read the output to determine what
went wrong.
```
it may be that some packages failed to install within the virtual machine, but you still should be able to operate without them. In the same console where you started vagrant, type:

1. `vagrant halt`
1. `vagrant up`

and the VM should start normally.


## Installing the client

I have not done this from scratch you will need to experiment the following is what I did before I ran out of time on the ticket. Ideally I think the plan is to place the compiled version of the client and an install script into the linex_env directory then on the ubuntu machine this appears in `/vagrant` (not home directory). You should be run install.sh and it should install and possibly start the client. To do this you will need at least java installed but I am unsure what else. see the instructions below of how I built and started my client.

# Initial notes of creating a client
## Create virtual machine

I am currently on a windows machine so it is useful to have a virtual machine on which to install. Using Michaels vagrant script seems like a good choice. So:

1. Install virtual box
2. Install vagrant (https://www.vagrantup.com/downloads.html)
3. Clone repo (https://github.com/DMSC-Instrument-Data/ecp-dev-envs)
4. cd directory
5. change virtual machine to use 

      config.vm.box = "ubuntu/trusty64"
      config.vm.box_url = "ubuntu/trusty64" #"../../vagrant_ubuntu_minimal/package.box"

6. cd `.../ecp-dev-envs\nicos-dev-env`
7. `vagrant up`
8. `vagrant ssh` from a git bash terminal

## Building it

Install prerequisites (this for the backend and front end so not all of these are needed for the client)
```
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        conserver-client \
        conserver-server \
        default-jdk \
        doxygen \
        git \
        ipython \
        libcurl4-openssl-dev \
        libjpeg8-dev \
        libnet1-dev \
        libpcap-dev \
        libreadline-dev \
        libxml2-dev \
        libxslt1-dev \
        maven \
        mysql-server-5.6 \
        perl \
        php5 \
        php5-dev \
        procServ \
        python \
        python-dev \
        python-matplotlib \
        python-pip \
        python-tk \
        re2c \
        swig \
        python-docutils \
        rst2pdf
```

clone epics repo

    git clone https://github.com/ISISComputingGroup/ibex_gui.git

alter preference supplier to be linux aware (there is an extra path in here to which needs to be updates for epics utils)
```
cd "$INSTALL_DIR/ibex_gui"
PREFERENCE_SUPPLIER="./base/uk.ac.stfc.isis.ibex.preferences/src/uk/ac/stfc/isis/ibex/preferences/PreferenceSupplier.java"
 
    sed -i -- "/DEFAULT_EPICS_BASE_DIRECTORY/s|\".*\"|\"$INSTALL_DIR/EPICS/base/master/bin/linux-x86_64\"|"  $PREFERENCE_SUPPLIER
    sed -i -- '/DEFAULT_PYTHON_INTERPRETER_PATH/s|".*"|"/usr/bin/python"|' $PREFERENCE_SUPPLIER
    sed -i -- "/DEFAULT_GENIE_PYTHON_DIRECTORY/s|\".*\"|\"$PACKAGE_DIR/genie_python\"|" $PREFERENCE_SUPPLIER
    sed -i -- "/DEFAULT_PYEPICS_DIRECTORY/s|\".*\"|\"$PACKAGE_DIR\"|" $PREFERENCE_SUPPLIER
```

Build the client (this must be done in a gui environment for all the tests to pass)
```
cd build
./build.sh
```

Install python modules:

    ./install_python_modules.sh (not all of these install but this seemed not to be a problem install those that work)

Add genie python to default python build:
```
GENIE_DIR="$INSTALL_DIR/genie_python/source"
PACKAGE_DIR=`python -c "import site; print site.getsitepackages()[0]"`
sudo cp -r "$GENIE_DIR" "$PACKAGE_DIR/genie_python"
```

Run product:

`ibex_gui\base\uk.ac.stfc.isis.ibex.client.product\target\products\ibex.product\linux\gtk\x86_64\ibex-client`


