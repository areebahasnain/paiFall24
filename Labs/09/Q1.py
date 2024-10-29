import matplotlib.pyplot as plt
import numpy as np

students = ['Student ' + str(i) for i in range(1, 21)]
heights = [150, 160, 165, 170, 155, 180, 175, 160, 162, 168,
           172, 158, 164, 169, 177, 182, 155, 163, 171, 159]

# Bar Chart
plt.figure(figsize=(12, 6)) # 12 inches wide and 6 inches tall

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD',
          '#E74C3C', '#3498DB', '#2ECC71', '#9B59B6', '#F39C12',
          '#D35400', '#1ABC9C', '#2C3E50', '#34495E', '#7D3C98',
          '#AAB7B8', '#D5DBDB', '#F7DC6F', '#E67E22', '#C0392B']
plt.bar(students, heights, color=colors) # names: x-axis and heights: y-axis.
plt.title('Student Heights Bar Chart')
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.xticks(rotation=45)
plt.tight_layout()

# Pie Chart
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=140)
plt.title('Student Heights Pie Chart')

# Show the plots
plt.tight_layout()
plt.show()