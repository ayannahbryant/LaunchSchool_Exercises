print(42 == 42) #True
print(42 == 43) #False
print(42 == '42') #True
print('foo' == 'foo') #True (works with strings)
print('FOO' == 'foo') #False (Case sensitive - it matters)

print(42 != 42) #False (different types)
print(42 != '42') #False (different types but same value
print(42 != 43) #True
print('foo' != 'foo') #False (works with strings)
print('FOO' != 'foo') #True (Case sensitive - it matters)