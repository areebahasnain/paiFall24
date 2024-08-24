num_list = input("Enter a list of numbers: ")

numbers = []
for item in num_list.split():
    numbers.append(int(item))

largest_number = numbers[0]    
    

for number in numbers:
    if number > largest_number:
        largest_number = number
    
print("The largest number is:", largest_number)
