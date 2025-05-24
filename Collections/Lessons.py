#Collection and non-collection types
letters = ['a', 'b', 'θ', 'd', 'e']
char = letters[2]
print(char is letters[2])     # True

letters = 'abθde'
char = letters[2]
print(char)
print(char is letters[2])     # False because char is a string of one character, not a list of one character 
#If the non-ASCII character was an ASCII character, it would return True because of the interning concept 
# (we treat strings as ordinary sequences of characters).

#Sets
numbers = { 1, 2, 3, 4, 5 }
print(numbers)      # { 1, 2, 3, 4, 5 }

numbers = { 5, 3, 1, 2, 4 }
print(numbers)      # { 1, 2, 3, 4, 5 }

numbers = { 1, 2, 37, 4, 5 }
print(numbers)      # {1, 2, 4, 37, 5}

my_str = 'Python'

my_list = list(my_str)
print(my_list)  # ['P', 'y', 't', 'h', 'o', 'n']

my_tuple = tuple(my_list)
print(my_tuple) # ('P', 'y', 't', 'h', 'o', 'n')

my_set = set(my_tuple)
print(my_set)   # {'t', 'o', 'n', 'h', 'P', 'y'}