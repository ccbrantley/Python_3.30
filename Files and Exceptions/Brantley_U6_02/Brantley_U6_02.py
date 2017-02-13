#File Head Display
def main():
    file_name = str(input('Enter file name: '))
    file = open(file_name, 'r')
    line_file = file.readline()
    for x in range(5):
        print (line_file, end='')
        line_file = file.readline()

main()
