import employee_class
def main():

    employee_1 =('Susan Meyers', 47899, 'Accounting', 'Vice President')
    employee_2 = ('Mark Jones', 39119, 'IT', 'Programmer')
    employee_3 = ('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
    employees = [employee_1, employee_2, employee_3]

    for employee in employees:
        display_output(employee)
def display_output(employee):
    name = employee[0]
    id_number = employee[1]
    department = employee[2]
    job_title = employee[3]
    employee_obj = employee_class.Employee(name, id_number, department, job_title)
    print('Name: ', employee_obj.get_name(), sep='')
    print('ID number: ', employee_obj.get_id(), sep='')
    print('Department: ', employee_obj.get_department(), sep='')
    print('Job Title: ', employee_obj.get_job(), sep='')
    print('\n')
main()    
