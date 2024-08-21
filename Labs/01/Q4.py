num_list = input("Enter a list of integers: ")

sum = 0

for num in num_list.split():
    sum += int(num)

print("Sum of all integers in the list: ", sum)