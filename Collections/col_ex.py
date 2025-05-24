people = len(list())
print(people)  # 6

stuff = ('hello', 'world', 'bye', 'now') 
stuff = list(stuff)
stuff[2] = 'goodbye'
print(stuff)  # ['hello', 'world', 'goodbye', 'now']
stuff = tuple(stuff)
print(stuff)  # ('hello', 'world', 'goodbye', 'now')

pi = 3.141592 
str_pi = str(pi)
print(str_pi) 

country = {
    'Alice': 'USA', 
    'Francois': 'Canada', 
    'Inti': 'Peru', 
    'Monika': 'Germany', 
    'Sanyu': 'Uganda', 
    'Yoshitka': 'Japan',
}

print(country['Alice'])

match country:
    case 'Alice': 
        print('Alice is from the USA')
    case 'Francois':
        print('Francois is from Canada')
    case 'Inti':
        print('Inti is from Peru')
    case 'Monika':
        print('Monika is from Germany')
    case 'Sanyu':
        print('Sanyu is from Uganda')
    case 'Yoshitka':
        print('Yoshitka is from Japan')
    case _:
        print('Some countries are missing')
