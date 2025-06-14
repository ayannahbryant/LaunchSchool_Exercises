from datetime import datetime as dt #The from statement imports the datetime module's datetime identifier into the program 
now = dt.now() 
print(now)

date = dt.strptime('May 26, 2025', '%B %d, %Y')
weekday_name = date.strftime('%A')
print(weekday_name) 




