# Technical Skills

This tutorial assumes a basic level of familiarity with Powershell. You will need to copy commands from this tutorial (perhaps with small edits) and run them in Powershell.

It is also assumed that you know what a plain text file (*.txt) is and are able to  provide your input training text in a plain text format.

# Software

## Operating System

This tutorial was written and tested on Windows 11. (It should work on Windows 10, too.)  Everything is written with the assumption that you're using Windows.

The Python scripts should run on Linux as well, but you will have to modify some command line syntax if you want to follow the tutorial.

## Software to install
To follow this tutorial, you will need to already have installed the following software:
* [Presage](https://presage.sourceforge.io/download/)
* [Git](https://git-scm.com/downloads/win)
* [Python 3](https://www.python.org/downloads/)

When installing Git and Python, keep an eye out the options "Add Git to PATH" and "Add  Python to PATH". (These might be phrased slightly differently.) You want to make sure both of these are selected in the respective installers. These settings can be changed after install, but it is easier if you don't have to.

## Check your installations

After installation, verify that the Presage icon appears in the system tray. It should say "Presage WCF Service" if you mouse-over the icon.

Verify that you can run both Git and Python from PowerShell. To check, open Powershell and try running:
```
git --version
```
which should output something like `git version #.#.#.windows.#`.

To check that you can run Python:
```
python --version
```
and the output should be something like `Python #.#.#`.

If your install was successful but you get a message like the one below, then you probably need to edit your `PATH` environment variable.
```
The term 'python' is not recognized as the name of a cmdlet, function, script file, or 
operable program. Check the spelling of the name, or if a path was included, verify that the path 
is correct and try again
```

# Clone the repository

In Powershell, navigate to a location on your file system where you want to keep your work.  

```
cd C:\path\to\project\directory
```

Then, clone this repository. This will create a local copy of this tutorial along with all the scripts and sample data.

```
git clone https://github.com/annakirkpatrick/presage-ngram-tutorial.git
```