import random
random_number = 0
remainder = random_number % 2
even = 0
odd = 0

for x in range(100):
    random_number = (random.randint(1,20))
    remainder = random_number % 2
    print(random_number)
    if remainder == 0:
        even += 1
    else:
         odd += 1
print(even, odd)

    

