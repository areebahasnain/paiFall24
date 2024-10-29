import matplotlib.pyplot as plt

age_groups = ['18-25', '26-30', '31-35', '36 and above']
age_distribution = [69, 70, 42, 7]

plt.figure(figsize=(8, 6))
colors = ['#FFB3BA', '#FFDFBA', '#B4A0FF', '#B3C6FF']

plt.pie(age_distribution, labels=age_groups, colors=colors, autopct='%1.1f%%')
plt.title("Student Ages", fontsize=16)

plt.show()
