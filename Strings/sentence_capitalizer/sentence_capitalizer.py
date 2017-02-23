#takes one input sentene and capitalizes first word
def main():
    get_input()
def get_input():
    user_input = input('Enter a sentence to capitalize: ')
    capital(user_input)

def capital(user_input):
    sentence_list = user_input.split('.')
    sen_list_len = len(sentence_list)
    for x in range(sen_list_len):
        line_list = sentence_list[x]
        line_len = len(sentence_list[x])
        for y in range(line_len):
            if y == 0:
                print(line_list[y].upper(), end='')
            elif line_list[y] == '.':
                print('here')
            else:
                print(line_list[y], end='')
        print('.', end='')
    
        


main()
