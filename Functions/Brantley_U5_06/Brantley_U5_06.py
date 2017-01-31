def main():
    fats = int(input('How many grams of fat consumed in a day? '))
    carbs = int(input('How many grams of carbohydrates consumed in a day? '))
    print('Calories from Fat: ', fat(fats))
    print('Calories from Carbohydrates: ', carbohydrate(carbs))

def fat(fats):
    return fats * 9

def carbohydrate(carbs):
    return carbs * 4

main()
