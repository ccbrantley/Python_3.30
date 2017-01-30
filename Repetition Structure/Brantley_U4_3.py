budget = 0
budgetOver = 0
budgetLess = 0
expense = 0
expenseTotal = 0

expenseCalculated = 1

budget = int(input('Please enter your budget for this month: '))
while expense != 0 or expenseCalculated == 1:
    expense = int(input('Enter Expense Amount (0 to exit): '))
    expenseTotal += expense
    print('So far your expense for the month is: $', format(expenseTotal, ',.2f'), sep='')
    
    expenseCalculated = expenseCalculated - 1


if expenseTotal > budget:
    budgetOver = expenseTotal - budget
    print('Budget Over by: $', format(budgetOver, ',.2f'), sep='')
elif expenseTotal < budget:
    budgetLess = budget - expenseTotal
    print('Budget Less by: $', format(budgetLess, ',.2f'), sep='')


    
    
