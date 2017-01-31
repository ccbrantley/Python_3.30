#minimum insurance
import insurance

def main():
    
    replacementCost = float(input('Replacement cost of building: '))
    print('Minimum amount of insurance you need: $', format(insurance.insurance(replacementCost), ',.2f'), sep='')
    
main()
