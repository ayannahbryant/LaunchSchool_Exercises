foo = None 
bar = 'qux' 
is_ok = bool(foo or bar) 

print(f'1. {1 or 2 and 3}')
print(f'2. {0 or 2 and 3}')
print(f'3. {1 or 0 and 3}')
print(f'4. {1 or 2 and 0}')
print(f'5. {0 or 0 and 3}')
print(f'6. {0 or 2 and 0}')
print(f'7. {1 or 0 and 0}')
print(f'8. {0 or 0 and 0}')

print(f'1. {1 and 2 or 3}')
print(f'2. {0 and 2 or 3}')
print(f'3. {1 and 0 or 3}')
print(f'4. {1 and 2 or 0}')
print(f'5. {0 and 0 or 3}')
print(f'6. {0 and 2 or 0}')
print(f'7. {1 and 0 or 0}')
print(f'8. {0 and 0 or 0}')
