#morse code converter 
def main():

    code_input = get_input()
    morse_code(code_input)

def get_input():
    return input('Enter morse code: ')

def morse_code(code_input):
    morse_code = code_input.split()

    convert = ['--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..',
               '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---' ,'-.-', '.-..', '--', '-.', '---',
               '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']
    new = [',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
    print(morse_code)
    length = len(morse_code)
    for x in range(length):
        for value in range(39):
            if morse_code[x] == convert[value]:
                print(new[value])
            

main()
