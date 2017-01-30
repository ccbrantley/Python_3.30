integer = 0
factorial = []
product = 1
integer = int(input('Please enter in a non-negative integer: '))
for number in range(1, integer + 1, 1):
    factorial.append(number)

print(factorial)
for x in factorial:
    product *= x

print('The factorial of', integer, 'is', product)
