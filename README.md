RobotPy Workshop
================

Requirements (Windows)
----------------------

From windows explorer, double click python-3.5.1.msi to install it, requires
admin access.

Next, install pyfrc via pip (requires internet). Open up the command prompt:

    py -3 -m pip install pyfrc

Requirements (OSX)
------------------

Install python-3.5.1-macosx10.6.pkg, requires admin access.

Next, install pyfrc via pip (requires internet).
Open up a terminal and do one of the following:

OSX (admin access):

    sudo pip3 install pyfrc

OSX (no admin access):

    pip3 install --user pyfrc

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

Linux:
    
    python3 robot.py sim

Or on windows:
    
    py -3 robot.py sim

From Eclipse (with pydev installed)
-----------------------------------

Open up robot.py, select "Run As" and "Python Run", and make sure to add the
'sim' argument to your run configuration.


More information
================

RobotPy Documentation is available online at:

    http://robotpy.readthedocs.org/
    http://pyfrc.readthedocs.org/

There are more RobotPy samples online at 

    https://github.com/robotpy/robotpy-wpilib/tree/master/examples/examples
    https://github.com/robotpy/pyfrc/tree/master/samples

Also see the RobotPy mailing list:

    https://groups.google.com/forum/#!forum/robotpy

Author
======

Dustin Spicuzza (dustin@virtualroadside.com)
