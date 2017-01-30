print("Serendipity Booksellers: Book Club")
bks = int(input('Please enter the amount of books you have \npurchased this month to display your accrued points: '))
if bks == 0:
    print('You have accrued no points this month...')
elif (2 <= bks <= 3):
    print('You have accrued five points for your purchase of', format(bks, ',.0f'), 'books.')
elif (4 <= bks <= 5):
    print('You have accrued fifteen points for your purchase of', format(bks, ',.0f'), 'books.')
elif (6<= bks <= 7):
    print('You have accrued thirty points for your purchase of', format(bks, ',.0f'), 'books.')
elif bks >= 8:
    print('You have accrued sixty points for your purchase of', format(bks, ',.0f'), 'books.')
