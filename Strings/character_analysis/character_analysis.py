#character analysis per included text.txt file
def main():
    text = get_file()
    upper_case, lower_case, space_case, digit_case = cases(text)
    display_output(upper_case, lower_case, space_case, digit_case)
def get_file():
    file = open('text.txt', 'r')
    line = file.readline()
    text = []
    while line != '':
        line = line.strip('\n')
        text.append(line)
        line = file.readline()
    return text


def cases(text):
    text_str = str(text)
    text_len = len(text_str)
    upper_case = 0
    lower_case = 0
    space_case = 0
    digit_case = 0
    for x in range(text_len):
        if text_str[x].isupper():
            upper_case += 1
        if text_str[x].islower():
            lower_case += 1
        if text_str[x].isspace():
            space_case += 1
        if text_str[x].isdigit():
            digit_case += 1
    return upper_case, lower_case, space_case, digit_case

def display_output(upper_case, lower_case, space_case, digit_case):
    print('This progam gives an analysis of the contents of the text.txt file in its directory.')
    print('Uppercase letters: ', upper_case, sep='')
    print('Lowercase letters: ', lower_case, sep='')
    print('Whitespace: ', space_case, sep='')
    print('Digits: ', digit_case, sep='')
    
        


main()
        
        
