balance = 1000.00
interest = 0.05
comp_interest = balance * (1 + interest) ** 5

print(comp_interest)    
print(balance)

#Single expression
balance = 1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print(balance)

#Augumented assignment
balance = 1000.00
balance += balance * interest
balance += balance * interest
balance += balance * interest
balance += balance * interest
balance += balance * interest
print(balance)

balance = 1000.00
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)