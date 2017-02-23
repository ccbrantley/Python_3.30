#date printer
import calendar
def main():
    date = str(input('Enter a date: (mm/dd/yyyy)'))
    date_sep(date)
def date_sep(date):
    date_list = date.split('/')
    print(calendar.month_name[int(date_list[0])],'{}, {}'.format(date_list[1], date_list[2]))

main()
