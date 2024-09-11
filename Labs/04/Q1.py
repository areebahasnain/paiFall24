a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]

result = [x + y for x, y in zip(a, b)]
print(result)


# [('He', 'llo'), ('th', 'is'), ('i', 's'), ('sal', 'man')] ---> zip(a, b)
# x + y ---> concatenate x and y.
 
