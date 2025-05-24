#Allows for resuable code for any set of list
def find_item_index(items_list,target_item):
    try:
        return items_list.index(target_item)
    except ValueError:
        return "Item not found"

fruits = ['apple', 'banana', 'cherry', 'peach', 'watermelon']

print(find_item_index(fruits,'I love you'))