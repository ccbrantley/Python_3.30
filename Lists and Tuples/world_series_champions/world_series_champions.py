#world series champions
print('Displays number of times a team has won the World Series from 1903 - 2009')
def main():
    w_list = create_list()
    user_input = get_input()
    program_output(w_list, user_input)

def create_list():
    w_list = []
    w_file = open('WorldSeriesWinners.txt', 'r')
    w_line = w_file.readline()
    while w_line != '':
        w_line = w_line.rstrip('\n')
        w_list.append(w_line)
        w_line = w_file.readline()
    return w_list

def get_input():
    return input('Enter a Team Name: ')

def program_output(w_list, user_input):
    w_len = len(w_list)
    times_won = 0
    for value in range(w_len):
        if user_input == w_list[value]:
            times_won += 1
    print('The {} have won {} World Series Championships as of 2009.'.format(user_input, times_won), sep='')
    main()
main()
        
