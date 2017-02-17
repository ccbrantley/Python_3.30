#lottery number generator
import random
def main():
    random_number = 0
    lottery_len = 7
    lottery_list = []
    for space in range (lottery_len):
        number = random.randint(0, 9)
        lottery_list.append(number)
    print(lottery_list)

main()
        
