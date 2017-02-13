#Exception Handling
def main():
    average_numbers()
    
def average_numbers():
    try:
        total = 0
        file = open('numbers.txt', 'r')
        file_line = file.readline()
        while file_line != '':
            number = int(file_line)
            total += number
            file_line = file.readline()
        print('Total: ', total)
        
    except ValueError as err:
        print(err)
    except IoError as err:
        print(err)
    
main()
