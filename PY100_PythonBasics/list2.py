#If the function tries to access an element at position 10 and the list 
#does not have an element at position 10, based on list_a, it will 
#throw an exception IndexError.

#To fix, you have to implement error handling to catch arguments that are 
#longer than a list length
    
def access_element(items_list, target_item): 
    if len(items_list) == 0:
        return 'List is empty'
    elif target_item < len(items_list):
        second_item = items_list[target_item]
        return second_item
    else:
        return 'Item is out of range'
        

dinner = ['fish', 'and', 'chips']
print(access_element(dinner, 10))
