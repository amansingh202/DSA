'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

expenses = [2200, 2350, 2600, 2130, 2190]

diff_feb_jan = expenses[1] - expenses[0]
print(f"Solution for 1 is {diff_feb_jan}")

total_expense_quarter = 0
for i in range(0,3):
    total_expense_quarter += expenses[i]

print(f"Total expenses for the 1st quarter is : {total_expense_quarter}")

month_count = 0
for i in range(0, len(expenses)):
    if (expenses[i] == 2000):
        month_count += 1
    
if month_count == 1:
    print("yes")
else:
    print("No such month")

#add june month expenses
expenses.append(1980)
print(expenses)

#refund in the month of april
expenses[3] = expenses[3] - 200
print(f"Updated expenses: {expenses}")