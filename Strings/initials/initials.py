#initials from full name
def main():
    full_name = str(input('Enter your full name: '))
    initials(full_name)

def initials(full_name):
    name_list = full_name.split(' ')
    firstName = name_list[0]
    middleName = name_list[1]
    lastName = name_list[2]
    print('First initial: {}.'.format(firstName[0]))
    print('Middle initial: {}.'.format(middleName[0]))
    print('Last initial: {}.'.format(lastName[0]))

main()
    
