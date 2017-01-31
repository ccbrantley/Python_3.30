import taxation
import totalSale

def main():
    
    purchaseAmount = float(input('Enter purchase amount: '))
    countyTax, stateTax, totalTax = taxation.taxation(purchaseAmount)
    
    print('Total w/o tax: ', format(purchaseAmount, ',.2f'))
    print('County tax: ', format(countyTax, ',.2f'))
    print('State tax: ', format(stateTax, ',.2f'))
    print('Total tax: ', format(totalTax, ',.2f'))
    print('Total with tax: ', format(totalSale.totalSale(totalTax, purchaseAmount), ',.2f'))
    
                       

   



main()
