import numpy as np
import matplotlib.pyplot as plt

# Dataset
data = np.array([
    [1500, 2000, 1800, 1200, 900],  
    [1600, 2100, 1900, 1300, 950],  
    [1700, 2200, 2000, 1400, 1000], 
    [1650, 2150, 1950, 1350, 980],  
    [1750, 2250, 2050, 1450, 1020], 
    [1800, 2300, 2100, 1500, 1050], 
    [1900, 2400, 2200, 1600, 1100], 
])

countries = ["A", "B", "C", "D", "E"]

# Total cases per country
totals = data.sum(axis=0)
print("Total cases per country:")
for country, total in zip(countries, totals):
    print(f"{country}: {total}")
print("Country with highest total cases:", countries[np.argmax(totals)])

# Daily totals and analysis
daily_totals = data.sum(axis=1)
print("Average daily cases:", daily_totals.mean())
print("Day with highest cases:", np.argmax(daily_totals) + 1)

# Percentage change
percent_change = ((data[-1] - data[0]) / data[0]) * 100
print("Percentage increase by country:", percent_change)
print("Country with highest increase:", countries[np.argmax(percent_change)])

# Normalized data
normalized = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
print("Normalized data:\n", normalized)

# Visualization
plt.figure(figsize=(10, 6))
for i, country in enumerate(countries):
    plt.plot(data[:, i], label=country, marker='o')

plt.legend()
plt.title("Daily Cases by Country")
plt.xlabel("Day")
plt.ylabel("Cases")
plt.xticks(ticks=range(7), labels=[f"Day {i+1}" for i in range(7)])
plt.grid()
plt.show()
