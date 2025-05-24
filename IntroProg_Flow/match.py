value = 6

match value: 
    case 5: 
        print('Value is 5')
    case 6:
        print('Value is 6')
    case _: #default case 
        print('Value is not 5 or 6')

if value == 5: 
    print('Value is 5')
elif value == 6:
    print('Value is 6')
else:
    print('Value is not 5 or 6')

match value: 
    case 1 | 2 | 3 | 4: 
        print('Value is < 5')
    case 5 | 6: 
        print('Value is 5 or 6')
    case _:
       print('Value is not 1 through 6') 
