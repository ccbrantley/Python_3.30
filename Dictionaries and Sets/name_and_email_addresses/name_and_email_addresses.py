import pickle
def main():
    user_choice = 0
    while user_choice == 0:
        print('1. Search for address.')
        print('2. Add new address.')
        print('3. Modify existing entry.')
        print('4. Delete existing entry.')
        print('5. Read data.')
        user_choice = int(input('Enter the numerical value corresponding to your choice: '))
    while user_choice == 1:
        search_menu()
    while user_choice == 2:
        add_data()
    while user_choice == 3:
        modify_data()
    while user_choice == 4:
        delete_data()
    while user_choice == 5:
        read_data()
def search_menu():
    file = open('email.dat', 'rb')
    end_file = False
    address = {}
    user_search = input('Enter the key name to search: ')
    while not end_file:
        try:
            address = pickle.load(file)
            search_func(address, user_search)
        except EOFError:
            end_file = True
    file.close()
    main()
def search_func(address, user_search):
        if user_search in address:
            for value in address:
                name = value
                email = address[value]
            print('\n\t', 'Name: ', name, sep='')
            print('\t','Email: ', email, '\n', sep='')
def add_data():
    file = open('email.dat', 'ab')
    address = {}
    name = input('Name: ')
    email = input('Email: ')
    address[name] = email
    pickle.dump(address, file)
    file.close()
    main()
def modify_data():
    file = open('email.dat', 'rb')
    end_file = False
    address = {}
    whole_address = {}
    while not end_file:
        try:
            address = pickle.load(file)
            for value in address:
                whole_address[value] = address[value]
        except EOFError:
            end_file = True
            file.close()
            modify_func(whole_address)
    main()
def modify_func(whole_address):
    overWrite = 0
    user_modify = input('Enter key name to modify.')
    if user_modify in whole_address:
        overWrite += 1
        name = user_modify
        email = whole_address.get(name)
        print('\tName: ', name, '\n\tEmail: ', email, sep='')
        name_mod = input('Modify name: ')
        email_mod = input('Modify email: ')
        whole_address.pop(name)
        whole_address[name_mod] = email_mod
    else:
        print('\n\tKey name not found.\n')
    if overWrite == 1:
        over_write(whole_address)
    main()
def over_write(whole_address):
    file = open('email.dat', 'wb')
    file.close()
    file = open('email.dat', 'ab')
    address = {}
    for value in whole_address:
        address[value] = whole_address[value]
        pickle.dump(address, file)
        address = {}
    file.close()
    main()
def delete_data():
    file = open('email.dat', 'rb')
    end_file = False
    address = {}
    whole_address = {}
    while not end_file:
        try:
            address = pickle.load(file)
            for key in address:
                whole_address[key] = address.get(key)
        except EOFError:
            end_file = True
            file.close()
            delete_func(whole_address)
    file.close()
def delete_func(whole_address):
    user_delete = input('Enter key name to remove.')
    file = open('email.dat', 'wb')
    file.close()
    file = open('email.dat', 'ab')
    address = {}
    if user_delete in whole_address:
        whole_address.pop(user_delete)
    for key in whole_address:
        address[key] = whole_address[key]
        pickle.dump(address, file)
        address = {}
    file.close()
    main()
def read_data():
    address = {}
    end_file = False
    file = open('email.dat', 'rb')
    print('\n','--Address Book--')
    while not end_file:
        try:
            address = pickle.load(file)
            print(address)
        except EOFError:
            end_file = True
    print('\n')
    file.close()
    main()
main()   
