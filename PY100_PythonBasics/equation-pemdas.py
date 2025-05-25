#The order of operation is as follows PEMDAS: 
#Expressions in the parentheses are solved first 
#Next, exponents are solved next 
#Then, multiplication and division are solved from left to right 
#Last, addition and subtraction are solved from left to right 

#To solve this equation, the program would: 
#Solve 3**2 = 9 (4 * 5 + 9 / 10)
#Solve 4 * 5 = 20 (20 + 9 / 10)
#Solve 9 / 10 = 0.9 (20 + 0.9)
#Solve 20 + 0.9 = 20.9

equation_result = (4 * 5) + ((3**2) / 10)
print(equation_result)