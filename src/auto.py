import datetime
import time
import schedule

from valuation import buy_judge

dt_now = datetime.datetime.now()

def job():
    buy_judge("1925")
print("ok")

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep
