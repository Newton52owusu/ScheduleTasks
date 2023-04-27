import schedule
from schedule import every,repeat
import time as tm
from datetime import time, timedelta, datetime


def break_reminder():
    print("Take a break! You have been working for 30minutes")

schedule.every().day.at("10:00").do(break_reminder)

while True:
    schedule.run_pending()
    tm.sleep(1)

"""
@repeat(every(5).seconds, message="Subscribe")
@repeat(every(2).seconds, message="Hey")

def job(message):
    print("Hello the message is:", message)

schedule.every().second.do(job, message="HELLO")

while True:
    schedule.run_pending()
    tm.sleep(1)
"""