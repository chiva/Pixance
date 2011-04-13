# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature,  QTimer,  SIGNAL

from Ui_mainwindow import Ui_MainWindow
import httplib,  urllib
import pythoncom, pyHook
from math import sqrt

distance = 0
oldPos = -1

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_btStart_released(self):
        """
        Slot documentation goes here.
        """
        #get ThingSpeak configuration
        self.btStart.setEnabled(False)
        self.apiKey = str(self.leApiKey.text())

        # start hooking mouse movements
        hm = pyHook.HookManager()
        hm.MouseMove = OnMouseEvent
        hm.HookMouse()

        # start timer
        self.timer = QTimer(self)
        self.connect(self.timer,
                    SIGNAL("timeout()"),
                     self.updateTS)
        self.timer.start(20000)

    def updateTS(self):
        global distance
        # update ThingSpeak channel
        # http://www.australianrobotics.com.au/?q=node/292
        params = urllib.urlencode({'field1': round(distance), 'key': self.apiKey})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print "Updating distance:", distance
        print "Answer:",  response.status, response.reason
        data = response.read()
        conn.close()
    
        # reset counter
        distance = 0

def OnMouseEvent(event):
    global distance,  oldPos
    newPos = event.Position
    # called when mouse events are received
    #print(newPos)
    if oldPos != -1:
        x = oldPos[0] - newPos[0]
        y = oldPos[1] - newPos[1]
        distance += sqrt(x**2 + y**2)
    oldPos = newPos
    # return True to pass the event to other handlers
    return True
