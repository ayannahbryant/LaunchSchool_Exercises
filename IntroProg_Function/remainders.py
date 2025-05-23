def remainders_3(numbers):
    return [number % 3 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1)))
# [0, 1, 2, 0, 1, 2, 0]
print(any(remainders_3(numbers_2)))
# [1, 2, 1, 2]
print(any(remainders_3(numbers_3)))
# [0, 0, 0]
print(any(remainders_3(numbers_4)))
# []

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
# [0, 1, 2, 0, 1, 2, 0]
print(all(remainders_5(numbers_2)))
# [1, 2, 1, 2]
print(all(remainders_5(numbers_3)))
# [0, 0, 0]
print(all(remainders_5(numbers_4)))
# []