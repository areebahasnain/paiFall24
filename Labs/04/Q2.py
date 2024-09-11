list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]
print(result)

# The first iteration of the outer loop picks "Hello "
# The second iteration of the outer loop picks "take ":
