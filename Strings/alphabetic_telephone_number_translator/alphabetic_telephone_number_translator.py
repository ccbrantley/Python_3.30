#alphabetic telephone number translator
def main():
    number = get_input()

    translate(number)

def get_input():
    return str(input('Enter telephone number (###-xxx-xxxx): '))
  

def translate(number):
    ran_accum = 0
    strip = number.split('-')
    
    txt_num = {'A': '2', 'B': '2', 'C': '2',
               'D': '3', 'E': '3', 'F': '3',
               'G': '4', 'H': '4', 'I': '4',
               'J': '5', 'K': '5', 'L': '5',
               'M': '6', 'N': '6', 'O': '6',
               'P': '7', 'Q': '7', 'R': '7',
               'T': '8', 'U': '8', 'V': '8',
               'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
               }

    strip_length = len(strip)
    for x in range(strip_length):
        index_length = len(strip[x])
        strip_argu = strip[x]
        for y in range(index_length):
            single_argu = strip_argu[y]
            value = txt_num.get(single_argu, single_argu)
            ran_accum += 1
            print(value, end='')
            if (3 == ran_accum or 6 == ran_accum):
                print('-', end='')
            
            


main()
    
