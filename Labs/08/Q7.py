import numpy as np

random_array = np.random.rand(1000)

average = np.mean(random_array)
variance = np.var(random_array)
std_deviation = np.std(random_array)

with open("Lab08_Q7.txt", "w") as f:
    f.write(f"Average: {average}\n")
    f.write(f"Variance: {variance}\n")
    f.write(f"Standard Deviation: {std_deviation}\n")

print("Results saved in 'Lab08_Q7.txt'")
