# obj = 42

obj = 'ABcd' #Reassignment of obj
obj.upper() #Neither mutation nor reassignment of obj; it creates a new string because we don't reassign obj and strings are immutable
obj = obj.lower() #Reassignment of obj because creates a new string, the address of obj changes, reassigns to obj
print(len(obj)) #Neither mutation nor reassignment of obj because it does not create a new object, reassigns to obj, or the address of obj does not change (like line 3)
obj = list(obj) #Reassignment of obj because it creates a new obj and the address of obj changes (like line 11)
obj.pop() #Mutation of obj because it removes the last element (list are mutable)
obj[2] = 'X' #Mutation of obj because it changes the third element (list are mutable)
obj.sort() #Mutation of obj because it changes the order of elements (list are mutable)
set(obj) #Neither mutation nor reassignment of obj because creates a new set obj but doesn't reassignment list obj (like line 3)
obj = tuple(obj) #Reassignment of obj because it creates a new obj and the address of obj changes (like line 6)

obj = 'ABcd'
#obj = 'ABcd' #reassignment
obj.upper() 
#obj = 'ABCD' #neither
obj = obj.lower() 
#obj = 'abcd' #reassignment
print(len(obj))
#obj = 4 #neither
obj = list(obj) 
#obj = ['a', 'b', 'c', 'd'] #reassignment
obj.pop()
#obj = ['a', 'b', 'c'] #mutation
obj[2] = 'X'
#obj = ['a', 'b', 'X'] #mutation
obj.sort()
#obj = ['X', 'a', 'b'] #mutation - Uppercase letters are sorted before lowercase letters because they have a lower ASCII value
set(obj)
#obj = {'X', 'a', 'b'} #neither
obj = tuple(obj)
#obj = ('X', 'a', 'b') #reassignment

print(type(obj)) #<class 'tuple'>