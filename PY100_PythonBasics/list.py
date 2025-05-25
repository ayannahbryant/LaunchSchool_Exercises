#If the function tries to access an element at position 10 and the list 
#does not have an element at position 10, based on list_a, it will 
#throw an exception IndexError.

def access_second_element(x): 
    if len(x) > 1:
        second_item = x[1]
        return print(second_item)
    elif len(x) == 1: 
        return print('List has one element')
    else: 
        return print('List is empty')

list_a = ['fish', 'and', 'chips']
access_second_element(list_a)
