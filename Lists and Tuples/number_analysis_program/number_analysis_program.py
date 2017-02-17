#number analysis program
def main():
    num_list = get_input()
    min_max(num_list)
    total_average(num_list)
    
def get_input():
    num_list = []
    print('Enter twenty numbers')
    for value in range(20):
        number = int(input('Enter number {}:'.format(value + 1)))
        num_list.append(number)
    return num_list

def min_max(num_list):
    print('Smallest Number: ', min(num_list), sep='')
    print('Biggest Number: ', max(num_list), sep='')

def total_average(num_list):
    total = 0
    average = 0
    for value in range(20):
        total += num_list[value]
    average = total / len(num_list)
    print('Total of Numbers: ', total, sep='')
    print('Average of Numbers: ', average, sep='')

main()
