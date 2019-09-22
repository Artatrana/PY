#!/usr/bin/python
# This script prevents screen saver get activated by moving mouse periodically.
# EAO-09.2012

import win32api, time
print ("Die screensaver !")
dif=1
exc=False
while True:
        try:
                pos=win32api.GetCursorPos()
                time.sleep(30)
                curPos=win32api.GetCursorPos()
                print ("Hmm.. let's see what we have..")
                if pos == curPos:
                        newPos=(curPos[0],curPos[1]+dif)
                        print ("Let's move to %s from %s" % (newPos,pos))
                        dif*=-1
                        win32api.SetCursorPos(newPos)
                exc=False
        except:
                if not exc:
                        print ("Something bad happened.. But never mind.")
                        exc=True