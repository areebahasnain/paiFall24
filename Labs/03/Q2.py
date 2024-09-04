def search_and_replace_in_file(file, search_word, replace_word):
    try:
        with open(file, "r") as f:
            data = f.read()
        
        if search_word in data:
            new_data = data.replace(search_word, replace_word)
            
            with open(file, "w") as f:
                f.write(new_data)
            
            print(f"All occurrences of '{search_word}' have been replaced with '{replace_word}'.")
        else:
            print(f"The word '{search_word}' was not found in the file. No replacement made.")
    
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file = "sample.txt"
search_word = "Areeba"
replace_word = "Emman"
search_and_replace_in_file(file, search_word, replace_word)
