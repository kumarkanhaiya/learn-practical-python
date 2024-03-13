total = 0
expenses = []

num_of_expenses = int(input("Enter # of expenses:"))

for i in range(num_of_expenses):
    expenses.append(float(input("Enter the expense: ")))

total = sum(expenses)

# sum = 0

# for expense in expenses:
#     sum = sum + expense

# for i in range(7):
#     expenses.append(float(input))

# sum = sum(expenses)

print("You spent", total)
print("You spent $", total, sep='')
