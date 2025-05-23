#Exercises 

#1
print('John' + ' ' + 'Doe')

#2 
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

#3
print('5' + '10') #510
#Because these are strings and we have a addition operators, there are concatenated instead of added.

#4
print(int('5') + int('10')) #15
#Because we are converting the strings to integers, they are added together instead of concatenated.

#5
foo = ['a', 'b', 'c']
print(foo[3])
#IndexError: list index out of range
#Because the list foo only has 3 elements (0, 1, and 2), trying to access index 3 will result in an IndexError.

#6
print('foo' == "Foo")
#False
#Because the first letter is lowercase in the first string and uppercase in the second string, they are not equal.

#7
print(int(3.1415))
#3
#Because the int() function truncates the decimal portion of the number, it returns only the integer part.

#8 
print('12' < '9')
#True
#Because '1' comes before '9', so '12' is less than '9'.
