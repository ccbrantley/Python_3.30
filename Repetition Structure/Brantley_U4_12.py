startOrgan = 0
dailyOrgan = 0
dailyOrgan_inc = 0
dailyInc = 0
days = 0

startOrgan = int(input('Starting number of organisms: '))
dailyInc = float(input('Daily percentage increase (ex: .3): '))
days = int(input('How many days: '))
print('Day Approximate\tPopulation')
print('1\t',startOrgan)

dailyOrgan = startOrgan

for day in range (2, days + 1, 1):
    dailyOrgan_inc = dailyOrgan * dailyInc
    dailyOrgan += dailyOrgan_inc
    print(day, '\t', format(dailyOrgan, ',.2f'))
    
    
