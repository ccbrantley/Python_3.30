number = 0
number_sum = 0
print('Enter positive numbers to sum them together and enter a negative number to stop.')
while number >= 0:
    number = float(input('Enter number: '))
    if number >= 0:
        number_sum += number
print('The sum is:', format(number_sum, ',.2f'))
