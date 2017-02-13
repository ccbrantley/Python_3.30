def main():
    data_file = open('data.txt', 'r')

    data_line = data_file.readline()
    
    while data_line != "":
       
        print(str(data_line))
        data_line = data_file.readline()

main()

