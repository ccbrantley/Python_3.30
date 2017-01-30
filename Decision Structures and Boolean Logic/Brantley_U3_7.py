print('There are three primary colors, red, blue, and yellow.\nPlease type two primary colors to mix: ')
firstColor = str(input('The first color to mix? '))
secondColor = str(input('The second color to mix? '))
combination = firstColor + secondColor
if combination in ['bluered', 'redblue']:
    print('The final color is purple!')
elif combination in ['redyellow', 'yellowred']:
    print ('The final color is orange!')
elif combination in ['blueyellow', 'yellowblue']:
    print ('The final color is green!')
else:
    print("NULL")
