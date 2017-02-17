#total sales
def main():
    days_week = 7
    total_sales = 0
    week_Sales = []
    for days in range(days_week):
        sales = float(input('Enter sales for day {} :'.format(days + 1)))
        week_Sales.append(sales)
        total_sales += sales
    print('The total sales for the week was: $',format(total_sales, ',.2f'), sep='')
    print(week_Sales)

main()
