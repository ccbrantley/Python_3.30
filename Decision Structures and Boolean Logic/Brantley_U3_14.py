weight = 0
height = 0
print('This progam will calculatey your BMI(Body Mass Index).')
weight = int(input('Please enter in your weight using a measurement of pounds.'))
height = int(input('Please enter in your height using a measurement of inches.'))
BMI = weight * 703/height**2
if 18.5 <= BMI <= 25:
    print('Your BMI is ', format(BMI, ',.2f'), ' and is classified as optimal.', sep='')
elif BMI > 25:
    print('Your BMI is ', format(BMI, ',.2f'), ' and is classified as overweight.', sep='')
elif BMI < 18.5:
    print('Your BMI is ', format(BMI, ',.2f'), ' and is classified as underweight.', sep='')
else:
    print('NULL')
