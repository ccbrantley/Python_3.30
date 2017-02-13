#Random Number File Reader
import random
def main():
    
    user_iteration = int(input('How many random numbers?'))
    write_random(user_iteration)
    total, accumulator = number_output()
    print('Total of Numbers: ', total, '\nTotal Random Numbers: ', accumulator, sep='')
    
def write_random(user_iteration):
    file = open('numbers.txt', 'w')
    for x in range (user_iteration):
        random_number = str(random.randint(1,500))
        file.write(random_number + '\n')

def number_output():
    file = open('numbers.txt', 'r')
    file_line = file.readline()
    accumulator = 0
    total = 0
    while file_line != '':
        number = int(file_line)
        accumulator += 1
        total += number
        file_line = file.readline()
    return total, accumulator
main()




    
