print(42 == 42) #True
print(42 == 43) #False
print(42 == '42') #False (different types
print('foo' == 'foo') #True (works with strings)
print('FOO' == 'foo') #False (Case sensitive - it matters)
print('\n')

print(42 != 42) #False (different types)
print(42 != '42') #True (different types
print(42 != 43) #True
print('foo' != 'foo') #False (works with strings)
print('FOO' != 'foo') #True (Case sensitive - it matters)
print('\n')

# Ordered comparisons
print('Ordered Comparisons')
print(42 < 41) #False
print(42 < 42) #False
print(42 <= 42) #True
print(42 < 43) #True
print('\n')

#Compare lexicographically
print('Compare lexicographically')
print('abcdf' < 'abcef') #True 'd' < 'e' and doesnt evaluate 'f'
print('abc' < 'abcdef') #True (because first string is shorter than the longer string)
print('abcdef' < 'abc') #False (because the first string continues with 'd' and the second string is shorter)
print('abc' < 'abc') #False (because they are equal)
print('abc' <= 'abc') #True (because they are equal)
print('abd' < 'abcdef') #False (because 'd' is greater than 'e')
print('A' < 'a') #True (because uppercase letters are less than lowercase letters)
print('Z' < 'a') #True (because upper case letters are less than lower case letters)
print('\n')

print('3' < '24') #False (only the first character is compared and '3' is greater than '2')
print('24' < '3') #True (only the first character is compared and '2' is less than '3')

#Sets 
print('Sets')
print({3, 1, 2} < {2, 4, 3, 1})         # True (because {3, 1, 2} is shorter of {2, 4, 3, 1})
print({3, 1, 2} > {2, 4, 3, 1})         # False (because {3, 1, 2} is shorter of {2, 4, 3, 1})
print({2, 4, 3, 1} > {3, 1, 2})         # True (because {2, 4, 3, 1} is longer of {3, 1, 2})
print('\n')

#Lists (tuples work identically)
print('Lists (tuples work identically)')
print([1, 2, 3] < [1, 2, 3, 4])         # True (because [1, 2, 3] is shorter of [1, 2, 3, 4])
print([1, 4, 3] < [1, 3, 3])            # False (because [1, 4, 3] has a greater value than [1, 3, 3])
print([1, 3, 3] < [1, 4, 3])            # True  (because [1, 3, 3] has a lesser value than [1, 4, 3])
print('\n')

#Concatenation
print('Concatenation')
print('foo' + 'bar') #foobar
print('1' + '2') #12
print('abc' * 3) #abcabcabc
print(3 * 'abc') #abcabcabc
print('\n')

#Coercion (converting one type to another)
print('Coercion')
print('\n')
#Strings to numbers
print('Strings to numbers')
print(int('5')) #5
print(float('3.141592')) #3.141592
print('\n')

#Numbers to strings
print('Numbers to strings')
print(str(5)) #'5'
print(str(3.141592)) #'3.141592'    
print('\n')

# (Unnecessary) Explicit coercion
print('Explicit coercion')
print(str(3))           # 3
print(str(False))       # False
print(str([1, 2, 3]))   # [1, 2, 3]
print(str({4, 5, 6}))   # {4, 5, 6}
print('\n')

# Implicit coercion
print('Implicit coercion')
print(3)                # 3
print(False)            # False
print([1, 2, 3])        # [1, 2, 3]
print({4, 5, 6})        # {4, 5, 6}
print('\n')

print(True + True + True)     # 3 (True is 1)
print(True + 1 + 1.0)         # 3.0 (True is 1)
print(False * 5000)           # 0 (False is 0)
print('\n')

#Determining the type 
print('Determining the type')
print(type(1))         # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type('abc'))     # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type(None))      # <class 'NoneType'>
print('\n')

foo = 42               # Variables work, too
print(type(foo))       # <class 'int'>
print('\n')

print(type('abc').__name__)   # str
print(type(False).__name__)   # bool
print(type([]).__name__)      # list
print('\n')

print(type('abc') is str)     # True
print(type('abc') is int)     # False
print(type(False) is bool)    # True
print(type([]) is list)       # True
print(type([]) is set)        # False
print('\n')

print(isinstance('abc', str))    # True
print(isinstance([], set))       # False

class A:
    pass

class B(A):
    pass

b = B()

print(type(b).__name__) # B
print(type(b) is B)     # True
print(type(b) is A)     # False (b's type is
                        # not A)
print(isinstance(b, B)) # True
print(isinstance(b, A)) # True (b is instance of A and B)
print('\n')

#String Representation
print('String Representation')
my_str = 'abc'
print(my_str)       # abc
print(str(my_str))  # abc (same as print(my_str)) - implicitly calls str() when it needs to print or interpolate a value
print(repr(my_str)) # 'abc' (note the quotes) - returns a string that can be used to create a new instance of the object 
print('\n')

