import random
y = 0
def main():
    z = 1
    rand_num = rand_generator()
    while z == 1:
        input_guess = guess() 
        define_guess(rand_num, input_guess)



    
def rand_generator():
    rand_num = random.randint(1,100)
    return rand_num

def guess():
    return int(input('Guess the number 1 - 100: '))
    


def define_guess(rand_num, input_guess):
    if input_guess > rand_num:
        print('Too high, try again ')
    elif input_guess < rand_num:
        print('Too low, try again ')
    else: 
        print('Congratulations!')
        print('A new number has been chosen!')
        z = 0
        main()
        
main()



