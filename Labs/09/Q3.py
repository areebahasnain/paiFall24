import matplotlib.pyplot as plt

# Sample data: List of ice cream flavors and the number of scoops sold
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough',
           'Rocky Road', 'Pistachio', 'Mango', 'Coffee', 'Cheesecake']
scoops_sold = [150, 200, 120, 80, 90,
                60, 70, 110, 130, 100]

# Create a pie chart
plt.figure(figsize=(8, 8))
colors = ['#FFB3BA', '#FFDFBA', '#B4A0FF', '#B3C6FF', '#D9B3FF',
          '#FFC2E2', '#BAF1FF', '#B3B3FF', '#E3B3FF', '#FFCCE5']
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140, colors= colors)
plt.title('Distribution of Ice Cream Sales by Flavor')

plt.tight_layout()
plt.show()