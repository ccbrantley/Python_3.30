distance = 0
speed = 0
time = 0

speed = int(input('Please enter the speed of the vehicle'))
time = int(input('Please enter the number of hours the vehicle traveled'))


for hour in range(1, time + 1):
    distance = speed * hour
    print('Hour: \t Distance Traveled:')
    print(hour, '\t', distance)
