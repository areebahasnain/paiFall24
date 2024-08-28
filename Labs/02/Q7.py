def temperatureData(temps, remove_day = None):
    print(f"Average Temperature: {(sum(temps) / len(temps)):.2f}")
    print("Highest Temperature:", max(temps))
    print("Lowest Temperature:", min(temps)) 
    print("Temperatures in ascending order:", sorted(temps))

    if remove_day is not None:
        if 0 <= remove_day < len(temps):
            day_removed = temps.pop(remove_day - 1) # idx 9 is 30, which is the 10th day.
            print(f"Temperatures without day {remove_day}: {temps}")

daily_temperatures = [30, 32, 31, 29, 28, 35, 33, 30, 31, 30, 29, 28, 31, 33, 34, 36, 37]
temperatureData(daily_temperatures, 10)
