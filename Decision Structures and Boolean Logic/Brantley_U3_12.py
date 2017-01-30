discount = 0
totalCost = 0
softCost = 99
pckpur = int(input('How many packages have you purchased?'))
total = pckpur * softCost

if pckpur < 10:
    print ('We do not offer a discount for only purchasing ', pckpur, ' of our software packages.', sep='')
elif 10 <= pckpur <= 19:
    discount = .10 * total
    totalCost = total - discount
    print('The discount for purchasing ', pckpur, ' items is: $', format(discount, ',.2f'), sep='')
    print('The total cost w/o the discount is: $', format(total, ',.2f'), sep='')
    print('The total cost with the discount is: $', format(totalCost, ',.2f'), sep='')
elif 20 <= pckpur <= 49:
    discount = .20 * total
    totalCost = total - discount
    print('The discount for purchasing ', pckpur, ' items is: $', format(discount, ',.2f'), sep='')
    print('The total cost w/o the discount is: $', format(total, ',.2f'), sep='')
    print('The total cost with the discount is: $', format(totalCost, ',.2f'), sep='')
elif 50 <= pckpur <= 99:
    discount = .30 * total
    totalCost = total - discount
    print('The discount for purchasing ', pckpur, ' items is: $', format(discount, ',.2f'), sep='')
    print('The total cost w/o the discount is: $', format(total, ',.2f'), sep='')
    print('The total cost with the discount is: $', format(totalCost, ',.2f'), sep='')
elif pckpur >= 100:
    discount =.40 * total
    totalCost = total - discount
    print('The discount for purchasing ', pckpur, ' items is: $', format(discount, ',.2f'), sep='')
    print('The total cost w/o the discount is: $', format(total, ',.2f'), sep='')
    print('The total cost with the discount is: $', format(totalCost, ',.2f'), sep='')
else:
    print('NULL')
