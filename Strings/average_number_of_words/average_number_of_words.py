#average number of words per included text.txt file
def main():
    line_list = read_file()

def read_file():
    file = open('text.txt', 'r')
    line = file.readline()
    line_list = []   
    while line != '':
        line = line.rstrip('\n')
        line_list.append(line)
        line = file.readline()
    calc_word(line_list)

def calc_word(line_list):
    argu_len = len(line_list)
    word_count = 0
    line = []
    for x in range(argu_len):
        line = line_list[x].split(' ')
        word_count += len(line)
        line = []
    line_avg(word_count, argu_len)
           
def line_avg(word_count, argu_len):
    avg_line = word_count / argu_len
    display_output(avg_line)

def display_output(avg_line):
    print('The average amount of words per sentence is: ', format(avg_line, ',.2f'), sep='')

    
main()
        
