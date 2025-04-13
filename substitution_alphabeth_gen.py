#Made by MScript 2024
#substitution alfabeth generator with key

#import ascii uppercase alphabet
from string import ascii_uppercase as alc

#input key
sleutel = input("Voer sleutel in: ")

#covert lowercase to uppercase
onlyCaps = sleutel.upper()

#first step
firstStep = dict.fromkeys(onlyCaps)

#second step
secondStep = {"key" : "value"}
for x in alc:
		secondStep[x] = 0
del secondStep["key"]

#third step
firstStep.update(secondStep)
 
 #fourth step
fourthStep = list(firstStep)

#list to string
fullString = ' '.join(fourthStep)

#remove spaces
onlyLetters = fullString.replace(" ", "")

#print result
print(onlyLetters)
