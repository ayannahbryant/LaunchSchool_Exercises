from datetime import date

today = date.today() #Today's date is stored in the variable today

today_year = today.year #The .year of todat stores #the current year in the variable today_year
iso_year = today.isocalendar()[0] #The .isocalendar() method returns a tuple with the ISO year, week number, and weekday
#ISOcalendar is a calendar system that is used in many parts of the world, especially in business and industry.
#The [0] index accesses the first element of the tuple, which is the ISO year

print(f'This is the year {today_year} and this is the ISO year {iso_year}.')
