print(1, 2, 3, 'a', 'b', sep=',') #1,2,3,a,b 
#sep=',' means that the values will be separated by a comma and no space

print('a', 'b', 'c','d', sep='') #abcd
#sep='' means that the values will be concatenated without any space or separator

print(1, 2, 'a', 'b', sep=',', end=' <-\n') #1,2,a,b <-\n
#end= used to specify what to print at the end of the line (used for compability with Windows)

print('a', 'b', end='', sep=','); print('c', 'd', sep=',') #a,bc,d

