stock_prices = [298,305,320,301,292]

result = stock_prices[3]

print(result)

#searching by value
for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        print(i)

#all values
for price in stock_prices:
    print(price)


stock_prices.insert(2,400)

#print(stock_prices)

#delete element
new_arr = [2,45,67,89,87]
new_arr.remove(3)
print(new_arr)