word = input("Enter a word: ")

reversed_word = ""
length = len(word)
index = length - 1

while index >= 0:
    reversed_word += word[index]
    index -= 1

print("Reversed word:", reversed_word)
