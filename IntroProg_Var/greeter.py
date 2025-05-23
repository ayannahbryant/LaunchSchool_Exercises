
first_name = 'Victor'

#The solution using concatenation
print('Good Morning, ' + first_name + '.') #Good Morning, Victor!
print('Good Afternoon, ' + first_name + '.') #Good Morning, Victor!
print('Good Evening, ' + first_name+ '.') #Good Morning, Victor! 

#The solution using f-strings interpolation 
name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')