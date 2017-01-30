attendance = int(input('How many people will be attending the cookout? '))
dogPer = int(input('How many hotdogs will each person be given? '))
dogNeed = attendance * dogPer
bunNeed = dogNeed
dogPackminus = dogNeed / 10
bunPackminus = bunNeed / 8
dogPackbremainder = dogNeed // 10
bunPackbremainder = bunNeed // 8
dogPackRemainder = dogPackminus - dogPackbremainder 
bunPackRemainder =  bunPackminus - bunPackbremainder
dogHave = dogPackRemainder * 10
bunHave = bunPackRemainder * 8
dogLeft = dogHave - attendance
bunLeft = bunHave - attendance


dogleft = dogHave - dogPackRemainder
bunleft = bunPackminus - bunPackRemainder

print(attendance, dogPer, dogNeed, bunNeed,dogHave, bunHave, dogLeft, bunLeft)
print(dogPackRemainder, bunPackRemainder, dogleft, bunleft)
