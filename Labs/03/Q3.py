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

def store_dictionary_in_file(dictionary, file):
    try:
        with open(file, 'w') as f:
            for key, value in dictionary.items():
                f.write(f"{key}: {value}\n")
        print(f"The dictionary has been stored in '{file}'.")
    except FileNotFoundError:
        print("Error: The file path was not found.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

try:
    list1 = input("Enter the first list: ").split()
    list2 = input("Enter the second list: ").split()

    if len(list1) != len(list2):
        raise ValueError("Error: The two lists must have the same number of elements.")
        
    dictionary = create_dictionary(list1, list2)
        
    print("The resulting dictionary is:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
    
    file = "dictionary.txt"
    store_dictionary_in_file(dictionary, file)
    
except ValueError as v:
    print(v)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
