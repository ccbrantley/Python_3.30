#employee management system
import pickle
import employee_class
employee_dict = {}
def main():
    load_data()

    menu = 0
    while menu == 0:
        print('1. Look up an employee.')
        print('2. Add new employee.')
        print('3. Modify existing entry.')
        print('4. Delete employee.')
        print('5. View employees.')
        print('6. Quit program.')
        menu = int(input('Enter selection: '))
        #look up
        while menu == 1:
            look_employee(employee_dict)
            menu = 0
        #add new
        while menu == 2:
            employee, id_number = add_employee()
            employee_dict[id_number] = employee
            print('Employee added.')
            menu = 0
        #modify
        while menu == 3:
            employee, id_number, user_input = modify_employee(employee_dict)
            employee_dict.pop(user_input)
            employee_dict[id_number] = employee
            print('Entry modified.')
            menu = 0
        #delete
        while menu == 4:
            pop_value = delete_employee(employee_dict)
            if pop_value != False:
                employee_dict.pop(pop_value, 'Id not found.')
                print('Entry deleted.')
            menu = 0
        #employee list
        while menu == 5:
            view_employee(employee_dict)
            menu = 0 
        #quit
        while menu == 6:
            save_data(employee_dict)
            print('Program closing.')
            break
def load_data():
    global employee_dict
    file = open('employee_directory.dat', 'rb')
    employee_dict = {}
    end_file = False
    while not end_file:
        try:
            employee_dict = pickle.load(file)
            print(employee_dict)
        except EOFError:
            end_file = True
    file.close()
    
def look_employee(employee_dict):
        try:
            user_input = int(input('Enter Id to look up: '))
            if user_input in employee_dict:
                employee = employee_dict.get(user_input)
                print('\n\tName: ', employee.get_name(), sep='')
                print('\tID: ', employee.get_id(), sep='')
                print('\tDepartment: ', employee.get_department(), sep='')
                print('\tJob title: ',employee.get_job(), '\n', sep='')
        except (ValueError, IOError):
            print('Employee not found under that id.')
            return


def add_employee():
    name = input('Enter name: ')
    id_number = int(input('Enter id: '))
    department = input('Enter department: ')
    job_title = input('Enter job: ')
    employee = employee_class.Employee(name, id_number, department, job_title)
    return employee, id_number
def modify_employee(employee_dict):
    user_input = int(input('Enter id number to modify: '))
    if user_input in employee_dict:
        name = input('Enter name: ')
        id_number = int(input('Enter id: '))
        department = input('Enter department: ')
        job_title = input('Enter job: ')
        employee = employee_class.Employee(name, id_number, department, job_title)
        return employee, id_number, user_input
    else:
        main()
def delete_employee(employee_dict):
    user_input = int(input('Enter id number to delete: '))
    if user_input in employee_dict:
        return user_input
    else:
        return False
def view_employee(employee_dict):
    for key in employee_dict:
        employee = employee_dict.get(key)
        print('\n\tName: ', employee.get_name(), sep='')
        print('\tID: ', employee.get_id(), sep='')
        print('\tDepartment: ', employee.get_department(), sep='')
        print('\tJob Title: ', employee.get_job(), '\n', sep='')
def save_data(employee_dict):
    file = open('employee_directory.dat', 'wb')
    pickle.dump(employee_dict, file)
    file.close()
        

main()
    
