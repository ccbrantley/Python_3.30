
celsius = 0
conversionFahrenheit = 0
print('°C\t°F')
print('----\t----\n')
for celsius in range (1,21,1):
    conversionFahrenheit = 9 / 5 * celsius + 32
    print(celsius, '\t', format(conversionFahrenheit, ',.2f'))
