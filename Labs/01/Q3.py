num_list = input("Enter a list of integers: ")

even_num = 0

for num in num_list.split():
    if int(num) % 2 == 0: even_num += 1

print("Count of even numbers in the list: ", even_num) 