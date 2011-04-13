Pixance
=======

Pixance allows you to measure how many pixels has your mouse covered in a given time.
It makes use of ThingSpeak, so you can put a dynamic chart wherever you want and show people how active/busy you are.

Libraries
---------

This script makes use of the following external libraries:

- pyHook_: intercepts mouse move events
- pyQt_: handles GUI and timing

.. _pyHook: http://pyhook.sourceforge.net/
.. _pyQT: http://www.riverbankcomputing.co.uk/software/pyqt/download

Pre-requisites
--------------

You must have an account at ThingSpeak_, create a channel and provide the *API Key* to the script at start.

.. _ThingSpeak: http://www.thingspeak.com

Usage
-----

Once you have installed the required libraries just launch the script, provide the ThingSpeak *API Key* and press *Start*.

Demo
----

You can watch my script in action updating (if I'm at the PC) my ThingSpeak channel_.

.. _channel: https://www.thingspeak.com/channels/67/charts/1?timescale=5&dynamic=true