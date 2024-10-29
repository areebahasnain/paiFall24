import matplotlib.pyplot as plt

# Sample data: List of cities and their respective populations
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
populations = [8419600, 3980400, 2716000, 2328000, 1681000,
               1584200, 1547200, 1423800, 1343000, 1027000]

# Create a horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color='pink')
plt.title('Population of Cities')
plt.xlabel("Population", fontsize=14)
plt.ylabel("Cities", fontsize=14)

plt.tight_layout()
plt.show()


