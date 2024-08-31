def create_dictionary(list1, list2):
    """
    Args:
        list1 (list): The list of keys.
        list2 (list): The list of values.
    """
    result = {}
    for i in range(len(list1)):
        result[list1[i]] = list2[i]
    
    return result

list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()
        
dictionary = create_dictionary(list1, list2)
        
print("The resulting dictionary is:")
for key, value in dictionary.items():
    print(f"{key}: {value}")

