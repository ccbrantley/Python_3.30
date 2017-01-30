#This program will take your age and tell you what age classification you are in
age = int(input('What is your age?'))
if age == 0:
    print('You are not born yet!')
elif age <= 1:
    print('You are a infant! How are you typing?!')
elif age > 1 and age < 13:
    print('You are a child!')
elif age >= 13 and age < 20:
    print('You are a teenager!')
elif age >= 20:
    print('You are an adult!')
