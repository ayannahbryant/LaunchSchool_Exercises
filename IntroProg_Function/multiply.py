#My solution
def multiply(num_1, num_2): 

    result = num_1 * num_2
    print(f'{num_1} * {num_2} = {result}')

    return num_1 * num_2

first_num = float(input('Enter first number: '))
second_num = float(input('Enter second number: '))

multiply(first_num, second_num)

#Launch School 
def multiply(left, right):
    return left * right

def get_number(prompt):
    return float(input(prompt))

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

#Global variables: multiply, get_number, first_number, second_number, product
#Local variables: left, right, prompt
#Built-in functions: input, float, print

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

#Functions: say
#Methods: upper(), lower()
#Built-in functions: input, print, max



