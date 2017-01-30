time = 0
caloriesburned = 0

print('This program loops to show calories burned after specific increments')
for time in range(10, 31, 5):
    caloriesBurned = time * 4.2
    print('While running ', time, ' minutes you have burned: ', caloriesBurned,' calories')
