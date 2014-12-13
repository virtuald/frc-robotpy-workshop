Simple pyfrc demo
=================

Requirements (Windows)
----------------------

From windows explorer, double click python-3.4.2.msi to install it, requires
admin access.

Next, install pyfrc via pip. Open up the command prompt:

    c:\Python34\Scripts\pip install --no-deps pyfrc\pyfrc-2014.7.5.tar.gz

Or on the internet:

    c:\Python34\Scripts\pip install pyfrc

Requirements (OSX)
------------------

Install python-3.4.2-macosx10.6.pkg, requires admin access.

Next, install pyfrc via pip. Open up a terminal and do one of the following:

OSX (admin access):

    sudo pip3 install --no-deps pyfrc/pyfrc-2014.7.5.tar.gz

Or on the internet:

    sudo pip3 install pyfrc

OSX (no admin access):

    pip3 install --user --no-deps pyfrc/pyfrc-2014.7.5.tar.gz

Or on the internet:

    pip3 install --user pyfrc

Running the code
================

Command prompt
--------------

Once you have the requirements installed, you can run this from a terminal or
command prompt.

Don't forget to change directory to where robot.py is! 

OSX:
    
    python3 robot.py sim

Windows:
    
    python3 robot.py sim

Or on windows:
    
    C:\Python34\python robot.py sim

From Eclipse (with pydev installed)
-----------------------------------

Open up robot.py, select "Run As" and "Python Run", and make sure to add the
'sim' argument to your run configuration.


More information
================

There are more pyfrc samples online at 

    https://github.com/robotpy/pyfrc/tree/master/samples

Check out http://pyfrc.readthedocs.org/ for more information!

Also see the RobotPy mailing list:

    https://groups.google.com/forum/#!forum/robotpy

Author
======

Dustin Spicuzza (dustin@virtualroadside.com)
