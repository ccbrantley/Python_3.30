tuition = 8000
percentIncrease = .03
tuitionIncrease = 0
print('Year\t Tuition Cost\n----\t---------')
for years in range(1,6,1):
    tuitionIncrease = tuition * percentIncrease
    tuition +=tuitionIncrease
    print(years, '\t $', format(tuition, ',.2f'), sep='') 
