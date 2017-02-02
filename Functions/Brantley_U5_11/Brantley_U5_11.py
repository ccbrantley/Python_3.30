import random
def main():
    number_1, number_2, total = random_2()
    print(number_1, '\n+', number_2)
    guess = int(input('This equals? '))
    if guess == total:
        print('Congratulations')
    else:
        print('The correct answer is : ', total)


def random_2():
    number_1 = random.randint(100,200)
    number_2 = random.randint(200,300)
    total = number_1 + number_2
    return number_1, number_2, total




main()
