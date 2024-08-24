num_list = input("Enter a list of integers: ")
num = int(input("Enter a number: "))

int_list = []
for item in num_list.split():
    int_list.append(int(item))  

new_list = []

for x in int_list:
    if x >= num: 
        new_list.append(x)

print("Updated list:", new_list)
