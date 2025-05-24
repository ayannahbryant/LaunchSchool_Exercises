#To slice an object you use variable_name[start:stop:step]
#if start and stop are empty the method will iterate over the entire object/string

#My solution 
string = 'hello'
print(string)
print(string[::-1])

#Launch School Solution 
def reverse_string(s):
  return s[::-1]

print(reverse_string('hello'))
print(reverse_string(''))
print(reverse_string('This is a long string'))
