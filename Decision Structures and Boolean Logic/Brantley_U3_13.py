weight = 0
charge = 0
weight = float(input('Please enter in the weight of your package to calculate the shipping cost: '))
if 0 < weight <= 2:
    charge = weight * 1.50
    print('For a package with a weight of ', format(weight, ',.2f'), ' lbs we would charge $', format(charge, ',.2f'), '.', sep='')
elif 2 < weight =< 6:
    charge = weight * 3.00
    print('For a package with a weight of ', format(weight, ',.2f'), ' lbs we would charge $', format(charge, ',.2f'), '.', sep='')
elif 6 < weight =< 10:
    charge = weight * 4.00
    print('For a package with a weight of ', format(weight, ',.2f'), ' lbs we would charge $', format(charge, ',.2f'), '.', sep='')
elif weight > 10:
    charge = weight * 4.75
    print('For a package with a weight of ', format(weight, ',.2f'), ' lbs we would charge $', format(charge, ',.2f'), '.', sep='')
else:
    print('NULL')
