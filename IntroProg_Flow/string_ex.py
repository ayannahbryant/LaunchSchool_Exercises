def string_allcaps(string):
    if len(string) > 10: 
        return string.upper()
    else:   
        return string

print(string_allcaps('hello world'))
print(string_allcaps('goodbye'))