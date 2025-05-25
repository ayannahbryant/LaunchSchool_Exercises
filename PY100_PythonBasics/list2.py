my_list = ['fish', 'and', 'chips']
try:
    print(my_list[10])  # This will raise an IndexError
except IndexError as e:
    print(f"Error: {e}")  # Prints: Error: list index out of range

# You could also show that negative indices work until they're out of range
print(my_list[-1])  # 'chips'
print(my_list[-3])  # 'fish'
try:
    print(my_list[-4])  # This will raise an IndexError
except IndexError as e:
    print(f"Error: {e}")  # Prints: Error: list index out of range
