month = int(input('Please enter in the month: '))
day = int(input('Please enter in the day: '))
year = int(input('Please enter in the year with a two digit format(EX:1999 = 99): '))
multiplied = month * day

if multiplied == year:
    print('The date you entered... ', month, '/', day, '/', year, ' is a magic date!', sep='')
elif multiplied != year:
    print("I'm sorry! ", month, '/', day, '/', year, ' is not a magic date...', sep='')
