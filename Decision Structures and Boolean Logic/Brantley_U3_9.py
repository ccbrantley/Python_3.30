pocketNumber = int(input('Please enter a Pocket Number to receive the corresponding color'))
if pocketNumber > 36 or pocketNumber < 0:
    print('NULL')
elif pocketNumber == 0:
    print('The pocket color is Green.')
elif (0 < pocketNumber <= 10 and pocketNumber % 2 == 1) or \
     (11 <= pocketNumber <= 18 and pocketNumber % 2 == 0) or \
     (19 <= pocketNumber <= 28 and pocketNumber % 2 == 1) or \
     (29 <= pocketNumber <= 36 and pocketNumber  % 2 == 0):   
    print('The pocket color is red.')
else:
    print('The pocket color is black.')

