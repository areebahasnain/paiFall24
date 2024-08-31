def count(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            character_count = len(text)

            # breaking the text into words based on spaces and counting the number of words
            word_count = len(text.split())

            print(f"Total Characters: {character_count}")
            print(f"Total Words: {word_count}")

    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "test.txt"
count(file_path)
