#personal information
import personal_information_class
def main():
    info_list = []
    for value in range(3):
        entry = create_obj()
        info_list.append(entry)
    for item in info_list:
        display_obj(item)

def create_obj():
    name = input('Enter name: ')
    address = input('Enter address: ')
    age = int(input('Enter age: '))
    phone = input('Enter phone (xxx-xxxx): ')
    entry = personal_information_class.Information(name, address, age, phone)
    return entry
def display_obj(entry):
    print('Name: ', entry.get_name(), sep='')
    print('Address: ', entry.get_address(), sep='')
    print('Age: ', entry.get_age(), sep='')
    print('Phone: ', entry.get_phone(), sep='')

main()
