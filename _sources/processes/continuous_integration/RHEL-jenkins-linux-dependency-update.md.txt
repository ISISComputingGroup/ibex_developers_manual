# Updating the RHEL Jenkins Node

## Update Java
 
* download latest jdk17 for linux and copy to a tree in /opt/jdk17
* edit `build.sh` in client gui build area to set correct `JAVA_HOME` path

## Update Python

* download python source
* on RHEL7 there is an issue with openssl versions. Open ssl 1.1 can be installed from yum, but will not be in the right directory for python. Make sure you install the openssl11-dev and openssl11-static packages as we will link statically to it
* create a `/usr/local/openssl11` with an include directory linked to /usr/include/openssl11 and a lib64 directory linked to /usr/lib64/openssl11
* configure with
```
env LDFLAGS="-L/usr/local/openssl11/lib64 -Wl,-Bstatic -lssl -lcrypto -Wl,-Bdynamic" ./configure --prefix=/usr/local/python --with-openssl=/usr/local/openssl11
```
Note that passing `--enable-optimizations` lead to a subsequent build failure
* now type `make` to build
* finally `sudo rm -fr /usr/local/python` and `sudo make insytall`
