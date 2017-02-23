#most frequent character from input
import collections

def main():
    user_input = get_input()
    count(user_input)
    
def get_input():
    return input('Enter a string: ')

def count(user_input):
    
    print(collections.Counter(user_input).most_common(1)[0])

main()
