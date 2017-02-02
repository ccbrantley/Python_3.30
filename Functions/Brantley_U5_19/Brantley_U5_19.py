f = 0
p = 0
i = 0
t = 0

def main():
    print('Calculates monthly compound monthly interest')
    p = int(input('Enter present value of account: '))
    i = float(input('Enter monthly interest rate(5% = .05): '))
    t = int(input('Enter the number of months: '))
    f = compound_interest(p, i, t)
    print('The accounts future value will be: $', format(f, ',.2f'), sep='')
    
def compound_interest(p, i, t):
    return p*(1+i)**t

main()
