#Line Numbers
def main():
    x = 0
    file = open('line.txt', 'r')
    line = file.readline()
    while line != '':
        x += 1
        print(x,': ', line, end='', sep='')
        line = file.readline()

main()
