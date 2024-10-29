import matplotlib.pyplot as plt

years = list(range(1920, 2021))
sea_levels = [10 + (0.1 * (year - 1920)) for year in years]

plt.figure(figsize=(12, 6))
plt.scatter(years, sea_levels, color='darkblue', marker='o')

# Adding labels and title
plt.title("Sea Level Rise Over the Past 100 Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Sea Level (in mm)", fontsize=14)
plt.grid()
plt.show()
