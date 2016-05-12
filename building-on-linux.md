# Building on Linux

Notes while I have a go at building the client on windows.

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

Install prerequsits
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

cd build
./build.sh


Did


./install_python_modules.sh

# Genie Python install
GENIE_DIR="$INSTALL_DIR/genie_python/source"
PACKAGE_DIR=`python -c "import site; print site.getsitepackages()[0]"`
sudo cp -r "$GENIE_DIR" "$PACKAGE_DIR/genie_python"

# TODO: Remove once fixed (hacks to make IBEX work on Linux)
cd "$INSTALL_DIR/ibex_gui"
PREFERENCE_SUPPLIER="./base/uk.ac.stfc.isis.ibex.preferences/src/uk/ac/stfc/isis/ibex/preferences/PreferenceSupplier.java"

sed -i -- "/DEFAULT_EPICS_BASE_DIRECTORY/s|\".*\"|\"$INSTALL_DIR/EPICS/base/master/bin/linux-x86_64\"|" $PREFERENCE_SUPPLIER
sed -i -- '/DEFAULT_PYTHON_INTERPRETER_PATH/s|".*"|"/usr/bin/python"|' $PREFERENCE_SUPPLIER
sed -i -- "/DEFAULT_GENIE_PYTHON_DIRECTORY/s|\".*\"|\"$PACKAGE_DIR/genie_python\"|" $PREFERENCE_SUPPLIER
sed -i -- "/DEFAULT_PYEPICS_DIRECTORY/s|\".*\"|\"$PACKAGE_DIR\"|" $PREFERENCE_SUPPLIER

Run product



