def number_range(n): 
    if n < 0:
        print(f'{n} is less than 0') 
    elif n > 0 and n < 51: 
        print(f'{n} is between 0 and 50')
    elif n > 50 and n < 101:
        print(f'{n} is between 51 and 100')
    elif n > 100: 
        print(f'{n} is greater than 100')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)   
number_range(101)
number_range(-1)

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)   
number_range(101)
number_range(-1)

