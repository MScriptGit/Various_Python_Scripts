#Made by MScript 2024
#geeft lengte van alle woorden in een string

#import ascii uppercase alphabet

from string import ascii_uppercase as alc

#call global vars
xDict = {"key" : "value"}

#function Start
def start():
	text = input("geef tekst in:")
	print("1: Alfabetisch, 2: aantal hoog naar laag, 3: beide")
	opt = input("Welke volgorde?")

	#remove all non-letters from string

	onlyLetters = "".join(filter(str.isalpha, text))

	#get string length

	strLength = len(text)
	onlyLettersLength = len(onlyLetters)

	print("\n")
	print("totale lengte is:", strLength)
	print("\n")
	print("aantal letters is:", onlyLettersLength)
	print("\n")

	#covert lowercase to uppercase
	onlyCaps = onlyLetters.upper()
	
	#call next function
	if opt == "1":
		alphaOrder(onlyCaps)
	elif opt == "2":
		highToLow(onlyCaps, xDict)
	elif opt == "3":
		alphaOrder(onlyCaps)
		print("\n")
		highToLow(onlyCaps, xDict)
	else:
		print("onbekende optie gekozen")
#volgende function geeft char count

def alphaOrder(onlyCaps):
	for x in alc:
		numLetter = onlyCaps.count(x)
		print(x, ":", numLetter)
		
#fill dict with letters and their value
def highToLow(onlyCaps, xDict):
	for x in alc:
		numLetter = onlyCaps.count(x)
		xDict[x] = numLetter
	del xDict["key"]
	getMax(xDict)
 
#get highest value in dict
def getMax(xDict):
	Key_max = max(xDict, key = lambda x: xDict[x])
	data = xDict.pop(Key_max)
	maxLoop(xDict, Key_max, data)
 
#Loop through dict
def maxLoop(xDict, Key_max, data):
	if data != 0:
		print(Key_max, data)
		getMax(xDict)
	else:
		pass

start()
