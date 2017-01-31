assessmentRate = .60

def main():
    value = float(input('Please enter the value of property: '))
    print('Your assessment value is: $', format(assessmentValue(value), ',.2f'), sep='')
    print('Your property tax is: $', format(propertyTax(assessmentValue(value)), ',.2f'), sep='')

def assessmentValue(aValue):
    return aValue * assessmentRate

def propertyTax(tax):
    taxRemainder = tax%100
    tax = tax - taxRemainder
    return (tax/100)*.72

main()
