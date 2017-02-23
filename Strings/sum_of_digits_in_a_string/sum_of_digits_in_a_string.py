#sum of digits in a string
print('Program takes a string of digits and adds them together.')
def main():
    num_string = str(input('Enter a list of digits with no space: '))
    char_sep(num_string)
def char_sep(num_string):
    num_list = []
    string_len = len(num_string)
    for value in range(string_len):
        num_list.append(int(num_string[value]))
    list_total = sum(num_list)
    print('Sum of string: {}'.format(list_total))
    main()
main()
    
    
