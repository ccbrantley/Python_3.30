mass = float(input('Please enter the objects mass'))
newtonMass = mass * 9.8
if mass > 500:
    print('This object is too heavy!')
elif mass < 100:
    print('This object is too light!')
elif mass < 500 or mass > 100:
    print('The Newton weight is: ', format(newtonMass, ',.2f'), sep='')
