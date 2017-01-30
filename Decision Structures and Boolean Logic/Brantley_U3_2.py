print('This program will ask for the length and width of two rectangles and calculate the area to tell you which one is larger')
oneRectL = int(input('Length of the first Rectangle? '))
oneRectW = int(input('Width of the first rectangle? '))
twoRectL = int(input('Length of the second rectangle? '))
twoRectW = int(input('Width of the second Rectangle? '))
areaOne = oneRectL * oneRectW
areaTwo = twoRectL * twoRectW
if areaOne > areaTwo:
    print('The first Rectangle has a larger area!')
elif areaOne < areaTwo:
    print('The second Rectangle has a larger area!')
elif areaOne == areaTwo:
    print('The two rectangles have the same area!')
