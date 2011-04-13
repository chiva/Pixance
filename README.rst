Pixance
=======

Pixance is a python script that allows you to measure how many pixels has your mouse covered in a given time.
It makes use of ThingSpeak, so you can put a dynamic chart wherever you want and show people how active/busy you are.

Requisites
----------

This script makes use of the following:

- `Python 2.7`_: executes the script
- pyHook_: intercepts mouse move events
- pyQt_: handles GUI and timing
- ThingSpeak_: you must have an account, create a channel and generate a *Write API Key*

.. _`Python 2.7`: http://ww.python.org
.. _pyHook: http://pyhook.sourceforge.net/
.. _pyQT: http://www.riverbankcomputing.co.uk/software/pyqt/download
.. _ThingSpeak: http://www.thingspeak.com

Usage
-----

Once you have installed the required libraries just launch the script, provide the ThingSpeak *Write API Key* and press *Start*.
As simple as that!

|window|

.. |WINDOW| image:: https://5603266437227755332-a-kungfulabs-com-s-sites.googlegroups.com/a/kungfulabs.com/wiki/pixance.png

Demo
----

You can watch my script in action updating (if I'm at the PC) my ThingSpeak channel_.

.. _channel: https://www.thingspeak.com/channels/67/charts/1?timescale=5&dynamic=true