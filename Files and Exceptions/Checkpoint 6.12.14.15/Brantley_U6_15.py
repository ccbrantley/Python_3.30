def main():
    data_file = open('data.txt', 'r')

    data_line = data_file.readline()
    
    for line in data_line:
        
        print(data_line, end="")
        data_line = data_file.readline()

main()

