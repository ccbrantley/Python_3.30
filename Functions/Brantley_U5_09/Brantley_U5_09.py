def main():
    total_sales = float(input('Enter total salese: '))
    state_tax, county_tax, total_tax = tax(total_sales)
    print('County sales tax: $', format(county_tax, ',.2f'), sep='')
    print('State sales tax: $', format(state_tax, ',.2f'), sep='')
    print('Total sales tax: $', format(total_tax, ',.2f'), sep='')
def tax(total_sales):
    county_tax = total_sales * .025
    state_tax = total_sales * .05
    total_tax = county_tax + state_tax
    return state_tax, county_tax, total_tax

main()
