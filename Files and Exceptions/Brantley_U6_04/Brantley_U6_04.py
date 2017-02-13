#Item Counter
def main():
    total = 0
    file = open('line.txt', 'r')
    line = file.readline()
    while line != '':
        total += 1
        line = file.readline()
    print('Number of strings: ', total, sep='')
main()
