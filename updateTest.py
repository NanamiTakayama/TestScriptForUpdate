#coding:utf-8

print("App started")
import time
import datetime
import commands
from slacker import Slacker

date = str(datetime.datetime.today())

while True:
    print("Generated at" + "2016-12-13 16:03:31.622823")
    #systate = str(commands.getoutput("ps aux | grep isaax"))
    #netstate = str(commands.getoutput("ping 8.8.8.8"))
    #print(netstate)
    #print(systate)
    print(date)
    time.sleep(30)
