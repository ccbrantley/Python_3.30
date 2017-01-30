print('This is a quick game. The goal is to type the \ncorrect quantity of change pieces to create a dollar')
pen = int(input('Please enter the amount of Pennies you would like to use: '))
penAdd = .01 * pen
print("You've added ", format(penAdd, ',.2f'), ' cents.', sep='')
nic = int(input('Please enter the amount of Nickles you would like to use: '))
nicAdd = .05 * nic
print("You've added ", format(nicAdd, ',.2f',), ' cents.', sep='')
dim = int(input('Please enter the amount of Dimes you would like to use: '))
dimAdd = .1 * dim
print("You've added ", format(dimAdd, ',.2f'), ' cents.', sep='')
qua = int(input('Please enter the amount of Quarters you would like to use: '))
quaAdd = .25 * qua
print("You've added ", format(quaAdd, ',.2f'), ' cents.', sep='')
total = penAdd + nicAdd + dimAdd + quaAdd
print('Your total was : $', format(total, ',.2f'), sep='')
if total == 1:
    print("Congratulations! You've calculated a dollar and won the game!")
elif total > 1:
    print('You added too much.')
elif total < 1:
    print('You did not add enough.')
