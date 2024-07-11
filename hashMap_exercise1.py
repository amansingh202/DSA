weather = []

with open("nyc_weather.csv", 'r') as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        # date = tokens[0]
        temp = int(tokens[1])
        weather.append(temp)


print(weather)

#(i). What was the average temperature in first week of Jan
average_temp = sum(weather[0:7])/ len(weather[0:7])
print(f"Average temp in the first week of Jan: {average_temp}F")

#(ii). What was the maximum temperature in first 10 days of Jan

max_temp = max(weather[0:10])
print(f"Maximum temperature is : {max_temp}")
