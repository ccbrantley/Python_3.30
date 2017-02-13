#Average of Numbers
def main():
    total = 0
    accumulator = 0
    file = open('numbers.txt', 'r')
    line = file.readline()
    while line != '':
        number = int(line)
        total = total + number
        accumulator += 1
        line = file.readline()
    average = number / accumulator
    print('Average: ', average)
main()
