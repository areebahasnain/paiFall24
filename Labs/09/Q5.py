import matplotlib.pyplot as plt

genders = ['Male', 'Female']
gender_distribution = [69, 30]

plt.figure(figsize=(8, 6))
plt.pie(gender_distribution, labels=genders, autopct='%1.1f%%', startangle=140)
plt.title("Gender Distribution Among Students", fontsize=16)
plt.axis('equal')
plt.show()
