import json

def save_dict_to_json(file, data):
    try:
        with open(file, 'w') as f:
            json.dump(data, f)
        print(f"Dictionary has been saved to '{file}'.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while saving the dictionary: {e}")

def load_dict_from_json(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except PermissionError:
        print("Error: You do not have permission to read the file.")
        return None
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the dictionary: {e}")
        return None

# Initial dictionary
dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}

# Take input from user to update the dictionary
try:
    while True:
        name = input("Enter name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        age = input(f"Enter age for {name}: ")
        
        if not age.isdigit():
            print("Age must be a number. Please try again.")
            continue
        
        dictionary[name] = int(age)
    
    file = "data.json"
    save_dict_to_json(file, dictionary)
    data = load_dict_from_json(file)
    
    if data is None:
        exit()
    
    # Find the person with the maximum age
    max_age = -1
    max_age_people = []
    
    for name, age in data.items():
        if age > max_age:
            max_age = age
            max_age_people = [name]
        elif age == max_age:
            max_age_people.append(name)
    
    if max_age_people:
        print(f"The person(s) with the maximum age ({max_age}) is/are: {', '.join(max_age_people)}")
    else:
        print("No data found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
