def main():
    number_file = open('numbers.txt', 'w')

    for number in range(1, 10 + 1, 1):
        number_file.write(str(number) + '\n')
    number_file.close()

main()
    
        
