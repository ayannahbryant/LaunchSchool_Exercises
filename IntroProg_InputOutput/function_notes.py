#Example of custom function
def hello():
    print('Hello')
    return True

hello()         # invoking function; ignore return value
print(hello())  # using return value in a `print` call

#Built-in Functions
for name in dir('__builtins__'):
    print(name)

print(min(-10, 5, 12, 0, -20))      # -20
print(max(-10, 5, 12, 0, -20))      # 12

print(min('over', 'the', 'moon'))   # 'moon'
print(max('over', 'the', 'moon'))   # 'the'

#print(max(-10, '5', '12', '0', -20))
# TypeError: '>' not supported between instances
# of 'str' and 'int'

my_tuple = ('i', 'tawt', 'i', 'taw', 'a',
            'puddy', 'tat')
print(min(my_tuple)) # 'a'
print(max(my_tuple)) # 'tawt'

#ord converts a character to its Unicode code point - standard ASCII
print(ord('a'))               # 97
print(ord('A'))               # 65
print(ord('='))               # 61
print(ord('~'))               # 126

#chr converts a Unicode code point to its character
print(chr(97))                # a
print(chr(65))                # A
print(chr(61))                # =
print(chr(126))               # ~

'''The following values are said to be falsy:
    False, None
    all numeric 0 values (integers, floats, complex)
    empty strings: ''
    empty collections: [], (), {}, set(), frozenset(), and range(0)
    Custom data types can also define additional falsy value(s).

    All other values are truthy.
'''
#any and all functions
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))       # False - Returns False if all values are falsy
print(any(collection2))       # True - Returns True if any value is truthy
print(any(collection3))       # True
print(any([]))                # False - Returns False since none of the elements are truthy

print(all(collection1))       # False - Returns False if all values are falsy
print(all(collection2))       # False - Returns False if any values are truthy
print(all(collection3))       # True - Returns True if all values are truthy
print(all([]))                # True - Returns True since none of the elements are falsy (all of the elements are thus truthy)
print('\n')

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])
# [True False True True False]

numbers = [2, 5, 8, 10, 13]
print(any([number % 2 == 0 for number in numbers])) # True
print(all([number % 2 == 0 for number in numbers])) # False

numbers = [5, 13]
print(any([number % 2 == 0 for number in numbers])) # False
print(all([number % 2 == 0 for number in numbers])) # False

numbers = [2, 8, 10]
print(any([number % 2 == 0 for number in numbers])) # True
print(all([number % 2 == 0 for number in numbers])) # True


# Identity and Interning
# Run only in python REPL
s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

s = 'supercalifragilisticexpialidocious' # This string is long enough to be interned
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))         # True

x = 5 # This integer is small enough to be interned (-5 to 256)
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False

