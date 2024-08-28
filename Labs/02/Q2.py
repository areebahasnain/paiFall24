def vowelOrConsonant(user_input):
    last_letter = user_input[-1]

    if last_letter.isalpha():
        if last_letter in "aeiouAEIOU":
            return "Vowel"
        else: 
            return "Consonant"
    else:
        return "Not an alphabet character"
    
input_string = input("Enter a string: ")
print("Last letter of the string is:", vowelOrConsonant(input_string))


