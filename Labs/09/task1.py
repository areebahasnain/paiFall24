from matplotlib import pyplot as plt
import pandas as pd

# Correct the file path and make sure to use double backslashes or raw string for Windows paths
df = pd.read_csv(r"D:\PAI Practice material\Iris.csv")

# Extract necessary columns
Sepal_length = df['SepalLengthCm']
Petal_length = df['PetalLengthCm']
Species = df['Species']

# 1. Line graph of Petal Length vs Sepal Length
plt.figure(figsize=(10, 6))
plt.plot(Sepal_length, Petal_length, marker='o', linestyle='-', color='b')
plt.xlabel("Sepal Length (cm)", fontsize=14)
plt.ylabel("Petal Length (cm)", fontsize=14)
plt.title("Petal Length vs Sepal Length", fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar graph to plot the number of different species
plt.figure(figsize=(10, 6))
species_counts = df['Species'].value_counts()
species_counts.plot(kind='bar', color='orange')
plt.xlabel("Species", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Number of Different Species", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Scatter plot of Species vs Petal Length
plt.figure(figsize=(10, 6))
for species in df['Species'].unique():
    subset = df[df['Species'] == species]
    plt.scatter(subset['Species'], subset['PetalLengthCm'], label=species)

plt.xlabel("Species", fontsize=14)
plt.ylabel("Petal Length (cm)", fontsize=14)
plt.title("Species vs Petal Length", fontsize=16)
plt.legend(title='Species')
plt.tight_layout()
plt.show()
