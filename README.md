﻿TWBlue -
======

[![Build status](https://ci.appveyor.com/api/projects/status/fml5fu7h1fj8vf6l?svg=true)](https://ci.appveyor.com/project/manuelcortez/twblue)

TW Blue is an app designed to use Twitter simply and efficiently while using minimal system resources.  
With this app you’ll have access to twitter features such as:

* Create, reply to, like, retweet and delete tweets,
* Send and delete direct messages,
* See your friends and followers,
* Follow, unfollow, block and report users as spam,
* Open a user’s timeline, which will allow you to get that user’s tweets separately,
* Open URLs when attached to a tweet or direct message,
* Play audio tweets
* and more!

See [TWBlue's webpage](http://twblue.es) for more details.

## Running TWBlue from source

This document describes how to run tw blue from source and how to build a binary version which doesn't need Python and the other dependencies to run.

### Required dependencies.

Although most dependencies can be found in the windows-dependencies directory, we provide links to their official websites. If you are cloning with git, don't forget to initialize and update the submodules to get the windows-dependencies folder. You can use these two commands to perform this task from git bash:  
```
    git submodule init  
    git submodule update
```

#### Dependencies packaged in windows installers

* [Python,](https://python.org) version 3.7.9  
If you want to build both x86 and x64 binaries, you can install python x86 to C:\python38 and python x64 to C:\python38x64, for example.

#### Dependencies that must be installed using pip

Python installs a tool called Pip that allows to install packages in a simple way. You can find it in the python scripts directory. To install packages using Pip, you have to navigate to the scripts directory using a command prompt, for example:

    `cd C:\python37x64\scripts`

	You can also add the scripts folder to your path environment variable or choose the corresponding option when installing Python.  
	Note: pip and setuptools are included in the Python installer since version 2.7.9.

Pip is able to install packages listed in a special text file, called the requirements file. To install all remaining dependencies, perform the following command:

    `pip install -r requirements.txt`

Note that if you perform the command from the path where Pip is located, you need to specify the path to your Tw Blue root folder where the requirements file is located, for example:

    `pip install -r D:\repos\TwBlue\requirements.txt`

Pip will automatically get the additional libraries that the listed packages need to work properly.  
If you need to update your dependencies, perform the following command:

    `pip install --upgrade -r requirements.txt`

#### Other dependencies

These dependencies are located in the windows-dependencies directory. You don't need to install or modify them.

* Bootstrap 1.2.1: included in dependencies directory.  
This dependency has been built using pure basic 4.61. Its source can be found at http://hg.q-continuum.net/updater
* [oggenc2.exe,](http://www.rarewares.org/ogg-oggenc.php) version 2.87  
* Microsoft Visual c++ 2019 redistributable dlls.
* VLC plugins and DLL libraries.

#### Dependencies required to build the installer

* [NSIS,](http://nsis.sourceforge.net/) version 3.04

#### Dependencies required to build the portableApps.com format archive

* [NSIS Portable,](http://portableapps.com/apps/development/nsis_portable) version 3.03
* [PortableApps.com Launcher,](http://portableapps.com/apps/development/portableapps.com_launcher) version 2.2.1
* [PortableApps.com Installer,](http://portableapps.com/apps/development/portableapps.com_installer) version 3.5.11

Important! Install these 3 apps into the same folder, otherwise you won't be able to build the pa.c version. For example: D:\portableApps\NSISPortable, D:\PortableApps\PortableApps.com installer, ...

#### Dependencies to make the spell checker multilingual ####

In order to add the support for spell checking in more languages than english you need to add some additional dictionaries to pyenchant. These are located on the dictionaries folder under windows-dependencies. Simply copy them to the share/enchant/myspell folder located in your enchant installation. They will be automatically copied when building a binary version.

### Running TW Blue from source

Now that you have installed all these packages, you can run TW Blue from source using a command prompt. Navigate to the repo's `src` directory, and type the following command:

    `python main.py`

	If necessary, change the first part of the command to reflect the location of your python executable. You can run TW Blue using python x86 and x64.

### Generating the documentation

To generate the documentation in html format, navigate to the doc folder inside this repo. After that, run these commands:  

    `python document_importer.py`  
    `python generator.py`  

The documentation will be generated, placing each language in a separate folder in the doc directory. Move these folders (for example `de`, `en`, `es`, `fr`, `it`, ...) to `src/documentation`, creating the directory if necessary.  
Also, copy the `license.txt` file located in the root of the repo to the documentation folder.

### Building a binary version

A binary version doesn't need python and the other dependencies to run, it's the same version that you will find on the TW Blue website if you download the zip files or the snapshot versions.

To build it, run the following command from the src folder:

    `python setup.py build`

	You will find the binaries in the dist directory.

### Building an installer

If you want to install TWBlue on your computer, you must create the installer first. Follow these steps:

* Navigate to the src directory, and create a binary version for x86: C:\python37\python setup.py build
* Move the dist directory to the scripts folder in this repo, and rename it to twblue
* Repeat these steps with Python for x64: C:\python37x64\python setup.py build
* Move the new dist directory to the scripts folder, and rename it to twblue64
* Go to the scripts folder, right click on the twblue.nsi file, and choose compyle unicode NSIS script
* This may take a while. After the process, you will find the installer in the scripts folder

### How to generate a translation template

Run the gen_pot.bat file, located in the tools directory. Your python installation must be in your path environment variable. The pot file will appear in the tools directory.

### How to build the portableApps.com archive

If you want to have TWBlue on your PortableApps.com platform, follow these steps:

* Navigate to the src directory, and create a binary version for x86: C:\python37\python setup.py build
* Move the dist directory to the misc\pa.c format\app folder in this repo, and rename it to twblue
* Repeat these steps with Python for x64: C:\python37x64\python setup.py build
* Move the new dist directory to the misc\pa.c format\app folder, and rename it to twblue64
* Run the PortableApps.com Launcher Generator, and follow the wizard. Choose the pa.c format folder and continue to generate the launcher. If the wizard is completed, you will see a file named TWBlue portable.exe inside the pa.c format folder.
* Run the PortableApps.com Installer, and follow the wizard. As in the above step, choose the pa.c format folder. When it completes, you will see a file named TWBluePortable_x.y.paf.exe inside the misc folder, where x.y is the version number.

