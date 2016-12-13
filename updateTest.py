import time
import datetime
import commands
from slacker import Slacker

date = str(datetime.datetime.today())

while True:
    systate = str(commands.getoutput("ps aux | grep isaax"))
    netstate = str(commands.getoutput("ping 8.8.8.8"))
    print(netstate)
    print(systate)
    print("Generated at" + "2016-12-13 15:42:25.351754")
    print(date)
    time.sleep(30)
