# Getting started with git and github

* Register with GitHub to create an account
* Download and install [git client for Windows](https://git-scm.com/download/win>) or [GitHub for Windows](https://windows.github.com/) or [Tortoise Git](https://tortoisegit.org/)

(if asked, Choose `Checkout-as-is; commit Unix style line-endings`)

During setup ensure you have selected "**Git from the command line and also 3rd-party software**" (do NOT add the optional Unix tools to your PATH). If `sh` is added to the PATH, Make will try to compile for Linux rather than Windows. This will cause syntax errors when reading the Makefiles (such as parse errors whenever a `(` is found in an echo message).

* Set you username and email address  via the command line:

```
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR EMAIL ADDRESS"
```

(Or from TortoiseGit, select "Setting->Git" and select "global" and enter your details.)

* Set a default commit editor (not needed for TortoiseGit):

```
git config --global core.editor "start notepad++"
```

* Set line-handling and passwords (Windows):
```
git config --global core.autocrlf true
git config --global credential.helper wincred
```        

* Set line-handling and passwords (Linux):
```
git config --global core.autocrlf input
```        

* Check submodules have been pushed before allowing an update of the master index
```
git config --global push.recurseSubmodules check
```

* You may now need to consider ["First time installing and building"](/overview/First-Time-Build)
