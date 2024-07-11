'''Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function'''

max = int(input("Enter max number: "))

list = []
for i in range (1, max+1):
    if (i %2 == 1):
        list.append(i)

print(list)