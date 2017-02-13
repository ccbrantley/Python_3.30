#Sum of Numbers
def main():
    total = 0
    file = open('numbers.txt', 'r')
    line = file.readline()
    while line != '':
        number = int(line)
        total = number + total
        line = file.readline()
    print(total)
main()
