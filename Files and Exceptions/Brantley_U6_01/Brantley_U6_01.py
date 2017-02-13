#File Display
def main():

    file = open('numbers.txt', 'r')

    file_contents = file.read()
    file.close()
    print(file_contents)

main()
