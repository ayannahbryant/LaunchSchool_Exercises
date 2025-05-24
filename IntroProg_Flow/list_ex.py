def is_list_empty(my_list): 
    if (my_list): # if checks to see if the list is empty, the if statement evaluates to falsy so it goes to the else statement
        print('Not empty') # if the list is not empty, it prints 'Not empty'
    else:
        print('Empty') # if the list is empty, it prints 'Empty'

is_list_empty([]) # The argument passed to the function is an empty list
is_list_empty([1, 2, 3]) 
is_list_empty([False])
is_list_empty([None])