expenseDict = {'loan payment' : 0, 'insurance' : 0, 'gas' : 0, 'oil' : 0, 'tires' : 0, 'maintenace' : 0}

def main():
    expense()
    totalMonthly, totalYearly = total()
    print('Total monthly cost: $', format(totalMonthly, ',.2f'), sep='')
    print('Total annual cost: $', format(totalYearly, ',.2f'), sep='')  

def expense():
    for x in expenseDict:
        y = int(input('Enter cost amount of ' + x +': '))
        expenseDict[x] = y
    totalMonthly = sum(expenseDict.values())
    
def total():
    x = sum(expenseDict.values())
    return x, x * 12

main()



    
