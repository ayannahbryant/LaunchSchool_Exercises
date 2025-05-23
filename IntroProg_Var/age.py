def age(input_age):
    print(f'You are {input_age} years old.')
    return input_age

user_age = age(input('Enter your age: '))
user_age = int(user_age)

print(f'In 10 years, you will be {user_age + 10} years old.')
print(f'In 20 years, you will be {user_age + 20} years old.')
print(f'In 30 years, you will be {user_age + 30} years old.')
print(f'In 40 years, you will be {user_age + 40} years old.')

