def count_characters_and_words(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            char_count = len(content)
            word_count = len(content.split())
            print(f"Total characters: {char_count}")
            print(f"Total words: {word_count}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file = 'sample.txt'
count_characters_and_words(file)
