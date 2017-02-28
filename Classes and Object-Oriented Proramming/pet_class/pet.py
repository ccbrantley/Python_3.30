#pet class
import pet_class
def main():
    add_pet()
def add_pet():
    name = input('Enter pet name: ')
    animal_type = input('Enter animal type: ')
    age = input('Enter pet age: ')
    pet = pet_class.Pet(name, animal_type, age)
    display_data(pet)
def display_data(pet):
    print("Pet's name: ", pet.get_name(), sep='')
    print("Pet's type: ", pet.get_animal_type(), sep='')
    print("Pet's age: ", pet.get_age(), sep='')
main()
