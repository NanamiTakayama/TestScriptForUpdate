#coding:utf-8

print("App started")
import time
import datetime
import commands

date = str(datetime.datetime.today())

while True:
    print("Generated at" + "2016-12-16 16:41:55.413760")
    systate = str(commands.getoutput("ps aux | grep isaax"))
    sysctl = str(commands.getoutput("systemctl status | grep isaax"))
    print("__ps__")
    print(systate)
    print("__systemctl__")
    print(sysctl)
    print(date)
    time.sleep(30)
