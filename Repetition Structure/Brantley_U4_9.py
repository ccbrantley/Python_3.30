years = 0
seaLevel = 0
seaLevel_rise = 1.6

print("Ocean's level rising over 25 years.")
print('Year\tSea Level\n\t(millimeters)\n-----\t---------')
for years in range (1,26,1):
    seaLevel = years * seaLevel_rise
    print(years, '\t', format(seaLevel, ',.2f'), ' mm')
