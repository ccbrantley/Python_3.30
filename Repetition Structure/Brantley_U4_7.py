days = 0
day = 0
pay = .02
total = .01


days = int(input('Please enter a number of days: '))


print('Day:\tSalary:/n----\t----\n1\t $0.01')
      
for day in range(2, days + 1, 1):
   pay = pay + pay
   total += pay
   print(day, '\t$', format(pay,',.2f'), sep='')
print('Total Pay: $', format(total, ',.2f'), sep='')
