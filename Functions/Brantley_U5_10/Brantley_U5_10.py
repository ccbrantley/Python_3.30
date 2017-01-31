import feet_to_inches
def main():
    feet = int(input('Enter number of feet: '))
    print(feet, ' feet is equivalent to ', feet_to_inches.feet_to_inches(feet), ' inches.', sep='')

main()
