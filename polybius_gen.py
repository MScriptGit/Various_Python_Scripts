#polybius square generator

#import ascii uppercase alphabet
from string import ascii_uppercase as alc

#input key
sleutel = input("Voer sleutel in: ")

#covert lowercase to uppercase
onlyCaps = sleutel.upper()
#change J to I
noJ = onlyCaps.replace("J", "I")

#first step
firstStep = dict.fromkeys(noJ)

#second step
secondStep = {"key" : "value"}
for x in alc:
		secondStep[x] = 0
del secondStep["key"]
del secondStep["J"]

#third step
firstStep.update(secondStep)
 
 #fourth step
fourthStep = list(firstStep)

#list to string
fullString = ' '.join(fourthStep)

#remove spaces
onlyLetters = fullString.replace(" ", "")

#fill rows
one = onlyLetters[:5:]
two = onlyLetters[5:10:]
three = onlyLetters[10:15:]
four = onlyLetters[15:20:]
five = onlyLetters[20:25:]

#print square
print(one)
print(two)
print(three)
print(four)
print(five)