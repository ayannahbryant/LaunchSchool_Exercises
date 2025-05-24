#The Python method to right justify a string is: str.rjust()
'''str.rjust(width[, fillchar])
Return the string right justified in a string of length width. Padding is done using the specified fillchar 
(default is an ASCII space). The original string is returned if width is less than or equal to len(s).

Width must be greater than the length of the string
'''

string = 'Align to the right!'
print(string.rjust(25))
