import kilometer_converter

print('This program converts kilometers into miles')

def main():
    kilometers = float(input('Enter the amount of kilometers: '))
    print('Miles: ', format(kilometer_converter.kilometer_converter(kilometers), ',.2f'))
    
main()
