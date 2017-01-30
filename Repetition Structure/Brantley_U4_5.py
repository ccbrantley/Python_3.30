years = 0
months = 0
rainFall = 0
total_rainFall = 0
avg_rainFall = 0

print('This program calculates average rainfall over a period of time')
years = int(input('How many years? '))
months = years * 12



for counter in range(1, years + 1, 1):
    for month in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'):
        rainFall = float(input(str('Please enter in the inches of rainfall for {} in '.format(month) + 'year ' + str(counter))))
        total_rainFall += rainFall

    
avg_rainFall = total_rainFall / months
print('There were', months, 'months in total.')
print('There was a total of ', format(total_rainFall, ',.2f'), ' inches of rainfall')
print('The average rainfall per month was ', format(avg_rainFall, ',.2f'), ' inches')
        
        
