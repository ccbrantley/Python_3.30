#car class
import car_class
def main():
    car = create_car()
    for value in range(5):
        car.accelerate()
        print('Accelerating...')
        print('Current speed: ', format(car.get_speed(), ',.2f'), sep='')
    for value in range(5):
        car.brake()
        print('Applying the brakes...')
        print('Current speed: ', format(car.get_speed(), ',.2f'), sep='')
    print(car.get_year())
    print(car.get_make())
    
def create_car():
    year = int(input("Enter car's model year: "))
    make = input("Enter car's make: ")
    car = car_class.Car(year,make)
    return car
def accelereate(car):
    car.accelereate()
def get_speed(car):
    car.get_speed()
def brake(car):
    car.brake()
main()
