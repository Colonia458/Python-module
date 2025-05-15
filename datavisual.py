import matplotlib.pyplot as plt

# Create a bar chart showing 5 different countries and their population.
Country = ['Kenya','Tanzania','Uganda','Ethiopia','Somalia']
population = [56, 63.2, 48.9, 121, 16.8]

plt.bar(Country, population, color='green')
plt.title("Population in East Africa")
plt.xlabel("Country")
plt.ylabel("Population in millions")
plt.show()

# Create a pie chart showing how a student spends 24 hours of their day.
activities = ['Studying', 'Eating', 'Coding', 'Gaming', 'Sleeping']
hours = [8, 2, 4, 2, 8]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Day in the life of a student")
plt.show()


# Make a line chart that shows temperature changes during the day (morning, noon, evening, night).
time_of_day = ['morning','noon', 'evening', 'night']
temperature = [18,28,24,16]

plt.plot(time_of_day, temperature)
plt.title("Nakuru daily temperature")
plt.xlabel("Time of Day")
plt.ylabel("Temperature")
plt.show()
