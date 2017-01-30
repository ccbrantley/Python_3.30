sec = int(input('Enter a number of seconds: '))
minu = sec / 60
hour = sec / 3600
day = sec / 86400
if sec >= 86400:
    print('There are ', format(day, ',.2f'), ' days in ', sec, ' seconds.', sep='')
elif sec >= 3600:
    print('There are ', format(hour, ',.2f'), ' hours in ', sec, ' seconds.', sep='')
elif sec >= 60:
    print('There are ', format(minu, ',.2f'), ' minutes in ', sec, ' seconds.', sep='')
else:
    print('NULL')


