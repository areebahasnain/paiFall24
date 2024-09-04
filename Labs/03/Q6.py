def write_question_to_file(file):
    try:
        sentence = input("Enter a sentence: ")
        
        if sentence.strip().endswith('?'):
            with open(file, 'w') as f:
                f.write(sentence)
            print(f"The sentence has been added to '{file}'.")
        else:
            print("The entered sentence is not a question.")
    
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file = "questions.txt"
write_question_to_file(file)