#Collection and String Lengths 
print('Collection and String Lengths')
print(len('Launch School'))       # 13 (string)
print(len(range(5, 15)))          # 10 (range)
print(len(range(5, 15, 3)))       # 4 (range) - Increment by 3 (5+3=8, 8+3=11, 11+3=14)
print(len(['a', 'b', 'c']))       # 3 (list)
print(len(('d', 'e', 'f', 'g')))  # 4 (tuple)
print(len({'foo': 42, 'bar': 7})) # 2 (dict)
print(len({'foo', 'bar', 'qux'})) # 3 (set)
print('\n')

#Indexing and Key Access 
print('Indexing and Key Access')
#Indices begin at 0 and run through 1 less than the length of the collection
#Indices can be negative, which means they count from the end of the collection (range from -1 to -len(seq))
my_str = "abc"                # string
print(my_str[0])              # 'a'
print(my_str[1])              # 'b'
print(my_str[2])              # 'c'
# print(my_str[3])
# IndexError: string index out of range
print('\n')

my_range = range(5, 8)         # range
print(my_range[0])             # 5
print(my_range[1])             # 6
print(my_range[2])             # 7
# print(my_range[3])
# IndexError: range object index out of range
print('\n')

my_list = [4, 5, 6]           # list
print(my_list[0])             # 4
print(my_list[1])             # 5
print(my_list[2])             # 6
# print(my_list[3])             
# IndexError: list index out of range
print('\n')

tup = (8, 9, 10)              # tuple
print(tup[0])                 # 8
print(tup[1])                 # 9
print(tup[2])                 # 10
# print(tup[3])
# IndexError: tuple index out of range
print('\n')

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])           # 1
print(my_dict['b'])           # 2
print(my_dict['c'])           # 3
# print(my_dict['d'])           # KeyError: 'd'
print('\n')

#Using [] to Update Elements
print('Using [] to Update Elements')
my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list)          # [1, 2, 6, 4]
# my_list[4] = 10
# IndexError: list assignment index out of range
print('\n')

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}
print(my_dict)

my_dict['pig'] = 'snorts'
print(my_dict)
# Pretty printed for clarity
# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts'
# }

my_dict['fish'] = 'glub glub'
print(my_dict)
# Pretty printed for clarity
# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts',
#     'fish': 'glub glub'
# }

'''Examples of expressions include:
    - Literals: 5, 'Karl', 3.141592, True, None
    - Variable references: foo or name when these variables have been previously defined.
    - Arithmetic operations: x + y or a * b - 5.
    - Comparison operations: 'x' == 'x' or 'x' < 'y'.
    - String operations: 'x' + 'y' or 'x' * 32. #Concatenation and repetition
    - Function calls: print('Hello') or len('Python').
    - Any valid combination of the above that evaluates to a single object.

    Examples of statements include:
    - Assignment: like x = 5. This doesn't evaluate as a value; it assigns a value to a variable.
    - Control flow: such as if, else, while, for, and so on. These determine the flow of your program but don't evaluate as a value themselves.
    - Function and class definitions: using def or class.
    - Return statements: like return x, which tells a function to exit and return a value. return itself doesn't return a value; it informs the function what value it should return.
    - Import statements: such as import math.
'''
# Examples of stand-alone expressions that are considered both expressions and statements:
3 + 4            # Simple expression
print('Hello')   # Function call; returns None
my_list.sort()   # Method call; returns None

'''Python evaluates that expression as 25: the multiplications occur first 
(4 * 5 is 20 and 2 * 3 is 6), followed by the additions and subtractions from 
left to right (20 - 1 + 6 is 25).
'''
4 * 5 - 1 + 2 * 3
# Python evaluates that expression as 25: the multiplications occur first

'''Parenthesized sub-expressions are usually evaluated before any non-parenthesized sub-expressions.
PEMDAS: Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right) 
Use parentheses to tell Python explicitly how you want to evaluate the expression
'''
print(((4 * 5) - 1) + (2 * 3))   # 25
print((4 * ((5 - 1) + 2)) * 3)   # 72
print(((((4 * 5) - 1) + 2) * 3)) # 63
print(4 * (5 - (1 + (2 * 3))))   # -8

#Output vs. Return Values
print
print(list(range(3)))

#Exercises 
#1 
number = 4936
ones = int(str(number)[3]) % 10
tens = int(str(number)[2]) % 10 * 10
hundreds = int(str(number)[1]) % 10 * 100
thousands = int(str(number)[0]) % 10 * 1000
print(ones) #6
print(tens) #30
print(hundreds) #900
print(thousands) #4000
print('\n')

#Launch School Solution (with no string conversion)
number = 4936
ones = number % 10 #Because 4936 % 10 = 6 (4930 with 6 remaining)
print(ones) #6
number = number // 10 #4936 // 10 = 493 (integer division) (removes the decimal)
print(number) #493

tens = number % 10 #Because 493 % 10 = 3 (490 with 3 remaining) 
print(tens) #3
number = number // 10 #493 // 10 = 49 (integer division) (removes the decimal)
print(number) #49

hundreds = number % 10 #Because 49 % 10 = 9 (40 with 9 remaining)
print(hundreds) #9

thousands = number // 10 #49 // 10 = 4 (integer division) (removes the decimal)
print(thousands) #4   #Because 4 % 10 = 4 (0 with 4 remaining)

#2