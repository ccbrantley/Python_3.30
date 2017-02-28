#course_information
#takes input of course name to retrieve room, instructor, and the class time
class_room = {'CS101': 3004, 'CS102': 47501, 'CS103': 6755,
	      'NT110': 1244, 'CM241': 1411}
class_instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado',
                    'CS103': 'Rich', 'NT110': 'Burke',
                    'CM241': 'Lee'}
class_time = {'CS101': '8:00 a.m.', 'CS102': '9.00 a.m.',
              'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.',
              'CM241': '1:00 p.m.'}
def main():
    get_input()
    
def get_input():
    course_number = (input('Enter course number: '))
    display_output(course_number)
    
def display_output(course_number):
    room = class_room.pop(course_number, 'Entry not found')
    instructor = class_instructor.pop(course_number, 'Entry not found')
    time = class_time.pop(course_number, 'Entry not found')
    print('The room number is: ', room, sep='')
    print('The class instructor is: ', instructor, sep='')
    print('The time class starts is: ', time, sep='')
    main()
main()
    
