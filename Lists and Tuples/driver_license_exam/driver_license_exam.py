#driver's license exam
def main():
    (grade_sheet, grade_stu) = create_lists()
    output(grade_sheet, grade_stu)

def create_lists():

    grade_sheet = []
    grade_stu = []
    file_grade_sheet = open('grade_sheet.txt', 'r')
    file_stu_ans = open('student_answer.txt', 'r')
    line_grade = file_grade_sheet.readline()
    line_ans = file_stu_ans.readline()

    while line_grade != '':
        line_grade = line_grade.rstrip('\n')
        grade_sheet.append(line_grade)
        line_grade = file_grade_sheet.readline()

    while line_ans != '':
        line_ans = line_ans.rstrip('\n')
        grade_stu.append(line_ans)
        line_ans = file_stu_ans.readline()
    return (grade_sheet, grade_stu)

def output(grade_sheet, grade_stu):
    grade = 0
    test_len = len(grade_sheet)
    for value in range(test_len):
        if grade_sheet[value] == grade_stu[value]:
            grade += 1
        else:
            print('You incorrectly answered #: ', value + 1)
    print('You answered {} questions correctly.'.format(grade))
    print('You answered {} questions wrong.'.format(test_len-grade))
     
    
main()
