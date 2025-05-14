from math import remainder
from decimal import Decimal
import math
# Arithmetic Operators in Python
# Python supports the following arithmetic operators:

#Addition with +
print(38 + 4) #42 
print(38.4 + 41.9) #80.3

#mixing integars and floats
print(38 + 41.5) #79.5

#Subtraction with -
print(38 - 4) #34
print(38.4 - 41.9) # -3.5

#mixing integars and floats
print(38 - 41.5) # -3.5

#Multiplication with *
print(38 * 4) #152
print(38.4 * 41.1) #1578.24

#mixing integars and floats
print(38 * 41.5) #1577.0

#Division with /
print(16 / 4) #4.0 
print(16 / 2.5) #6.4

#Integer division with //
print(16 // 3) #5
print(16 // -3) # -6
print(16 // 2.3) #6.0
print(-16 // 2.3) # -7.0

#Exponentiation (powers) with **
print(16 ** 3) #4096
#or 
print(16 * 16 * 16) #4096

#Modulo with %
print(15 % 3) #0
print(16 % 3) #1
print(17 % 3) #2
print(18 % 3) #0

#Need to be careful with negative numbers
print(14 % 7) #0, remainder is 0
print(17 % 7) #3, remainder is 3
print(17 % -7) #-4, remainder is 3
print(-17 % 7) #4, remainder is -3
print(-17 % -7) #-3, remainder is -3 

print(int(remainder(14, 7))) #0
print(int(remainder(17, 7))) #3
print(int(remainder(17, -7))) #3
print(int(remainder(-17, 7))) #-3
print(int(remainder(-17, -7))) #-3

#floating point imprecision
print(0.1 + 0.2 == 0.3) #False

math.isclose(0.1 + 0.2, 0.3) #True

print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3')) #True
print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3)) #False
