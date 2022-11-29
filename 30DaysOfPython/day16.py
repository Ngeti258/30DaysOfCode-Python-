from datetime import datetime
now=datetime.now()
print(now)

time_one=now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)


current_date_string='5 December,2019'
current_date_object=datetime.strptime(current_date_string,"%d %B,%Y")
print("Current_date_object: ",current_date_object)

from datetime import date
new_year= date(year=2023,month=1,day=1)
today= date(year=2022,month=11,day=23)
time_left_for_new_year=new_year-today
print("Time left for new year: ",time_left_for_new_year)

past_year=date(year=1970,month=1,day=1)
date_today=date(year=2022,month=11,day=23)
day_difference=date_today-past_year
print('day_difference: ',day_difference)

