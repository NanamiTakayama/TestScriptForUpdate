#coding:utf-8

print("App started")
import time
import datetime
import commands
from slacker import Slacker

date = str(datetime.datetime.today())

while True:
    print("Generated at" + "2016-12-13 16:18:00.381864")
    systate = str(commands.getoutput("ps aux | grep isaax"))
    print(systate)
    print(date)
    time.sleep(30)
