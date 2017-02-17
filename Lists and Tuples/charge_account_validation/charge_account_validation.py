#charge account validation
#getting error when a 0 is input as it will return valid if it is 0 or 00
#need to compare string values rather than int values
def main():
    acc_list = file_content()
    found = valid_loop(acc_list)
    if found == True:
        print('The number is valid.')

def file_content():
    acc_list = []
    acc_file = open('charge_accounts.txt', 'r')
    acc = acc_file.readline()
    while acc != '':
        acc = acc.rstrip('\n')
        acc_list.append(acc)
        acc = acc_file.readline()
    return acc_list

def valid_loop(acc_list):
    found = False
    acc_len = len(acc_list)
    while found != True:
        user_input = int(input('Enter your account number: '))
        for index in range(acc_len):
            acc_number = int(acc_list[index])
            if acc_number == user_input:
                return True
        print('The number is invalid.')


main()
