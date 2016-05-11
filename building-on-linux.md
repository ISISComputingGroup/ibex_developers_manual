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


