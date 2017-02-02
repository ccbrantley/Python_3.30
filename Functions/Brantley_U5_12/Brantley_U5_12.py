def main():
    int_1 = int(input('Integer 1 : '))
    int_2 = int(input('Integer 2: '))
    max(int_1, int_2)
    



def max(int_1, int_2):
    if int_1 > int_2:
        print('The first value, ', int_1, ', is greater', sep='')
    else:
        print('The second value, ', int_2, ', is greater', sep='')

main()
