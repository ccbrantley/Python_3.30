#Christopher Brantley
#creating main function
def main():
#setting global constants
    expenseTotal = 0
    expense = -1
    budget = 0
#asking user input for budget amount
    budget = float(input('Enter budget amount: $ '))
#while loop to calculate running total that will break when user enters 0
    while expense != 0:
        expense = float(input('Enter expense amount (0 to exit): $ '))
        expenseTotal += expense
        print('Your current total for expenses this month is: $ ', format(expenseTotal, ',.2f'), sep='')
#if function to print out whether the expenses were over or less then budget
    if expenseTotal > budget:
        budget_over = expenseTotal - budget
        print('Budget over by : $', format(budget_over, ',.2f'), sep='')
    elif expenseTotal < budget:
        budget_less = budget - expenseTotal
        print('Budget less by : $', format(budget_less, ',.2f'), sep='')
#calling main function
main()
