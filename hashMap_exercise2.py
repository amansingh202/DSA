weather = {}

with open("nyc_weather.csv", "r") as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        date = tokens[0]
        temperature = int(tokens[1])
        weather[date] = temperature

print(weather)

# (i). What was the temperature on Jan 9?
print(weather['Jan 9'])

# (ii). What was the temperature on Jan 4?
print(weather['Jan 4'])