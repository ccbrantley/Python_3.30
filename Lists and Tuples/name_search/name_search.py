#name search
print('This program checks to see if a name is popular.')
def main():
    (list_boy, list_girl) = create_lists()
    user_input = get_input()
    name_search(list_boy, list_girl, user_input)
    
def create_lists():
    list_boy = []
    list_girl = []
    file_boy = open('BoyNames.txt', 'r')
    file_girl = open('GirlNames.txt', 'r')
    line_boy = file_boy.readline()
    line_girl = file_girl.readline()
    while line_boy != '':
        line_boy = line_boy.rstrip('\n')
        list_boy.append(line_boy)
        line_boy = file_boy.readline()
    while line_girl != '':
        line_girl = line_girl.rstrip('\n')
        list_girl.append(line_girl)
        line_girl = file_girl.readline()
    return list_boy, list_girl

def get_input():
    return input('Enter a name: ')

def name_search(list_boy, list_girl, user_input):
    len_list = (len(list_boy))
    for value in range(len_list):
        if list_boy[value] == user_input or list_girl[value] == user_input:
                print(user_input, 'was a popular name.')
                return
    print(user_input, 'was not a popular name.')
    main()
main()
        
        
