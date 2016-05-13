# Building on Linux

## Creating a linux box on your desktop

1. Install virtual box
1. Install vagrant (https://www.vagrantup.com/downloads.html)
1. Clone repo (https://github.com/ISISComputingGroup/ibex_utils.git)
1. cd .../ibexutils/linux_env
1. vagrant up

Should start a fresh vagrant machine (will take a while but is quicker second time round). With a gui you can log into.

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

Install prerequsits (this for the backend and front end so not all of these are needed for the client)
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
        swig
```

clone epics repo

    git clone https://github.com/ISISComputingGroup/ibex_gui.git

alter perfernce supplier to be linux aware (there is an extra path in here to which needs to be updates for epics utils)
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


