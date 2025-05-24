print(False or (True and False)) # False because (True and False) is False
print(True or (1 + 2)) # True
print((1 + 2) or True) # 3
print(True and (1 + 2)) # 3
print(False and (1 + 2)) # False
print((1 + 2) and True) # True
print((32 * 4) >= 129) # False
print(False != (not True)) # False
print(True == 4) # False
print(False == (847 != 847)) # True


def even_or_odd(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd' 
    
print(even_or_odd(4)) # even
print(even_or_odd(5)) # odd

def even_or_odd2(r): 
    print('even' if r % 2 == 0 else 'odd') 

n = 1905

match (n % 2):
    case 0:
        print('even')
    case 1:
        print('odd')
    case _:
        print('not a number')

#def baz(): 
#    if foo(): 
#        return 'bar'
#    else: 
#        return qux()

