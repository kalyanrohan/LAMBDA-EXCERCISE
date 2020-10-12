import datetime
datetime=str(datetime.datetime.now())
extract= lambda y:y.split()
extract2= lambda x:x.split("-")
extract3=(extract2(str(extract(datetime)))
year1=extract3[0]
month1=extract3[1]
day1=extract3[2]
# time=extract3[3]
print(f"year={year1}")
print(f"month={month1}")
print(f"day={day1}")
# print(f"time={time}")


