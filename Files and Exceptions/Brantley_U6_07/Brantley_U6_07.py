#Random Number File Writer
import random
def main():
    user_iteration = int(input('How many numbers to write? '))
    file = open('numbers.txt', 'w')
    for x in range (user_iteration):
        random_number = str(random.randint(1,500))
        file.write(random_number + '\n')
main()
