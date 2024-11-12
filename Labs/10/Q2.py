import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("Concrete_Data.csv")
x=data[["Cement (component 1)(kg in a m^3 mixture)", "Blast Furnace Slag (component 2)(kg in a m^3 mixture)", "Fly Ash (component 3)(kg in a m^3 mixture)", "Water  (component 4)(kg in a m^3 mixture)"]]

# Comprehensive exploratory data analysis.

x.hist(bins=30, figsize=(10, 5))
plt.suptitle("Distributions")
plt.show()
plt.figure(figsize=(12,10))
plotnumber=1
for column in x.columns:
    plt.subplot(2, 2, plotnumber)
    sns.boxplot(y=x[column])
    plt.title(f"Boxplot of {column}")
    plotnumber += 1  

plt.tight_layout()
plt.show()

# Overall distribution of the data.

plt.figure(figsize=(12, 10))
for i, column in zip(range(len(x.columns)), x.columns):
    plt.subplot(2, 2, i + 1)
    plt.hist(x[column], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(x[column].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    plt.axvline(x[column].median(), color='green', linestyle='dashed', linewidth=1, label='Median')
    plt.title(f"Overall Histogram of {column}")
    plt.xlabel('Value (kg in a m^3 mixture)')
    plt.ylabel('Frequency')
    plt.legend()

plt.suptitle("Overall Distribution of Concrete Components", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Correlations between the variables.

correlation_matrix = x.corr()
plt.figure(figsize=(6, 3))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title("Correlation Matrix of Concrete Components")
plt.show()

# Observable trends

plt.figure(figsize=(12, 10))
for i, column in zip(range(len(x.columns)), x.columns):
    plt.subplot(2, 2, i + 1)
    sns.regplot(x=data['Concrete compressive strength(MPa, megapascals) '], y=x[column], scatter_kws={'alpha':0.5})
    plt.title(f"Compressive Strength vs. {column} with Regression Line")
    plt.xlabel('Compressive Strength (MPa)')
    plt.ylabel(f'{column} (kg in a m^3 mixture)')
    plt.grid(True)

plt.tight_layout()
plt.show()

# Relationship between the most significant features

features = [
    "Cement (component 1)(kg in a m^3 mixture)", 
    "Blast Furnace Slag (component 2)(kg in a m^3 mixture)", 
    "Fly Ash (component 3)(kg in a m^3 mixture)", 
    "Water  (component 4)(kg in a m^3 mixture)"
]

label = 'Concrete compressive strength(MPa, megapascals) '

correlation_matrix = data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title("Correlation Matrix of Concrete Components")
plt.show()


significant_features = correlation_matrix[label].abs().nlargest(5).index.tolist()

plt.figure(figsize=(10, 8))
plot_number = 1
for feature in significant_features[1:]: 
    plt.subplot(2, 2, plot_number)
    sns.regplot(x=data[label], y=data[feature], scatter_kws={'alpha': 0.5})
    plt.title(f"Compressive Strength vs. {feature}")
    plt.xlabel('Compressive Strength (MPa)')
    plt.ylabel(f'{feature} (kg in a m^3 mixture)')
    plot_number += 1

plt.tight_layout()
plt.show()
