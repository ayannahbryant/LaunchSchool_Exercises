#Variable and Variable Names
#Assigning and reassigning an object to a variable
answer = 41
print(answer)       # 41

answer = 42
print(answer)       # 42

'''
Variable names are often referred to by the broader term identifiers. In Python, identifiers refer to several things:
    Variable and constant names
    Function and method names
    Function and method parameter names
    Class and module names
'''

#Naming Conventions
#Naming conventions for most identifiers (excluding constant and class names):
''' 
    Use snake_case formatting for these names.
    Names may contain lowercase letters (a-z), digits (0-9), and underscores (_).
    Names should begin with a letter.
    If the name has multiple words, separate the words with a single underscore (_).
    Names that begin or end with one or two underscores have special meaning under 
    the naming conventions. Don't use them until you understand how they are used.
    Names may only use letters and digits from the standard ASCII character set.  

    Idiomatic Names (Legal names)
        foo
        answer_to_ultimate_question
        eighty_seven
        index_2
        index2
'''
#Constant names (unchanging values):
'''
    Note: An unchanging value is completely up to the programmer. 
    Note: Do not create a constant in a function.

    Use SCREAMING_SNAKE_CASE formatting for these names.
    Names may contain uppercase letters (A-Z), digits (0-9), and underscores (_).
    Names should begin with a letter.
    If the name has multiple words, separate the words with a single underscore (_).
    Names that begin or end with one or two underscores have special meaning 
    under the naming conventions. Don't use them until you understand how they are used.
    Names may only use letters and digits from the standard ASCII character set.

    Idiomatic Names (Legal names)
        FOO
        ANSWER_TO_ULTIMATE_QUESTION
        EIGHTY_SEVEN
        INDEX_2
        INDEX2
'''

#Class names:
'''
Use PascalCase formatting for these names. PascalCase is sometimes called CamelCase (with both Cs capitalized).
Names may contain uppercase and lowercase letters (A-Z, a-z) and digits (0-9).
Names should begin with an uppercase letter.
If the name has multiple words, capitalize each word.

Idiomatic Names (Legal names)
    Foo
    UltimateQuestion
    FourLeggedPets
    PythonVersion2Rules
'''

#Non-Idiomatic Names (Still Legal) 
'''
Non-Idiomatic Names	    Explanation
fourWayIntersection	    camelCase
Schön	                Extended ASCII
'''

#Illegal names
'''
Illegal Names	        Explanation
pass	                Reserved word
3xy	                    Starts with digit
ultimate-question	    Hyphen
one two three	        Whitespace
is_lowercase?	        Punctuation
is+lowercase	        Special character
'''

#Valid variable names 
first,last = ['Mary', 'Wonder']
print(first) #Mary
print(last)  #Wonder

#Augmented assignment
print('Augmented assignment')
foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo**3        # foo is now 15.625
print(foo)          # prints 15.625

foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625

#Augmented assignment with strings
print('Augmented assignment with strings')
bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc

#Augmented assignment with lists
print('Augmented assignment with lists')
bar = [1, 2, 3]     # bar is [1, 2, 3]
bar += [4, 5]       # + with lists appends
                    # bar is now [1, 2, 3, 4, 5]
print(bar)          # prints [1, 2, 3, 4, 5]

#Augmented assignment with sets 
print('Augmented assignment with sets')
bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}

#Returing Values
print('Returning Values')
def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)                # 1764

def foo(bar):
    print(bar)

a = 3
#foo(a *= 2)
#     ^^
# SyntaxError: invalid syntax

def foo():
    a = 3
#   return a *= 2
#            ^^
# SyntaxError: invalid syntax



#Reassignment vs. Mutation
print('Reassignment vs. Mutation')
#Reassignment - A reassignment will move the variable to a new object (new object address)
#Mutation - A mutation will change (or mutate) the object in place (same object address)
#Only mutatable objects can be mutated. Immutable objects cannot be mutated.

num = 3               # assignment (initialization)
my_list = [1, 2, 3]   # assignment (initialization)
my_dict = {           # assignment (initialization)
    'a': 1,
    'b': 2,
}

num = 42              # Reassignment
my_list[1] = 42       # Reassignment of element,
                      # my_list is mutated! 
my_dict['b'] = 3      # Reassignment of dict pair
                      # my_dict is mutated!

# You can still reassign the variables
my_list = [2, 3, 4]   # Reassignment
my_dict = { 'x': 0 }  # Reassignment