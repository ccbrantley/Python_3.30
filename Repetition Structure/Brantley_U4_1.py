totalBugs = 0
bugs = 0
day = 0

for days in range(5):

    day += 1
        
    bugs = int(input(str("How many bugs did you collect on day {0}: ").format(day)))
    totalBugs += bugs
    print('\nYou collected ', bugs,' bugs on day ', day, '\nCurrent Total: ', totalBugs, 'bugs')

print('\nYou collected a total of ', totalBugs, 'bugs')
