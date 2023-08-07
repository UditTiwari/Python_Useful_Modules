import datetime


mytime = datetime.time(2,20)
print(mytime)

today = datetime.date.today().strftime(
            "%Y_%m_%d"
        )
print(today)