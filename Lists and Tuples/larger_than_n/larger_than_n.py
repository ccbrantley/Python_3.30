#larger than n
def main():
    compar_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    user_input = int(input('Enter a number 0-20: '))
    compar_input(compar_list, user_input)

def compar_input(compar_list, user_input):
    list_len = len(compar_list)
    print('Compared to the list these numbers are greater than your input')
    for index in range(list_len):
        list_num = int(compar_list[index])
        if list_num > user_input:
            print(list_num)
    

main()
