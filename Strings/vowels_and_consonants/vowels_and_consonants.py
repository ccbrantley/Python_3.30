#vowels and consonants
def main():
    get_input()

def get_input():
    text = input('Enter text to determine the vowel and consonant count: ')
    vowels(text)
    consonants(text)
def vowels(text):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel_total = 0
    for value in (vowel_list):
        for char in(text):
           if value == char:
               vowel_total += 1
    print('Number of vowels: ',vowel_total, sep='')
            
def consonants(text):
    vowel_list = ['a', 'e', 'i', 'o', 'u',]
    consonant_total = 0
    for char in(text):
        if char.isalpha() and char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            consonant_total += 1
    print('Number of consonants: ', consonant_total, sep='')

main()
    
